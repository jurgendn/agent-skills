---
name: model-eval-error-analysis
description: Evaluate a model rigorously and inspect where it fails. Use when benchmark numbers alone are insufficient and you need slices, failure categories, and explanations.
when_to_use: Use after training, during comparison to baselines, for LLM/system evaluations, or when results look noisy or suspiciously clean.
---

# Model Eval Error Analysis

Do not stop at one headline metric.

## Workflow

1. Verify the metric implementation and data split.
2. Report the headline result with provenance.
3. Slice performance by relevant factors such as:
   - difficulty
   - length / scale
   - class imbalance
   - domain shift
   - prompt family
   - robustness setting
4. Inspect failures manually and cluster them.
5. Separate:
   - random noise
   - systematic failure modes
   - evaluator bugs
6. Compare against the strongest baseline on the same slices.
7. End with concrete next actions.

## Rules

- Never smooth away inconvenient variation.
- If confidence intervals or multiple seeds matter, say so.
- A higher average may still hide a worse model for important slices.

## Output shape

Return:
- Metrics checked
- Slice analysis
- Failure taxonomy
- Suspected causes
- Recommended fixes or follow-up experiments
