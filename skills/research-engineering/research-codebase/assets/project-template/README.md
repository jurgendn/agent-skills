# Project Name

One sentence: what question this answers.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python sanity_check.py        # four checks; run this first, and after any change
python run.py --prototype     # tiny sweep: exercises the whole pipeline cheaply
python run.py                 # the full sweep; finished runs are skipped
python aggregate.py           # outputs/ -> results/table.csv and results/table.tex
```

`python run.py` is the single command that re-runs every experiment in the paper.

## Where things live

| File | Role | You edit it when |
|---|---|---|
| `configs.py` | the experiment plan | running more experiments |
| `data.py` | config + seed -> one instance | changing the data or generator |
| `algorithms/` | one file per method, registered in `__init__.py` | adding a method |
| `metrics.py` | `metric(result, data) -> float` | adding a number to report |
| `run.py` | the runner | never |
| `aggregate.py` | runs -> paper table | never |
| `outputs/` | one directory per run (git-ignored) | never by hand |
| `results/` | the generated table (tracked) | never by hand |

Adding an experiment is one entry in `configs.py`. Adding a method is one file plus
one line in `algorithms/__init__.py`. Nothing else changes.

## Provenance

Every run directory holds `config.json` (params, seed, git commit, argv) and
`metrics.json`. Every number in `results/table.csv` is computed from those files, so
no result is ever transcribed by hand and every one traces back to a commit.

`data/raw/` is read-only. Derived data goes to `data/processed/`.
