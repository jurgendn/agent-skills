---
name: professor-research-direction-mapper
description: Define a professor's recent and trending research direction from publications, lab pages, grants, talks, students, and public materials before writing PhD application fit notes or cold emails. Use this skill whenever the user asks what a professor is working on now, whether a faculty member's research is shifting, how to infer current interests from recent papers, how to prepare for contacting a professor, or how to turn scattered professor evidence into application-ready research-fit angles.
---

# Professor Research Direction Mapper

A professor's current direction is not the same as their most cited paper or their lab's generic webpage. For applications and outreach, the useful question is: what are they actively moving toward, and where could the applicant plausibly connect?

## Use this when

- The user wants to understand a professor's recent or trending research direction.
- The user is preparing faculty-specific PhD fit notes, SOP material, or a cold email.
- The user has a professor name, lab page, Google Scholar profile, DBLP/Semantic Scholar page, publication list, grant page, or talk abstract and needs synthesis.
- The user asks which of a professor's topics are active, fading, emerging, or risky to mention.
- The user wants to identify credible bridges between their own interests and the professor's current work.

## Do not use this when

- The user is choosing entire programs or building a school shortlist. Use `phd-program-fit-mapper`.
- The user wants the actual cold email draft. Use `professor-cold-email-drafter` after the direction is mapped.
- The user wants polished SOP prose. Use `sop-writer`.
- The user wants a broad field literature map not centered on one professor. Use `literature-triangulation`.

## Workflow

### 1. Establish evidence sources

Collect or ask for:

- professor name, institution, department, and homepage
- recent publications, preferably the last 3-5 years
- lab or group page, project pages, grants, news, talks, preprints, and student projects
- the applicant's research interests, prior projects, and reason for contacting this professor
- target use: cold email, SOP fit paragraph, interview preparation, or shortlist decision

If current evidence is missing, explain what can and cannot be inferred. Do not pretend that old or sparse information proves current activity.

### 2. Separate research timeline from research identity

Classify evidence into:

- **Long-running identity**: themes present across many years or central to the lab.
- **Recent active direction**: topics appearing repeatedly in the last few years.
- **Emerging trend**: new papers, grants, talks, students, or collaborations suggesting a shift.
- **Legacy or lower-confidence topic**: older work, one-off papers, or webpage keywords with little recent support.

Use years and concrete artifacts when available. A trend needs repeated or strategically important evidence, not one title match.

### 3. Infer the professor's current research questions

Turn publication/project evidence into 2-4 likely research directions:

- the problem they seem to care about
- the methods, datasets, theory, systems, or applications they use
- what changed recently compared with older work
- collaborators, venues, grants, or lab members that strengthen the inference
- uncertainty or missing evidence

Phrase directions as research questions or agendas, not as keyword lists.

### 4. Map applicant bridges

For each direction, identify:

- applicant experiences or skills that genuinely connect
- possible questions the applicant could ask or propose
- what to read before contacting the professor
- what would sound shallow, outdated, or unsupported

Prefer one precise fit angle over many generic overlaps.

### 5. Recommend outreach positioning

If the user is preparing an email or SOP, recommend:

- the strongest topic to mention first
- one recent paper/project to reference
- one concise bridge to the applicant's background
- one informed question or possible research direction
- topics to avoid because they appear inactive, too broad, or weakly connected

Hand off to `professor-cold-email-drafter` for the actual message.

## Output format

Use:

```markdown
# Professor Research Direction Map: [Professor]

## Evidence reviewed
- [Source]: [what it contributes / date if known]

## Research timeline
| Direction | Evidence | Status | Confidence |
|---|---|---|---|
| [Theme] | [papers/projects/grants] | Active / emerging / legacy / unknown | High / medium / low |

## Likely current research agenda
1. **[Direction as a research question]**
   - Evidence: ...
   - Why it seems current: ...
   - Uncertainty: ...

## Best applicant fit angles
| Fit angle | Applicant evidence | Professor-side evidence | How to use it |
|---|---|---|---|

## Outreach or SOP positioning
- Lead with: ...
- Mention this recent work: ...
- Ask or propose: ...
- Avoid saying: ...

## What to verify next
- [Specific missing source, paper, student project, or grant detail]
```

## Quality bar

A strong output helps the applicant sound informed without overclaiming. It should distinguish active directions from legacy keywords, ground every inference in evidence, and produce one or two credible angles that can later become a cold email or SOP fit paragraph.
