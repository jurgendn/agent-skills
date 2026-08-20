---
name: apply-sop-writer
description: >-
  Write, review, score, improve, or iterate on Statements of Purpose and PhD application essays for research programs. Use this skill whenever the user is applying to PhD programs, research internships, fellowships, or graduate programs and asks for SOP strategy, essay structure, research fit, faculty alignment, motivation framing, draft critique, or revision help. Every review and plan checks the statement against the programme's declared theme, specialisation, or track before faculty fit, searching the web for the live official programme page when the target is not already known. This skill is especially relevant for research-focused applications where the essay must connect prior work, future research direction, and program fit.
---

# SOP Writer

A strong Statement of Purpose is not a life story or a generic motivation essay. It is an argument that the applicant is prepared to do research, knows what questions they want to pursue, and fits the program's intellectual environment.

## Use this when

- The user is applying to PhD programs, research masters programs, fellowships, or research internships.
- The user asks for SOP structure, draft review, scoring, revision, or school-specific tailoring.
- The user needs to connect research experience to future research goals.
- The user wants to discuss faculty fit, program fit, or application narrative.

## Do not use this when

- The user is writing a research paper. Use paper-writing skills instead.
- The user needs a CV/resume rewrite without an essay narrative.
- The user wants generic motivational prose without research positioning.

## Workflow

### 1. Extract the application context

Identify:

- target program and degree
- research area
- faculty or labs of interest
- prior research experience
- technical preparation
- long-term research direction
- constraints: word limit, prompt, deadline, country/program norms

If the user has not provided the prompt or word limit, ask for it or make assumptions explicit.

**The prompt defines the document — its name does not.** "Statement of purpose," "motivation letter," and "personal statement" are used inconsistently and overlap heavily, so do not infer requirements from the label. `references/statement-conventions-by-system.md` covers what genuinely varies: whether the application targets a **named project or position** (much of Europe, MSCA/EURAXESS, UK studentships, Australian projects — argue fit to *that* project) or a **department or cohort** (typical US admissions — argue direction and fit to several possible advisors); whether a separate research proposal carries the research content; and the extra scored dimension that mission-driven scholarships attach to post-degree plans.

That file flags its own register claims — how personal or narrative a statement should be — as **weakly sourced**. Do not assert them as national rules. Read the prompt's own verbs and answer the question actually asked.

Three rules from that file are hard, and apply to every draft and every critique:

- **Never praise a country to show fit.** "I admire Germany's precision," "Singapore is renowned for excellence" — these give a reader no evidence of applicant–programme fit and signal that the applicant researched the country instead of the lab. Test: if a sentence would survive being moved to an application in a different country, it is doing no work.
- **Facts fixed; weights vary.** Adapting across targets changes which evidence is salient, its order, depth, and which published criterion it is framed against. It never changes what the applicant did, never adds a claim, and never drops an inconvenient one. Seven targets do not mean seven identities.
- **Never force-fit a declared theme.** Where the programme states a theme, specialisation, or track ("digital and green transition", a mission-scoped school, a topic-restricted call), relevance to it is a published criterion the statement must answer — but only with a bridge naming specific work the applicant actually did and the specific part of the theme it serves. Same swap test: if the sentence survives substituting a different specialisation, it proves nothing. Where no honest bridge exists, tell the user this is the wrong programme instead of wording around it; screen with `apply-program-fit-mapper` first.

**Identify the scheme's genre before drafting** — it decides what must dominate the document, and two schemes from the same national agency routinely differ. The reference file names seven (academic-excellence, development/change, leadership/influence, industry/professional, research-cooperation, consortium/mobility, diplomatic/bilateral) and carries the extraction method: identify the application regime, identify the funding regime, extract the published criteria, reweight existing evidence against them, note the hard constraints. Watch for **two selectors** on one application — a host institution or national sending partner may screen and nominate before the funder reads anything.

A country only enters the reasoning where it produces a **documented institutional mechanism** (France's supervisor-and-laboratory doctoral structure, Australia Awards' development mandate, HKPFS's published four-part rubric). A true geopolitical fact does not by itself license an emphasis — that requires the full chain *geopolitical objective → programme objective → published selection criterion*.

When the essay is (or contains) a forward-looking **research plan** or a fellowship
proposal, `references/proposal-and-research-plan-craft.md` covers proposal-specific
craft: the research-statement-vs-plan distinction, the hourglass structure, the four
highest-leverage parts (title / abstract / opening / conclusion), word-level
discipline (kill "unique"/"I believe", avoid negativity bias), and the resubmission
mindset. Grounded in Knapen et al. (2025), arXiv:2504.01645.

### 2. Build the research narrative

A strong SOP usually answers:

1. What research problem or area motivates the applicant?
2. What experiences prepared them to work on it?
3. What did they actually do, not just participate in?
4. What questions do they want to pursue next?
5. Why is this program/lab a good environment for that direction?

Prefer concrete research details over broad passion claims.

### 3. Evaluate fit and specificity

**Check the declared theme first — before faculty fit.** Run this on every draft review and every plan, not only when the user raises it.

Where the target declares a theme, specialisation, track, or topic scope, relevance to it is a published criterion, and a statement that never answers it fails on the committee's own terms no matter how strong the research record behind it is. **Academic strength does not compensate for an unanswered declared theme.**

Get the theme from the live source. If the target is not one you already have text for in this conversation, **search the web for the programme's or call's official page** — including the specific track or pathway page where the programme has several — and read the declared scope in the programme's own words. Never infer the theme from the programme's name. If the page cannot be found or the cycle's call is unpublished, say so and ask the user for the link rather than reviewing against a guessed theme.

Then judge the draft:

- Does the statement name the theme's actual content, or only its slogan?
- Is the bridge built from **specific work the applicant did**, serving a **specific part** of the theme?
- Swap test: substitute a different specialisation into the bridging sentence. If it still reads fine, it proves nothing — mark it as filler and rewrite it or cut it.
- For multi-pathway programmes, does the draft fit the **chosen pathway**, not just the umbrella? Fitting the umbrella while fitting no pathway is a common disqualifier.
- Where no honest bridge exists, say plainly that this is the wrong programme instead of wording around it, and route to `apply-program-fit-mapper`.

Where the target declares no theme, record `no declared theme — N/A` with the page checked, so the reader can see the check was run.

Then, for each target program, check:

- named faculty/labs are genuinely relevant
- fit is intellectual, not just prestige-based
- proposed interests are specific but not too narrow
- the applicant does not overpromise a fixed dissertation topic
- prior experience supports the claimed direction

### 4. Revise for admissions readers

Improve:

- opening: research problem or trajectory, not cliché origin story
- transitions: show progression between experiences
- contribution clarity: what the applicant personally did
- future direction: questions, methods, or domains
- fit paragraph: program-specific and evidence-based
- ending: concise forward-looking close

Avoid inflated language, generic praise, and unsupported claims of passion.

## Output formats

For draft review:

```markdown
# SOP Review

## Overall assessment

## Declared-theme fit
<!-- Theme in the programme's own words + source page and date checked, or "no declared theme — N/A".
     Verdict: core / adjacent, bridged / stretch / outside scope.
     Quote the draft's bridging sentence and state whether it survives the swap test. -->

## Research narrative

## Strengths

## Weaknesses / risks

## Program-fit issues

## Revision plan

## Line-level notes
```

For planning:

```markdown
# SOP Plan

## Declared-theme fit
<!-- Same contract as the review format: theme in the programme's own words, source page and
     date checked (or "no declared theme — N/A"), verdict, and the bridge the draft must earn. -->

## Core research identity

## Experiences to emphasize

## Future research direction

## Program/faculty fit

## Suggested structure

## Details to gather
```

## Quality bar

A good SOP should make an admissions reader believe the applicant can become a productive researcher in that program, not merely that they are hardworking or enthusiastic.
