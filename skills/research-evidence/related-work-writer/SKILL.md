---
name: related-work-writer
description: Write or revise a Related Work section from a source-grounded literature map, annotated bibliography, paper list, or draft. Use this skill whenever the user asks to write related work inside an original research paper, position a paper against prior work, organize citations into themes, explain how their work differs from baselines or prior methods, avoid citation laundry lists, or calibrate novelty claims. This skill assumes the user has sources or a literature map; if they need to discover and verify the literature first, use literature-triangulation before this skill. If the user wants to write a standalone survey, tutorial, review, or perspective paper whose main contribution is the synthesis itself, use survey-paper-writer instead.
---

# Related Work Writer

Related work is not a bibliography in paragraph form. It is the part of the paper that teaches the reader which intellectual neighborhood the contribution belongs to and why the current paper is still needed.

## Use this when

- The user has papers, notes, or a source map and wants Related Work prose.
- A draft reads like a citation laundry list.
- The user needs to position their work without overstating novelty.
- The user wants to group prior work thematically.
- The paper needs fair contrasts against baselines, methods, datasets, or theory lines.

## Do not use this when

- The literature has not been gathered or checked. Use `literature-triangulation` first.
- The user is writing a standalone survey, tutorial, review, or perspective paper. Use `survey-paper-writer`.
- The user needs the whole paper argument. Use `paper-argument-planner`.
- The user only needs BibTeX formatting or citation cleanup.

## Workflow

### 1. Inventory the source material

For each source or group of sources, identify:

- What problem it addresses.
- What method, theory, benchmark, or finding it introduced.
- How it relates to the user's paper.
- What limitation or open question remains.
- Whether the contrast is supported by the source or inferred.

If a claim about prior work is not grounded in a provided or verifiable source, mark it as needing citation support.

### 2. Choose the organizing principle

Pick the structure that best supports the paper's argument:

- **By problem lineage** — when the field evolved through successive problem formulations.
- **By method family** — when techniques are the main contrast.
- **By evidence/benchmark** — when evaluation practice is the key issue.
- **By theory vs empirical work** — when the paper bridges or separates them.
- **By limitation** — when the current paper targets a specific gap.

Avoid chronological ordering unless the chronology itself explains the gap.

### 3. Write contrast fairly

Use calibrated language:

- Prefer: “Closest to our work is X, which studies Y; our setting differs in Z.”
- Prefer: “Prior work establishes A, but leaves B unresolved.”
- Avoid: “No prior work has considered...” unless the evidence is very strong.
- Avoid: dismissive contrasts that make prior work sound foolish.

The goal is to make the contribution look necessary, not to make prior work look bad.

### 4. Control citation density

Each paragraph should have a conceptual job. Citations support that job.

Good paragraph pattern:

1. Topic sentence naming the line of work.
2. Representative citations grouped by role.
3. What that line establishes.
4. How the current paper differs or builds on it.

Do not attach a citation to every sentence if one grouped citation set can support the paragraph.

### 5. Preserve uncertainty

If the source map has disagreements, say so. If the boundary between this work and prior work is subtle, explain the subtlety. Reviewers trust precise distinctions more than loud novelty claims.

## Output format

When drafting a section, return:

```markdown
# Related Work Draft

[Draft prose]

## Structure rationale

## Citation gaps or claims needing verification

## Novelty-risk notes
```

When auditing an existing section, return:

```markdown
# Related Work Audit

## What works

## Citation laundry-list issues

## Unfair or overbroad contrasts

## Missing lines of work

## Suggested rewrite plan
```

## Quality bar

A good Related Work section lets a skeptical reviewer say: “They understand the field, they represented my area fairly, and the distinction they claim is specific enough to evaluate.”
