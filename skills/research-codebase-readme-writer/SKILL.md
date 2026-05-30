---
name: research-codebase-readme-writer
description: |
  Write or audit a README.md for a research repository. Use this skill whenever the user wants to write, improve, fix, or review a README for a research codebase — including phrasings like "write my README", "what should my README say", "is my README good", "help me document my repo", "my README is just a usage example", or "I need to share this repo". Also trigger when the user has just set up a research codebase (e.g. after using research-codebase skill) and hasn't written a README yet. Prevents the two most common failure modes: (1) the one-example README that looks complete but can't actually reproduce any paper result, and (2) the motivation-first README that explains the research but not the code.
---

# README Writer for Research Repos

The README has one job: let someone (including you in 6 months) reproduce the main result without asking a question.

Everything else is secondary.

## Two failure modes to prevent

**Failure mode 1 — The decorative README.**
Has a title, a usage example, and a citation block. Looks like a README. Can't actually reproduce Table 2 because the data download step is missing, the argument name changed, and nobody knows which script maps to which paper claim.

**Failure mode 2 — The motivation README.**
Two paragraphs on why the problem matters, zero information on where the dataset goes or how long training takes. Written for a reader of the paper, not a runner of the code.

---

## What to produce

Generate a `README.md` with exactly these sections, in this order. Skip a section only if it genuinely doesn't apply — don't pad.

### 1. One-line claim (no header, top of file)

The actual claim the repo supports, not a description of the paper. Concrete and falsifiable.

```
# RWGP-DFL-Overlap

Overlapping community detection via random-walk graph partitioning with dynamic fuzzy labels.
Reproduces Table 2 and Figure 3 from [Paper Title, Venue Year].
```

Not: *"Code for our paper on community detection."*

### 2. Reproduce the main result

The most important section. Three commands or fewer. Include expected output and approximate runtime.

```markdown
## Reproduce main result

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Download / generate data
bash data/download_lfr.sh   # or: python data/generate_lfr.py --mu 0.5 --seed 42

# 3. Run
bash experiments/lfr_mu0.5.sh
# → results/lfr_table2.csv (~12 min on CPU, ~2 min on GPU)
# Expected: NMI ≈ 0.83, F1 ≈ 0.79 (Table 2, row μ=0.5)
```
```

If there is no single "main result," reproduce the one most likely to be requested by a reviewer.

### 3. Results map

Link paper claims to commands. This is what separates a research repo from a code dump.

```markdown
## Results

| Claim | Script | Output | Runtime |
|---|---|---|---|
| Table 2 | `experiments/lfr_mu0.5.sh` | `results/lfr_table2.csv` | ~12 min |
| Figure 3 | `experiments/temporal_coherence.sh` | `results/fig3.png` | ~5 min |
| Ablation (no overlap) | `experiments/ablation_no_overlap.sh` | `results/ablation.csv` | ~8 min |
```

### 4. Project layout

One line per folder. Purpose, not content.

```markdown
## Layout

```
data/raw/        ← original datasets, never modified
data/processed/  ← derived; regenerable from raw
models/          ← one file per method variant
experiments/     ← one .sh file per experiment (these are the configs)
outputs/         ← gitignored: logs, checkpoints
results/         ← committed: final numbers and plots
results/README.md ← maps every table row to the exact command that produced it
```
```

### 5. Setup

Exact, not aspirational. If it has ever broken on a fresh machine, document the fix.

```markdown
## Setup

Python 3.10+

```bash
pip install -r requirements.txt
```

**Non-pip dependencies** (if any):
- `torch-scatter`: install via `pip install torch-scatter -f https://data.pyg.org/whl/torch-2.0.0+cpu.html`
```

### 6. Data

Where does it come from? Is it committed, downloaded, or generated? Include the seed if synthetic.

```markdown
## Data

**LFR benchmarks**: generated synthetically — `python data/generate_lfr.py --seed 42`
generates the exact graphs used in Table 2.

**SNAP datasets**: downloaded via `bash data/download_snap.sh` (requires internet, ~200 MB).

Raw data is never overwritten by any script. See `data/raw/README.md` for provenance.
```

### 7. Known issues / sharp edges

What doesn't work, what's slow, what requires a non-obvious flag.

```markdown
## Known issues

- Training on CPU is 6× slower; use `--device cuda` if available.
- `evaluate.py` with `--metric conductance` requires the `igraph` backend: `pip install python-igraph`.
- LFR generation with μ > 0.7 can fail (~5% of seeds); rerun with a different `--seed`.
```

---

## Process

### If the user has an existing README

Read it. Identify which sections are missing or broken, starting from the results map — that's almost always the gap. Rewrite or extend, don't just annotate.

### If the user is starting from scratch

Ask for:
1. The paper's main quantitative claim (one sentence)
2. The script that produces it and its expected output
3. Whether data is committed, downloaded, or generated
4. Any non-obvious setup steps that have broken before

You can infer the rest from the codebase if they share it, or generate placeholders they fill in.

### If the user just wants a quick skeleton

Give them the full template with `[TODO]` markers in the right places. Don't make them think about structure — just hand them something they can fill in.

---

## What to leave out

- **Abstract / motivation.** That's the paper. The README is for running the code.
- **Installation of standard packages.** `pip install -r requirements.txt` covers it.
- **Contribution guidelines.** Single-author research repos don't need them.
- **Badges.** Optional. Add only if CI actually runs.
- **Changelog.** Lives in `CHANGELOG.md`, not the README.

---

## Acid test

Before finalizing, mentally simulate: someone clones the repo on a fresh machine. Can they reproduce the main result using only the README, without asking the author a single question? If yes: done. If no: the gap is the next thing to write.
