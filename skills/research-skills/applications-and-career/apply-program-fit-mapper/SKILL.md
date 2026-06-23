---
name: apply-program-fit-mapper
description: Map PhD applicant research interests to faculty, labs, departments, and program-fit evidence before writing school-specific application materials. Use this skill whenever the user asks which professors or programs fit their interests, how to shortlist schools, how to compare faculty fit, how to turn interests into searchable research themes, or how to prepare school-specific fit notes for SOPs.
---

# PhD Program Fit Mapper

Good program fit is not name-dropping. It is a grounded match between the applicant's preparation, future research questions, and the intellectual environment of specific faculty, labs, and departments.

## Use this when

- The user is choosing PhD programs, departments, labs, or advisors.
- The user wants to map their interests to faculty or research groups.
- The user asks whether a professor is a strong, medium, or weak fit.
- The user needs school-specific fit notes before writing an SOP.
- The user wants a balanced shortlist based on research fit rather than prestige alone.

## Do not use this when

- The user wants to write the SOP itself. Use `apply-sop-writer`.
- The user wants a broad literature review not tied to application fit. Use `literature-triangulation`.
- The user wants to audit a finished application package. Use `apply-package-auditor`.
- The user wants CV structure or bullet rewriting. Use `apply-cv-builder`.

## Workflow

### 1. Extract the applicant's research direction

Identify:

- target field and subfield
- concrete research questions or themes
- prior projects and methods
- preferred theory/empirical/system-building balance
- constraints: country, funding, geography, deadlines, degree type
- target programs or faculty already under consideration

If interests are vague, turn them into several searchable themes instead of forcing one narrow topic.

### 2. Define fit criteria

Use criteria such as:

- topic overlap with the applicant's future questions
- methodological overlap with prior preparation
- active recent work by the faculty or lab
- room for the applicant to contribute something specific
- departmental ecosystem: multiple relevant faculty, seminars, centers, collaborators
- evidence quality: papers, lab pages, grants, student placements, recent projects
- risk factors: inactive advising, weak overlap, only one possible advisor, outdated webpages

Separate strong evidence from assumptions that need verification.

### 3. Classify fit

For each professor, lab, or program, classify:

- **Strong fit**: clear topic and method overlap, active work, multiple concrete bridges to applicant's background.
- **Medium fit**: plausible overlap but needs more evidence or has partial mismatch.
- **Weak fit**: mostly keyword overlap, prestige-driven, inactive, or unrelated to the applicant's actual direction.
- **Unknown**: insufficient information; list what to check.

### 4. Produce school-specific fit notes

For each target, produce notes that can feed later SOP tailoring:

- why this faculty/lab fits
- which applicant experience connects to the fit
- what future question could be pursued there
- what evidence still needs checking
- what not to say because it is shallow or unsupported

Do not write polished SOP paragraphs unless the user asks; hand off to `apply-sop-writer` for prose drafting.

### 5. Balance the shortlist

If the user is building a list, group programs by:

- research fit strength
- application competitiveness if known
- advisor depth and single-advisor risk
- funding or structural constraints
- deadline priority

Avoid presenting prestige as a substitute for fit.

## Output format

Use:

```markdown
## Applicant research themes
- [Theme]: [why it matters for search]

## Fit criteria
- [Criterion]: [how to judge it]

## Faculty/program fit table
| Program/lab/faculty | Fit level | Evidence | Risks / unknowns | Follow-up |
|---|---|---|---|---|

## School-specific fit notes
### [School or professor]
- Fit bridge: ...
- Applicant evidence to mention: ...
- Future question: ...
- Verify before applying: ...

## Shortlist priorities
1. [Target to investigate/apply to first]
```

## Quality bar

A strong output distinguishes real intellectual fit from shallow keyword overlap. It should help the applicant investigate programs, produce credible school-specific notes, and avoid wasting application effort on poor-fit targets.
