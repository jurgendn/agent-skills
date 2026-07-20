---
name: hypothesis-and-ablation-planner
description: Design ablations that isolate causal mechanisms instead of producing decorative tables. Use during paper preparation, benchmark analysis, reviewer response, or whenever multiple mechanisms could explain an observed gain and the user needs to determine which component matters, why it matters, and whether alternative explanations remain plausible.
---

# Hypothesis and Ablation Planner

Ablations should test explanations, not merely remove components.

## Procedure

1. State the main empirical claim.
2. Decompose the method into causal components.
3. For each component, define:
   - claimed mechanism
   - minimal ablation
   - expected directional effect
   - competing explanation
4. Add controls for:
   - parameter count
   - compute budget
   - data leakage/filtering
   - prompt/template effects
   - preprocessing artifacts
   - implementation bias
5. Minimize the ablation set:
   - remove redundant studies
   - prioritize hypothesis-separating experiments
6. Label each ablation:
   - must-have
   - useful
   - optional

## Rules

- Every ablation must answer a specific causal question.
- Avoid ablation explosion.
- If two explanations remain confounded, state it explicitly.
- Prefer interpretable ablations over cosmetic variants.
- “Removing one block” is not sufficient unless tied to a hypothesis.
- Keep training budget and evaluation protocol controlled whenever possible.

## Output Format

| Hypothesis | Component | Ablation | Expected Result | Alternative Explanation Controlled | Priority |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | Must-have / Useful / Optional |

## Final Checks

After the table, briefly state:
- which hypotheses are still confounded
- which ablation is most decisive
- which ablation is cheapest per unit insight
