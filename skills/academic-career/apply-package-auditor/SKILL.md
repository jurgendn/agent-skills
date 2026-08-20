---
name: apply-package-auditor
description: >-
  Audit a full PhD or research-application package for declared-theme fit, coherence, missing evidence, narrative consistency, program fit, recommender risk, and deadline priorities. Use this skill whenever the user asks whether their whole application is ready, how to prioritize fixes before deadlines, whether their CV/SOP/research statement/faculty fit/recommenders align, whether the SOP and letters actually answer the programme's declared theme, specialisation, or track, or what weaknesses an admissions committee may notice across materials. Every audit runs the declared-theme screen first, before any academic- or faculty-fit finding, searching the web for the live official programme page whenever the target is not already known from the conversation.
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
- The user wants a numeric/anchored score, tier, eligibility verdict, or scholarship-mission fit rather than a qualitative readiness report. Use `apply-dossier-evaluator`.
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

### 2. Screen the declared theme — run this before any other finding

Many targets declare a **theme, specialisation, track, or topic scope** (a consortium master's pathway list, a mission-scoped doctoral school, a topic-restricted call). Where one exists it is **published selection content**: the committee reads the package against it. Run this screen on **every** audit, for **every** target, before assessing the application thesis, evidence coverage, or faculty fit.

**Get the theme from the live official page, not from memory.** For any target you do not already have text for in this conversation:

1. **Search the web** for the programme's or call's own page — the university/consortium/funder site, the current cycle's call document, and the track or pathway page if the programme has several.
2. Read the declared scope **off those pages, in the programme's own words**. Never infer a theme from the programme's *name*: "AI for Society" and "Applied Data Science" scope very different work, and the name is marketing.
3. If the official page cannot be found, or the cycle's call is not published yet, **say so and ask the user for the link or the call PDF**. Do not audit against a guessed theme — a fabricated theme produces confident, wrong fixes.
4. Note the page and access date, and flag anything cycle-specific (pathway lists, topic restrictions, deadlines) as needing live re-verification before submission.

Then check the package against it:

- **Decompose** the theme into the concrete research activities it actually covers.
- **Map real applicant evidence** onto that decomposition — projects, methods, data, application domains, outputs.
- **Check each document separately**: does the SOP answer the theme, and does each letter's briefing point its recommender at evidence the theme cares about? A package can be thematically strong in the CV and silent about it in the two documents the committee weighs most.

Classify each target:

- **Core** — the applicant's real work sits inside the declared theme.
- **Adjacent, bridged** — outside the stated theme but connected by a **named, checkable bridge**: specific work the applicant actually did, serving a specific part of the theme.
- **Stretch** — a bridge exists only in generalities.
- **Outside scope** — no honest bridge exists. **Recommend dropping the target.** This is a legitimate audit outcome, not a failure to find framing.

Three rules are hard:

- **The swap test.** If the bridging sentence still reads fine after substituting a different specialisation, it proves nothing — record it as filler, not fit.
- **Academic strength does not compensate.** Where a theme is declared and the package never answers it, that is a finding in its own right, regardless of publications, grades, or faculty fit. Do not let a strong record downgrade it to polish.
- **Never manufacture a bridge.** Facts stay fixed; a theme changes which real work leads and how deeply it is developed, never what the applicant did.

**Where no theme is declared**, record `no declared theme — N/A` explicitly with the page checked, so the reader can see the screen was run rather than skipped.

If `apply-program-fit-mapper` has already produced a thematic verdict for a target, consume it rather than re-deriving it; run this compact screen only where no verdict exists.

### 3. Extract the application thesis

Identify the implicit thesis of the application:

- what research area the applicant is entering
- what preparation they have already demonstrated
- what future questions they want to pursue
- why the target program is a credible environment
- what kind of researcher they are becoming

If the materials imply different theses, flag the inconsistency.

### 4. Cross-check evidence

For each major claim, ask:

- Is it supported by CV evidence?
- Is it validated by a recommender?
- Is it connected to faculty/program fit?
- Is it specific enough to be credible?
- Is it overclaimed relative to the applicant's actual record?

Separate admissions-critical problems from polish issues.

### 5. Audit risks

Look for:

- a declared theme the SOP never answers, or answers only with a sentence that survives the swap test
- letters briefed with no evidence the declared theme cares about
- unclear research identity
- generic program fit
- SOP claims not backed by CV entries
- CV evidence not used in narrative
- recommender gaps or redundancy
- missing explanation for transcript anomalies
- unfocused school list
- deadline-driven bottlenecks
- materials that sound like different applicants

### 6. Prioritize fixes

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

## Declared-theme fit
| Target | Declared theme / track (programme's own words) | Source page + date checked | Fit | SOP answers it? | Letters briefed for it? | Bridge (one sentence, or "none") |
|---|---|---|---|---|---|---|

<!-- Fit: core / adjacent, bridged / stretch / outside scope / no declared theme — N/A -->
<!-- Where the official page could not be found, write "page not located — link needed" and do not classify. -->

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

The declared-theme screen is not optional and not a polish item. An audit that reports a coherent, well-evidenced package while the SOP never answers the programme's declared theme has missed the finding most likely to decide the outcome — and an audit that invents a theme it never read on the programme's own page is worse than one that asks for the link.
