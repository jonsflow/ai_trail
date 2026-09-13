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
tools/review_server.py    Local host, paper renderer, comment store
tools/extract_sections.js Dumps the game's authored content as JSON, for the server
tools/review_ui.html      The review front end: the paper, and a thin game tab
review/               Review working state. Gitignored.
```

No build step. No package.json. No dependencies. Node is used only by the tools
(simulation, section extraction); Python only by the review server, standard
library. The game is opened directly in a browser.

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
- **A round = three screens**: `askPace()` → `askInvest()` → an event or landmark →
  `nextTurn()`.
- **`PACE_TEXT`** — 20 unique per-round framings, indexed by `turn`. One per round.
  The UI says **ROUND**, never "leg": `turn` is a time budget (20 of them, 2026–37)
  and the trail bar is `compute` distance. They are two different races and were
  both called "leg", which is why nobody could tell which one they were losing.
- **`INVEST_POOL`** — 22 options tagged by `stat`. `investOffers()` builds a
  rotating slate each leg: always something for the weakest stat, plus two others,
  with different wording each time a stat comes round.
- **`EVENTS`** — 35 events with weight functions `w(S)` that bias toward whatever
  the player is neglecting. Drawn **without replacement** via `S.usedEvents`.
- **`LANDMARKS`** — fixed compute thresholds with bigger scripted decisions.
- The deck covers permission to **build** (moratoria, abatements, protests) and,
  since `evict` / `minorban` / `procure`, permission to **operate** — losing the
  site you already have, a state barring the model for under-18s, and a
  procurement bar pending independent audit. That second axis was missing
  entirely even though §8 and §9 of `NARRATIVE.md` are about little else.
- **`DIVIDENDS`** — 7 positive state-changes, gated on *state* rather than compute:
  each fires once when a pillar is genuinely high, shows its own screen, and then
  leads into that leg's event rather than replacing it. They exist because the
  reward for good play was previously invisible — revenue simply accrued and a
  player had to be watching the number to notice. **Keep them light on capital.**
  An early version paid out ~$310M across a run and took `steward` from 18% to 99%
  on THE LONG FUTURE, which destroys the whole "three of four is normal" argument.
  Money is the pillar the game is hardest about; a dividend must not buy you out
  of it.
- **Revenue is a trust multiplier** — `40 + compute*0.9*(0.65 + trust/150)`, so
  trust 90 earns roughly a third more than trust 20 on the same compute. The log
  line now names that swing against the starting trust of 65 ("Goodwill is worth
  $43M of that" / "Low trust is costing you $52M a leg"). Purely legibility; it
  does not change the arithmetic.
- **`choices(list)`** — every screen renders through this. Options carry
  `{label, desc, go, stat?, always?}`. The `stat` tag is how the simulation
  expresses intent without matching button text — **keep it on any new money
  option**. The click handler is `if(!ended || c.always) c.go()`: the `ended`
  guard stops stale buttons firing after an ending, so any button that lives *on*
  an ending screen needs `always:true` or it is dead. The restart button shipped
  without it and did nothing.
- **`pillars()` / `finish()` / `checkEnd()`** — 8 failures, 3 survivals, 1
  flourishing future. `ending(id, ...)` renders the scorecard. Endings 1–7 are the
  run-ending losses; 8, 9 and 10 are the survivals, one per dropped pillar, styled
  `good`; 11 (*YOU ARRIVED FIRST*) is styled `bad` — you finished the trail having
  dropped two or three pillars, which the game treats as a failure that happens to
  end with a banner. 12 is THE LONG FUTURE. The doc said "7 failures, 4 survivals"
  for a while, counting 11 as a survival; the code is the authority and 11 is a
  failure.
  - A pillar is a list of **separate tests**, and the scorecard prints every one
    with its number and threshold. ETHICAL is three clauses — alignment, trust,
    *and* `cutCorners <= 3` — so it can fail on corners alone with alignment 100
    and trust 99, which is unreadable as a bare ✗.
  - `S.corners` records **which** decision cut each corner, with its leg, and the
    ending lists them. "Corners cut: 4" is a number; players want the four.
  - **An ending must never assert a failure it has not checked.** Endings 8–11
    each hard-coded one — ending 10 told a player with alignment 100 that "nobody
    can quite say why the model does what it does". Titles and bodies now compose
    from `ethicalGap()` / `greenGap()` / `moneyGap()`, which describe only the
    clauses that actually failed. If you add an ending, compose it the same way.
- **`MARGIN_CALL`** — one warning screen, fired once at `debt > 700 ||
  capital < -250`. The other five stats already turn red on the HUD below 25, so
  they warn themselves; money did not, and the fiscal ending used to arrive
  between two screens with no notice. It is a real margin call — raises ~$95M by
  force-selling 13 compute, a rescue that costs the thing you are racing for.
  Bankruptcy sits at **`capital < -500`** (was −400) so the call lands before the
  cliff. There was briefly a symmetric set of seven of these called ARREARS, one
  per pillar; it was cut as over-built, and because the word describes overdue
  payments rather than warnings. Don't rebuild it.
- **Every dividend carries an `earned` string** naming the state that triggered
  it, shown on the screen and in the log. A dividend whose cause is invisible is
  just a scene, which defeats the point. Titles must also be legible on their
  own: "The hearing runs twenty minutes" required the reader to infer that short
  meant good, and collided with the Public Hearing landmark, which runs four
  hours.

## The admin page

```
http://localhost:8017/admin
```

Every state and card the game holds, read live out of `aitrail.html` — pillar
thresholds, loss conditions (parsed straight from the `if`s at the top of
`checkEnd`), all 12 endings with their conditional titles, paces, money options,
dividends, the margin call, landmarks, the 35-card event deck and the 20 leg
framings. 122 cards. `?q=` filters and is linkable.

A sticky index across the top jumps to any group and shows its live count, which
dims to 0 under a filter. That exists because the first version was one 122-card
scroll in a bad order — the 7 dividends sat behind 12 endings and 22 money
options, about 3,000px down, and were effectively invisible. State machine first
(pillars, losses, endings, dividends, margin call), bulk decks after.

It reads through `tools/extract_sections.js`, so it cannot drift from the game —
if a card is not on the page, the extractor could not see it, which is itself the
signal. That is how the conditional ending titles were caught breaking the
endings regex (12 → 9).

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
- The `=== restart ===` section reports `click guard lets it fire: yes` and
  `new game started: yes`. This harness swaps `choices()` for a collector and so
  never runs the real click handler — that is exactly how a dead restart button
  shipped — so that check replays the guard by hand. Verify it still fails when
  you remove `always:true`; a regression test that cannot fail is worse than none.

Note on the harness: `simulate.js` and `strategies.js` are evaluated in **one
`eval`** so they share scope with the game's `let` bindings. Two separate evals
cannot see `S`, `turn` or `ended`. Don't "clean this up" into `require()`.

### The failure this exists to catch

The first version was **unwinnable**. Revenue started at 18/turn against ~150/turn
of costs, so every strategy — including the careful one — went bankrupt 200/200.
It looked completely fine by inspection. Only simulation caught it.

## Review workflow

```bash
python3 tools/review_server.py        # http://localhost:8017
```

Stdlib only; Node is shelled out to once, for `tools/extract_sections.js`.

**The paper** is the point of the tool. `NARRATIVE.md` is rendered as a document
— serif reading column, contents rail, evidence tags as pills, real tables and
pull quotes — with **one comment anchor per section**, 20 in all. Coarse on
purpose: a note box per paragraph is friction, not signal. The markdown renderer
lives in `review_server.py` and covers the subset the file actually uses
(headings, tables, blockquotes, wrapped list items, links, emphasis, and the
`[Documented]`/`[Estimate]`/`[Contested]` tags). If you add markdown the
narrative has not used before, check it renders.

A heading is a **Part** — a divider in the contents rail — only if `###`
sections hang off it. That is why "What to watch" and "Sources" read as ordinary
sections despite being `##`.

**The game** is a second tab, deliberately thin: what the game is, four numbers,
one comment anchor for the whole thing, and the 93 authored items collapsed
behind a disclosure for when a note needs to land on one specific event.

- **`GROUP_LABELS` in `review_server.py` is a presentation map, not a filter.**
  Any key the extractor grows still reaches the page under a derived label. It
  used to be a hardcoded tuple of five, so dividends, the margin call, paces,
  pillars and loss conditions were extracted and then silently dropped — the
  Game tab showed 96 of 122 cards and looked perfectly fine doing it. If you add
  a group to the extractor, it appears; add it here only to name and order it.
- Comments persist to `review/comments.json` with a status of
  `open` / `doing` / `done` / `wontfix`. Section keys are stable
  (`narrative:6-the-money-the-part-that-decides-everything-else`,
  `game:event:drought`, `game:overview`).
- URL carries review state: `?view=game`, `?filter=open`, `?theme=dark`,
  `?open=<key>`, and `#s-<key>` to land on a section.
- **write FEEDBACK.md** → `review/FEEDBACK.md`, the open notes as a work list
  grouped by section. That is the file to read when picking up a round.
- **approve →** → `review/APPROVAL.md`, naming what to publish and carrying a
  note. That file is the go-ahead to publish the shareable Artifact; record the
  URL in it and delete it once the round is closed.

Work a round by reading `review/FEEDBACK.md`, making the changes, running
`node tools/simulate.js` if anything numeric moved, and marking the notes `done`
in the UI.

`extract_sections.js` uses the same one-eval stub-DOM trick as `simulate.js`.
Endings are the exception — they are inline `ending(...)` calls rather than a
table, so those come off the source text by regex. If you ever move them into a
table, simplify the extractor with them.

## Writing conventions

**In `NARRATIVE.md`:**

- Every factual claim is tagged **`[Documented]`** (primary sources, official
  filings, government reports), **`[Estimate]`** (single analysis, direction
  useful, precision not), or **`[Contested]`** (advocacy or industry figures where
  framing is part of the argument). Preserve this. It's what keeps Part I
  separable from Part II.
- Part II is explicitly projection and says so. Don't let the two blur.
- **Risk and positive ESG carry equal weight, section by section.** Every domain
  section in Part I states its cost *and* its documented counterweight — §2 the
  $9.33bn and the 1 GW of demand response, §3 Bessemer and Fairwater, §4 the
  moratoria and Frederick County's $110M. Part I ran 7% positive before this rule;
  it now runs near half, and the rule is what keeps it there. When adding a risk,
  add its counterweight or say plainly that there isn't one. §5 (power deals) and
  §8 (children) were already balanced and need no padding.
- **Every Part I section is a mini paper: thesis → marked arguments → recap.**
  1. An italic thesis line under the heading, which the renderer picks up as a
     standfirst (`<p class="standfirst">`, styled as a deck with a rule under it —
     deliberately *not* the left rule that marks a blockquote, which carries someone
     else's words).
  2. Two or more **bold lead-ins** naming each argument move, the convention §7
     already used. Without them the middle is undifferentiated prose and the
     structure is not visible to a reader.
  3. A closing recap.
  **The thesis poses; the recap concludes.** They must not be the same sentence. The
  failure mode here is writing the thesis by paraphrasing the recap that already
  exists — §5 and §6 once shared six and eight distinctive words between the two,
  which meant the section stated its point twice and argued it never. §1 had it
  three times: thesis, a first recap, and a second recap added on top.
  A shape check (is there a standfirst, are there tags, is the last paragraph long
  enough) will pass all of that. Check overlap and lead-in count instead.
- **Don't close a section with a moral.** The counterweights invite a summing-up
  paragraph that tells the reader what to conclude — "the honest summary is…",
  "both things are true…", a rhythmic list of sentence fragments. Cut those. End on
  the specific: Lancaster's 20,000 gallon/day cap, PJM's next auction, the ECB
  survey that never broke its result down by seniority. And never invent a concrete
  detail for rhythm — an earlier draft had a trial in "Boston" shutting down in
  "Nairobi", neither of which was in any source.
- The counterweights get the same scepticism as the costs: company-reported
  environmental figures are **`[Contested]`** with the boundary problem named
  (Microsoft's water-positive accounting), un-signed agreements are flagged as
  un-signed (Frederick was in public comment), and where an expert panel disputes
  the value of a safety measure, say so (FLI's "entirely inadequate").
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

## The subtitle

The line under the title on the start screen. It has been rewritten several times
and the current one is long:

> You're leading the buildout. The prize is a world where work that used to consume
> a life takes an afternoon. Everything short of that is a doomer cliché you've
> already read.

Shorter is probably better. Candidates, parked here rather than shipped — the idea
was to rotate one per new game so the restart button rerolls it:

- Build the future. Try not to break it.
- The hard part was never the technology.
- Everyone's shouting about AI. You have to actually build it.
- Turns out the future is a series of bad tradeoffs.
- A game about the decisions nobody's making out loud.
- You have eighteen months and a very good idea.

Two notes if this ever gets built. **"Eighteen months" contradicts the HUD** — the
clock is 20 rounds across 2026–2037, so that line needs to become twelve years or
be dropped; it is the only candidate that names a number. And **none of the six
names the upside**, so a rotation built from them alone frames the whole game as
damage control, which is the thing ending 12 exists to argue against. Something
like "Build it well enough and nobody has to make ends meet again" would carry that
side.

## Publishing the artifact

The shareable build lives at

```
https://claude.ai/code/artifact/ea5e0214-a817-4092-9862-f230ef3e7f20
```

It is **a derived copy, not `aitrail.html` itself**. The artifact host wraps the
file in its own `<!doctype>/<html>/<head>/<body>`, so the published file must have
none of those, and the CSP blocks external stylesheets — `arcade.css` has to be
inlined. The build is currently done by hand in a scratchpad, which means the
artifact silently lags the repo after any game change. Rebuild before republishing,
and republish to the **same URL** (pass it as `url`) or you strand the link.

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
- **Question variety: done.** 20 round framings, 22 rotating money options, 35
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
