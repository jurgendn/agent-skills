---
name: applicant-profile-reader
description: Read an academic-career applicant profile from files, folders, notes, CVs, resumes, transcripts, research statements, project writeups, publication lists, GitHub summaries, recommendation notes, and target-school materials. Use this skill whenever the user asks Claude to read "my profile", "my application folder", "my CV and notes", "my PhD materials", "my academic background", or wants a reusable structured profile before SOP writing, academic CV building, professor emails, faculty/program fit mapping, recommender packets, or application-package audits. This skill is for academic career and research-application contexts; do not use it for generic job-search resumes, industry recruiter profiles, literature surveys, or writing a final SOP/CV directly.
---

# Applicant Profile Reader

Read the user's academic-career materials and turn them into a structured applicant profile that downstream application skills can use without repeatedly re-reading every file.

The goal is not to polish one document. The goal is to build a faithful evidence map: who the applicant is academically, what research trajectory their materials support, where the evidence is strong, and what information is missing before writing SOPs, CVs, cold emails, recommender packets, or school-specific fit notes.

## Use this when

- The user gives a file or folder containing application materials and asks you to understand their profile.
- The user wants to prepare for PhD, research master's, fellowship, research internship, RA, post-bacc, visiting-student, or lab applications.
- The user asks for a reusable profile before using `sop-writer`, `academic-cv-builder`, `phd-program-fit-mapper`, `professor-cold-email-drafter`, `recommendation-letter-strategist`, or `phd-application-package-auditor`.
- The user has scattered materials: CV/resume, project notes, publications, transcripts, GitHub links, drafts, emails, target-school lists, or recommender notes.
- The user wants to know what their academic-career narrative currently looks like and what evidence is missing.

## Do not use this when

- The user wants a final SOP draft or essay revision. Use `sop-writer` after extracting the profile.
- The user wants a finished academic CV. Use `academic-cv-builder` after extracting the evidence inventory.
- The user wants faculty matching from scratch. Use `phd-program-fit-mapper` after extracting research interests and constraints.
- The user wants a full cross-document readiness audit. Use `phd-application-package-auditor` after extracting the profile.
- The user is optimizing a generic industry resume or LinkedIn profile rather than an academic or research application.

## Workflow

### 1. Inventory the sources

List every available source and classify it:

- CV, resume, or biosketch
- transcript, grade report, or coursework notes
- SOP, research statement, personal statement, or draft essays
- research-project writeups, thesis notes, lab notes, posters, talks, papers, preprints, manuscripts, or abstracts
- publication list, Google Scholar, ORCID, GitHub, portfolio, dataset, or code links
- awards, scholarships, grants, competitions, teaching, service, leadership, or mentoring notes
- target programs, target faculty, school list, deadlines, country constraints, funding constraints, or application prompts
- recommender list, collaboration notes, or letter packet material

If the user gives a folder, inspect filenames first, then read the most central materials before optional extras. Do not assume every file is equally important.

### 2. Separate facts, evidence, and interpretation

For each major claim, keep track of its source:

- **Facts:** degree, institution, dates, roles, titles, venues, grades, awards, outputs.
- **Evidence:** concrete research contributions, methods used, artifacts produced, advisor/lab context, results, publications, talks, code, datasets.
- **Interpretation:** likely research identity, trajectory, strengths, gaps, and application positioning.

Do not invent missing details. Mark uncertain or inferred information as `[inferred]` and missing details as `[needs confirmation]`.

### 3. Extract academic-career identity

Synthesize the applicant's profile around admissions-relevant questions:

1. What research area or intellectual direction do they appear to be moving toward?
2. What prior work proves they can do research?
3. What methods, theory, systems, tools, or domains do they know?
4. What outputs can committees or PIs verify?
5. What kind of environment, advisor, program, or role would make sense next?
6. What constraints shape their applications: geography, funding, timeline, degree type, topic flexibility, recommender coverage, or transcript risks?

Keep this synthesis grounded in the provided materials. If the materials support multiple possible narratives, present the alternatives instead of forcing one story.

### 4. Build the evidence inventory

Organize evidence so downstream skills can reuse it:

- education and coursework
- research experience
- publications, preprints, manuscripts, posters, talks, workshops, or submissions
- selected projects and technical artifacts
- methods and technical skills tied to evidence
- teaching, mentoring, service, leadership, or community work
- awards, grants, scholarships, selective programs, or competitions
- industry or applied experience relevant to research
- target programs, faculty, and fit evidence
- recommenders and what each can credibly validate

For each item, include: source, dates if known, applicant contribution, methods/tools, output, and credibility signal.

### 5. Flag gaps and follow-up questions

Identify missing information that would materially affect academic applications:

- unclear research contribution or personal ownership
- missing advisor, lab, collaborator, venue, date, link, grade, or output
- technical skills listed without project evidence
- research interests not supported by experience
- possible transcript or timeline concerns needing explanation
- generic or weak target-faculty fit
- recommender coverage gaps
- evidence that belongs in the CV but not yet in essays, or vice versa

Prioritize gaps by downstream impact. Do not drown the user in minor clerical issues before admissions-critical gaps.

## Output format

Use this structure:

```markdown
# Applicant Profile

## Source inventory
| Source | Type | Used for | Notes |
|---|---|---|---|

## Applicant snapshot
- Current status:
- Target application context:
- Likely research area:
- Strongest evidence:
- Main risks or unknowns:

## Research identity
[1-3 paragraphs synthesizing the applicant's research trajectory, with uncertainty marked.]

## Evidence inventory
### Education and coursework
- [Evidence item] — Source: [file/note]; Confidence: [high/medium/low]

### Research experience
- [Project/role]: [contribution, methods, output, advisor/lab/context]

### Publications, talks, and artifacts
- [Item]: [status, venue/link if known, applicant contribution]

### Technical and methodological skills
- [Skill/method] — Evidence: [project/course/output]

### Awards, teaching, service, and leadership
- [Item] — Application value: [why it matters]

## Application narrative options
1. **[Narrative name]** — Best for: [programs/labs]; Evidence: [support]; Risk: [weakness]
2. **[Narrative name]** — Best for: [programs/labs]; Evidence: [support]; Risk: [weakness]

## Downstream use
- For `sop-writer`: [themes and experiences to emphasize]
- For `academic-cv-builder`: [CV sections/items to strengthen]
- For `phd-program-fit-mapper`: [interests, constraints, faculty-fit clues]
- For `professor-cold-email-drafter`: [compact pitch material]
- For `recommendation-letter-strategist`: [who can validate what]
- For `phd-application-package-auditor`: [cross-document risks]

## Missing information and questions
### High priority
1. [Question/detail needed] — Why it matters: [impact]

### Medium priority
- [Question/detail needed]

### Low priority
- [Question/detail needed]
```

## Quality bar

A strong profile is accurate, source-grounded, and reusable. It should make later writing faster while reducing hallucination risk: downstream skills should be able to cite the profile's evidence inventory instead of guessing from vague self-descriptions.
