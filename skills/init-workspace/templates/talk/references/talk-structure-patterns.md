# Talk structure patterns (reference)

Common arcs and time budgets by talk type. These are starting templates — the
actual narrative, pacing, and cuts are decided with `research-talk-planner` and
written to `narrative/`.

## Conference talk (12–20 min)

Tight, single-contribution. Roughly:

1. Problem + why it matters (1–2 slides).
2. The gap / what's missing in prior work (1 slide).
3. Key idea in one sentence (1 slide) — the spine.
4. Method, only as deep as needed to believe the result (2–4 slides).
5. Headline result (1–2 slides), then one supporting result/ablation.
6. Takeaway + limitation (1 slide).

Leave time for questions. ~1 minute per slide is a safe upper bound.

## Job talk / colloquium (45–60 min)

A research *agenda*, not one paper. Open with your through-line, deep-dive one or
two works, then sketch the broader programme and future vision. Budget for
interruptions; the first 5 minutes decide the room.

## Seminar / lecture (45–90 min)

Teaching, not selling. Build intuition before formalism; use worked examples;
plan checkpoints where the audience should be able to re-derive or answer a
question.

## Thesis / proposal defense

Objectives → completed work → remaining work → timeline. Anticipate committee
questions; back-up slides for likely deep-dives. Use
`deck-beamer-proposal-report` for proposal/progress framing.

## Executive / industrial report

Lead with the recommendation and impact (situation → recommendation → impact),
not the methodology. The audience wants the decision; detail goes in an appendix.
Use `deck-business-report`.

## Universal

- Settle the **one message** first; every slide serves it.
- Build the arc, then count slides against the time budget; cut from the arc if
  over.
- Practise the open and close cold — they carry the most weight.
