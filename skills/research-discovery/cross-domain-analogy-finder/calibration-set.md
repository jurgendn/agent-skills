# Calibration Set — cross-domain-analogy-finder

Ground truth for the four-way classifier. The three seed examples are drawn from a
real motivation letter, which happened to contain one of each useful class sitting
next to each other. The point: all three *feel* like "huh, that looks related," yet
they grade differently — and a careful reader agrees with the grades. If the skill
cannot reproduce these verdicts, its classifier is miscalibrated.

Append every verdict you later accept, so the set compounds with the store.

---

## Seed 1 — Perturb & Observe = Hill Climbing  →  PORTABLE  (the gold standard)

- **Skeleton:** `local-greedy-ascent` — perturb a point, keep it if the objective
  improved, repeat.
- **The move:** recognized that MPPT's Perturb & Observe (energy systems) and Hill
  Climbing (optimization) are the same skeleton, then **imported** optimization
  methods into the energy setting — "applying this insight with different
  optimization methods significantly improved our results."
- **Carry-able result:** escape/step-size strategies actually crossed over and moved
  the metric. This is the import-a-result test *passing*.
- **Verdict:** PORTABLE. The Sinkhorn move in miniature: a tool carried across a
  domain gap and it paid.

## Seed 2 — random walk stays in a community = people talk within groups = supply-chain transactions  →  ABSTRACTION SEED (not a transfer)

- **Skeleton:** a random walk dwells within a cluster before escaping.
- **The move:** noticed the *same phenomenon* recurs across social groups, supply
  chains, transaction networks.
- **Why it is not a win (yet):** nothing was *imported*. No theorem or method was
  carried from social-network theory into community detection — the structure was
  *recognized* in several places. That recognition is the **abstraction step**: the
  seed that tells you where to dig, not the payoff.
- **Verdict:** ABSTRACTION SEED. Valuable as setup; files cleanly as a skeleton with
  multiple instances. Becomes a win only once a result crosses over.

## Seed 3 — ReID feature closeness = family resemblance in biology  →  SURFACE-ONLY  (the discard)

- **Skeleton (claimed):** members of a class are closer to each other than to
  outsiders.
- **The move:** illustrated representation-space closeness via "people in a family
  resemble each other more than outsiders."
- **Why it fails the gate:** nothing carry-able. No theorem, bound, or method moves
  from biology into the ReID model. The biology line is an *illustration for the
  reader*. (The actual contribution — viewpoint-invariance — the analogy does not
  even touch.)
- **Verdict:** SURFACE-ONLY → DISCARD. The canonical example of the bucket the gate
  exists to fill. Most honest runs should land here.

---

## How to read the seeds together

The same author, in the same letter, produced one PORTABLE, one ABSTRACTION SEED,
and one SURFACE-ONLY. The classifier's entire value is that these are
*distinguishable* — the one that produced a result and the one that produced a nice
sentence are not the same kind of thing, even though both read as "related."
