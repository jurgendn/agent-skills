---
name: apply-cv-builder
description: Build, revise, and audit academic CVs for PhD applications, research master's programs, fellowships, research internships, RA roles, and lab applications. Use this skill whenever the user asks to turn a resume into an academic CV, improve research-experience bullets, organize publications/projects/teaching/awards, identify missing evidence for research readiness, or make a CV fit research admissions expectations.
---

# Academic CV Builder

An academic CV is an evidence document. It should make the applicant's research preparation legible: what they worked on, what methods they used, what outputs resulted, and what signal an admissions committee or PI can trust.

## Use this when

- The user is applying to PhD programs, research master's programs, fellowships, research internships, RA roles, or labs.
- The user wants to create, revise, or audit an academic CV.
- The user asks to convert an industry-style resume into a research-oriented CV.
- The user needs stronger research-experience, project, publication, teaching, award, or technical-skill entries.
- The user wants to identify missing or weak evidence in their research profile.

## Do not use this when

- The user wants to write or revise a Statement of Purpose. Use `apply-sop-writer`.
- The user wants faculty or program matching. Use `apply-program-fit-mapper`.
- The user wants a full application-package risk audit. Use `apply-package-auditor`.
- The user wants a purely industry resume optimized for recruiters rather than research admissions.

## Workflow

### 1. Identify the application context

Extract:

- target degree, role, fellowship, or lab
- field and subfield
- application country or norm if relevant
- current CV/resume material
- publications, preprints, posters, talks, projects, code, datasets, awards, teaching, service, and technical skills
- constraints such as page limits or required formats

If the user has not provided their current material, ask for it or provide a fill-in template.

### 2. Separate evidence from presentation

Classify material into:

- direct research evidence: projects, papers, preprints, theses, lab work, RA work
- technical preparation: methods, tools, systems, datasets, experiments
- communication evidence: posters, talks, writing, teaching
- recognition: awards, grants, scholarships, selective programs
- service and leadership: mentoring, reviewing, community work
- weaker or ambiguous evidence that needs clearer framing

Do not inflate claims. If an item is vague, mark what detail is needed.

### 3. Choose the CV structure

Prefer an academic CV order such as:

1. Education
2. Research interests
3. Research experience
4. Publications, preprints, posters, or talks
5. Selected projects
6. Teaching or mentoring
7. Awards and honors
8. Technical skills
9. Service, leadership, or outreach
10. References if appropriate

Adjust for the applicant's strongest evidence. For early applicants, strong projects may come before sparse publications.

### 4. Rewrite entries as research evidence

For each research or project bullet, emphasize:

- research question or goal
- applicant's concrete contribution
- methods, tools, or theory used
- scale, dataset, experiment, proof, system, or evaluation
- output: paper, preprint, poster, code, result, deployed tool, or learned finding
- advisor, lab, or collaboration context when useful

Avoid vague verbs like “worked on” unless the actual contribution is unclear.

### 5. Audit gaps and priorities

Flag:

- missing dates, advisors, titles, venues, links, or outcomes
- unsupported claims of research interest
- overlong industry details that crowd out research evidence
- skills lists not tied to projects
- weak ordering that hides the best signal
- items that belong in the SOP rather than the CV

Prioritize fixes that improve admissions signal, not cosmetic polish.

## Output format

When auditing or building a CV, use:

```markdown
## Recommended CV structure
- [Section order with rationale]

## Revised or example entries
### [Section]
- [Edited bullet or entry]

## Missing information
- [Specific detail needed]

## Research-readiness signal
- Strong signals: ...
- Weak or unclear signals: ...

## Priority fixes
1. [Highest-impact fix]
2. [Next fix]
3. [Next fix]
```

For a full rewrite, preserve the user's facts and mark uncertain details as `[confirm]` rather than inventing them.

## Quality bar

A strong output makes the applicant's research evidence easier to evaluate without exaggeration. It should improve structure, specificity, and credibility while keeping boundaries clear between CV facts, SOP narrative, and program-fit claims.
