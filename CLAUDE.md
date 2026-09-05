# CLAUDE.md — The AI Buildout Trail

## What this project is

A thought experiment, in two forms, about scaling AI without wrecking what you're
building it for.

- **`NARRATIVE.md`** — the research spine. Part I is a sourced account of what
  actually happened 2022–2026. Part II projects five futures, one of which is the
  good one.
- **`aitrail.html`** — a playable decision game built on the same material.
  Oregon Trail's structure applied to an AI buildout.

The document is the authority. The game is a way of feeling the tradeoffs the
document describes.

## Files

```
NARRATIVE.md          Part I (sourced history) + Part II (five futures)
README.md             Orientation for a human arriving cold
aitrail.html          The game. Self-contained except for arcade.css
arcade.css            Shared styling, copied from the kid_games arcade
tools/simulate.js     Headless balance/integrity simulation
tools/strategies.js   The strategies simulate.js plays (read as text, not required)
```

No build step. No package.json. No dependencies. Node is used only for the
simulation. The game is opened directly in a browser.

## The four pillars

Both the document and the game are organised around one test. A buildout must
satisfy **all four at once**; nearly every failure mode is dropping one.

| Pillar | The question |
|---|---|
| **Ethical** | Is the system understood, honest, accountable to the people it affects? |
| **Environmental** | Are the watershed and grid healthier or poorer for its existence? |
| **Fiscally sound** | Paid for out of value created, or debt someone else services? |
| **Arrived** | Did it get built, in time to matter? |

Three of four is the normal outcome and yields one of the survival endings. All
four is the only path to **THE LONG FUTURE** (ending 12). There is no partial
credit. If you change ending thresholds, preserve this property — it is the whole
argument.

## Game architecture

Single `<script>` block in `aitrail.html`. Key structures:

- **`S`** — all game state: five stats 0–100 (`water`, `grid`, `trust`,
  `alignment`, `team`), plus `capital`, `debt`, `compute`, `cursor` (per-stat
  wording rotation), `usedEvents`, `kindness`, `cutCorners`, `snap` (previous
  leg's snapshot, for the recap bar).
- **A leg = three screens**: `askPace()` → `askInvest()` → an event or landmark →
  `nextTurn()`.
- **`PACE_TEXT`** — 20 unique per-leg framings, indexed by `turn`. One per leg.
- **`INVEST_POOL`** — 22 options tagged by `stat`. `investOffers()` builds a
  rotating slate each leg: always something for the weakest stat, plus two others,
  with different wording each time a stat comes round.
- **`EVENTS`** — 32 events with weight functions `w(S)` that bias toward whatever
  the player is neglecting. Drawn **without replacement** via `S.usedEvents`.
- **`LANDMARKS`** — fixed compute thresholds with bigger scripted decisions.
- **`choices(list)`** — every screen renders through this. Options carry
  `{label, desc, go, stat?}`. The `stat` tag is how the simulation expresses
  intent without matching button text — **keep it on any new money option**.
- **`pillars()` / `finish()` / `checkEnd()`** — 7 failure endings, 4 survivals,
  1 flourishing future. `ending(id, ...)` renders the scorecard.

## Testing

```bash
node tools/simulate.js
```

Reads the `<script>` block out of `aitrail.html` and plays thousands of games under
13 strategies. **Run it before committing any change to pace yields, costs,
revenue, interest, or ending thresholds.**

What it must report:

- `prudent` reaches **THE LONG FUTURE ~100%** — a careful, green, debt-aware
  player must reliably win, or the game argues the opposite of what it means to.
- Every shortcut fails characteristically (`reckless` → people said no,
  `debtLover` → money ran out, `safetyOnly`/`greenOnly` → time ran out,
  `greenRacer` → lost the thread).
- `random` never finds the good ending.
- **`endings never reached: none`** and **`dead ends: 0`**.
- Question variety: pace screens, money slates all unique; zero repeated events.

Note on the harness: `simulate.js` and `strategies.js` are evaluated in **one
`eval`** so they share scope with the game's `let` bindings. Two separate evals
cannot see `S`, `turn` or `ended`. Don't "clean this up" into `require()`.

### The failure this exists to catch

The first version was **unwinnable**. Revenue started at 18/turn against ~150/turn
of costs, so every strategy — including the careful one — went bankrupt 200/200.
It looked completely fine by inspection. Only simulation caught it.

## Writing conventions

**In `NARRATIVE.md`:**

- Every factual claim is tagged **`[Documented]`** (primary sources, official
  filings, government reports), **`[Estimate]`** (single analysis, direction
  useful, precision not), or **`[Contested]`** (advocacy or industry figures where
  framing is part of the argument). Preserve this. It's what keeps Part I
  separable from Part II.
- Part II is explicitly projection and says so. Don't let the two blur.
- Prefer primary sources. The International AI Safety Report 2026 (Bengio chair,
  DSIT 2026/001) and IEA *Energy and AI* are the strongest anchors.
- Include leading indicators, not just claims — the "What to watch" section is
  what makes the futures falsifiable rather than decorative.

**In the game:**

- Scenarios are written as **archetypes, not named companies**. Accurate to what
  happened without asserting things about real firms, and it keeps the framing
  fair.
- **No doom porn.** The alignment-failure ending is deliberately undramatic: not a
  monster, a measurement failure — a system nobody understood running faster than
  anyone could read the logs. That's what the evidence actually supports.
- Failure endings are written as lessons, ending with what you'd do differently.
- The teen-safety event is handled with care: nobody is harmed in it, and the
  choice is whether you rebuild the safeguards or ship a disclaimer.

## Editing the HTML

`aitrail.html` is edited with `python3` string replacement rather than large
rewrites — the file is one big self-contained page and targeted replacements keep
diffs readable. After any edit:

```bash
# syntax check the script block
sed -n '/^<script>$/,/^<\/script>$/p' aitrail.html | sed '1d;$d' > /tmp/at.js
node --check /tmp/at.js
node tools/simulate.js
```

## Current state

- **Mechanics: done and verified.** 12 endings, all reachable, balance holds.
- **Question variety: done.** 20 leg framings, 22 rotating money options, 32
  no-repeat events.
- **Narrative: the weak link.** The in-game writing is flavour text. The material
  in `NARRATIVE.md` is considerably stronger and better sourced than anything the
  game currently says.

## Next step

Fold Part I into the game's event deck so scenarios carry their real weight — the
PJM market monitor's $9.33bn counterfactual, the 14% welcome poll, the evaluation
gap, Bessemer's two-thirds-of-the-city water draw. The events already exist as
archetypes; they need the actual numbers and consequences behind them.

Open question worth deciding first: whether the game should cite sources inline
(more honest, heavier) or stay clean and let `NARRATIVE.md` carry the citations
(more playable). Leaning toward a per-event "based on" footnote that links back to
the relevant section of `NARRATIVE.md`.

## Origin

Started as one of several games built for the user's nephews (8 and 11), in
`../kid_games`. It outgrew that context — the arcade keeps the seven kids' games,
and this became its own project because it wants to be a serious thought
experiment rather than a game on a menu.
