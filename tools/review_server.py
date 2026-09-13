#!/usr/bin/env python3
"""
Local review server for The AI Buildout Trail.

    python3 tools/review_server.py            # http://localhost:8017
    python3 tools/review_server.py --port 9000

Serves the project out of the repo root with caching turned off, so a reload
always shows the current file, and puts a review pass on top of it: every
section of NARRATIVE.md, README.md and every authored piece of the game -
event, landmark, leg framing, money option, ending - is listed with a comment
box and a status.

Comments live in review/comments.json. Two buttons write files Claude reads:

    review/FEEDBACK.md   - the open comments, as a work list
    review/APPROVAL.md   - written when you approve, asking for the artifact

Standard library only. Node is used once, to pull the game's own data
structures out of aitrail.html (tools/extract_sections.js).
"""

import argparse
import json
import mimetypes
import os
import re
import subprocess
import sys
import threading
import time
import uuid
import webbrowser
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REVIEW_DIR = os.path.join(ROOT, "review")
COMMENTS = os.path.join(REVIEW_DIR, "comments.json")
FEEDBACK = os.path.join(REVIEW_DIR, "FEEDBACK.md")
APPROVAL = os.path.join(REVIEW_DIR, "APPROVAL.md")

STATUSES = ("open", "doing", "done", "wontfix")
LOCK = threading.Lock()

# Files a browser is allowed to fetch from the repo root.
SERVEABLE = re.compile(r"^[A-Za-z0-9_./-]+\.(html|css|js|md|png|svg|jpg|jpeg|gif|ico)$")


# --------------------------------------------------------------------------
# sections
# --------------------------------------------------------------------------

def slug(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:60] or "section"


def game_sections():
    try:
        raw = subprocess.run(
            ["node", os.path.join(ROOT, "tools", "extract_sections.js")],
            capture_output=True, text=True, timeout=30, cwd=ROOT)
    except FileNotFoundError:
        return {"error": "node not found on PATH - game sections unavailable"}
    if raw.returncode != 0:
        return {"error": (raw.stderr or "extract_sections.js failed").strip()[-800:]}
    return json.loads(raw.stdout)


# Labels and running order for whatever the extractor hands back. This is a
# presentation map, NOT a filter: any key the extractor grows that is missing
# here still gets through, under a derived label. The previous version was a
# hardcoded tuple of five, so dividends, the margin call, paces, pillars and
# loss conditions were all extracted and then silently dropped on the floor.
GROUP_LABELS = [
    ("rules",     "Game — pillars, the win test"),
    ("losses",    "Game — loss conditions"),
    ("endings",   "Game — endings"),
    ("dividends", "Game — dividends"),
    ("margin",    "Game — margin call"),
    ("landmarks", "Game — landmarks"),
    ("paces",     "Game — pace options"),
    ("invest",    "Game — money options"),
    ("events",    "Game — events"),
    ("pace",      "Game — leg framings"),
]


def build_sections():
    """The game's authored content, grouped. The narrative is not here - it is
    the paper, and paper() owns it."""
    g = game_sections()
    if "error" in g:
        return [{"id": "game", "label": "Game", "sections": [], "error": g["error"]}]

    known = [gid for gid, _ in GROUP_LABELS]
    labels = dict(GROUP_LABELS)
    order = known + [k for k in g if k not in known]

    groups = []
    for gid in order:
        rows = g.get(gid) or []
        if not rows:
            continue
        groups.append({"id": gid,
                       "label": labels.get(gid, "Game — " + gid.replace("_", " ")),
                       "sections": rows})
    return groups


# ---- markdown -> html, for the subset NARRATIVE.md actually uses ----

TAGS = {"Documented": "doc", "Estimate": "est", "Contested": "con"}


def inline(text):
    """Inline markdown. Order matters: code and links are protected before
    emphasis, so a URL with an underscore or a tag inside a link survives."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    keep = []

    def stash(html):
        keep.append(html)
        return "\x00%d\x00" % (len(keep) - 1)

    text = re.sub(r"`([^`]+)`", lambda m: stash("<code>%s</code>" % m.group(1)), text)
    def emphasis(t):
        t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
        return re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", t)

    # Link labels carry their own emphasis - *Energy and AI* is a title, and the
    # link is stashed before the emphasis pass would otherwise reach it.
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
                  lambda m: stash('<a href="%s" target="_blank" rel="noopener">%s</a>'
                                  % (m.group(2), emphasis(m.group(1)))), text)

    # Evidence tags, bolded or bare, singly or paired as [Documented/Estimate].
    def pills(m):
        names = m.group(1).split("/")
        if not all(n in TAGS for n in names):
            return m.group(0)
        return stash(" ".join('<span class="tag t-%s">%s</span>' % (TAGS[n], n)
                              for n in names))

    text = re.sub(r"\*\*\[([A-Za-z/]+)\]\*\*|\[([A-Za-z/]+)\](?!\()",
                  lambda m: pills(m) if m.group(1) else pills(
                      re.match(r"\[([A-Za-z/]+)\]", m.group(0))), text)
    text = emphasis(text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], text)
    return text


def render_markdown(src):
    """Block-level markdown. Returns HTML."""
    out, i = [], 0
    lines = src.split("\n")
    para, ul, ol = [], [], []

    def flush():
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para).strip()))
            para.clear()
        if ul:
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % inline(x) for x in ul))
            ul.clear()
        if ol:
            out.append("<ol>%s</ol>" % "".join("<li>%s</li>" % inline(x) for x in ol))
            ol.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            flush()
            i += 1
            continue

        if re.match(r"^(---+|\*\*\*+)$", stripped):
            flush()
            out.append('<hr>')
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            flush()
            lvl = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (lvl, inline(m.group(2)), lvl))
            i += 1
            continue

        if stripped.startswith(">"):
            flush()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            out.append("<blockquote>%s</blockquote>" % render_markdown("\n".join(quote)))
            continue

        if stripped.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head, body = rows[0], rows[1:]
            if body and all(re.match(r"^:?-+:?$", c) for c in body[0]):
                body = body[1:]
            out.append(
                "<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (
                    "".join("<th>%s</th>" % inline(c) for c in head),
                    "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r)
                            for r in body)))
            continue

        m = re.match(r"^[-*]\s+(.*)$", stripped)
        if m:
            if para:
                flush()
            ul.append(m.group(1))
            i += 1
            continue

        m = re.match(r"^\d+[.)]\s+(.*)$", stripped)
        if m:
            if para:
                flush()
            ol.append(m.group(1))
            i += 1
            continue

        # A wrapped list item: a continuation line while a list is open belongs
        # to the last bullet, not to a new paragraph.
        if (ul or ol) and not para:
            (ul or ol)[-1] += " " + stripped
            i += 1
            continue

        if ul or ol:
            flush()
        para.append(stripped)
        i += 1

    flush()
    return "".join(out)


def paper():
    """NARRATIVE.md as a document: a masthead plus one commentable chapter per
    ## / ### heading. Coarse on purpose - a comment anchor per paragraph is
    more friction than signal."""
    path = os.path.join(ROOT, "NARRATIVE.md")
    if not os.path.exists(path):
        return {"title": "NARRATIVE.md not found", "front": "", "chapters": []}
    lines = open(path, encoding="utf-8").read().split("\n")

    title, front, chapters, cur = "The AI Buildout Trail", [], [], None
    for line in lines:
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m and len(m.group(1)) == 1 and not chapters and cur is None:
            title = m.group(2).strip()
            continue
        if m and len(m.group(1)) in (2, 3):
            if cur:
                chapters.append(cur)
            t = m.group(2).strip()
            cur = {"key": "narrative:" + slug(t), "title": t,
                   "level": len(m.group(1)), "src": []}
            continue
        (cur["src"] if cur else front).append(line)
    if cur:
        chapters.append(cur)

    # Anything before the first Part heading is the standfirst, not a chapter:
    # the file opens with two ### banners that are really a table of contents.
    while chapters and chapters[0]["level"] != 2:
        c = chapters.pop(0)
        front.append("**%s**" % c["title"])
        front.append("")
        front.extend(c["src"])

    # "What to watch" and "Sources" are level 2 but childless, so they read as
    # ordinary sections rather than parts with one nameless chapter inside.
    for n, c in enumerate(chapters):
        nxt = chapters[n + 1] if n + 1 < len(chapters) else None
        c["part"] = c["level"] == 2 and nxt is not None and nxt["level"] == 3

    for c in chapters:
        body = "\n".join(c["src"]).strip()
        c["html"] = render_markdown(body)
        # A section opening on a wholly italic paragraph is stating its thesis.
        # Tag it so the page sets it as a standfirst rather than body copy.
        c["html"] = re.sub(r"^<p><em>(.*?)</em></p>",
                           r'<p class="standfirst">\1</p>', c["html"], count=1)
        c["words"] = len(body.split())
        # A part divider carries no prose of its own - no point hanging a
        # comment box off it.
        c["banner"] = c["words"] == 0
        del c["src"]

    html = render_markdown("\n".join(front).strip())
    if html.endswith("<hr>"):
        html = html[:-4]
    return {"title": title, "front": html, "chapters": chapters}


# --------------------------------------------------------------------------
# comment store
# --------------------------------------------------------------------------

def load_comments():
    if not os.path.exists(COMMENTS):
        return []
    try:
        with open(COMMENTS, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_comments(items):
    os.makedirs(REVIEW_DIR, exist_ok=True)
    tmp = COMMENTS + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=1, ensure_ascii=False)
    os.replace(tmp, COMMENTS)


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# --------------------------------------------------------------------------
# exports
# --------------------------------------------------------------------------

def section_titles():
    titles = {}
    for c in paper()["chapters"]:
        titles[c["key"]] = ("NARRATIVE.md", c["title"])
    for grp in build_sections():
        for s in grp["sections"]:
            titles.setdefault(s["key"], (grp["label"], s["title"]))
    titles["game:overview"] = ("The game", "The game, as a whole")
    return titles


def write_feedback():
    items = load_comments()
    titles = section_titles()
    live = [c for c in items if c.get("status") in ("open", "doing")]
    lines = ["# Review feedback — The AI Buildout Trail", "",
             "Written by tools/review_server.py at %s." % now(),
             "%d open of %d total comments." % (len(live), len(items)), ""]
    if not live:
        lines += ["_No open comments._", ""]
    by_group = {}
    for c in live:
        grp, title = titles.get(c["section"], ("Unknown", c["section"]))
        by_group.setdefault(grp, []).append((title, c))
    for grp in by_group:
        lines.append("## %s" % grp)
        lines.append("")
        for title, c in by_group[grp]:
            lines.append("### %s" % title)
            lines.append("`%s` · %s · %s" % (c["section"], c["status"], c["created"]))
            lines.append("")
            lines.append(c["text"].strip())
            lines.append("")
    os.makedirs(REVIEW_DIR, exist_ok=True)
    with open(FEEDBACK, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return len(live)


def write_approval(note, target):
    items = load_comments()
    open_n = len([c for c in items if c.get("status") in ("open", "doing")])
    body = [
        "# Approved for publishing",
        "",
        "Approved at %s via tools/review_server.py." % now(),
        "",
        "- **Publish:** %s" % (target or "(not specified)"),
        "- **Open comments at approval:** %d" % open_n,
        "",
        "## Note",
        "",
        (note or "_none_").strip(),
        "",
        "---",
        "",
        "Claude: this file is the go-ahead to publish the target above as a",
        "shareable Artifact. Delete it once published and record the URL below.",
        "",
        "**Artifact URL:** _(pending)_",
        "",
    ]
    os.makedirs(REVIEW_DIR, exist_ok=True)
    with open(APPROVAL, "w", encoding="utf-8") as f:
        f.write("\n".join(body))
    return open_n


# --------------------------------------------------------------------------
# http
# --------------------------------------------------------------------------

class Handler(BaseHTTPRequestHandler):
    server_version = "AITrailReview/1.0"

    def log_message(self, fmt, *args):
        sys.stderr.write("  %s\n" % (fmt % args))

    # -- helpers --

    def send_json(self, obj, code=200):
        payload = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)

    def send_bytes(self, data, ctype):
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.end_headers()
        self.wfile.write(data)

    def read_json(self):
        n = int(self.headers.get("Content-Length") or 0)
        if not n:
            return {}
        try:
            return json.loads(self.rfile.read(n).decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return {}

    # -- routes --

    def do_GET(self):
        path = urlparse(self.path).path
        if path in ("/", "/index.html", "/review"):
            return self.serve_file("tools/review_ui.html")
        if path == "/play":
            return self.serve_file("aitrail.html")
        if path == "/admin":
            return self.serve_file("tools/admin_ui.html")
        if path == "/api/game":
            return self.send_json(game_sections())
        if path == "/api/paper":
            return self.send_json(paper())
        if path == "/api/sections":
            return self.send_json({"groups": build_sections()})
        if path == "/api/comments":
            return self.send_json({"comments": load_comments()})
        return self.serve_file(path.lstrip("/"))

    def do_POST(self):
        path = urlparse(self.path).path
        data = self.read_json()

        if path == "/api/comments":
            text = (data.get("text") or "").strip()
            section = (data.get("section") or "").strip()
            if not text or not section:
                return self.send_json({"error": "section and text required"}, 400)
            item = {"id": uuid.uuid4().hex[:10], "section": section,
                    "text": text[:8000], "status": "open", "created": now()}
            with LOCK:
                items = load_comments()
                items.append(item)
                save_comments(items)
            return self.send_json({"comment": item})

        m = re.match(r"^/api/comments/([0-9a-f]{10})$", path)
        if m:
            with LOCK:
                items = load_comments()
                for c in items:
                    if c["id"] == m.group(1):
                        if data.get("status") in STATUSES:
                            c["status"] = data["status"]
                        if isinstance(data.get("text"), str) and data["text"].strip():
                            c["text"] = data["text"].strip()[:8000]
                        save_comments(items)
                        return self.send_json({"comment": c})
            return self.send_json({"error": "no such comment"}, 404)

        if path == "/api/feedback":
            with LOCK:
                n = write_feedback()
            return self.send_json({"written": "review/FEEDBACK.md", "open": n})

        if path == "/api/approve":
            with LOCK:
                write_feedback()
                n = write_approval(data.get("note", ""), data.get("target", ""))
            return self.send_json({"written": "review/APPROVAL.md", "open": n})

        return self.send_json({"error": "not found"}, 404)

    def do_DELETE(self):
        m = re.match(r"^/api/comments/([0-9a-f]{10})$", urlparse(self.path).path)
        if not m:
            return self.send_json({"error": "not found"}, 404)
        with LOCK:
            items = load_comments()
            kept = [c for c in items if c["id"] != m.group(1)]
            save_comments(kept)
        return self.send_json({"deleted": m.group(1)})

    # -- static --

    def serve_file(self, rel):
        if not SERVEABLE.match(rel) or ".." in rel:
            return self.send_json({"error": "not found"}, 404)
        full = os.path.realpath(os.path.join(ROOT, rel))
        if not full.startswith(ROOT + os.sep) or not os.path.isfile(full):
            return self.send_json({"error": "not found"}, 404)
        ctype = mimetypes.guess_type(full)[0] or "application/octet-stream"
        if ctype.startswith("text/") or ctype.endswith(("javascript", "json")):
            ctype += "; charset=utf-8"
        with open(full, "rb") as f:
            return self.send_bytes(f.read(), ctype)


def main():
    ap = argparse.ArgumentParser(description="Local review server for The AI Buildout Trail.")
    ap.add_argument("--port", type=int, default=8017)
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--no-open", action="store_true", help="don't open a browser")
    args = ap.parse_args()

    os.makedirs(REVIEW_DIR, exist_ok=True)
    url = "http://%s:%d/" % (args.host, args.port)
    srv = ThreadingHTTPServer((args.host, args.port), Handler)
    print("The AI Buildout Trail — review server")
    print("  review : %s" % url)
    print("  game   : %splay" % url)
    print("  store  : review/comments.json")
    print("  ctrl-c to stop")
    if not args.no_open:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")


if __name__ == "__main__":
    main()
