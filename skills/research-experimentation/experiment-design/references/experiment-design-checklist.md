# Experiment Design Checklist

Use this reference for detailed experiment-design prompts.

## Hypothesis

Write the claim as:

```text
Method/intervention X improves outcome Y over baseline Z under condition C,
measured by metric M.
```

Avoid:
- "works better";
- "improves graph learning";
- "is robust" without a defined perturbation.

## Minimal Experiment

Specify:
- dataset or environment;
- split protocol;
- intervention;
- fixed controls;
- compute budget;
- smallest sample that can answer the question.

## Baselines

Include:
- simplest reasonable baseline;
- current strong baseline;
- ablation that removes the claimed mechanism;
- oracle or upper-bound baseline if useful.

## Metrics

Primary metric should decide the claim. Secondary metrics should expose
tradeoffs: runtime, memory, calibration, fairness, robustness, or failure slices.

## Confounders

Check:
- parameter count;
- compute budget;
- data filtering;
- prompt/template effects;
- preprocessing artifacts;
- hyperparameter effort;
- implementation maturity.

## Decision Criteria

State before running:
- minimum effect size;
- acceptable variance;
- required baseline gap;
- what result would stop the idea;
- what result would require reframing.
