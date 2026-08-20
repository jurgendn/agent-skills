---
name: apply-program-fit-mapper
description: >-
  Map an applicant's research interests to programmes, tracks, faculty, labs, and departments, and check whether their profile actually matches a programme's
  declared theme, specialisation, or application focus before writing target-specific materials. Covers PhD, research master's, and joint/consortium
  programmes such as Erasmus Mundus. Use whenever the user asks which professors or programmes fit their interests, how to shortlist targets, how to compare
  faculty fit, "does my profile match this programme's focus", "is my background relevant to this specialisation/track/theme", "should I even apply to this
  one", how to turn interests into searchable research themes, or how to prepare target-specific fit notes for SOPs.
---

# Program Fit Mapper

Good program fit is not name-dropping. It is a grounded match between the applicant's preparation, future research questions, and the intellectual environment of a specific programme, track, faculty, or lab.

Fit has **three independent axes**, and a target can pass one while failing another:

- **Structural** — how does this target admit people, and what is a shortlist entry here? (step 1)
- **Thematic** — is the applicant's actual work inside the programme's declared theme, specialisation, or track scope? (step 2)
- **Intellectual** — which specific people or groups does the applicant connect to? (steps 3–5)

Check theme before people. Where a themed programme has no single advisor to map — a consortium master's with specialisation pathways, a thematic call, a mission-scoped track — thematic fit *is* the fit assessment.

## Use this when

- The user is choosing PhD programmes, research master's, departments, labs, or advisors.
- The user asks whether their profile matches a programme's declared theme, specialisation, track, or application focus.
- The user wants to map their interests to faculty or research groups.
- The user asks whether a professor is a strong, medium, or weak fit.
- The user needs target-specific fit notes before writing an SOP.
- The user wants a balanced shortlist based on research fit rather than prestige alone.
- The user is deciding whether a given programme is worth applying to at all.

## Do not use this when

- The user wants to write the SOP itself. Use `apply-sop-writer`.
- The user wants a broad literature review not tied to application fit. Use `literature-triangulation`.
- The user wants to audit a finished application package. Use `apply-package-auditor`.
- The user wants CV structure or bullet rewriting. Use `apply-cv-builder`.
- The question is only what a programme, track, or call selects for, with no applicant evidence in play — including characterising a whole candidate list before comparing any of it to a profile. Use `apply-program-theme-extractor`, then return here with its dossier.

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

**Establish each target's application regime before shortlisting — it decides what a shortlist entry even is.** `references/application-regimes.md` carries the four regimes and their consequences:

- **Supervisor-first** (France, French-speaking Belgium, many project-funded posts) — the unit is *a person and a project*; outreach is the critical path; depth beats breadth.
- **Vacancy-first** (Sweden, Norway, MSCA/EURAXESS) — the unit is *an advertised position* and the applicant becomes an employee; you monitor vacancy boards rather than shortlist departments.
- **Call/competition-first** (Italian *bandi*) — the unit is *a specific call* with ranked selection and a fixed window.
- **Department-first** (typical US admissions) — the unit is *a department with several plausible advisors*; pre-application contact is optional and sometimes discouraged.

Identify the **funding regime separately**, since it may have a different selector — programme-attached, a standalone scholarship, project or employment funding, or a nominated scheme screened by the host institution or a national sending partner. Also check for the two edge cases: funding that is eligibility-assessed rather than competitive (Italian DSU is income-based), and levels where a country simply has no general government scholarship, so there is nothing to apply to.

Ask which regime applies per target rather than assuming from country — most countries contain several, and a single university can differ by department or funding source.

### 2. Screen thematic fit — before mapping any faculty

Many programmes declare a **theme, specialisation, track, or application focus** that scopes what work belongs there: an Erasmus Mundus joint master's with named specialisation pathways, a doctoral school organised around a mission area, a call restricted to listed topics, a centre funded for one agenda. That declared scope is published selection content, not marketing. `references/application-regimes.md` carries the theme axis and the extraction method; the short form:

**If a theme dossier from `apply-program-theme-extractor` already exists for this target, consume it** — take its declared theme, decomposition, pathway list, and **status label** as given and start at classification below. Otherwise run the extraction inline. Where the dossier's status is `inferred`, the operative theme may reorder which real evidence leads, but it **cannot produce an "outside scope" verdict** — only a declared theme can drop a target. Where the status is `genuinely open`, skip this step and record it as such; where it is `link needed`, leave the target unclassified.

1. **Extract the declared theme from the live official pages** — the programme's own words, plus the pathway/track list, the stated objectives, and any funder mission behind it. Never infer a theme from the programme's name or your prior knowledge of the field. **Search the web for every target you do not already have page text for**, including programmes you have never encountered; a programme absent from your prior knowledge is the normal case, not a reason to skip the screen. Fetch the programme/consortium page, the current cycle's call, and each pathway page separately, and record the URL and access date. Where the official page cannot be located or the cycle's call is unpublished, ask the user for the link and leave the target unclassified rather than screening against a guess.
2. **Decompose it** into the concrete research activities it actually funds. A theme like "digital and green transition" is a container: read the pathway descriptions, module lists, and example projects to see which mathematics or engineering it means, and note where the container is genuinely broad rather than narrowing it for the user.
3. **Map the applicant's real evidence onto it** — projects, methods, data, application domains, publications. Method-level matches (optimisation, PDEs, statistical learning) count only where the programme's own materials show that method serving the theme.
4. **Classify, and let the verdict decide whether the target stays on the list.**

Classify each target's thematic fit as:

- **Core** — the applicant's existing work sits inside the declared scope on its own terms. State which pathway or track it maps to.
- **Adjacent, bridged** — the work is outside the stated theme but connects through a **named, checkable bridge**: a specific method the applicant has used that the programme's own materials apply to this theme, a shared problem structure, or a domain the applicant has actually worked in. Write the bridge down as one sentence and record what evidence supports it.
- **Stretch** — a plausible connection exists but rests on a project the applicant has not done, an interest they cannot evidence, or a claim that would need the programme to take their word for it. Treat as a weak target and say why.
- **Outside scope** — no honest bridge exists. **Deprioritize or drop the target.** This is a legitimate, expected output. Do not manufacture a connection to keep a target alive; a fabricated theme bridge is the single most detectable weakness in a themed application and it costs a wasted cycle.

Two guards:

- **Facts fixed, weights vary.** A thematic bridge changes which of the applicant's real work leads, how deeply it is described, and which published criterion it is framed against. It never changes what they did, never adds an interest they do not have, and never converts an unrelated project into a themed one by relabelling it.
- **The swap test.** If the bridging sentence still reads fine after substituting a different specialisation, it is not evidence of thematic fit — it is filler. Rewrite it or downgrade the classification.

Where thematic fit is *core* or *adjacent, bridged*, hand the bridge sentence and its supporting evidence to `apply-sop-writer`. Where it is *stretch* or *outside scope*, say so before the user invests in the application.

### 3. Define fit criteria

Use criteria such as:

- topic overlap with the applicant's future questions
- methodological overlap with prior preparation
- active recent work by the faculty or lab
- room for the applicant to contribute something specific
- departmental ecosystem: multiple relevant faculty, seminars, centers, collaborators
- evidence quality: papers, lab pages, grants, student placements, recent projects
- risk factors: inactive advising, weak overlap, only one possible advisor, outdated webpages

Separate strong evidence from assumptions that need verification.

### 4. Classify fit

For each professor, lab, or program, classify:

- **Strong fit**: clear topic and method overlap, active work, multiple concrete bridges to applicant's background.
- **Medium fit**: plausible overlap but needs more evidence or has partial mismatch.
- **Weak fit**: mostly keyword overlap, prestige-driven, inactive, or unrelated to the applicant's actual direction.
- **Unknown**: insufficient information; list what to check.

### 5. Produce target-specific fit notes

For each target, produce notes that can feed later SOP tailoring:

- why this faculty/lab fits
- which applicant experience connects to the fit
- what future question could be pursued there
- what evidence still needs checking
- what not to say because it is shallow or unsupported

Do not write polished SOP paragraphs unless the user asks; hand off to `apply-sop-writer` for prose drafting.

### 6. Balance the shortlist

If the user is building a list, group programs by:

- thematic fit level, with *outside scope* targets moved off the list rather than ranked last
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

## Thematic fit
| Target | Declared theme / track (as published) | Thematic fit | Bridge (one sentence, or "none") | Evidence behind the bridge |
|---|---|---|---|---|
<!-- Thematic fit: core / adjacent, bridged / stretch / outside scope -->

## Faculty/program fit table
| Program/lab/faculty | Regime | Fit level | Evidence | Risks / unknowns | Follow-up |
|---|---|---|---|---|---|

## Target-specific fit notes
### [Programme, track, or professor]
- Thematic fit and pathway: ...
- Fit bridge: ...
- Applicant evidence to mention: ...
- Future question: ...
- Verify before applying: ...

## Shortlist priorities
1. [Target to investigate/apply to first]

## Deprioritized targets
- [Target] — [why the theme, regime, or evidence does not support applying]
```

## Quality bar

A strong output distinguishes real intellectual fit from shallow keyword overlap, and real thematic fit from a relabelled project. It should help the applicant investigate programmes, produce credible target-specific notes, and avoid wasting application effort on poor-fit targets. An output that finds every target to be a good fit has failed: naming at least what would have to be true for a weak target to become viable — or dropping it — is part of the job.
