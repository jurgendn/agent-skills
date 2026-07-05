---
name: representation-probe-designer
description: Design probes and diagnostics to inspect what a model representation has learned. Use for embeddings, intermediate features, collapse checks, retrieval behavior, clustering structure, mechanistic interpretation-lite, or when aggregate accuracy does not explain internal behavior.
---

# Representation Probe Designer

Probe structure, not just outputs.

## Intake

Clarify:
- which layer/embedding/state is being probed;
- what property should be represented;
- available labels or proxy labels;
- suspected failure mode;
- whether the probe is for diagnosis, paper evidence, or debugging.

## Workflow

1. Define the representation and target property.
2. Choose minimal probes: linear probe, nearest-neighbor, clustering, retrieval, or collapse diagnostic.
3. Add controls for trivial cues.
4. Choose negative controls and random/label-shuffled baselines.
5. Define what would count as meaningful structure.
6. Recommend the smallest informative probe set.

## Rules

- A probe is evidence, not full explanation.
- Control for capacity and leakage.
- Prefer probes that distinguish two hypotheses over probes that merely look interesting.
- Do not overinterpret a high-capacity probe as proof the base representation contains a simple feature.

## Output

Return:
- target representation and property;
- probe plan;
- controls;
- interpretation rules;
- failure modes and limits;
- smallest next diagnostic.
