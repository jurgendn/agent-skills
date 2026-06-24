# Proof techniques (reference)

A working menu of strategies to reach for when sketching a proof. This is a
prompt list, not a textbook — the actual sketching and auditing is done by
`theory-proof-sketcher` and `theory-derivation-auditor`.

## General strategies

- **Direct** — unfold definitions and chain implications to the conclusion.
- **Contradiction** — assume the negation, derive an impossibility.
- **Contrapositive** — prove ¬B ⇒ ¬A instead of A ⇒ B.
- **Induction** — base case + inductive step; watch the strength of the
  hypothesis (ordinary vs strong induction).
- **Construction** — exhibit the object the claim asserts exists.
- **Reduction** — map the problem to one already solved.

## Analysis / probability

- **ε–δ and triangle-inequality splitting** — bound a quantity by summing
  controllable pieces.
- **Union bound** — control many bad events at once (cheap, often loose).
- **Concentration** (Hoeffding, Bernstein, McDiarmid) — sums/functions of
  independent variables stay near their mean.
- **Probabilistic method** — show a random object has the property with positive
  probability.
- **Coupling / change of measure** — relate two distributions.
- **Markov/Chebyshev → Borel–Cantelli** — from moments to almost-sure statements.

## Optimization / linear algebra

- **Convexity + first-order conditions** — characterise optima; Jensen for
  inequalities.
- **Duality / KKT** — pass to the dual; certify optimality.
- **Fixed-point** (Banach, Brouwer) — existence via contraction/continuity.
- **Spectral arguments** — eigenvalues/singular values for bounds and stability.

## Hygiene

- Name where each **assumption** is used; an unused assumption is a clue (it may
  be removable, or you proved something weaker).
- Keep the **quantifier order** straight (∀∃ vs ∃∀) — see `common-pitfalls.md`.
- After a sketch, audit each step with `theory-derivation-auditor` and try to
  break the result with `theory-counterexample-hunter`.
