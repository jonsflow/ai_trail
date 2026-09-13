#!/usr/bin/env node
/*
 * Dumps the game's authored content as JSON, for tools/review_server.py.
 *
 *   node tools/extract_sections.js
 *
 * Same trick as simulate.js: read the <script> block out of aitrail.html and
 * eval it against a stub DOM, so the data structures are the real ones rather
 * than a regex's guess at them. Endings are the exception - they are inline
 * ending(...) calls rather than a table, so those are pulled out of the source
 * text.
 */

const fs = require("fs");
const path = require("path");

const root = path.join(__dirname, "..");
const html = fs.readFileSync(path.join(root, "aitrail.html"), "utf8");
const GAME = html.slice(html.indexOf("<script>") + 8, html.lastIndexOf("</script>"));

/* ---- stub DOM, same shape simulate.js uses ---- */
function fakeEl(){
  const el={dataset:{},children:[],innerHTML:"",textContent:"",className:"",style:{},
    classList:{add:()=>{},remove:()=>{},toggle:()=>{}},
    appendChild:c=>el.children.push(c), querySelectorAll:()=>[], addEventListener:()=>{},
    scrollTop:0, scrollHeight:0};
  return el;
}
const reg={};
global.document={createElement:()=>fakeEl(), getElementById:id=>(reg[id]||=fakeEl()),
  querySelector:()=>fakeEl(), querySelectorAll:()=>[], addEventListener:()=>{}};

const DUMP = `
  out.events = EVENTS.map(e => ({
    key: "game:event:" + e.id,
    kind: "event",
    title: e.title,
    body: e.text,
    detail: e.opts.map(o => "• " + o.label + " — " + (o.desc || ""))
  }));
  out.landmarks = LANDMARKS.map(l => ({
    key: "game:landmark:" + l.at,
    kind: "landmark",
    title: l.nm,
    body: "Reached at " + l.at + " of " + GOAL + " compute.",
    detail: []
  }));
  out.pace = PACE_TEXT.map((t, i) => ({
    key: "game:pace:" + i,
    kind: "pace",
    title: "Leg " + (i + 1) + " framing",
    body: t,
    detail: []
  }));
  out.dividends = DIVIDENDS.map(d => ({
    key: "game:dividend:" + d.id,
    kind: "dividend",
    title: d.title,
    body: d.text,
    detail: ["earned by: " + d.earned, "pays: " + gains(d.d)]
  }));
  out.margin = [{
    key: "game:margin-call",
    kind: "margin",
    title: MARGIN_CALL.title,
    body: MARGIN_CALL.text,
    detail: ["triggered by: " + MARGIN_CALL.trigger,
             "does: " + gains(MARGIN_CALL.d),
             "warns: " + MARGIN_CALL.warn]
  }];
  out.paces = PACES.map((p, i) => ({
    key: "game:pace-option:" + i,
    kind: "pace-option",
    title: p.label,
    body: p.desc,
    detail: ["$" + p.cost + "M", p.corner ? "cuts a corner" : "no corner cut"]
  }));
  out.rules = (() => {
    const probe = {water:0, grid:0, trust:0, alignment:0, team:0,
                   capital:0, debt:0, compute:0, cutCorners:0};
    const save = S; S = probe;
    const rows = Object.entries(pillars()).map(([name, v]) => ({
      key: "game:pillar:" + name.toLowerCase().replace(/ /g, "-"),
      kind: "pillar",
      title: name,
      body: v.why,
      detail: v.tests.map(t => t.label
        .replace(/^(.*?) [^ ,]+, /, "$1 — ")
        .replace(/^(.*?) 0 of /, "$1 — "))
    }));
    S = save;
    return rows;
  })();
  out.invest = INVEST_POOL.map((o, i) => ({
    key: "game:invest:" + i,
    kind: "invest",
    title: o.label,
    body: o.desc,
    detail: ["pillar: " + o.stat, "cost: $" + o.cost + "M"]
  }));
`;

const out = {};
eval(GAME + "\n" + DUMP);

/* ---- endings: inline calls, so read them off the source ---- */
/* Titles are no longer always literals - several endings pick a title with a
   ternary so the wording matches the clause that actually failed. So collect
   every string in the call and sort them: SHOUTED short strings are titles,
   the long sentence-case ones are the body. */
const re = /ending\(\s*(\d+)\s*,([\s\S]*?)\n\s*"(good|bad)"\s*,/g;
out.endings = [];
let m;
while ((m = re.exec(GAME)) !== null) {
  const strings = (m[2].match(/"(?:[^"\\]|\\.)*"/g) || [])
    .map(x => x.slice(1, -1).replace(/\\"/g, '"').replace(/\\n/g, "\n"));
  const titles = strings.filter(x => x.length < 60 && x === x.toUpperCase() && /[A-Z]/.test(x));
  const body = strings.filter(x => !titles.includes(x)).join("").trim();
  out.endings.push({
    key: "game:ending:" + m[1],
    kind: "ending",
    title: `Ending ${m[1]} — ${titles.join("  /  ") || "(untitled)"}`,
    body,
    detail: titles.length > 1 ? ["title varies with the failing clause"] : []
  });
}
/* ---- loss conditions: the ifs at the top of checkEnd ---- */
const body = GAME.slice(GAME.indexOf("function checkEnd"));
// [^;{}] stops a condition running past the statement it belongs to
const lre = /if\(([^;{}]{1,160}?)\)\s*\n?\s*return ending\((\d+),/g;
out.losses = [];
let lm;
while ((lm = lre.exec(body)) !== null) {
  out.losses.push({
    key: "game:loss:" + lm[2],
    kind: "loss",
    title: "Ending " + lm[2],
    body: lm[1].replace(/\s+/g, " ").trim(),
    detail: []
  });
}

out.endings.sort((a, b) => +a.key.split(":")[2] - +b.key.split(":")[2]);

process.stdout.write(JSON.stringify(out, null, 1));
