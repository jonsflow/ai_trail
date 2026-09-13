# The AI Buildout Trail

A thought experiment about scaling AI without wrecking what you're building it for.

## Contents

| File | What it is |
|---|---|
| **[NARRATIVE.md](NARRATIVE.md)** | The research spine. **Part I** is a sourced narrative of what actually happened 2022–2026 — energy, water, siting politics, financing, safety evidence, regulation, labour. **Part II** projects five possible futures, one of which is the good one. |
| **[aitrail.html](aitrail.html)** | A playable decision game built on the same material. Open it in any browser; no build step, no dependencies. |

## Reviewing it

```bash
python3 tools/review_server.py     # http://localhost:8017
```

Renders `NARRATIVE.md` as a paper — contents rail, evidence tags, one comment
box per section — and hosts the game alongside it at `/play`. Notes are saved to
`review/comments.json`; one button writes the open ones out as a work list, the
other approves the round for publishing. Python standard library only.

## The four pillars

Both the document and the game are organised around the same test. A buildout has to
satisfy all four of these at once, and almost every failure mode is dropping one:

| Pillar | The question |
|---|---|
| **Ethical** | Is the system understood, honest, and accountable to the people it affects? |
| **Environmental** | Are the watershed and the grid healthier or poorer for its existence? |
| **Fiscally sound** | Is it paid for out of value created, or debt someone else services? |
| **Arrived** | Did it get built, in time to matter? |

Three out of four is the normal outcome. All four is the only path to the future
worth wanting.

## The game

Twenty rounds, 2026 to 2037. Each round you choose a build pace and where the money
goes, then face an
event drawn from a 35-card deck of real scenarios — permit moratoria, transmission
cost allocation, an open-weights shock, a sycophantic update that raises engagement
and lowers quality, a model that scores lower on danger evals than it does in
ordinary use.

Twelve endings: seven failures, four survivals with a pillar dropped, and one
flourishing future.

Balance is verified by simulation — twelve strategies over 2,600 playthroughs. A
careful, green, debt-aware strategy reaches the good ending reliably; every shortcut
fails in its own characteristic way; random play never finds it.

## Status

The game mechanics are done and tested. The **narrative wants development** — the
current in-game writing is flavour text, and the material in `NARRATIVE.md` is
considerably stronger than what the game currently says. Next step is folding Part I
into the game's events so the scenarios carry their real sources and consequences.
