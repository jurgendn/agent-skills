---
name: apply-dossier-evaluator
description: Score and evaluate a further-education application dossier (PhD, research master's, scholarship/fellowship, or research internship) against a reproducible rubric, and check eligibility for cross-border and scholarship programs. Use this skill whenever the user asks to "rate my profile", "score my application", "how strong is my dossier", "am I competitive for a PhD/scholarship", "evaluate me for VEF/DAAD/Fulbright/Erasmus/MSCA", "does my Vietnamese BSc qualify for an EU PhD", "what's my admit/funding chance", or wants a graded scorecard with per-dimension reasoning rather than a prose readiness report. Distinct from apply-package-auditor, which produces a qualitative coherence audit with no scores; use this skill when the user wants numbers, tiering, eligibility verdicts, or scholarship-mission fit. Use apply-profile-reader first if no structured profile exists yet.
---

# Further-Education Dossier Evaluator

This skill produces a **reproducible, anchored score** for a further-education
application dossier and a verdict on eligibility and target fit. It does not
rewrite any single document; it evaluates the whole package against a fixed
scale so two runs on the same dossier land on the same numbers.

## Use this when

- The user wants a **graded scorecard** (per-dimension 1–5 + total), not prose.
- The user asks how **competitive** they are for a PhD, research master's,
  scholarship/fellowship, or research internship.
- The user asks whether they are **eligible** (degree equivalence, cross-border
  credit expectations, scholarship gating rules).
- The user wants **scholarship-mission fit** scored (return-home, leadership,
  development impact) for VEF / DAAD / Fulbright / Erasmus Mundus / MSCA.
- The user wants the same dossier re-scored consistently across iterations.

## Do not use this when

- The user wants a **qualitative coherence audit** and a prioritized fix list
  with no scores. Use `apply-package-auditor`.
- The user wants to write/line-edit one artifact: SOP → `apply-sop-writer`,
  CV → `apply-cv-builder`, letters → `apply-recommendation-letter-strategist`.
- The user wants to choose faculty/programs from scratch → `apply-program-fit-mapper`.
- No structured profile exists yet → run `apply-profile-reader` first, then return.

## Reproducibility contract

Scoring MUST be anchored, not impressionistic:

- Apply the **1 / 3 / 5 anchor descriptors** in
  `references/rubric-descriptors.md` for every dimension. Do not score from gut feel.
- Calibrate the total against the worked examples in
  `references/calibration-anchors.md` so the scale stays fixed across runs.
- For every score, cite the concrete evidence and the anchor band it matched.

## Volatility rule (read before scoring eligibility or programs)

NEVER treat a cached deadline, GPA cutoff, score minimum, CV/SOP word limit, or
funding amount as authoritative — these change every cycle. Where such a number
matters, **verify it against the live official call** and say so in the output.
A stale cached cutoff is worse than none, because it will be trusted.

## Step 0 — Missing-info gate

Before scoring, confirm you have enough to evaluate. Minimum inputs:

- the **target** (degree type, country/region, and named program(s) if any)
- CV / publication-project list
- SOP or research statement (or note that it is missing)
- transcript / grade context
- recommender list (who, relationship)
- for scholarships: the **named sponsor** and its stated mission

If material is missing, list exactly what is needed and score only what is
present, marking ungraded dimensions as `N/A — insufficient evidence`. Do not
invent program criteria, professor interests, or eligibility rules.

## Step 1 — Target classification

Classify the dossier into exactly one primary target type. This selects the
adaptive weighting in Step 3.

| Type | Trigger | Optimizes for |
|---|---|---|
| **A. Research PhD** | direct-entry or post-master's doctorate | research potential, fit, letters |
| **B. Research / coursework Master's** | MS/MSc, incl. PhD stepping-stone | academic record, preparation, trajectory |
| **C. Scholarship / Fellowship** | VEF, DAAD, Fulbright, Erasmus Mundus/EMJM, MSCA | mission fit (return-home/impact), leadership, excellence |
| **D. Research internship / pre-doc / RA** | lab placement, summer/visiting research | technical depth, immediate fit, supervisor match |

If two targets genuinely apply (e.g. a PhD pursued *through* a scholarship),
score both relevant program layers: the academic target with its rubric AND the
sponsor layer via Dimension 2.

## Step 2 — The 11 evaluation dimensions

Score each 1–5 using `references/rubric-descriptors.md` anchors. Several
dimensions have a different bar per target type; the descriptor file carries the
per-type variants.

1. **Eligibility & degree equivalence** — does the applicant formally qualify?
   For EU / cross-border targets (does a 4-year Vietnamese BSc satisfy a
   master's-required EU PhD; US vs EU credit expectations), consult
   `references/degree-equivalence.md`. This is a **gate**: a hard fail here caps
   the dossier regardless of other strengths — flag it explicitly.
2. **Target & program / sponsor fit** — alignment to the named program's stated
   priorities. For scholarships and external programs, consult
   `references/external-programs.md` for what each sponsor weights and which
   documents it requires, **then verify all cutoffs/limits against the live
   official call**.
3. **Academic record & preparation** — transcript rigor, trajectory, relevant
   coursework, grade context (interpret GPA against institution and grading
   scale; never against a hardcoded cutoff).
4. **Research potential & output** — publications, preprints, projects, evidence
   of independent contribution. **Rate publications by venue quality using
   `references/venue-quality.md`, not raw counts.** A single first-author A*/A
   paper outweighs several weak-venue entries.
5. **Technical & methodological depth** — demonstrated command of methods,
   tooling, and rigor appropriate to the field and target.
6. **Statement / research narrative quality** — clarity of research identity,
   credible future direction, specificity (not generic ambition).
7. **Letters of recommendation** — strength, relevance, and coverage of
   recommenders relative to the target (research letters for research targets).
8. **Faculty / lab fit** — concreteness of match to named people or groups.
   **Fetch this live per run** (Scholar / DBLP / lab page); do NOT rely on any
   cached professor file — none exists by design.
9. **Leadership, service & impact** — especially weighted for scholarships;
   includes return-home / development-impact / mobility signals where the
   sponsor requires them.
10. **Dossier coherence** — does the package tell one consistent story? Work
    through `assets/coherence-checklist.md` (SOP lead narrative present in CV;
    every SOP claim CV-backed; proposal matches target; transcript weakness
    addressed).
11. **Risk & readiness** — red flags and submission-readiness. Classify findings
    Critical / Major / Minor using `references/failure-patterns.md`.

## Step 3 — Adaptive weighting per target type

Combine dimension scores into a weighted total. Weights shift by target type
(the four adaptive rubrics). Use these relative emphases; normalize to 100%.

| Dimension | A. PhD | B. Master's | C. Scholarship | D. Internship |
|---|---|---|---|---|
| 1 Eligibility (gate) | gate | gate | gate | gate |
| 2 Target/sponsor fit | High | Med | **Highest** | High |
| 3 Academic record | Med | **Highest** | High | Med |
| 4 Research potential | **Highest** | High | High | High |
| 5 Technical depth | High | Med | Med | **Highest** |
| 6 Statement quality | High | Med | High | Med |
| 7 Letters | High | Med | High | Med |
| 8 Faculty/lab fit | High | Low | Med | **Highest** |
| 9 Leadership/impact | Low | Low | **Highest** | Low |
| 10 Coherence | Med | Med | High | Med |
| 11 Risk/readiness | Med | Med | High | Med |

Eligibility is a gate, not a weighted term: if Dimension 1 is a hard fail, report
the dossier as **ineligible as-is** and present the remediation path rather than
a competitive score.

## Step 4 — Total, tiering, and verdict

Convert the weighted total to a tier, calibrated against
`references/calibration-anchors.md`:

- **Top tier (~top 2%)** — clear admit/funding signal at competitive targets.
- **Strong (~next 8%)** — competitive; specific gaps to close.
- **Plausible** — viable at well-matched targets; material gaps.
- **Developing** — not yet competitive at the stated target; reframe or build.

State the tier with the per-dimension evidence that drove it, and the single
highest-leverage fix.

## Output format

```markdown
## Target classification
[Type A/B/C/D] — [named program(s)] — [reasoning]

## Eligibility verdict
[Eligible / Conditional / Ineligible as-is] — [evidence; live-verify notes]

## Scorecard
| # | Dimension | Score (1–5) | Anchor band matched | Evidence | Weight (this target) |
|---|---|---|---|---|---|
| 1 | Eligibility (gate) | … | … | … | gate |
| … | | | | | |

## Weighted total & tier
[Total] → [Tier], calibrated against calibration-anchors.md

## Strengths
- [Dimension]: [evidence]

## Critical / Major / Minor risks
- [Critical] …
- [Major] …
- [Minor] …

## Coherence findings
- [Checklist item]: [pass/fail + note]

## Sponsor / program fit notes
- [Program]: [what it weights] — [fit] — [LIVE-VERIFY: cutoffs/limits]

## Highest-leverage fixes
1. [Fix] — [why it moves the score]

## Live-verification checklist
- [ ] [Each cutoff/limit/deadline that must be confirmed against the official call]

## Ungraded / insufficient evidence
- [Dimension]: [what is missing]
```

## Quality bar

A strong evaluation is **anchored** (every score traces to a rubric band and
concrete evidence), **honest about volatility** (no cached cutoff presented as
fact), and **decision-useful** (clear tier, clear gate verdict, one highest-
leverage fix). If the evaluator cannot defend a score against
`references/rubric-descriptors.md`, the score is not ready.
