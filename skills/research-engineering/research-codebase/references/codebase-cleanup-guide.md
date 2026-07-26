# Codebase Cleanup Guide

Use this when an existing research codebase has become hard to navigate, or when a number in the draft can no longer
be traced to a command.

The mess this guide is aimed at is the one that accumulates when the author is a domain expert rather than a
programmer: many near-duplicate scripts, results that overwrote each other, and disagreement between files about what
the experiment actually was. It is *not* aimed at over-abstraction — that is a different failure, made by people who
can refactor their way out of it.

## Patterns to look for first

- **Duplicated entry points.** `train2.py`, `train_final.py`, `train_v2_final_REAL.py`. Each is a fork of an earlier
  script with one thing changed; nobody remembers which. This is what the params list in `configs.py` replaces.
- **Overwritten outputs.** Every run writing to `output/` or `results/latest`, so only the most recent survives and
  no earlier number can be regenerated.
- **Numbers with no command.** A figure or table cell whose generating invocation is unknown.
- **Disagreement about the experiment.** Two files that split the data differently, normalize differently, or use a
  different metric under the same name. Find these before trusting any comparison between them.
- **Notebooks as the only source of paper numbers.** Cell execution order is not recorded; the number is not
  reproducible even by its author.
- **Hidden preprocessing.** Data transformations buried inside a training script, so the "same" data differs between
  methods.
- **Unrecorded seeds**, or a seed set for one library but not the others in use.
- **Copy-pasted metric functions** that have since drifted, so two methods are scored by subtly different code.

Over-abstraction (an abstract base class with one implementation, a config system larger than the experiment) does
occur in inherited codebases written by someone else. Collapse it only after the steps below — an interface used by
several real methods is load-bearing even if it looks ornate.

## Procedure

1. List the experiments the paper actually claims. Not the ones that were run — the ones in the draft.
2. For each final number, trace it back to a command and a file. Write what you find down as you go; the gaps are
   the real finding.
3. Keep every code path that produces a claimed number.
4. Reconcile the disagreements found above. If two scripts split or normalize differently, decide which is correct
   and note that the other's numbers must be regenerated.
5. Introduce the pipeline contract from `SKILL.md` around the surviving code, then re-run to reproduce the claimed
   numbers through the new harness. Do not delete anything until the numbers match.
6. Quarantine dead experiments in one directory rather than deleting them outright; delete after the numbers match.
7. Collapse abstractions that no longer serve a real method.

## Do not delete

- Scripts that generated submitted or published numbers.
- Raw data.
- Preprocessing needed to regenerate processed data.
- Exact configs for reported runs.
- Seed and environment records.
- Any interface used by two or more real methods.

## Done when

- One command runs the whole sweep, and re-running it skips work already finished.
- Every number in the paper is produced by `aggregate.py` from stored per-run metrics, not transcribed.
- Every run directory contains the config and git commit that produced it.
- Adding a method touches one file plus one dict line.
- Two runs can never overwrite each other.
- Nothing survives only because it looked architecturally nice.
