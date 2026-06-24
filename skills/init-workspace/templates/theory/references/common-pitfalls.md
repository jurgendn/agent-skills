# Common pitfalls (reference)

The recurring ways theory arguments go wrong. Scan this before marking a claim
`proved`. Use `theory-counterexample-hunter` to actively try to trip each one and
`theorem-and-claim-audit` for a full pass.

## Quantifiers and logic

- **Quantifier swap** — proving ∀x ∃y (a y for each x) but claiming ∃y ∀x (one y
  for all x). The order is the theorem.
- **Vacuous / degenerate cases** — n = 0, empty set, single point, zero variance.
  Check the boundaries.
- **Hidden "for large enough n"** — an asymptotic statement smuggled into a
  finite claim.

## Assumptions

- **Stronger-than-stated assumption used silently** — the proof needs
  independence/convexity/boundedness that the theorem doesn't state. List every
  assumption actually used (`theory-assumption-extractor`).
- **Uniformity** — constants that secretly depend on the dimension, the sample,
  or the distribution. "O(1/n)" with a hidden d is not uniform.
- **Exchange of limits / sum and integral** — needs justification (dominated
  convergence, uniform convergence); don't swap for free.

## Bounds and algebra

- **Off-by-epsilon / off-by-constant** — a dropped factor that flips a tight
  bound into a false one. Audit with `theory-derivation-auditor`.
- **Loose union bound presented as tight** — fine for existence, fatal if the
  claim is about the rate.
- **Direction of an inequality reversed** — especially after dividing by a
  possibly-negative quantity or applying a decreasing function.
- **Norm/space mismatch** — bounding in the wrong norm and claiming the result in
  another.

## Statistics / ML-specific

- **Train/test leakage** in a claimed generalisation guarantee.
- **iid assumed** where data are dependent (time series, graphs).
- **Conditioning ignored** — a bound that holds in expectation claimed to hold
  with high probability (or vice versa).

A claim survives only when a counterexample hunt and a `toy-cases/` sanity check
have both failed to break it.
