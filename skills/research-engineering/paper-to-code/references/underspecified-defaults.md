# Commonly underspecified details and defensible defaults

Consult this when filling the assumptions ledger (SKILL.md step 2). For each gap the paper leaves open: pick the default below unless the paper's context implies otherwise, record it in the ledger, and note the sensitivity rating — **high**-sensitivity gaps are the first suspects when Gate 3 fails.

## Initialization

| Gap | Defensible default | Sensitivity |
|---|---|---|
| Linear/conv weight init | Framework default (PyTorch: Kaiming-uniform) | Low at toy scale |
| Embedding init | N(0, 0.02) (GPT-2 convention) or framework default | Low |
| New/custom component's own params | Match the component it replaces (e.g. replacing attention → init like attention projections) | Medium |
| Gate/scale parameters (learnable α, temperature) | Init so the component starts near identity / neutral (α=0 or 1, T=1) | **High** — wrong init can kill the mechanism outright |
| Residual branch scaling | None unless the paper is depth-focused | Low–medium |

## Normalization and architecture wiring

| Gap | Defensible default | Sensitivity |
|---|---|---|
| Pre-norm vs post-norm | Pre-norm (post-2020 transformer convention) | Medium |
| LayerNorm ε, elementwise affine | Framework defaults | Low |
| Where dropout sits | After attention weights and after FFN activation; p from paper's table or 0.1 | Low at toy scale — consider dropping dropout entirely for the sanity check |
| Bias terms in linear layers | Keep biases (framework default) unless paper says otherwise | Low |
| Activation in FFN | GELU for transformers, ReLU for MLPs/CNNs, unless stated | Low |
| Tied vs untied embeddings | Untied unless the paper is LM-focused (then tied) | Low |

## Loss and objective

| Gap | Defensible default | Sensitivity |
|---|---|---|
| Sum vs mean over batch/tokens | Mean (framework default) — but note it couples with LR | **High** if LR is copied from the paper |
| Auxiliary-loss weight λ when unstated | 1.0, then sweep {0.01, 0.1, 1.0} if Gate 3 fails | **High** — a regularizer's entire effect lives in λ |
| Label smoothing | Off for the sanity check | Low |
| Masking/padding handling in the loss | Exclude pad positions from the mean | Medium |
| Where a penalty applies (all layers vs last, pre- vs post-activation) | The reading that makes the paper's equations type-check; flag if ambiguous | **High** |

## Optimization

| Gap | Defensible default | Sensitivity |
|---|---|---|
| Optimizer when unstated | AdamW, β=(0.9, 0.999), wd=0.01 | Medium |
| Learning rate at toy scale | Do NOT copy the paper's full-scale LR; sweep {1e-4, 3e-4, 1e-3} for both method and baseline | **High** — the most common cause of false "does not reproduce" |
| Warmup/schedule | Constant LR (or short linear warmup) at toy scale | Low at toy scale |
| Gradient clipping | 1.0 if training is unstable, else none | Low |
| Batch size | Whatever fits; keep identical between method and baseline | Low (given same for both arms) |

## Data and evaluation

| Gap | Defensible default | Sensitivity |
|---|---|---|
| "Standard augmentation" | None for the sanity check — augmentation helps both arms and adds noise | Low for a directional test |
| Train/val split when unstated | 90/10 random with fixed seed | Low |
| Sequence length / image size at toy scale | Smallest that still exercises the mechanism (e.g. long enough for attention patterns to matter) | Medium — too small can hide the effect (→ verdict "inconclusive", not "fails") |
| Metric definition ambiguity (per-token vs per-sequence, macro vs micro) | The one that matches the paper's reported magnitudes | Medium |
| Tokenizer/vocab for text toys | Character-level or a tiny BPE — same for both arms | Low |

## Cross-cutting rules

- **Symmetry beats optimality.** Any default is acceptable for a directional test as long as method and baseline get *identical* treatment. An assumption only threatens the verdict when it interacts with the mechanism itself.
- **When a high-sensitivity gap has no defensible default** (e.g. the paper's loss is ambiguous between two readings that both type-check), implement both readings behind a flag if cheap, otherwise stop and flag to the user (SKILL.md step 2).
- **Ledger sensitivity drives Gate-3 failure triage:** on a failed reproduction, re-test flipping only the high-sensitivity assumptions, highest-suspicion first, before declaring "does not reproduce".
