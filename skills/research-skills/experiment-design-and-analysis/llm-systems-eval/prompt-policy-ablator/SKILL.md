---
name: prompt-policy-ablator
description: Design controlled comparisons for prompts, routing, tools, and system policies. Use when a system changed and you need to know why performance moved.
when_to_use: Use for agent systems, prompt refactors, and policy tuning.
---

# Prompt Policy Ablator

Isolate the mechanism behind the gain.

## Workflow

1. State the claimed improvement.
2. List changed components.
3. Propose minimal controlled variants.
4. Hold everything else fixed.
5. Predict expected directional effects.
6. Flag confounds such as context length or tool access changes.

## Rules

- One ablation, one question.
- If multiple changes moved together, say attribution is weak.
