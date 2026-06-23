---
name: theory-formalism-translator
description: Translate an idea across optimization, probability, information theory, dynamical systems, graph theory, and statistics language. Use to determine whether different fields are expressing the same structure under different notation.
when_to_use: Use for interdisciplinary theory work, reframing a problem into a more tractable formalism, connecting literatures, or discovering alternative analytical tools.
---

# Formalism Translator

Look for structural equivalence, not superficial analogy.

The goal is not to rename concepts.  
The goal is to determine whether:
- two formalisms encode the same invariant structure;
- one formalism exposes stronger tools;
- or the similarity is only metaphorical.

---

# Procedure

## 1. State the Original Formalism

Describe the concept in its native language.

Specify:
- objects;
- operators;
- constraints;
- dynamics;
- optimization target;
- probabilistic interpretation if applicable.

Example:
```text
Original formalism:
Random walk on a graph with transition matrix P,
analyzed through mixing time and spectral gap.
```

Avoid vague summaries such as:
```text
Diffusion process on networks.
```

---

## 2. Identify Core Structural Objects

Extract the mathematical structure underneath the notation.

Look for:
- state space;
- energy or objective function;
- conservation law;
- invariant measure;
- transition operator;
- geometry;
- symmetry;
- equilibrium condition;
- entropy;
- curvature;
- flow;
- distance metric.

Example:
```text
Core objects:
- Markov operator P
- stationary distribution π
- spectral gap γ
- diffusion dynamics
- local-to-global information propagation
```

This step matters more than terminology.

---

## 3. Define the Translation Target

State the target formalism explicitly.

Possible targets:
- optimization;
- probability;
- information theory;
- statistical physics;
- dynamical systems;
- control theory;
- graph signal processing;
- variational inference;
- optimal transport;
- spectral theory.

Example:
```text
Target formalism:
Optimal transport interpretation of graph diffusion.
```

---

## 4. Map Objects Across Formalisms

Construct an explicit correspondence.

Example:
| Original Formalism | Target Formalism |
|---|---|
| Random walk transition | Transport kernel |
| Stationary distribution | Equilibrium measure |
| Spectral gap | Contraction / mixing rate |
| Diffusion distance | Wasserstein-like geometry |
| Community boundary | Transport bottleneck |

Do not skip mismatches.

If the mapping is only partial, say so.

---

## 5. Identify Preserved Structure

State what survives the translation.

Examples:
```text
Preserved:
- equilibrium structure
- diffusion locality
- entropy decay
- conservation of probability mass
```

Distinguish:
- exact equivalence;
- asymptotic equivalence;
- heuristic similarity.

---

## 6. Identify What Is Lost

Every translation discards information.

Examples:
```text
Lost:
- discrete graph combinatorics
- exact path interpretation
- local neighborhood semantics
- node-level interpretability
```

Do not present the target formalism as strictly superior.

---

## 7. Identify What Becomes Easier

Ask whether the new formalism provides:
- stronger theorems;
- cleaner optimization;
- better geometry;
- sharper concentration;
- stability analysis;
- computational advantages;
- alternative intuition.

Example:
```text
Optimal transport formalism may provide:
- metric geometry tools;
- contraction analysis;
- curvature interpretation;
- continuous relaxation methods.
```

---

## 8. Check Whether the Translation Is Genuine

Distinguish between:
- structural equivalence;
- reusable machinery;
- notation change only.

Bad translation:
```text
Graph diffusion is basically attention.
```

Better:
```text
Both can be interpreted as weighted information propagation operators,
but attention is data-adaptive and non-Markovian,
while graph diffusion is typically fixed and stochastic.
```

---

## 9. Suggest New Tools Enabled by the Translation

If the translation is useful, identify concrete tools now available.

Examples:
| New Formalism | Potential Tools |
|---|---|
| Optimal transport | Wasserstein geometry, Sinkhorn |
| Dynamical systems | Stability analysis, Lyapunov functions |
| Information theory | Entropy bounds, mutual information |
| Spectral theory | Eigenvalue perturbation |
| Control theory | Controllability, observability |

If no genuinely new tool appears, state that explicitly.

---

# Rules

- Do not claim equivalence unless the mapping is explicit.
- Surface mismatches, not just analogies.
- Distinguish:
  - exact equivalence;
  - asymptotic similarity;
  - heuristic resemblance.
- Preserve assumptions during translation.
- Do not confuse shared notation with shared structure.
- If the translation only renames concepts, say so.
- Prefer explicit operator/object mappings over narrative analogy.

---

# Output Format

```text
# Original Formalism

State the original framing precisely.

# Core Structural Objects

List the key operators, invariants, constraints, and dynamics.

# Target Formalism

State the destination framework.

# Structural Mapping

| Original | Target | Notes |
|---|---|---|
| ... | ... | ... |

# Preserved Structure

- ...

# Lost Structure

- ...

# What Becomes Easier

- ...

# Mismatches / Non-Equivalences

- ...

# New Tools Enabled

- ...

# Verdict

Choose one:
- Deep structural equivalence
- Useful reframing
- Partial analogy
- Mostly notation change

Reason:
...
```