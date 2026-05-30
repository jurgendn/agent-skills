---
name: code-simplify
description: |
  Diagnose and reduce complexity in research codebases. Use this skill whenever the user wants to simplify, clean up, or audit code for over-engineering — including phrases like "simplify this", "this is too complex", "I over-engineered it", "help me flatten this", "too many abstractions", "I inherited this codebase", "this is getting hard to navigate", or "I need to clean this up before sharing". Also trigger when the user pastes code that contains config classes wrapping argparse, abstract base class hierarchies with 2 concrete subclasses, registry/factory patterns for models, or dataclasses used as dicts. Prevents the two failure modes: (1) deleting abstractions that are actually load-bearing, and (2) stopping at surface-level cleanup while structural complexity remains.
---

# Code Simplify

Research code accumulates complexity silently. Each decision was locally reasonable. The result is a codebase where changing one hyperparameter requires touching 4 files. This skill cuts the decorative complexity while protecting the load-bearing kind.

**The target is not minimum lines. It's minimum complexity needed to reproduce the paper.**

---

## Step 1: Diagnose before touching anything

Read the code. Produce a **complexity audit** — a ranked list of overhead sources, from highest impact to lowest. Frame each item as:

```
[PATTERN] → [WHAT IT COSTS] → [PROPOSED MOVE]
```

Example:
```
Config class wrapping argparse wrapping a dict
→ Changing one hyperparameter requires editing 3 files
→ Delete config class, use argparse directly in train.py
```

Do not propose rewrites yet. Get the user's agreement on the diagnosis first.

---

## Step 2: Classify each abstraction

For every abstraction in the codebase, classify it as one of:

**Load-bearing** — removing it breaks correctness, reproducibility, or something used in 3+ places.
- Shared `evaluate.py` called by 5 scripts
- `set_seed()` utility
- A base model class that handles checkpointing shared across all variants

**Decorative** — adds indirection without adding correctness. Safe to cut.
- Abstract base class with exactly 2 subclasses that don't share behavior
- Config dataclass that just mirrors argparse args
- `Registry` / `Factory` for models that are never dynamically loaded
- `__init__.py` re-exports that make imports look clean but add 3 files to trace
- Logging infrastructure for a script that runs once

**Ambiguous** — ask the user before touching. Usually things that *look* decorative but might encode a design decision.

Never touch **load-bearing**. Cut **decorative**. Clarify **ambiguous** before acting.

---

## Step 3: Propose a flattening plan

Concrete, ordered moves. Each move is independently reversible. Never propose a full rewrite.

Format:
```
Move 1 [HIGH]: Inline ModelConfig into train.py argparse
  Before: train.py → config.py → ModelConfig → argparse
  After:  train.py → argparse directly
  Files affected: train.py, config.py (delete)
  Risk: none — config.py has no other callers

Move 2 [MEDIUM]: Merge base_model.py into rwgp.py
  Before: base_model.py (80 lines) + rwgp.py (40 lines inheritance)
  After:  rwgp.py (100 lines flat)
  Files affected: rwgp.py, base_model.py (delete), rwgp_overlap.py (update import)
  Risk: low — check rwgp_overlap.py still works after

Move 3 [LOW]: Replace custom logger with print()
  Before: utils/logger.py with handlers, formatters, levels
  After:  print() calls in train.py
  Files affected: utils/logger.py (delete), train.py
  Risk: none
```

Order by impact, not by ease.

---

## Research-specific anti-patterns

These appear constantly in research code. Name them explicitly when found.

**Config class over argparse**
Three layers (dataclass → argparse → dict) for one thing. Cut to argparse only.
```python
# Before
@dataclass
class Config:
    lr: float = 0.01
    epochs: int = 200
config = Config(**vars(parser.parse_args()))

# After
args = parser.parse_args()  # use args.lr, args.epochs directly
```

**Abstract base class with 2 subclasses**
If the two subclasses don't actually share behavior (just an interface), the ABC adds indirection without adding safety. Flatten to two independent files.

**Registry / Factory for static model sets**
```python
MODEL_REGISTRY = {"rwgp": RWGP, "gcn": GCN}
model = MODEL_REGISTRY[args.model]()
```
Useful when models are dynamically loaded or plugin-defined. In a research repo where you know every model at write time: just use an if-statement.

**Pydantic / dataclass for single-use dicts**
If the structured object is created once and passed once, it's a dict with extra steps.

**Logging infrastructure for terminal scripts**
`FileHandler`, `StreamHandler`, `Formatter`, log levels — for a script you run once and watch. Replace with `print()`. Add real logging when you actually need to parse log files.

**`src/` as an installable package**
Unnecessary unless the code is a library. Flat files at the project root are fine for a single-paper repo.

**`experiments/config/` YAML files + a config loader**
Unless you have 10+ variants, shell scripts are simpler and more transparent. The `.sh` file *is* the config.

---

## What not to touch

- **`data/raw/`** — immutable by convention. Never.
- **Anything that affects numerical output** — even if it looks like refactoring. Simplifying a forward pass is a correctness risk.
- **Complex code that's complex because the math is complex** — an 80-line graph kernel isn't over-engineered, it's faithful to the math. Don't flatten it.
- **Things the user explicitly says are intentional** — ask before overriding.

---

## Output modes

Adapt based on what the user provides and what they ask for:

**Full repo** → run the full audit (Steps 1–3), produce a prioritized flattening plan.

**Single file or paste** → skip the audit, go straight to classifying abstractions in that file and proposing inline simplifications.

**"Just tell me what's wrong"** → produce the diagnosis only (Step 1), no proposals yet.

**"Fix it"** → produce the plan and rewrite the affected files. Preserve comments that explain *why* something works, not just *what* it does.

---

## Stopping criterion

Stop simplifying when:
- Every script can be understood top-to-bottom without jumping to another file (except genuine utilities used in 3+ places)
- Changing one hyperparameter touches at most 1 file
- The full experiment can be reproduced by reading `experiments/*.sh` + `train.py`

If the user pushes for more cuts after this point, name the stopping criterion explicitly: *"Further cuts would remove load-bearing abstractions. The complexity that remains is there for a reason."*
