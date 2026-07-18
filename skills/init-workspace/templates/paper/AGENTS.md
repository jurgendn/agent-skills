# AGENTS.md — Paper: <PROJECT TITLE>

Orientation for any agent operating on this research-paper vault. This file is
the map and the rules; the actual writing/analysis knowledge lives in the
installed research skills this file routes to. This vault holds the **paper**
(argument, writing, figures, submission). It does **not** hold the experiment
**codebase** — for source layout and runnable experiments use the
`research-codebase` skill in a separate code repo, and keep only experiment
*notes* here.

## Operating contract

Read this before doing any work in this vault. Where a rule here conflicts with
your own default behavior, this file wins. This makes the vault behave the same
across agents instead of varying with each one's defaults.

- **This is research work, not coding.** Produce research artifacts — notes,
  synthesis, drafts, claims. Do **not** write code, scripts, or notebooks unless
  the user explicitly asks. `data/` holds pointers; experiment code lives in a
  separate repo.
- **Substantial artifacts go through the pipeline — in one file.** For any
  artifact a reader will rely on (a section draft, a synthesis note), run the
  four-pass pipeline in `agents/pipeline.md` — **evidence → draft → review →
  verify** — inside the artifact's own file: ground evidence in `related-work/`
  + `experiments/` + `figures/` + `references/`, draft from it, critique claims
  that outrun it, then anchor every claim to a source. The pipeline produces
  exactly one file; never create per-stage side files. Small notes skip the
  pipeline (the rules below still apply).
- **Synthesis is source-grounded.** Every factual claim links to a source (a
  `related-work/` note, an `experiments/` note, a `figures/` id, or a
  `references/` file). A claim with no source is not done.
- **Mark uncertainty explicitly.** Separate established results from inference.
  Tag anything not directly source-backed as `(inference)` or `#unverified`, and
  say what evidence would settle it. Never present speculation as fact.
- **Report what you actually did, not what you intended.** Before marking a step,
  section, or check done, point to the artifact or source that shows it. If a step
  was skipped or a result is unverified, say so plainly — never present intended,
  plausible, or in-progress work as completed.
- **Check inputs before running a skill; ask for what's missing.** Each skill/stage
  draws from specific folders (see *Layout*) — `ideas/` for the spine,
  `related-work/` for literature, `experiments/` for results, `figures/` for
  visuals. Before running one, confirm its input folder(s) actually contain the
  needed notes; if a required input is empty or missing, **stop and ask the user to
  add it (or say where it lives) — do not proceed on an empty folder or fabricate
  the input.**

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
references/       # venue-conventions, reviewer-risk-checklist, notation/citation, repro-checklist
agents/           # pipeline.md: evidence → draft → review → verify (one file)
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
| `drafts/` full-paper drafting | `paper-writer` (coordinates the writing phase and delegates section specialists) |
| `drafts/abstract.md`, `intro.md` | `abstract-and-intro-writer` for isolated abstract/intro work |
| `drafts/method.md` | `method-section-writer` |
| `drafts/results.md` | `results-writeup` |
| `submission/` | `venue-targeting`, `submission-readiness-audit`, `professor-critic` (adversarial Reviewer-2 pass on the draft), `reviewer-response-strategist` |
| artifact release | `artifact-release-packager`, `reproducibility-audit` |
| the code itself | `research-codebase` (separate repo) |

Use `flow-paper-lifecycle` to orchestrate the whole sequence when unsure what
comes next.

## Default actions

- **Given a new result:** create `experiments/exp-{NNN}-…md`, fill the
  frontmatter, write the *Reading* tying it back to the paper's claim, and
  update `_dashboard/experiment-index.md`.
- **Asked to draft/revise the paper or multiple sections:** run the four-pass
  pipeline (`agents/pipeline.md`) in each section file under `drafts/`: ground
  in `ideas/` + `related-work/` + `experiments/` + `figures/`, draft, critique,
  verify every claim against a source — using `paper-writer` to coordinate the
  writing phase.
- **Asked to draft/revise one narrow section:** run the four-pass pipeline
  (`agents/pipeline.md`) in `drafts/<section>.md`, grounding in `ideas/` +
  `experiments/` and using the matching writer skill from the routing table for
  the draft pass. Never draft a section before checking `ideas/` for the agreed
  spine.
- **Before submission:** run `submission-readiness-audit` and `citation-auditor`;
  use `references/reviewer-risk-checklist.md` to catch OpenReview-era reviewer
  objections; then run an adversarial reviewer pass with `professor-critic`
  (reader: "Reviewer 2 at the target venue"; bar: accept/major-revision/reject)
  and resolve any FATAL before submitting. Record the venue + checklist state in
  `submission/`.

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
- **Reviewer risk is tracked before submission.** Use
  `references/reviewer-risk-checklist.md` to check claim support, novelty,
  baselines, reproducibility, limitations/ethics, data attribution, and rebuttal
  readiness before the final audit.
- **Every claim is source-grounded and uncertainty is marked** (see *Operating
  contract*): no unsourced factual claim, and inference is tagged `(inference)` /
  `#unverified` rather than stated as fact.

## Obsidian formatting rules

A few silent failures: the file saves fine but renders broken in Obsidian. Follow
these whenever you write a note here.

- **Frontmatter must be valid YAML and start on line 1** — nothing before the
  opening `---`, not a title or even a blank line, and no `#` heading above it.
- **Quote wikilinks in frontmatter.** A bare `related: [[other-note]]` is invalid
  YAML and makes Obsidian render the whole block as raw text. Use a quoted list
  on one line: `related: ["[[other-note]]", "[[a-summary]]"]`.
- **Quote any frontmatter value that contains a colon** (and values starting with
  `[`, `{`, `#`, `@`, `` ` ``, `!`, `&`, `*`, `>`, `|`, or a quote). A colon-space
  inside an unquoted value — most often a paper title with a subtitle,
  `title: Stochastic Blockmodels: First Steps` — makes YAML read it as a nested
  key, so the whole block fails to parse and renders as raw text. Wrap the value
  in double quotes: `title: "Stochastic Blockmodels: First Steps"`. The same goes
  for `authors`, `aliases`, or any field whose value has a `:` in it.
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
