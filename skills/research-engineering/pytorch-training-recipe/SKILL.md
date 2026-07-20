---
name: pytorch-training-recipe
description: Produce an implementable PyTorch or PyTorch Lightning training recipe with dataset handling, optimization, logging, checkpointing, and debugging checks. Use when turning a paper idea into runnable training code — including new experiments, reproductions, fine-tuning setups, scaling recipes, and debugging unstable training.
---

# PyTorch Training Recipe

Translate a research idea into a training setup that can fail loudly, debug
quickly, and scale only after correctness is verified.

For concrete implementation checklists and templates, read
`references/training-recipe-details.md` when needed.

## Intake

Specify:
- task, dataset, and split protocol;
- model family and input/target format;
- loss and metrics;
- baseline or reproduction target;
- hardware/compute budget;
- framework preference: raw PyTorch or Lightning.

## Workflow

1. Define the experiment and claim it supports.
2. Define the data pipeline, including leakage checks.
3. Choose the simplest training stack that supports the experiment.
4. Set optimization choices: optimizer, schedule, batch size, precision, clipping.
5. Add first-run safety checks.
6. Define metrics and error slices.
7. Define logging, checkpoints, seeds, and config recording.
8. Flag likely failure modes.
9. Recommend a staged rollout from tiny sanity run to full experiment.

## Non-Negotiable Checks

- Run a shape/dtype/device check.
- Verify loss is finite at initialization.
- Overfit a tiny batch.
- Run one deterministic seed twice if reproducibility matters.
- Compare against a simple baseline before scaling.
- Save config, commit, seed, and command with each run.

## Rules

- Do not start with distributed training.
- Do not tune hyperparameters before the tiny-batch check passes.
- Do not trust a metric until its implementation is checked.
- Keep the first runnable version boring.

## Output

Return:
- training recipe;
- data pipeline;
- model/loss/optimizer choices;
- minimal config;
- first-run checks;
- logging/checkpointing plan;
- likely failure modes;
- scale-up plan.
