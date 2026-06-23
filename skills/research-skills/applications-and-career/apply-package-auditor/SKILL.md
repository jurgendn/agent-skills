---
name: apply-package-auditor
description: Audit a full PhD or research-application package for coherence, missing evidence, narrative consistency, program fit, recommender risk, and deadline priorities. Use this skill whenever the user asks whether their whole application is ready, how to prioritize fixes before deadlines, whether their CV/SOP/research statement/faculty fit/recommenders align, or what weaknesses an admissions committee may notice across materials.
---

# PhD Application Package Auditor

A strong application package is coherent across documents. The CV supplies evidence, the SOP explains trajectory and fit, recommenders validate the claims, and program choices make the research direction credible.

## Use this when

- The user wants a holistic audit of PhD, research master's, fellowship, research internship, RA, or lab application materials.
- The user has multiple materials and needs cross-document consistency checks.
- The user asks what to fix first before deadlines.
- The user wants to identify missing evidence, overclaims, weak fit, recommender risk, or narrative inconsistency.
- The user needs a readiness report rather than a full rewrite of one artifact.

## Do not use this when

- The user wants to write or line-edit a Statement of Purpose. Use `apply-sop-writer`.
- The user wants to build or rewrite an academic CV. Use `apply-cv-builder`.
- The user wants to choose faculty or programs from scratch. Use `apply-program-fit-mapper`.
- The user wants recommender emails or letter strategy only. Use `apply-recommendation-letter-strategist`.
- The user has only one document and wants detailed editing of that document.

## Workflow

### 1. Inventory the package

List available and missing materials:

- CV
- SOP
- research statement
- personal/diversity statement
- writing sample
- transcript or grade context
- publications, preprints, posters, code, datasets, or portfolio links
- target programs, faculty, and deadlines
- recommender list and letter coverage
- test scores or administrative requirements when relevant

If materials are incomplete, audit what is available and mark gaps explicitly.

### 2. Extract the application thesis

Identify the implicit thesis of the application:

- what research area the applicant is entering
- what preparation they have already demonstrated
- what future questions they want to pursue
- why the target program is a credible environment
- what kind of researcher they are becoming

If the materials imply different theses, flag the inconsistency.

### 3. Cross-check evidence

For each major claim, ask:

- Is it supported by CV evidence?
- Is it validated by a recommender?
- Is it connected to faculty/program fit?
- Is it specific enough to be credible?
- Is it overclaimed relative to the applicant's actual record?

Separate admissions-critical problems from polish issues.

### 4. Audit risks

Look for:

- unclear research identity
- generic program fit
- SOP claims not backed by CV entries
- CV evidence not used in narrative
- recommender gaps or redundancy
- missing explanation for transcript anomalies
- unfocused school list
- deadline-driven bottlenecks
- materials that sound like different applicants

### 5. Prioritize fixes

Rank fixes by:

- impact on admissions signal
- deadline urgency
- ease of correction
- dependency on other people, especially recommenders
- whether the issue affects many schools or only one program

## Output format

Use:

```markdown
## Package inventory
| Material | Status | Notes |
|---|---|---|

## Application thesis
[One-paragraph synthesis of the current profile]

## Coherence audit
| Claim / theme | Evidence source | Supported? | Risk | Fix |
|---|---|---|---|---|

## Major risks
1. [Risk]: [why it matters]

## Priority fix list
### Fix now
- [High-impact urgent fix]

### Fix next
- [Important but less urgent fix]

### Nice to have
- [Polish item]

## School-specific notes
- [Program]: [fit or package issue]
```

## Quality bar

A strong audit is candid, specific, and prioritized. It should reveal whether the application tells one credible research story, what evidence is missing, and which fixes matter most before submission.
