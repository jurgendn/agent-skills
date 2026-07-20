---
name: survey-paper-writer
description: Write, plan, or revise standalone survey, tutorial, review, or perspective papers whose main contribution is synthesizing a research area. Use when the user asks to write a survey paper, tutorial paper, review article, perspective article, field overview, taxonomy paper, roadmap, or future-directions paper; needs to turn many papers into a coherent synthesis; wants survey structure, taxonomy design, inclusion/exclusion criteria, visual field maps, tables, tutorial examples, or open-problem sections. If the user only needs a Related Work section inside an original research paper, use related-work-writer instead. If the literature has not been discovered or checked, use literature-triangulation first.
---

# Survey Paper Writer

A survey paper is not an expanded Related Work section. Its contribution is the
map itself: the taxonomy, synthesis, tutorial framing, critical comparison, and
research agenda that help a reader understand a field.

Use `references/survey-paper-craft.md` when designing the structure, figures,
tables, or future-directions section.

## When Not to Use

- The user needs 2-4 paragraphs of Related Work for their own method paper → use
  `related-work-writer`.
- The user has not gathered or verified the literature → use
  `literature-triangulation` first.
- The user only wants citation correctness → use `citation-auditor`.

## Workflow

### 1. Define the survey's contribution

Before drafting, state what the survey adds:
- **Taxonomy:** a clearer organization of a messy field.
- **Tutorial:** an accessible path into a technical area.
- **Critical synthesis:** what works, what fails, and why.
- **Perspective / roadmap:** open problems, trends, and future directions.
- **Benchmark / resource map:** datasets, metrics, tools, and evaluation practice.

Reject vague scopes like "survey all of deep learning for X." Narrow by problem,
method family, application setting, time window, or unresolved tension.

### 2. Audit the source base

Require a source map or paper list. Check:
- canonical early papers;
- recent high-impact papers;
- surveys/tutorials already in the area;
- negative, dissenting, or limitation-focused papers;
- benchmarks, datasets, and code resources;
- adjacent-field terminology that may hide relevant work.

If the source base is thin or one-cluster, stop and route to
`literature-triangulation`.

### 3. Choose the organizing axis

Pick one primary axis and keep it consistent:
- problem/task taxonomy;
- method-family taxonomy;
- data/benchmark/evaluation taxonomy;
- historical phases;
- application scenarios;
- assumptions/failure modes;
- theory-to-practice gap.

Use secondary axes only in tables or subsections. A survey with several competing
taxonomies reads like a pile of notes.

### 4. Build the evidence artifacts

Most strong surveys need visual and tabular artifacts:
- a taxonomy figure that defines the field's main branches;
- a comparison table with methods, assumptions, datasets, metrics, and limitations;
- a timeline only when chronology explains conceptual change;
- a benchmark/resource table when evaluation practice is central;
- a future-directions table mapping open problems to concrete evidence gaps.

Every artifact should teach a decision-relevant distinction, not decorate the
paper.

### 5. Draft synthesis, not bibliography

For each section:
1. State the conceptual question the section answers.
2. Group papers by role, not one paragraph per paper.
3. Explain what the group establishes.
4. Compare assumptions, evidence, and limitations.
5. End with what remains unresolved.

Avoid exhaustive citation laundry lists. Exhaustiveness belongs in the search
protocol or appendix; the main text should compress the field into usable
structure.

### 6. Write the future agenda

Open problems must be specific enough to act on:
- what is unknown;
- why current methods/evidence do not settle it;
- what experiment, theorem, dataset, benchmark, or tool would make progress;
- who would care if the problem were solved.

Do not write generic directions such as "more robust models are needed" unless
they are tied to concrete failure modes.

## Output Format

For planning:

```markdown
# Survey Paper Plan

## Scope and contribution
## Audience
## Source-base audit
## Proposed taxonomy
## Section outline
## Figures and tables
## Future-directions plan
## Missing literature / risks
```

For drafting or revision:

```markdown
# Survey Paper Draft / Revision

## Revised structure
## Draft prose
## Artifact plan
## Citation and coverage gaps
## Overclaiming / synthesis risks
```

## Quality Bar

A good survey lets a newcomer enter the field, lets an expert see a sharper
organization than they had before, and makes the next research questions more
concrete. It should be useful even to readers who already know many of the cited
papers.
