# Ideas — future enhancements

Parked, not planned. Nothing here is committed to; it exists so the good ideas
stop living in chat logs. Anything picked up should get a line in `CLAUDE.md`
once it is real.

## 1. AI playtesters — bots that look for the best path

The most interesting idea on this list, and the one that fits the project's own
subject.

**What exists already.** `tools/simulate.js` plays thousands of games under 13
hand-written strategies (`tools/strategies.js`). Each is a fixed policy — a few
lines of `if` — and they exist to prove specific failure modes (`reckless` loses
the town, `debtLover` runs out of money). They are a regression harness, not
players. None of them *searches*. `prudent` reaches THE LONG FUTURE ~100% because
a human tuned it until it did.

**What's missing.** Nobody has ever asked the game the obvious question: what is
the *best* reachable outcome, and how many distinct routes get there? A search
would answer things a fixed policy cannot —

- Is there a path that wins with a Breakneck round in it? If yes, the "go careful"
  reading is softer than the game currently implies.
- What is the true minimum spend on each pillar? The thresholds are authored
  (alignment 65, trust 65, corners ≤ 3); nobody has checked which are actually
  binding and which are slack.
- Which events are pivotal — where does a single wrong choice cost the run — and
  which are flavour? That would tell us where the writing needs to carry weight.
- How wide is the winning corridor? If exactly one route works, the game is a
  puzzle pretending to be a simulation, and that undercuts its argument.

**Two ways to build it, in order of cost.**

*Cheap and probably sufficient:* search, not AI. Beam search or MCTS over the
choice tree, scored on the four pillars, reusing the existing headless harness —
`choices()` is already swappable, which is the whole reason the simulation works.
A few hundred lines of Node, no dependencies, no API calls, and it runs in CI.
This answers every question above.

*The version that's actually fun:* an LLM plays it. Feed a model the same screen
text a human sees — the story, the options, the HUD — and let it choose, with no
access to the numbers behind the choices. That tests something the search cannot:
**is the game legible?** A player who can only read the prose should be able to
work out that trust compounds into revenue and that corners are counted. If a
capable model reading only the surface text loses in a way a human wouldn't, the
writing is hiding the mechanics, and that is a real bug in a game whose entire
point is that the tradeoffs should be visible before you pay for them.

Run both, compare: search finds the ceiling, the LLM finds how much of the ceiling
is reachable by reading. The gap between them is the design note.

**Live on the page** is a further step and a different project — bots playing in a
panel beside you, a "watch the careful strategy" demo, a leaderboard of routes.
Fun, but it turns a static page into an application with an API key in it. The
offline version gets ~90% of the value at ~5% of the cost. Do that first.

## 2. Render the paper properly on the site

`index.html` links `NARRATIVE.md` through GitHub's markdown view, which works but
sends readers off the site. `tools/review_server.py` already contains a markdown
renderer built for exactly this file — evidence-tag pills, real tables, standfirsts,
blockquotes. Pointing it at `NARRATIVE.md` once to emit a static `narrative.html`
would keep readers here and give the document the presentation it was written for.
Small job; the renderer is the hard part and it exists.

## 3. Two live copies of the game

The Artifact at `claude.ai/code/artifact/ea5e0214-…` and the Pages site both serve
the game. The Artifact is a *derived* copy — doctype skeleton stripped, `arcade.css`
inlined — and it already lags the repo. Either fold the build into a script so
republishing is one command, or retire the Artifact now that Pages has a cleaner
URL and updates on push.

## 4. The subtitle, and the tagline

Six candidate subtitles are parked in `CLAUDE.md` under "The subtitle", along with
the rotation idea (one per new game, so the restart button rerolls it) and two
notes: "eighteen months" contradicts the 20-round clock, and none of the six names
the upside.

Separately, `README.md` and `CLAUDE.md` still describe the project as "scaling AI
without wrecking what you're building it for" — the exact construction that was
rewritten out of the game. The landing page sidestepped it with a descriptive line.
It wants settling once and propagating.

## 5. Fold Part I into the event deck

Already written up as the next step in `CLAUDE.md`, repeated here so this file is
the whole list: the events are archetypes and the research has the real numbers —
the PJM market monitor's $9.33bn counterfactual, the 14% welcome poll, Bessemer's
two-thirds-of-the-city water draw. Open question is whether events cite sources
inline or stay clean and let `NARRATIVE.md` carry them.
