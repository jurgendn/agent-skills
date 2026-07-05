---
name: research-codebase
description: |
  Structure and maintain a research codebase for fast hypothesis testing on a single paper. Optimized for local runs, one experiment at a time. Use when starting a new project, organizing experiments, or cleaning up a codebase that has become hard to navigate. Trigger on "how should I structure my code", "set up my project", "organize my experiments", "starting a new paper", "my code is getting messy", "simplify this", "too many abstractions", "I over-engineered it", or "I inherited this codebase". Prevents both directions of failure: (1) adding structure before there is pain to justify it, and (2) deleting abstractions that are actually load-bearing.
---

# Research Codebase

Structure research code so a researcher can go from idea to number quickly, with
results they can trust and reproduce.

Three rules dominate:
- **Keep it simple.** The simplest thing that produces the right number wins.
- **Add structure when the pain justifies it, not before.**
- **Keep the call graph shallow.** Indirection is a cost; pay it only when it buys
  correctness or real reuse.

For the external precedent behind the minimum-viable stance, read
`references/good-enough-practices.md`. For cleanup and refactoring decisions, read
`references/codebase-cleanup-guide.md`.

## Starter Structure

```text
project/
├── data/
│   ├── raw/          # original data, never modified
│   └── processed/    # generated from raw
├── models/           # one file per method
├── train.py          # runs the experiment
├── evaluate.py       # computes metrics
├── utils.py          # only shared code used in 2+ files
├── experiments/      # one .sh file per run
├── outputs/          # ignored by git; logs/checkpoints
├── results/          # tracked final numbers/plots
├── requirements.txt
└── README.md
```

`assets/project-template/` contains this starter skeleton. When starting a new
project, copy it and delete what is not needed.

## Non-Negotiables

- Never modify `data/raw/`.
- Always set and record random seeds.
- Track command-to-result provenance.
- Keep final numbers reproducible from scripts, not notebooks.
- Save final results in `results/`; keep transient outputs in ignored `outputs/`.

## Experiment Scripts

Use one shell script per meaningful run:

```bash
python train.py --model rwgp --seed 1 --output outputs/rwgp_seed1
python evaluate.py --run outputs/rwgp_seed1 --save results/rwgp_seed1.json
```

The filename should describe the experiment, not the iteration:
`ablation_no_overlap.sh`, not `try3.sh`.

## What to Skip Until It Hurts

- CI for a solo prototype.
- Complex package layout.
- Experiment tracking services.
- Abstract config systems.
- Deep class hierarchies.
- Branch-heavy workflows before basic commit discipline exists.

## When to Add Structure

Add only when there is repeated pain:

| Pain | Add |
|---|---|
| same helper copied 3 times | `utils.py` or a small module |
| many models with same interface | `models/base.py` |
| repeated commands | `experiments/*.sh` |
| hard to reproduce numbers | `results/README.md` |
| sharing with collaborators | fuller `README`, `CONTRIBUTING`, license |

## Output

When advising:
- propose the minimal structure;
- identify what to delete or defer;
- name load-bearing abstractions to preserve;
- give command-to-result conventions;
- provide next cleanup steps.
