---
name: judge-reliability-checker
description: Audit LLM-as-judge setups for bias, prompt sensitivity, variance, and disagreement with human criteria. Use before trusting automatic evaluation.
when_to_use: Use for pairwise ranking, rubric judging, and subjective eval pipelines.
---

# Judge Reliability Checker

Evaluate the evaluator.

## Workflow

1. State what the judge is deciding.
2. Test prompt sensitivity and ordering effects.
3. Check agreement with trusted human labels if available.
4. Look for verbosity, position, or style bias.
5. Recommend whether the judge is usable, limited, or unsafe.

## Rules

- Do not treat one judge prompt as ground truth.
- Bias discovered in evaluation is a result, not a nuisance.
