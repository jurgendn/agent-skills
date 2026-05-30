---
name: counterexample-hunter
description: Search for edge cases, pathological constructions, and violated assumptions that break a conjecture or weaken a theorem. Use when a claim feels too broad, an assumption seems suspiciously weak, or a proof step needs stress-testing. Trigger on phrases like "is this always true", "does this hold in general", "check this claim", "try to break this", "stress-test this theorem", "find a counterexample", "is this assumption necessary", or whenever the user states a result and asks whether it can be trusted. Also trigger when reviewing a proof and a step feels hand-wavy or a quantifier feels wrong.
---

# Counterexample Hunter

Try to break the claim before trusting it.

The two failure modes to avoid:
- **Fake counterexample**: something that looks like it breaks the claim but actually doesn't violate any assumption. Always check the assumptions explicitly.
- **Empty survival**: concluding "no counterexample found" without saying what was actually tested. A claim that survived three degenerate cases is not a claim that has been stress-tested.

---

## Step 1: Restate the claim precisely

Write out:
- The exact statement (universal quantifiers, domains, topology, finiteness — don't paraphrase)
- Every assumption, explicit and implicit
- What "breaks" the claim means (counterexample to existence? to uniqueness? to a bound?)

If the claim is ambiguous, name the ambiguity and ask which reading to test.

---

## Step 2: Find the load-bearing assumption

Ask: **which single assumption, if dropped, would make the claim obviously false?**

That assumption is where to attack first. Weakening or violating it is the most efficient path to a counterexample.

---

## Step 3: Generate candidates systematically

Work through each category. Don't skip a category just because it seems unlikely — the point is coverage.

**Degenerate cases**
Empty set, singleton, zero, identity, trivial structure. Does the claim hold vacuously? Does it break?

**Boundary / extremal cases**
What happens at the limit of each parameter? As n → ∞, as ε → 0, as the graph becomes a path or a clique?

**Discontinuous or singular cases**
Non-continuous functions where continuity was implicitly assumed. Singular matrices. Graphs with isolated nodes. Distributions with no mean. Measures with atoms.

**High-asymmetry cases**
One very large component and one very small one. A graph with one high-degree node and all others degree 1. A sequence that is Cauchy but not convergent in the given space.

**Adversarial constructions**
Build an object specifically designed to exploit the gap between what the assumptions say and what the proof needs. Ask: *what property does the proof silently use that isn't in the assumptions?* Construct something that has the stated assumptions but lacks that silent property.

---

## Step 4: Check each candidate honestly

For each candidate, verify explicitly:
1. Does it satisfy all the stated assumptions? (If not, it's not a counterexample — it's irrelevant.)
2. Does it violate the conclusion?

If both: **counterexample found**. State it, verify it, and stop.

If only (1): the claim survived this case. Record it.

If neither: the construction was malformed. Discard and move on.

---

## Step 5: Report the outcome

**If a counterexample is found:**
- State the counterexample concretely (give the object, not just the idea of it)
- Verify it satisfies the assumptions
- Verify it violates the conclusion
- Identify which assumption, if strengthened, would block this counterexample

**If the claim survived:**
- List what was tested (be specific — "I tested disconnected graphs, the empty graph, singleton sets, and the limit as n → ∞")
- Identify the narrowest version of the claim that the tests actually support
- Name which adversarial construction felt closest to working — that's the assumption most worth examining

**If the claim is unprovable in either direction from here:**
- Say so. Sometimes the right output is "this needs a proof attempt, not a counterexample search."

---

## Principles

A toy counterexample on ℤ/2ℤ or a two-node graph is enough if it genuinely breaks the claim. Simplicity is a virtue.

Distinguish: *the claim is false* (counterexample exists) vs. *the claim needs stronger assumptions* (a family of near-misses that all get blocked by one missing condition) vs. *the claim is true but the proof is wrong* (no counterexample found, but the argument has a gap).

Never report a counterexample without checking the assumptions. The most common error is constructing something that violates the conclusion but doesn't satisfy the hypotheses.
