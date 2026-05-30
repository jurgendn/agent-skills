---
name: proof-sketcher
description: Convert an informal mathematical idea into a precise theorem, lemma, or proof scaffold with explicit assumptions, dependency structure, and clearly marked gaps.
when_to_use: Use when developing a new proof, formalizing intuition, planning a theorem structure, or evaluating whether an argument is actually complete.
---
# Proof Sketcher
Turn intuition into a checkable proof scaffold before attempting full formalization.
The objective is not to fake completeness.  
The objective is to expose structure, assumptions, and unresolved gaps as early as possible.
---
# Procedure
## 1. State the Target Claim Precisely
Write the claim in mathematically checkable form.
Include:
- quantified variables
- domain restrictions
- asymptotic regime if relevant
- probabilistic qualifiers
- exact conclusion
Avoid:
- “behaves like”
- “roughly”
- “should converge”
- “is stable”
- “works well”
Bad:
> The walk mixes quickly.
Better:
> For any connected non-bipartite graph \(G\), the lazy random walk satisfies
> \[
> \|P^t(v,\cdot)-\pi\|_{\mathrm{TV}} \le \varepsilon
> \]
> for all
> \[
> t \ge C \gamma^{-1}\log(n/\varepsilon),
> \]
> where \(\gamma\) is the spectral gap.
---
## 2. Define Objects, Notation, and Assumptions
Explicitly define:
- spaces
- operators
- matrices
- measures
- norms
- graph families
- regularity assumptions
- independence assumptions
- asymptotic assumptions
Every symbol used later must already be defined.
Separate:
- standing assumptions
- temporary assumptions
- conjectural assumptions
Example:
```text
Assumption A1.
G is connected, undirected, and non-bipartite.
Assumption A2.
The transition matrix P is reversible with stationary distribution π.

⸻

3. Decompose the Argument

Split the proof into:

* lemmas
* propositions
* reduction steps
* intermediate estimates

Prefer:

Main theorem
├── Lemma 1: spectral estimate
├── Lemma 2: concentration bound
└── Lemma 3: coupling argument

over a single monolithic proof sketch.

Each sub-result should have:

* explicit input assumptions
* explicit output statement
* clear dependency chain

⸻

4. For Each Stage, Specify the Proof Skeleton

For every lemma or stage, include the following fields.

Goal

State exactly what must be shown.

Candidate Technique

Examples:

* spectral decomposition
* coupling
* martingale inequality
* compactness argument
* variational characterization
* induction
* contradiction
* perturbation analysis
* concentration inequality
* optimal transport duality

Dependencies

List:

* previous lemmas
* external theorems
* hidden assumptions
* required estimates

Likely Weak Points

Identify:

* unjustified limit interchange
* missing regularity
* non-uniform constants
* dependence assumptions
* dimension blow-up
* unproved concentration
* unjustified approximation

Do not hide uncertainty.

⸻

5. Mark Gaps Explicitly

Any unresolved step must be labeled as a gap.

Use labels such as:

GAP 1.
Need a uniform lower bound on conductance.
GAP 2.
The coupling argument only works for reversible chains.
GAP 3.
The concentration step currently assumes sub-Gaussian tails.

Never present an unproved step as established fact.

Separate:

* proved step
* heuristic argument
* conjectural extension

⸻

6. Compare Competing Proof Strategies

If multiple approaches exist, compare them briefly.

Example:

Strategy A: Spectral method
- cleaner constants
- requires reversibility
Strategy B: Coupling method
- more probabilistic
- may extend to directed graphs
- weaker quantitative bounds

Do not expand every branch fully.
Focus on the most plausible route.

⸻

7. End with the Minimal Next Action

Conclude with the smallest concrete step needed to advance the proof.

Good:

Next step:
Prove that the random-walk refinement operator is contractive under the chosen diffusion metric.

Bad:

Next step:
Finish the proof.

⸻

Output Format

Use the following structure.

# Target Claim
...
# Assumptions and Definitions
...
# Proof Structure
## Lemma 1
### Goal
...
### Technique
...
### Dependencies
...
### Weak Points
...
## Lemma 2
...
# Gaps
...
# Alternative Strategies
...
# Minimal Next Step
...

⸻

Rules

* Prefer explicit assumptions over implicit context.
* Prefer incomplete honesty over fake rigor.
* Distinguish theorem, heuristic, and conjecture.
* Avoid narrative filler.
* Avoid undefined notation.
* Avoid skipping dependency chains.
* Do not claim a result is “obvious” without stating why.
* Do not compress multiple logical steps into one sentence.
* Keep the scaffold minimal but structurally rigorous.

