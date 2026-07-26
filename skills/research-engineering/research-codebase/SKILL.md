---
name: research-codebase
description: >-
  Set up and maintain a research-experiment harness so experiments run fast and every paper number traces to one
  command. Use when starting a new project, running a sweep, aggregating runs into a
  paper table, or cleaning up a codebase that has become hard to navigate. Trigger on "how should I structure my
  code", "set up my project", "organize my experiments", "starting a new paper", "run all these configurations",
  "collect my results into a table", "my code is getting messy", "which run produced this number", or "I inherited
  this codebase". Built for researchers who are strong in the mathematics and weak in software: it fixes a pipeline
  contract up front so adding an experiment is one line in a list, never an edit to shared code. Not for designing
  the training loop itself (pytorch-training-recipe / jax-training-recipe), reproducing one paper's method
  (paper-to-code), choosing which experiment to run or diagnosing overfitting (experiment-design), or auditing a
  released artifact (reproducibility-audit).
---

# Research Codebase

Build the harness around the science: a fixed pipeline contract, a runner that executes many configurations, and an
aggregator that turns finished runs into the paper's table. The user supplies the mathematics; this skill makes sure
the mathematics gets run many times and reported correctly.

Two rules dominate:

- **Fix the contract up front, then never edit shared code again.** Adding an experiment must be one line in a list
  or one entry in a dict. If it requires editing the entry point, the contract is wrong.
- **Provenance is a mechanism, not a discipline.** Every run writes what produced it. Nothing depends on the user
  remembering to record anything.

The second rule is why "add structure only when the pain justifies it" is *not* the stance here. Deferring structure
assumes someone who will recognize the pain and can perform the refactor. When the user cannot code, the refactor
never happens — the project just accumulates `train_v2_final_REAL.py`. Give the small fixed skeleton once, correct,
and forbid growing it.

For what the published evidence does and does not support, read `references/evidence-base.md`. For reorganizing an
existing mess, read `references/codebase-cleanup-guide.md`.

## Step 0 — Intake (one batch, before writing any file)

Ask these together, in one round. Phrase them in the vocabulary of the paper, never of software.

1. **What is the main table or figure?** Rows, columns, and what is in a cell. Design the aggregator backward from
   this; it is the deliverable.
2. **What is one run?** What it computes and what numbers it returns — including diagnostics, not just the headline
   metric (iterations to converge, runtime, rank, sparsity, final gap, whether it converged). This answer becomes
   the required keys of the result dict.
3. **What varies across runs?** Methods, datasets, one or two parameters, seeds. This becomes the params list, and
   the run count decides whether skip-if-done and parallelism are worth building.
4. **How long is one run, and where does it run?** Seconds on a laptop / minutes on one GPU / hours on a cluster
   with a scheduler. This is the biggest branch in the generated code.
5. **New project, or existing code to reorganize?** Check with `ls` first; ask only if genuinely ambiguous.

Do **not** ask about: where metrics are stored, output directory layout, number of seeds, whether to emit LaTeX,
whether to build a config system. Each has a right answer below. Default them and state the defaults in one line.

**One round only.** Every clarification round asks a non-coder to make a decision they have no basis for. If an
answer is vague, take the default, name it, and proceed. Never block: with no answer to Q1, aggregate to a long CSV
(one row per run) and say the table shape is still needed; with no answer to Q4, use a serial loop, which is always
correct if slow.

## The pipeline contract

Four stages with fixed signatures. Generate exactly these, and the harness is written once.

| Stage | Contract | Extend by |
|---|---|---|
| Data | `load(name, seed)` or `generate(params, seed)` → problem instance | new function |
| Algorithms | `ALGORITHMS: dict[str, Callable]`, uniform call | one dict line |
| Metrics | `METRICS: dict[str, Callable]`, `metric(result, data) -> float` | one dict line |
| Store | `outputs/<run_id>/{config.json, metrics.json}` → `aggregate.py` | never — fixed |

A plain dict is the right registry here — not an if-chain in the entry point, and not a decorator plugin system.
An if-chain forces an edit to the shared entry point for every new method, which is the highest-risk edit available
to someone who cannot code and breaks every run at once when it goes wrong. A dict is one line, no magic:

```python
# algorithms/__init__.py — add a method by adding one line.
from algorithms.ridge import ridge
ALGORITHMS = {"ridge": ridge}
```

**Metrics are model-free.** Each algorithm returns a result dict, and metrics only read from it:

```python
{"preds": ..., "n_iters": 34, "rank": 7, "fit_seconds": 1.2}
```

A metric that "needs the model" — sparsity, rank, iteration count, wall-clock — is satisfied because the algorithm
reported it. Never let a metric touch a fitted object: the moment one baseline is a `sklearn` estimator and the
method is a custom class, a metric reading `model.coef_` crashes on some methods and not others, which is a failure
a non-coder cannot debug. The uniform result dict makes that impossible by construction. If a metric genuinely must
re-probe a fitted object (evaluating on a third split, tuning a threshold post-fit), allow an optional `"model"`
key as a documented escape hatch, never the default path.

This is why Q2 asks for every number up front: adding a *new diagnostic* later means one line in each algorithm
file, so front-load that cheap decision.

## Non-negotiables (each with its mechanism)

- Every run writes `config.json` with argv, resolved params, seed, and `git rev-parse HEAD`. Never a
  hand-maintained mapping file — with hundreds of runs, manual provenance is not fragile, it is impossible.
- Every run writes `metrics.json` with the Q2 keys. A missing key fails loudly at run time, not as a hole in the
  table after 200 runs.
- Seeds are set and recorded for every RNG in use.
- `data/raw/` is never modified.
- `results/` is tracked; `outputs/` is git-ignored and regenerable.
- Final numbers come from scripts, never from a notebook.
- The paper's table is generated by `aggregate.py`, not transcribed by hand.

## The runner

One script over a params list. **Not** one shell script per run — with N configs × M seeds that convention is the
bottleneck, and hand-editing N×M files is where a non-coder introduces silent errors.

```python
# configs.py — the whole experiment plan lives here.
CONFIGS = [
    {"data": "synthetic", "algorithm": a, "n": n}
    for a in ("ridge", "lasso")
    for n in (100, 1000)
]
SEEDS = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```

The runner iterates `CONFIGS × SEEDS`, derives a deterministic `run_id` from the config, **skips any run whose
`metrics.json` already exists**, and writes into `outputs/<run_id>/`. A crash mid-sweep costs only the unfinished
runs. Serial by default; parallel workers or a scheduler array job only if Q4 says the runs are long.

Switch to a config *file* (YAML/TOML) only past roughly 50 runs or when configs must be shared across machines.
Below that, a Python list is less machinery and easier for the user to read.

## Aggregation

`aggregate.py` globs `outputs/*/metrics.json`, groups by config across seeds, and emits both a CSV and
booktabs-ready LaTeX rows. Emit LaTeX always — the user writes in LaTeX, and generating the rows removes a whole
class of transcription error.

Report, per config: **n_seeds, mean, and a bootstrap confidence interval** — and keep train and test quantities as
separate columns (`metric_train`, `metric_test`, `sigma_train`, `sigma_test`) rather than folding them into a
composite score.

Two rules that are not stylistic:

- **Aggregate every run matching a config.** Never the maximum, never top-N of the seeds. Selecting the best of
  several trials is a named source of misleading results.
- **Do not hardcode a seed count as sufficient.** Ten is a reasonable starting default, but two disjoint groups of
  five seeds, same hyperparameters, have been shown to yield statistically different distributions. If the
  confidence interval is wide enough that it overlaps a baseline, the answer is more seeds, not a bolder claim.
  Route the "is this difference real" question to `statistical-testing-guide`, and ablation structure to
  `hypothesis-and-ablation-planner`.

Overfitting diagnostics and "do these gains look real" belong to `experiment-design`. This skill emits the raw
train/test columns that such a diagnosis needs and stops there.

## Prototype gate

Before launching the full sweep, run the whole pipeline once on trivial data — a tiny generated instance or a
trimmed dataset. The point is not the numbers; it is exercising logging, aggregation, and the LaTeX emission
end-to-end, and estimating runtime so the full sweep's cost is known before it is paid. Extrapolate from this run
to decide whether the sweep as planned is affordable.

## sanity_check.py

Not a test suite — the smallest set of checks that stands between fast publishing and a retraction. Four checks,
each one the user can verify is *mathematically* the right check even if they cannot write it:

1. **Determinism** — same seed twice gives a bit-identical metric. Catches unseeded randomness.
2. **Required keys** — every algorithm returns every Q2 key. Catches holes in the table.
3. **Leakage** — train and test index sets are disjoint (learning setups only).
4. **Learning / correctness** — the method drives loss to ~0 on a tiny batch, or agrees with a known reference
   solution on a case with a closed form (simulation and numerical setups).

## What to skip

Skip until there is a concrete reason: packaging (`pyproject.toml`, PyPI), continuous integration, type checking,
generated documentation sites, experiment-tracking services, abstract config systems, class hierarchies. Some
published guidance argues for the first four in ML research generally; that argument targets *released artifacts*
and its own authors qualify it as applying "only when appropriate." For in-flight experimentation by a
non-programmer under deadline, the cost is real and the benefit arrives after submission. Revisit at artifact
release — `artifact-release-packager` owns that stage.

What is *not* skippable from that same guidance: explicit recorded seeds, pinned dependencies, and one command
that re-runs every experiment in the paper. The runner is that command.

## Output

When advising:

- ask the Step 0 batch, then restate the filled-in contract (four stages, the result-dict keys, the params list);
- name the defaults taken without asking;
- generate a skeleton that **runs end-to-end** on toy data before any of the user's mathematics is added — a
  template with `TODO` holes is not usable by someone who cannot code;
- state the command-to-table path: `run.py` → `outputs/<run_id>/metrics.json` → `aggregate.py` → `results/`;
- for existing code, follow `references/codebase-cleanup-guide.md` and name what is load-bearing before deleting.

Generated code the user cannot read still has to be correct. Verify the harness by running it, not by inspection:
plausible-looking code that executes and is wrong is the characteristic failure mode here.
