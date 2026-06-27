# AGENTS.md — Paper: <PROJECT TITLE>

Orientation for any agent operating on this research-paper vault. This file is
the map and the rules; the actual writing/analysis knowledge lives in the
installed research skills this file routes to. This vault holds the **paper**
(argument, writing, figures, submission). It does **not** hold the experiment
**codebase** — for source layout and runnable experiments use the
`research-codebase` skill in a separate code repo, and keep only experiment
*notes* here.

## What this vault is

A single research paper tracked from idea to submission and artifact release.
One note per experiment, one draft per section, one dashboard for status. The
vault optimises for knowing *what is claimed, what supports it, and what is left
to write* — not for storing data or code.

## Layout

```text
ideas/            # scoping notes, the paper's argument/spine, contribution claims
related-work/     # per-paper literature notes + the synthesized related-work map
experiments/      # one note per experiment: hypothesis, setup, result, verdict
figures/          # figure sources + caption drafts (the visual evidence)
drafts/           # section drafts: abstract, intro, method, results, discussion
data/             # POINTERS to datasets (paths, URLs, licences) — not raw data
submission/       # venue choice, checklist, cover letter, rebuttal
references/       # venue-conventions, notation-and-citation-style, repro-checklist
_dashboard/       # experiment-index, draft-status
```

## Filename conventions

```text
experiments/  exp-{NNN}-{shortname}.md      # exp-001-baseline.md
figures/      fig-{NNN}-{shortname}.{ext}   # fig-003-ablation.pdf  (+ .md caption)
drafts/       {section}.md                  # abstract.md, intro.md, method.md, ...
```

Zero-pad numbers (`exp-001`, not `exp-1`). A figure's caption draft lives next to
it as `fig-003-ablation.md`.

## Experiment note format

Every file in `experiments/` opens with YAML frontmatter so `_dashboard/` can
track status and verdict:

```markdown
---
exp: exp-001
title: linear baseline on benchmark A
status: done            # planned | running | done | abandoned
hypothesis: a linear model is a fair floor for the main metric
result: 0.71 main-metric (vs 0.78 ours)
verdict: supports        # supports | refutes | inconclusive
figures: [fig-001]
date: 2026-06-24
---

## Setup
...

## Result
...

## Reading
What this means for the paper's claim, and what to run next.
```

## Routing

| Folder | Skill to use |
|---|---|
| `ideas/` | `paper-argument-planner` (spine, contribution); `paper-idea-and-scope-brainstormer`, `research-idea-stress-test` upstream |
| `related-work/` | `literature-triangulation` (map) → `related-work-writer` (prose); `citation-auditor` to verify |
| `experiments/` | `experiment-design`, `benchmark-and-baseline-selector`, `hypothesis-and-ablation-planner`, `statistical-testing-guide`, `model-eval-error-analysis` |
| `figures/` | `figure-table-planner` |
| `drafts/abstract.md`, `intro.md` | `abstract-and-intro-writer` |
| `drafts/method.md` | `method-section-writer` |
| `drafts/results.md` | `results-writeup` |
| `submission/` | `venue-targeting`, `submission-readiness-audit`, `reviewer-response-strategist` |
| artifact release | `artifact-release-packager`, `reproducibility-audit` |
| the code itself | `research-codebase` (separate repo) |

Use `flow-paper-lifecycle` to orchestrate the whole sequence when unsure what
comes next.

## Default actions

- **Given a new result:** create `experiments/exp-{NNN}-…md`, fill the
  frontmatter, write the *Reading* tying it back to the paper's claim, and
  update `_dashboard/experiment-index.md`.
- **Asked to draft/revise a section:** use the matching writer skill from the
  routing table and save to `drafts/<section>.md`; never write a section from
  scratch without first checking `ideas/` for the agreed spine.
- **Before submission:** run `submission-readiness-audit` and `citation-auditor`;
  record the venue + checklist state in `submission/`.

## Rules

- **Claims are backed by experiments.** Every contribution claim in `ideas/` or
  `drafts/` must point to an `experiments/` note (or a figure) that supports it.
  If it can't, mark it as unsupported rather than asserting it.
- **No raw data or code here.** `data/` holds pointers only; experiment code
  lives in the `research-codebase` repo. Keep this vault about the *paper*.
- **Notation is consistent.** Follow `references/notation-and-citation-style.md`
  across all drafts; don't let `\citep`/`\citet` or symbol use drift per section.
- **Reproducibility is tracked as you go**, not bolted on at the end — keep
  `references/reproducibility-checklist.md` current per experiment.

## Obsidian formatting rules

A few silent failures: the file saves fine but renders broken in Obsidian. Follow
these whenever you write a note here.

- **Frontmatter must be valid YAML and start on line 1** — nothing before the
  opening `---`, not a title or even a blank line, and no `#` heading above it.
- **Quote wikilinks in frontmatter.** A bare `related: [[other-note]]` is invalid
  YAML and makes Obsidian render the whole block as raw text. Use a quoted list
  on one line: `related: ["[[other-note]]", "[[a-summary]]"]`.
- **Never put a raw `|` in a table cell.** The pipe is the column separator, so an
  aliased wikilink `[[a-note|label]]` splits the cell and corrupts the table
  (stray `label]]` leaks into a phantom column). In a table use an unaliased link
  `[[a-note]]` or escape the pipe as `\|`. Aliased links are fine in prose — just
  never inside a table.
- **Inline math in a table must not contain a bare `|` either, and `\|` does not
  fix it.** The table parser splits the cell on `|` first, so `$d \ll |V|$`
  fragments into phantom columns. And `\|` is the wrong repair: inside `$...$` it
  renders as the norm symbol `‖`, silently changing the meaning. Use the LaTeX
  command for the bar you mean — cardinality / absolute value `|V|` →
  `$\lvert V\rvert$`, norm `\|x\|` → `$\lVert x\rVert$`, conditional `P(u|v)` →
  `$P(u \mid v)$`.
- **A bare `$` in prose can open math mode.** A second `$` later on the same line
  — a price like `$30k … $45k`, "raise $5M" — makes everything between the two
  render as italicised math. Escape literal dollar signs: `\$30k`.
- **`#` without a trailing space is a tag, not a heading.** `#Results`, `#1`, or a
  mid-line `#` (e.g. `C#`) silently becomes a tag. Write `# Heading` with a space,
  or escape it as `\#`.
