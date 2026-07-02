---
name: paper-to-code
description: Reproduce a paper's method in minimal, direct PyTorch when no official code is available, to check whether the method works as claimed. Use whenever the user says "reproduce this paper", "implement this paper's method", "there's no code for this paper", "I want to check if this paper actually works", "turn this algorithm/equation into code", or shares a paper/arXiv link and wants a working implementation of its core mechanism. The output is a small, single-file, readable implementation plus staged verification gates (shape checks → overfit tiny batch → baseline comparison at toy scale) and an explicit assumptions ledger for everything the paper left underspecified. Do NOT use for designing training recipes for your own experiments (pytorch-training-recipe / jax-training-recipe), auditing an existing released artifact (reproducibility-audit), or structuring a research repo (research-codebase).
---

# Paper to Code

Turn a paper with no released code into the smallest implementation that can answer one question: **does the method work as the paper claims?**

The output is a verdict, not a codebase. Everything in this skill serves fast falsification: if the method doesn't work, you want to find out in an afternoon at toy scale, not after a week of building infrastructure around a broken mechanism.

## When not to use

- The paper has official code → read/audit that instead (use `reproducibility-audit` if the question is whether the released artifact reproduces the results).
- The user wants to adapt a paper's component into their own codebase or design a full training setup → `pytorch-training-recipe`.
- The user wants to understand the method, not run it → `professor-mentor-technical-teaching` or `flow-deep-understanding`.

## Process

### 1. Reduce the paper to one testable claim

Before writing anything, identify the single mechanism the reproduction should test. Papers bundle many things (new component + tuned baseline + data tricks); reproducing all of it is expensive and unnecessary for a sanity check.

State the claim in one falsifiable sentence, e.g. *"Replacing softmax attention with mechanism X preserves accuracy while reducing memory"* — not *"reproduce Table 2"*. Confirm this framing with the user if the paper makes several claims.

Then pick the **smallest setting that can exercise the mechanism**: a toy dataset (synthetic, MNIST-scale, or a small slice of the paper's dataset), the smallest model that contains the component, short training runs. The paper's full-scale numbers are out of scope by default.

### 2. Extract the method

Work from the paper's algorithm box, equations, and prose. Produce two artifacts before coding:

**Notation → tensor table.** For each symbol in the core equations: name, shape, dtype/range, and where it comes from. This is where most reproduction bugs are born (batch vs. feature axis, pre- vs. post-normalization, sum vs. mean). Keep variable names in the code matching the paper's symbols (`alpha`, `z_t`, `H`) so the code can be read against the paper line by line.

**Assumptions ledger.** Papers always omit details: init scheme, normalization order, where dropout goes, learning-rate warmup, whether a loss term is averaged or summed, the exact form of "standard augmentation". For every underspecified detail, record: the gap, the assumption you chose, why (common default, cited prior work, ablation-implied), and how sensitive the result is likely to be to it. Read `references/underspecified-defaults.md` for a catalog of the common gaps, defensible defaults, and sensitivity ratings — the high-sensitivity entries are the first suspects when a reproduction fails. The ledger travels with the verdict — a failed reproduction with a documented ledger is evidence about the paper; one without is only evidence about your guesses.

If a detail is both load-bearing and unguessable (the mechanism literally cannot be implemented without it), stop and flag it to the user rather than silently inventing it.

### 3. Implement minimally

Direct, readable, single-file PyTorch. The style rules exist because the code's only job is to be checkable against the paper:

- **One file** (`reproduce_<method>.py`) unless it genuinely cannot fit: model, data, training loop, evaluation, in that order. No config system, no CLI framework, no abstractions for hypothetical reuse. Hyperparameters as a plain dict or constants at the top, values annotated with where they came from (paper §4.1, assumption #3, …).
- **Plain PyTorch**, no Lightning/framework wrappers — every line should correspond to something in the paper or a documented assumption.
- **The core mechanism gets its own class/function** with the paper's equation numbers in comments, so gates can test it in isolation.
- **A vanilla baseline is part of the implementation**, not an afterthought: the same script must be able to run the ablated/standard variant (e.g. regular attention instead of mechanism X) with one flag, because the verdict in step 5 is comparative.
- Fixed seed, deterministic where cheap, and print/log the few numbers the gates need — no experiment-tracking stack.

### 4. Staged verification gates

Run the gates in order; do not proceed past a failing gate. Each gate exists to localize a different failure class before it can masquerade as "the method doesn't work".

**Gate 1 — mechanics.** Unit-level checks on the core component in isolation: output shapes for a couple of input shapes, gradients flow to all parameters (`.grad` is not None and not all zeros after one backward), any invariants the paper states (rows sum to 1, output is a valid probability, equivariance, conservation of X). Catches translation bugs.

**Gate 2 — capacity.** Overfit a tiny batch (8–32 samples): loss must go to ~0 / accuracy to 100%. A model that cannot memorize 16 samples has a broken loss, a detached graph, or a data bug — not an underperforming method. Catches wiring bugs.

**Gate 3 — mechanism.** The actual test: method vs. vanilla baseline at toy scale, same budget, same seed policy (≥3 seeds if the effect looks small). The pass criterion is **directional**: does the effect the paper claims appear at all (method beats baseline / uses less memory / converges faster)? Effect sizes at toy scale won't match the paper and that's fine.

**Gate 4 — anchor (optional).** If the paper reports any number small enough to reach cheaply (a small-config row in an ablation table), try to land within a reasonable band of it. This upgrades the verdict's confidence but is not required for the sanity check.

### 5. Verdict

Close with an explicit verdict, one of:

- **Works as claimed (at toy scale):** the directional effect appeared; state the observed effect and which assumptions it rests on.
- **Does not reproduce:** gates 1–2 passed but the effect is absent/reversed; list the ledger assumptions most likely to be responsible and, if any is cheap to flip, test the flip before finalizing.
- **Inconclusive:** a load-bearing detail was unguessable, or toy scale can't exercise the claim (e.g. the mechanism only matters at long context / large width). Say what would be needed to decide.

## Output format

Deliver in this order:

1. **Claim under test** (one sentence) and the toy setting chosen.
2. **Assumptions ledger** (table: gap / assumption / basis / sensitivity).
3. **The implementation** (single file, runnable as `python reproduce_<method>.py`).
4. **Gate results** (per gate: pass/fail + the numbers).
5. **Verdict** with the reasoning above.

If the user only wants the plan first (no code yet), stop after 1–2 and confirm before implementing.
