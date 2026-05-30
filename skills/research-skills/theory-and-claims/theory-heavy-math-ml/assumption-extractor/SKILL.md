---
name: assumption-extractor
description: Extract explicit and hidden assumptions from a proof, model, or empirical argument. Use to determine which premises are logically necessary, which are proof conveniences, and where the argument actually breaks.
when_to_use: Use for theorem reading, paper review, proposal critique, debugging proofs, or whenever a conclusion appears stronger than the stated setup.
---

# Assumption Extractor

Make hidden premises visible before trusting the conclusion.

A strong result often depends on assumptions that are:
- implicit;
- buried in notation;
- hidden inside a theorem citation;
- or introduced indirectly through the proof technique.

The goal is not merely to list assumptions.  
The goal is to determine:
- which assumptions are structurally necessary;
- which are artifacts of the proof;
- and what fails if they are removed.

---

# Procedure

## 1. State the Target Claim

Write the conclusion precisely.

Bad:
```text
The method converges.
```

Better:
```text
The estimator converges almost surely to the true parameter
under increasing sample size.
```

The claim should specify:
- variables;
- regime;
- convergence notion;
- probabilistic qualifier;
- comparison target.

---

## 2. Extract Explicit Assumptions

List assumptions stated directly in the theorem, model, or experiment.

Example:
```text
Explicit assumptions:
- graph is connected;
- loss function is convex;
- samples are IID;
- Markov chain is reversible.
```

Separate:
- mathematical assumptions;
- statistical assumptions;
- computational assumptions;
- data-generation assumptions.

---

## 3. Search for Hidden Assumptions

Inspect every proof step, approximation, and empirical claim.

Common hidden assumptions include:

### Regularity Assumptions
- smoothness;
- Lipschitz continuity;
- differentiability;
- bounded gradients.

### Structural Assumptions
- convexity;
- sparsity;
- low rank;
- separability;
- stationarity.

### Probabilistic Assumptions
- independence;
- exchangeability;
- concentration;
- sub-Gaussian tails;
- ergodicity.

### Identifiability Assumptions
- uniqueness of optimum;
- invertibility;
- sufficient excitation;
- non-degenerate covariance.

### Asymptotic Assumptions
- large-sample regime;
- vanishing noise;
- fixed dimension;
- infinite-time horizon.

### Empirical Assumptions
- train/test distributions match;
- benchmark labels are reliable;
- preprocessing does not leak information.

---

## 4. Identify Where Each Assumption Enters

Do not merely list assumptions.  
State where the argument actually uses them.

Example:
```text
Convexity is required when applying Jensen's inequality
during the convergence proof.

Independence is used only in the concentration step.
```

This separates:
- logically necessary assumptions;
- proof-specific assumptions.

---

## 5. Classify Assumptions

For each assumption, label it as:

### Essential
Removing it invalidates the claim itself.

Example:
```text
Connectivity is essential for global mixing.
```

### Proof Convenience
Used to simplify analysis but may not be fundamentally required.

Example:
```text
Bounded degree simplifies concentration bounds
but may not be strictly necessary.
```

### Likely Overkill
Stronger than needed.

Example:
```text
Global Lipschitz continuity may only be needed locally.
```

---

## 6. Test Assumption Removal

Ask:
```text
What breaks if this assumption is removed?
```

Be specific.

Bad:
```text
The proof becomes harder.
```

Better:
```text
Without reversibility, the spectral decomposition step fails
because orthogonal eigenbasis arguments no longer apply.
```

---

## 7. Suggest Weaker Alternatives

Where possible, replace strong assumptions with weaker ones.

Examples:
| Strong Assumption | Possible Relaxation |
|---|---|
| IID samples | Mixing process |
| Global convexity | Local convexity |
| Bounded support | Finite variance |
| Exact sparsity | Approximate sparsity |
| Deterministic graph | Random graph ensemble |

Do not claim the weaker version works unless the proof pathway is plausible.

---

# Rules

- Distinguish logical necessity from proof convenience.
- Hidden assumptions inside cited theorems still count.
- If removing an assumption breaks the argument, state exactly where.
- Avoid treating asymptotic assumptions as automatically realistic.
- Separate:
  - mathematically sufficient;
  - empirically plausible;
  - computationally feasible.
- Do not confuse “common in literature” with “necessary.”

---

# Output Format

```text
# Target Claim

...

# Explicit Assumptions

- ...

# Hidden Assumptions

| Assumption | Where It Enters | Essential or Convenient | What Breaks Without It |
|---|---|---|---|
| ... | ... | ... | ... |

# Likely Over-Strong Assumptions

- ...

# Possible Weaker Alternatives

| Original Assumption | Possible Relaxation |
|---|---|
| ... | ... |

# Main Structural Dependency

State the single assumption the argument depends on most heavily.

# Risk Assessment

Which assumptions are:
- mathematically fragile;
- empirically unrealistic;
- difficult to verify in practice.
```