---
name: research-idea-stress-test
description: Stress-test a research idea before major investment. Use to expose hidden assumptions, weak novelty, confounders, and the cheapest decisive experiment.
when_to_use: Use before starting a project, writing a proposal, scaling experiments, or committing major compute/resources.
---

# Research Idea Stress Test

Assume the idea is false until it survives cheap attacks.

The objective is not to prove the idea correct.  
The objective is to determine whether the idea is:
- scientifically meaningful;
- empirically distinguishable;
- and worth additional time or compute.

---

# Procedure

## 1. State the Core Idea

Write the idea in one sentence.

Bad:
```text
Use random walks for dynamic graphs.
```

Better:
```text
Adaptive random-walk length based on spectral gap improves
dynamic community split detection compared to fixed-length walks.
```

The statement should specify:
- mechanism;
- task;
- comparison target;
- expected improvement.

---

## 2. State the Claimed Contribution Separately

Do not mix:
- the method;
- the hypothesis;
- the contribution.

Example:
```text
Method:
Adaptive walk-length refinement.

Claim:
Mixing-time-aware walks better preserve local fragmentation structure.

Contribution:
A spectral-gap-based walk selection rule for dynamic community detection.
```

This separation helps detect fake novelty.

---

## 3. Ask What Must Be True

List the assumptions required for the idea to matter.

Example:
```text
For the method to matter:
- spectral gap must correlate with useful walk length;
- dynamic graph fragmentation must not already be captured by modularity;
- adaptive walk selection must outperform simple heuristics;
- runtime overhead must remain acceptable.
```

Then separate:
- verified assumptions;
- plausible assumptions;
- completely unverified assumptions.

---

## 4. Identify Nearest Existing Work

Find the closest mechanisms, not merely the closest application domain.

Bad comparison:
```text
Related work:
Graph neural networks.
```

Better:
```text
Nearest work:
- personalized PageRank diffusion
- heat-kernel clustering
- mixing-time estimation
- random-walk refinement methods
- spectral partitioning
```

Then ask:
```text
Could the proposed method be re-described as an existing method
with different notation?
```

If yes, novelty may be weak.

---

## 5. Detect Novelty Illusions

Common novelty illusions:
- changing notation only;
- combining known modules without interaction;
- hidden scaling advantage;
- extra supervision disguised as modeling;
- benchmark selection bias;
- evaluating only on favorable datasets;
- larger receptive field mistaken for better reasoning.

Example:
```text
Potential novelty illusion:
Improvement may come from longer effective diffusion radius,
not from spectral adaptation itself.
```

---

## 6. Identify Hidden Advantages

Explicitly check for:
- more parameters;
- more compute;
- more memory;
- cleaner preprocessing;
- privileged metadata;
- stronger filtering;
- additional tuning effort.

Example:
```text
Potential hidden advantage:
Adaptive walks require estimating spectral properties,
adding extra preprocessing unavailable to baselines.
```

If the method is stronger because it secretly uses more information,
state this clearly.

---

## 7. Predict Failure Modes

List where the idea is expected to fail.

Example:
```text
Expected failure modes:
- nearly regular graphs with weak community structure;
- highly noisy temporal updates;
- graphs with extremely fast mixing;
- sparse snapshots with unstable spectral estimates.
```

A useful idea should have identifiable boundaries.

---

## 8. Define the Cheapest Falsifying Test

Do not start with the full benchmark suite.

Design the smallest experiment capable of invalidating the main claim.

Good:
```text
Run adaptive and fixed walk lengths on synthetic dynamic LFR graphs
with controlled fragmentation and overlap.
```

Bad:
```text
Train on 15 datasets with full hyperparameter sweeps.
```

The cheapest decisive experiment should:
- isolate the claimed mechanism;
- run quickly;
- produce interpretable outcomes.

---

## 9. Define the Strongest Fair Baseline

Weak baselines invalidate conclusions.

A strong baseline should:
- represent the current best simple alternative;
- receive comparable tuning effort;
- use similar compute budget when possible.

Example:
```text
Strong fair baseline:
Fixed random-walk refinement with tuned walk length selected
by validation performance.
```

Not:
```text
Baseline:
Vanilla Louvain with default parameters.
```

---

## 10. Define Minimal Success Criteria

Specify what outcome would actually justify continuation.

Example:
```text
Minimum success criterion:
Consistent ONMI improvement over tuned fixed-length baselines
across at least 3 fragmentation regimes without major runtime increase.
```

Avoid vague goals such as:
```text
Looks promising.
```

---

## 11. State What Evidence Would Change Your Mind

Explicitly define failure evidence.

Example:
```text
Evidence against the idea:
- tuned fixed-length walks perform equally well;
- gains disappear after compute normalization;
- spectral-gap estimate is unstable across snapshots;
- improvements occur only on synthetic datasets.
```

If no possible evidence could change the conclusion,
the process is not scientific.

---

## 12. Make a Recommendation

Choose one:

### Pursue
The mechanism appears distinguishable and empirically testable.

### Narrow
The idea is too broad; isolate a smaller claim.

### Reframe
The framing is weak, but a useful subproblem exists.

### Drop
The idea is likely redundant, confounded, or low-value.

---

# Rules

- Prefer cheap disconfirmation over expensive confirmation.
- “Interesting” is not evidence.
- Novelty without measurement does not count.
- If a simpler explanation exists, state it explicitly.
- Separate:
  - interesting if true;
  - likely true;
  - practically useful.
- Do not confuse benchmark gain with mechanism validation.
- Avoid scaling experiments before isolating the causal claim.

---

# Output Format

```text
# Core Idea

Adaptive walk length selected from spectral properties improves
community split detection in dynamic graphs.

# Claimed Contribution

A mixing-time-aware refinement strategy for random-walk-based
community detection.

# Why It Might Work

- walk length affects locality/globality tradeoff;
- spectral gap controls mixing behavior;
- fragmentation may require graph-dependent diffusion scale.

# Why It Might Fail

- fixed tuned walk length may already be sufficient;
- spectral estimates may be noisy;
- gain may come only from larger diffusion radius.

# Hidden Assumptions

- spectral gap is stable enough to estimate;
- dynamic updates preserve meaningful mixing structure;
- adaptive selection overhead is acceptable.

# Nearest Baselines / Related Work

- personalized PageRank
- heat-kernel diffusion
- fixed-length random-walk refinement
- spectral clustering

# Cheapest Decisive Experiment

Compare:
- fixed walk length
- validation-tuned walk length
- spectral-gap-adaptive walk length

on synthetic dynamic LFR benchmarks with controlled fragmentation.

# Evidence That Would Change My Mind

- no improvement over tuned fixed-length baselines;
- instability across seeds;
- gain disappears after runtime normalization.

# Recommendation

Narrow

Reason:
The core mechanism is plausible, but novelty currently overlaps
heavily with existing diffusion-scale selection ideas.
```