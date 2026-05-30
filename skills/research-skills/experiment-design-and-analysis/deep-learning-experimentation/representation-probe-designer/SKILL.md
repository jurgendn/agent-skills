---
name: representation-probe-designer
description: Design probes and diagnostics to inspect what a model representation has learned. Use when aggregate accuracy does not explain internal behavior.
when_to_use: Use for embeddings, intermediate features, collapse checks, and mechanistic interpretation-lite.
---

# Representation Probe Designer

Probe structure, not just outputs.

## Workflow

1. Define the representation and target property.
2. Choose minimal probes: linear probe, nearest-neighbor, clustering, retrieval, or collapse diagnostic.
3. Add controls for trivial cues.
4. Define what would count as meaningful structure.
5. Recommend the smallest informative probe set.

## Rules

- A probe is evidence, not full explanation.
- Control for capacity and leakage.
