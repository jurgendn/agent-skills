---
name: figure-table-planner
description: Plan, audit, or revise the figures, tables, captions, and visual evidence for a research paper. Use this skill whenever the user asks what figures or tables they need, whether a result should be a plot or table, how to present experiments, how to design ablation tables, how to make captions self-contained, what belongs in the appendix, or whether the current visual evidence supports the paper's claims. This skill is especially useful after experiment design and before writing the Results section.
---

# Figure Table Planner

Figures and tables are the evidence architecture of a paper. A good paper does not ask readers to infer the argument from a pile of plots; it shows the minimum set of artifacts needed to believe the claims.

## Use this when

- The user has results and needs to decide how to present them.
- A paper draft has too many tables, redundant figures, or unclear captions.
- The main claim lacks a clear visual/table artifact.
- The user needs to split main-paper vs appendix evidence.
- The user wants to plan ablations, diagnostics, failure examples, or scaling plots.

## Do not use this when

- The user needs to decide which experiments to run. Use `experiment-design` or `hypothesis-and-ablation-planner`.
- The user needs prose for the Results section. Use `results-writeup` after the evidence layout is clear.
- The user needs plotting code implementation details unless they explicitly ask for code.

## Workflow

### 1. List the claims first

Before planning visuals, extract the paper claims:

- main empirical claim
- mechanism/ablation claim
- robustness or generality claim
- efficiency or cost claim
- qualitative/failure-mode claim
- theory or conceptual claim

No figure or table should exist without a claim it supports.

### 2. Choose the right artifact type

Use the artifact that makes the comparison easiest to judge:

- **Table** — exact comparisons across methods, datasets, metrics, or ablations.
- **Line plot** — trends over scale, time, data size, compute, or hyperparameters.
- **Bar plot** — small categorical comparisons when exact numbers are less important.
- **Scatter plot** — relationship between two continuous variables.
- **Diagram** — method structure, pipeline, or conceptual contribution.
- **Example grid** — qualitative outputs, failure modes, or interpretability cases.
- **Appendix table** — exhaustive results that support but do not carry the main story.

Prefer tables when readers need exact numbers. Prefer plots when shape or trend is the claim.

### 3. Design the main-paper evidence set

Aim for a compact sequence:

1. **Method or problem diagram** if the contribution is structurally hard to understand.
2. **Main result table/figure** that supports the headline claim.
3. **Ablation table/figure** that supports the mechanism claim.
4. **Robustness or failure analysis** that bounds the claim.
5. **Efficiency/resource artifact** only if efficiency is part of the contribution.

If two artifacts support the same claim in the same way, merge them or move one to appendix.

### 4. Specify caption jobs

A caption should tell the reader what to look for and what the artifact proves.

Caption checklist:

- names the setup and metric
- states the takeaway
- identifies higher/lower is better where relevant
- defines abbreviations
- mentions uncertainty or number of runs if relevant
- does not claim more than the artifact shows

### 5. Check statistical and visual hygiene

Look for:

- missing baselines
- inconsistent metrics
- unclear axes or units
- unreadable labels
- absent confidence intervals/standard deviations when variance matters
- cherry-picked examples
- color-only distinctions without labels
- appendix artifacts referenced nowhere in the main text

## Output format

```markdown
# Figure/Table Plan

## Claim-to-artifact map
| Claim | Artifact | Type | Main/appendix | Status |
|---|---|---|---|---|

## Recommended main-paper sequence

## Appendix evidence

## Caption drafts

## Redundant or missing artifacts

## Visual/statistical risks
```

## Quality bar

A reader should be able to skim the figures, tables, and captions and recover the paper's argument without reading every paragraph.
