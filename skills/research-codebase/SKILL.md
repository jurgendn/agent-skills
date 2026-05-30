---
name: research-codebase
description: |
  Structure and maintain a research codebase for fast hypothesis testing on a single paper. Optimized for local runs, one experiment at a time. Use when starting a new project, organizing experiments, or cleaning up a codebase that has become hard to navigate. Trigger on "how should I structure my code", "set up my project", "organize my experiments", "starting a new paper", "my code is getting messy", "simplify this", "too many abstractions", "I over-engineered it", or "I inherited this codebase". Prevents both directions of failure: (1) adding structure before there is pain to justify it, and (2) deleting abstractions that are actually load-bearing.
---

# Research Codebase

The user is a mathematician or researcher, not a software engineer. Structure the code so they can go from idea to number as fast as possible, with results they can trust and reproduce.

Three rules above all:

- **KISS — Keep it simple, stupid.** The simplest thing that produces the right number wins. Clever is a liability when you have to debug it at 2am the night before a deadline.
- **Add things when you feel the pain of not having them, not before.**
- **Keep the call graph shallow.** A reader should understand any script top-to-bottom without jumping between four files. Indirection is a cost; pay it only when it buys correctness or real reuse.

The first rule sets the taste. The second prevents premature scaffolding. The third prevents the scaffolding that does get added from sprouting layers.

---

## The structure

```
project/
├── data/
│   ├── raw/          ← original data, never modified
│   └── processed/    ← cleaned/derived from raw
│
├── models/           ← one file per method you're comparing
│   ├── rwgp.py
│   └── rwgp_overlap.py
│
├── train.py          ← runs the experiment
├── evaluate.py       ← computes metrics
├── utils.py          ← shared functions (add only when used in 2+ files)
│
├── experiments/      ← one .sh file per experiment
│   ├── baseline.sh
│   └── ablation_no_overlap.sh
│
├── outputs/          ← ignored by git; logs, checkpoints
├── results/          ← saved to git; final numbers and plots
│
├── requirements.txt
└── README.md
```

That's it. Don't add folders you don't have content for yet.

**Naming files in `models/`**: name each file after what the method *is*, not what iteration it is. `rwgp_overlap.py`, not `model_v2.py`. Git tracks versions — the filename should tell you what the method does.

---

## Three rules that are never optional

**1. Never modify raw data.**
`data/raw/` is read-only. Everything writes to `data/processed/` or `outputs/`. If raw data gets corrupted, the error is silent until your results are wrong and you can't tell why.

**2. Always set a random seed.**
Put this at the top of `train.py` and always pass the seed from the command line:

```python
import random, numpy as np, torch

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
```

```bash
python train.py --seed 42
```

An unseeded result cannot be reproduced. It cannot be defended to a reviewer.

**3. Every number in the paper maps to one command.**
Write it down in `results/README.md` as you go, not after submission:

```
Table 2, Row 1: python train.py --dataset cora --seed 42 --lr 0.01
Table 2, Row 2: python train.py --dataset citeseer --seed 42 --lr 0.01
```

When Reviewer 2 asks you to rerun with a different metric six months later, this file is the answer.

---

## Experiments as shell scripts

One `.sh` file per experiment. The script *is* the configuration — no YAML, no config loader needed:

```bash
# experiments/ablation_no_overlap.sh
python train.py \
  --dataset cora \
  --seed 42 \
  --no-overlap \
  --lr 0.01 \
  --epochs 200
```

Switch to a config file only when you have more than ~10 experiment variants.

## Output naming

Name output folders by what produced them:

```python
output_dir = f"outputs/{args.dataset}_seed{args.seed}_lr{args.lr}"
```

Never use `output_final/`, `output_v3/`, `output_new/`. Two runs with different settings should never overwrite each other.

---

## What to skip

- **A `src/` folder.** Not needed for a single-paper repo. Flat files at the root are fine.
- **Experiment tracking tools** (Weights & Biases, MLflow). Add only when comparing dozens of parallel runs. For now, `results/README.md` is enough.
- **Unit tests.** Write `sanity_check.py` instead — 20 lines that check loss decreases in the first few steps and output shapes are right. Run it after big changes.
- **Jupyter notebooks for final results.** Fine for exploration. Never put a paper number in a notebook — reproduce it from a script first.

---

## Code style that pays off

A short list of low-cost habits that earn back their effort. These are not generic best practices — each one prevents a specific failure mode that's common in research code.

**Type hints on functions that pass arrays and tensors around.**
The biggest source of silent bugs in math-heavy code is shape confusion: is this `[N, d]` or `[N, N]`? Is this a `Tensor` or a `np.ndarray`? A hint makes the answer readable without running the code.

```python
# Avoid
def diffusion_distance(P, t):
    ...

# Prefer
def diffusion_distance(P: np.ndarray, t: int) -> np.ndarray:
    """P: [N, N] transition matrix. Returns [N, N] distance matrix."""
    ...
```

Shapes in the docstring (or as a comment) catch what type hints alone can't. You don't need to hint every loop variable — focus on function signatures and anything that crosses a file boundary.

**Docstrings on the public functions, not on every helper.**
One sentence on what it computes, plus the shapes if it's array-valued. Skip the `:param:` / `:return:` rituals unless you're publishing a package.

**Meaningful names for the things the math cares about.**
`transition_matrix` not `P` in code (use `P` in math, but in code the variable lives longer than your memory of it). `n_communities` not `k`. The exception: established notation that everyone in the field reads as a name — `lambda_max`, `alpha`, `epsilon` are fine.

**`f"..."` strings for output paths and log messages.** Concatenation with `+` and `%`-formatting are both prone to silent type errors.

---

## Patterns to avoid

These look professional and accumulate easily. In a single-paper repo they almost always add indirection without adding correctness. Name them when you see them — in your own code or someone else's.

**Config class wrapping argparse**
Three layers (dataclass → argparse → dict) for one thing. Use argparse only.
```python
# Avoid
@dataclass
class Config:
    lr: float = 0.01
    epochs: int = 200
config = Config(**vars(parser.parse_args()))

# Prefer
args = parser.parse_args()   # use args.lr, args.epochs directly
```

**Abstract base class with two subclasses that don't actually share behavior**
If the ABC only enforces an interface and the two implementations share no code, the abstraction adds indirection without adding safety. Flatten to two independent files in `models/`.

**Registry / Factory for a static set of models**
```python
MODEL_REGISTRY = {"rwgp": RWGP, "gcn": GCN}
model = MODEL_REGISTRY[args.model]()
```
Useful when models are dynamically loaded or plugin-defined. In a research repo where every model is known at write time: an `if`-statement in `train.py` is clearer and shorter.

**Dataclass / Pydantic for single-use dicts**
If a structured object is created once and passed once, it's a dict with extra steps.

**Logging infrastructure for terminal scripts**
`FileHandler`, `StreamHandler`, `Formatter`, log levels — for a script you run once and watch in the terminal. `print()` is fine. Add real logging when you actually need to parse log files.

**`__init__.py` re-exports that hide the import path**
`from models import RWGP` looks cleaner than `from models.rwgp import RWGP`, but now finding `RWGP` means opening `models/__init__.py` first. For a small repo, the explicit path is friendlier to a reader.

**YAML config files for under ten experiments**
A `.sh` file is more transparent and equally short. Switch to YAML when the shell scripts start duplicating large blocks of arguments.

---

## When to add something new

| You feel this pain... | Then add... |
|---|---|
| Same 10 lines copy-pasted in 3 files | `utils.py` |
| Too many experiment `.sh` files to track | `configs/base.yaml` + command-line overrides |
| Can't tell which run produced which number | `outputs/<name>/run_record.json` with settings + git commit hash |
| Sharing the repo with someone | Expand `README.md` with setup steps and one working example |
| Submitting to a conference | Pin `requirements.txt`, write the exact reproduction command |

---

## When the code already got messy

If the project is past the starting point and now feels hard to navigate, don't refactor by reflex. Work in three short passes.

**Pass 1 — Audit, don't touch.**
Read through the repo and list the indirections that cost you the most. One line each:

```
[pattern]  →  [what it costs]  →  [proposed move]
```

Example:
```
Config class wrapping argparse  →  changing one hyperparameter touches 3 files  →  delete config.py, use argparse directly
ABC ModelBase with 2 subclasses  →  no shared behavior, just an interface  →  inline into rwgp.py and rwgp_overlap.py
utils/logger.py with handlers   →  script runs once in terminal  →  replace with print()
```

Order by impact, not by ease.

**Pass 2 — Classify each abstraction before cutting.**

- **Load-bearing** — removing it breaks correctness, reproducibility, or something used in 3+ places. *Never cut.* Examples: `set_seed()`, `evaluate.py` called by multiple scripts, a checkpointing helper shared across all model variants.
- **Decorative** — adds indirection without adding correctness. *Safe to cut.* Most of the patterns above.
- **Ambiguous** — looks decorative but might encode a design decision you've forgotten. *Ask first.*

**Pass 3 — Propose ordered, independently reversible moves.**
Never propose a full rewrite. Each move should be small enough to undo with one `git revert`.

```
Move 1: Inline ModelConfig into train.py argparse
  Files: train.py (edit), config.py (delete)
  Risk: none — config.py has no other callers

Move 2: Merge base_model.py into rwgp.py
  Files: rwgp.py (edit), base_model.py (delete), rwgp_overlap.py (update import)
  Risk: low — re-run sanity_check.py after
```

---

## What never to touch when simplifying

- **`data/raw/`** — immutable by convention.
- **Anything that changes numerical output.** Even if it looks like a pure refactor. Simplifying a forward pass is a correctness risk, not a style change. If you must touch it, re-run a known-good experiment and compare to the previous result before committing.
- **Code that is complex because the math is complex.** An 80-line graph kernel isn't over-engineered — it's faithful to the math. Don't flatten it.
- **Anything the original author marked as intentional.** Ask before overriding.

---

## When you've simplified enough

Stop when:

- Every script can be read top-to-bottom without jumping to another file (except for genuine utilities used in 3+ places).
- Changing one hyperparameter touches at most one file.
- The full set of paper results can be reproduced from `experiments/*.sh` + `train.py`.

Past this point, further cuts start removing load-bearing abstractions. The complexity that remains is there for a reason.

---

## The only README you need right now

```markdown
# Project Name

One sentence: what this is.

## Setup
pip install -r requirements.txt

## Run
python train.py --dataset cora --seed 42

## Results
See results/README.md
```

Expand it when you share the repo. Not before.
