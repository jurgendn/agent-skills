---
name: submission-readiness-audit
description: Audit a research paper, draft, appendix, or submission package before deadline. Use this skill whenever the user asks if a paper is ready to submit, wants a pre-submission checklist, needs to find reviewer-obvious weaknesses, check claim/evidence consistency, verify figures and tables are referenced, inspect limitations/ethics/reproducibility statements, or prepare camera-ready materials. This is the final gate after argument planning, experiment analysis, and results writing.
---

# Submission Readiness Audit

The last pass before submission is not another writing pass. It is a risk audit: what would make reviewers distrust the paper, misunderstand the contribution, or find a preventable compliance issue?

## Use this when

- The user has a draft or near-final paper.
- The user asks what is missing before submission.
- The paper needs a checklist against venue or artifact requirements.
- The user wants to catch overclaims, inconsistent numbers, missing references, or appendix drift.
- The user is preparing camera-ready revisions.

## Do not use this when

- The paper argument is still unclear. Use `paper-argument-planner` first.
- The user needs new related work prose. Use `related-work-writer`.
- The user needs artifact packaging rather than paper audit. Use `artifact-release-packager`.

## Workflow

### 1. Identify submission context

Record:

- venue or format if known
- page limit
- anonymity requirements
- required sections or checklists
- artifact/reproducibility expectations
- current draft components available

If the venue is unknown, run a general research-paper audit and mark venue-specific items as unknown.

### 2. Audit claims against evidence

For abstract, introduction, results, discussion, and conclusion:

- list major claims
- identify supporting figure/table/proof/citation
- mark unsupported or overstated claims
- check that conclusion does not exceed results
- check that limitations do not contradict contributions

Unsupported claims should be narrowed, supported, or removed.

### 3. Audit experimental and numerical consistency

Check:

- numbers match between text, tables, captions, and appendix
- metrics are defined consistently
- higher/lower-is-better is clear
- baselines are named consistently
- datasets and splits are described consistently
- statistical uncertainty is reported where it matters
- ablations correspond to claimed mechanisms

### 4. Audit paper mechanics

Check:

- every figure/table is referenced in order
- captions are self-contained
- appendix references resolve
- citations support the sentences they are attached to
- notation is introduced before use
- acronyms are defined
- method names are consistent
- limitations, ethics, and broader impact are present if expected
- anonymization is preserved for double-blind submissions

### 5. Classify blockers

Use severity levels:

- **Blocker** — likely to cause rejection, desk rejection, or serious reviewer distrust.
- **Major** — weakens the paper but may be fixable quickly.
- **Minor** — polish or clarity issue.
- **Venue-specific unknown** — cannot verify without venue requirements.

Do not bury blockers in a long checklist.

## Output format

```markdown
# Submission Readiness Audit

## Verdict
Ready / Not ready / Conditionally ready

## Blockers

## Major issues

## Minor issues

## Claim-evidence consistency
| Claim | Location | Evidence | Status | Fix |
|---|---|---|---|---|

## Figures, tables, and appendix checks

## Venue/checklist items

## Final action list
```

## Quality bar

A good audit should reduce preventable reviewer objections. It should be specific enough that the user can fix issues directly, not just feel vaguely worried.
