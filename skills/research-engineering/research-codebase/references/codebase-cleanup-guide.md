# Codebase Cleanup Guide

Use this when a research codebase has become hard to navigate or over-engineered.

## Patterns to Avoid

- `model_v2_final.py` filenames.
- Abstract base classes with one implementation.
- Config systems more complex than the experiment.
- Utility modules filled with unrelated functions.
- Notebooks as the only source of paper numbers.
- Hidden preprocessing inside training scripts.
- Results whose generating command is unknown.

## Simplification Procedure

1. Identify the paper's actual experiments.
2. Trace each final number back to a command.
3. Keep code paths that produce final numbers.
4. Delete or quarantine dead experiments.
5. Collapse unused abstractions.
6. Preserve load-bearing interfaces used by multiple real methods.
7. Write a minimal `results/README.md`.

## What Not to Touch

Do not delete:
- scripts that generated submitted or published numbers;
- raw data;
- preprocessing scripts needed to regenerate processed data;
- exact configs for reported runs;
- seed and environment records.

## "Simplified Enough" Test

The codebase is simple enough when:
- a new run starts from one script;
- a final number points to one command and one output file;
- a new method can be added without editing unrelated modules;
- a reader can understand the main path in one sitting;
- no abstraction exists only because it seemed architecturally nice.

## Minimal README

```markdown
# Project Name

## Setup
pip install -r requirements.txt

## Run
bash experiments/baseline.sh

## Results
See results/README.md for command-to-number mapping.
```
