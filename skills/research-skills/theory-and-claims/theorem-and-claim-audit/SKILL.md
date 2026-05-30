---
name: theorem-and-claim-audit
description: Pressure-test mathematical arguments and ML paper claims. Use to find hidden assumptions, skipped proof steps, invalid generalization, weak empirical support, and overclaimed conclusions.
when_to_use: Use for theorem sketches, proof outlines, derivations, ML paper claims, reviewer-mode critique, and whenever a result looks cleaner or stronger than expected.
---

# Theorem and Claim Audit

Audit the argument before polishing the writing.

The goal is not to make the claim sound stronger.  
The goal is to find the strongest version that is actually supported.

---

# Procedure

## 1. Restate the Target Claim

Rewrite the claim precisely.

For mathematical claims, include:
- objects;
- assumptions;
- quantifiers;
- conclusion;
- regime;
- probability statement if applicable.

For empirical claims, include:
- task;
- dataset;
- metric;
- baseline;
- claimed improvement;
- causal wording if present.

Bad:
```text
Our method is robust.
```

Better:
```text
The proposed random-walk refinement improves ONMI over DF-Louvain
on dynamic LFR graphs under edge perturbation rates from 1e-5 to 1e-3.
```

---

## 2. List Explicit Assumptions

Extract all assumptions stated in the proof, theorem, experiment, or surrounding text.

Examples:
```text
Mathematical assumptions:
- graph is connected;
- transition matrix is reversible;
- loss is convex;
- samples are IID.

Empirical assumptions:
- train/test split is fixed;
- baselines use the same input features;
- all methods use comparable tuning budgets.
```

---

## 3. Check Definitions and Notation

Verify that every object is defined before use.

Check:
- overloaded symbols;
- ambiguous graph direction or weights;
- unclear probability space;
- undefined convergence mode;
- inconsistent metric definitions;
- mismatched train/test notation.

Example failure:
```text
The proof uses P as both a transition matrix and a probability measure.
```

---

## 4. Audit Each Logical Step

For each step, classify it as:

- valid;
- valid only under extra assumptions;
- heuristic;
- unsupported;
- false.

Ask:
```text
Does this follow formally?
Which theorem justifies it?
Are the theorem conditions satisfied?
Is there an unstated approximation?
Does the conclusion overreach the premises?
```

Example:
```text
Step:
Use spectral decomposition of P.

Audit:
Valid only if P is reversible or otherwise diagonalizable
in a suitable basis.
```

---

## 5. Search for Hidden Assumptions

Look for unstated requirements such as:
- smoothness;
- boundedness;
- compactness;
- convexity;
- independence;
- stationarity;
- reversibility;
- identifiability;
- concentration;
- uniform convergence;
- finite variance;
- non-degeneracy;
- fixed dimension;
- large-sample asymptotics.

State where each hidden assumption enters.

---

## 6. Test Edge Cases and Counterexamples

Try to break the claim.

Useful stress cases:
- disconnected graph;
- bipartite graph;
- complete graph;
- star graph;
- path graph;
- sparse graph with isolated nodes;
- degenerate distribution;
- adversarial label imbalance;
- small-sample regime;
- non-IID samples;
- equal baseline performance;
- high variance across seeds.

Example:
```text
If the graph is disconnected, global mixing claims fail
because no walk can cross components.
```

---

## 7. Audit Empirical Claims

For ML or experimental papers, check whether the evidence supports the wording.

Inspect:
- metric-choice alignment;
- baseline fairness;
- hyperparameter tuning fairness;
- data leakage;
- seed variance;
- ablation coverage;
- compute budget;
- dataset selection;
- statistical significance;
- causal language.

Example:
```text
Claim:
The module improves reasoning.

Audit:
The reported metric only shows higher accuracy.
Without ablations, the result may be caused by extra parameters,
longer context, or stronger retrieval.
```

---

## 8. Downgrade Overclaims

If evidence is weak, replace strong language with a safer claim.

Examples:
```text
Original:
The method solves dynamic community detection.

Safe:
The method improves ONMI on the tested dynamic LFR settings
relative to the selected baselines.
```

```text
Original:
This proves robustness.

Safe:
This suggests robustness under the evaluated perturbation regime.
```

---

## 9. Report the Strongest Surviving Claim

End with the strongest claim that remains defensible.

It should be:
- narrower if needed;
- explicitly conditioned on assumptions;
- separated from conjectures;
- aligned with available evidence.

---

# Rules

- Prefer exactness over elegance.
- If a proof is incomplete, state exactly where it breaks.
- Downgrade claims when evidence is weaker than wording.
- Distinguish theorem, lemma, heuristic, conjecture, and empirical observation.
- Do not treat empirical improvement as mechanism validation.
- Do not let clean notation hide missing assumptions.
- Do not accept “obvious” steps without justification.
- If multiple interpretations exist, choose the weakest interpretation that still supports the result.

---

# Output Format

```text
# Claim

State the audited claim in precise form.

# Assumptions

## Explicit Assumptions
List assumptions directly stated by the author.

## Hidden Assumptions
List assumptions required by the argument but not stated clearly.

# Valid Steps

List the parts of the proof or empirical argument that are justified.

# Gaps / Failure Points

For each gap, include:
- location;
- why it fails;
- what assumption or evidence is missing.

# Counterexamples or Stress Cases

List cases that could break or weaken the claim.

# Empirical Evidence Audit

Use this section only for experimental claims.

Check:
- metric alignment;
- baseline fairness;
- ablation sufficiency;
- seed/statistical stability;
- causal overclaiming.

# Revised Safe Claim

State the strongest defensible version of the claim.

# Verdict

Choose one:
- Accept as stated
- Accept with added assumptions
- Downgrade claim
- Treat as conjecture
- Reject current argument

Reason:
Give the shortest precise reason.
```