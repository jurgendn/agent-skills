---
name: apply-program-theme-extractor
description: >-
  Determine what a programme, track, specialisation pathway, doctoral school, or funding call actually selects for — its declared theme, or, where none is
  published, its operative theme inferred from official evidence. Use whenever the user asks "what is this programme's theme", "what does this call actually
  want", "is this track themed or open", "the landing page doesn't say what they focus on", "what do these 12 programmes each specialise in", or wants a
  candidate list of targets characterised before any of them is compared against a profile. Works applicant-free and over many targets at once, producing a
  reusable theme dossier per target. Distinct from apply-program-fit-mapper, which needs the applicant's evidence and issues the four-way
  fit verdict — route there once a profile enters. Distinct from apply-research-direction-mapper, which maps one person's research direction rather than
  an institution's selection scope. Also builds, on request for shortlisted targets, a programme profile kept apart from the theme — the
  programme's verified selling points, the graduate it intends to produce, and its expected learning outcomes — for questions like "why should I
  choose this track", "what makes this programme different", "what kind of graduate does this scholarship want to produce", "what will I actually learn
  there", or material for a "why this programme" paragraph or interview answer.
---

# Program Theme Extractor

Before anyone can ask "does my work fit here", someone has to answer "what is *here*". This skill answers only the second question, for one target or for a whole candidate list, with no applicant evidence in play.

It also answers a second, separate question on request: what does *here* **offer and produce**? That is the programme profile (step 6) — selling points, intended graduate, expected outcomes. It is kept apart from the theme on purpose: what a programme advertises is not what it selects for.

A programme's theme is **published selection content**, not marketing. Where it is declared, quote it. Where it is not declared, it may still be *operative* — visible in what the programme teaches, funds, and graduates — or the programme may be genuinely open, which is an equally real answer.

The load-bearing distinction in this skill:

- A **declared** theme is what the institution says it selects for. It can disqualify a target.
- An **inferred** theme is *your hypothesis* about what it selects for. It can shift emphasis. It can never disqualify a target.

Presenting an inferred theme with the authority of a declared one is worse than not running the screen at all — it manufactures a selection criterion that nobody published.

## Use this when

- The user has one target and its focus is unclear from the landing page.
- The user has a candidate list (a consortium's pathway list, a doctoral school's research areas, a country's advertised positions, a saved shortlist) and wants each characterised before comparing anything to their profile.
- The user asks whether a call is topic-restricted or open.
- The user needs a pathway-level answer for a multi-specialisation joint programme.
- A downstream skill needs a theme dossier that does not exist yet.
- The user has shortlisted a target and asks what it offers: why choose this track, what graduate it aims to produce, what it teaches — usually as material for a "why this programme" paragraph or interview answer (step 6).

## Do not use this when

- The applicant's evidence is in play and the question is fit. Use `apply-program-fit-mapper` — it owns the core / adjacent-bridged / stretch / outside-scope verdict and the fit swap test on the bridging sentence.
- The question is about one professor's research direction. Use `apply-research-direction-mapper`.
- The question is how a target *admits* or *funds* people rather than what it selects for thematically. That is the application-regime and funding-regime axis inside `apply-program-fit-mapper`.
- The user wants statement prose built on a theme. Use `apply-sop-writer`.

## Workflow

### 1. Fix the unit of extraction

A theme attaches to a specific selecting body. Before searching, decide which one the user is asking about, because a programme and its pathways often differ:

- a whole programme or consortium
- one specialisation, track, or pathway inside it
- a doctoral school, graduate school, or research centre
- one funding call or cycle
- one advertised position or project

For multi-pathway programmes, extract at the **pathway** level as well as the umbrella level. Fitting the umbrella while fitting no individual pathway is a common disqualifier, and it is invisible if you only extract the umbrella.

### 2. Fetch the official pages — always live, never from memory, in two passes

**Search the web for every target that is not already in the conversation as page text.** A programme you have never heard of is the normal case, not a reason to screen from recall. Titles are marketing and themes change per cycle, so neither the programme's name nor your prior knowledge of the field is evidence.

Inference is search-expensive and the cost scales with the candidate list, so run it in two passes and never spend the expensive one on targets that are already out.

**Pass A — cheap, every target.** Fetch only the programme or consortium page (plus each pathway page) and the **current cycle's** call, admission page, or vacancy text. This answers one question: *is a theme declared here or not?* Targets that come back `declared` are finished — go to step 3 and stop. Targets that come back `link needed` are finished too.

**Pass B — expensive, only where pass A found nothing declared *and* the target is still a live candidate.** Ask the user which targets survive their other filters (country, funding, degree level, deadline) before spending here; inferring themes for fifteen programmes when four survive is the main waste this skill can cause. Then fetch, recording URL plus access date for each:

- the stated objectives, mission, or strategic-plan page behind the programme
- the funder's own mission page where the programme is funded for an agenda
- module or course lists — compulsory before elective, since required modules define scope and electives advertise breadth
- the thesis or dissertation repository, or any published list of past or example project titles
- the published research-area listing, and the faculty or partner roster **as a distribution**, not as individual profiles

Where the pages cannot be located, or the cycle's call is unpublished, output `link needed` and leave the target **unclassified**. Do not substitute a guess.

### 3. Extract the declared theme, if there is one

Take the institution's own wording verbatim, with its source. Then **decompose** it into the concrete research activities it actually covers. Umbrella phrases — "digital and green transition", "smart society", "sustainable industry" — are containers, not topics; pathway descriptions, module lists, partner composition, and example projects show what the container holds. Where the container is genuinely broad, record it as broad rather than narrowing it.

### 4. Where no theme is declared, test for an operative one

Only after step 3 finds nothing declared, and only for targets that reached pass B. Read the programme's behaviour off its official pages, in tiers, strongest first:

- **Tier 1 — funded and advertised work.** Project portfolio, advertised positions, funded theses, centre grants. What it pays for is what it selects for.
- **Tier 2 — curriculum and output.** Compulsory modules first, then specialisation options, past or example thesis titles, graduate destinations.
- **Tier 3 — people composition, in aggregate only.** The published research-area listing, or the faculty/partner roster read as a *distribution*, and only where that roster is narrow and published as the programme's scope.
- **Tier 4 — framing language.** Repeated vocabulary across objectives, news, and admission pages. The weakest tier and the easiest to over-read.

Three gates. An operative theme must pass all three, or the answer is `genuinely open`.

1. **Two sources from two different tiers.** A module list and an objectives page that paraphrases that curriculum are one source counted twice. At least one of the two must come from tier 1 or tier 2 — tier 3 and tier 4 cannot establish a theme between them. Record URL and access date for each.
2. **Recency.** Weight the current cycle's pages, and the last three to five years of projects, positions, and theses. A ten-year portfolio can encode a scope the programme has already left. Where the converging evidence is older than that, say so and downgrade to `genuinely open` rather than reporting a stale theme as current.
3. **The exclusion test — the one that matters most.** State what the hypothesised theme *rules out*. If the scope excludes no plausible applicant — "applied mathematics with societal impact", "data science for a changing world" — it is not a theme, it is a description of the field, and the honest status is `genuinely open`. An inferred theme that excludes nothing will otherwise fire on almost every target, which is exactly how this skill would decay into the framing generator its status labels exist to prevent.

**Stop as soon as all three gates pass.** Do not keep fetching to raise confidence in a label that already cannot drop a target. If the gates have not passed after the pass-B page list is exhausted, the answer is `genuinely open` — not a wider search.

### 4b. What is not evidence about a programme's theme

- **An individual professor's research.** It is *their* direction, not the institution's selection scope, and generalising from three faculty pages invents a criterion nobody published. Person-level direction belongs to `apply-research-direction-mapper`. Only the aggregate roster distribution in tier 3 counts here.
- **The country.** A nation has no theme. A country enters only where it produces a **documented institutional mechanism**, and only through the falsifiable chain *geopolitical objective → programme objective → published selection criterion* — which is already captured when step 2 fetches the funder's own mission page. "Programmes in this country tend to emphasise X" is a cultural prior, not published selection content, and must never appear in a dossier.
- **The programme's name, its department, its ranking, or your prior knowledge of the field.**
- **Selling points.** "Why study with us" copy, rankings claims, and brochure differentiators are the programme persuading applicants, not publishing a selection criterion. They are not even tier-4 framing evidence: they cannot count toward any gate and can never drop a target. They belong in the programme profile (step 6) only.

### 5. Assign exactly one status, and state it in the output

| Status | Meaning | What it licenses downstream |
|---|---|---|
| `declared` | The institution publishes a theme, track scope, or topic restriction | Full fit screen, including "outside scope → drop the target" |
| `inferred` | No declared theme; two or more official sources converge on an operative scope | Reweighting emphasis and ordering of real evidence; at worst a *stretch* label plus "verify with the programme". **Never a drop.** |
| `genuinely open` | Official pages fetched; no declared theme, and the inference gates did not pass — no cross-tier convergence, evidence too old, or the scope excludes nobody | No thematic screen applies; fit rests on the intellectual axis |
| `link needed` | Official pages not located or cycle's call unpublished | Nothing. Target stays unclassified until the link exists |

`genuinely open` and `link needed` must both remain visible outputs. Producing a theme for every target turns this skill into a framing generator — precisely the failure the whole screen exists to prevent.

### 6. Programme profile — pass C, on request, shortlisted targets only

Run this only when the user asks what a target offers, or when a "why this programme" paragraph or interview answer needs material — and only for targets the user is actually applying to. It runs for any target whose official programme page was located, even when the cycle's call is unpublished — skip it only when no official page exists — and it does not depend on passes A or B having found a theme. Characterising fifteen candidates does not need fifteen marketing reads. Fetch live, recording URL and access date, and give every item one **authority label**:

- `declared` — formal institutional content: published programme learning outcomes, a qualification or graduate profile, compulsory modules, thesis requirements.
- `evidenced` — observed data about what actually happens: graduate destination statistics, alumni placements, a published partner or internship list.
- `advertised` — the programme's own persuasion: "why study with us", scholarship mission slogans, claimed differentiators.

The authority label `declared` is not the dossier status `declared`: a declared graduate profile or learning outcome is never a declared theme and licenses no thematic screen.

Never merge the labels. An `advertised` claim and the `evidenced` data behind it are reported as two lines.

**(a) Selling points — what staff would say to convince you.** Collect them from the landing page, "why this programme" and FAQ pages, the scholarship or funder mission page, and partner lists. First write one **Positioning** sentence, in the programme's own frame, of how it sells itself — what it leads with (industry links rather than research training, mobility rather than depth) is itself informative about what it wants to be. Label it `advertised`; it informs the user and is never handed downstream as a differentiator. Then run two checks on each claim:

1. **Swap test.** Would the claim survive being moved to a competing programme? "World-class faculty", "international environment", "strong industry links", "interdisciplinary" — every programme says these. Mark them `generic` and drop them from the differentiator list.
2. **Backing check.** Is there a page that shows the claim — a named partner list, a mobility structure, a funded placement, a lab or dataset only this programme has? Backed → keep with its source. Unbacked → keep, labelled `advertised, unbacked`.

The differentiator list is the backed rows only. `advertised, unbacked` rows are listed beneath it for completeness and are never handed downstream as differentiators. An empty list is a legitimate answer.

**(b) Intended graduate — who the programme is built to produce.** Read the formal graduate or qualification profile (`declared`) and the career-prospects page — which is `advertised` unless it is itself a formal profile or is backed by destination data, then any destination or alumni data (`evidenced`). Extract the specialisations and capabilities the graduate is meant to hold, and the destinations the programme aims at — research/PhD pipeline, industry, public sector, the funder's home-country mission. Where the declared profile and the destination data disagree (a "research-oriented" programme whose graduates mostly go to industry), report both; the disagreement is the finding.

**(c) Expected outcomes — what they actually teach.** Formal programme learning outcomes first, then compulsory modules before electives, then required thesis, internship, or mobility components. Report what the programme **commits to teaching**, not what electives make possible.

Where a part has no official page, output `none published` for that part. Do not reconstruct a graduate profile from the programme's name or field.

The profile is **offer content, not selection content**. It never changes the theme status, and never drops a target. Pages fetched in pass C are never re-fed into step 4; for targets with status `inferred` or `genuinely open`, if pass C surfaces a tier-1 or tier-2 page that pass B missed, record `candidate theme evidence — re-run pass B` and leave the status unchanged.

### 7. Hand off

State explicitly which downstream question this dossier does *not* answer: whether the applicant fits. Route to `apply-program-fit-mapper` with the dossier, and carry the status label with it — the fit verdict's power depends on it.

## Output format

One block per target.

```markdown
# Theme Dossier: [Programme / pathway / call]

- **Unit extracted:** [programme | pathway | doctoral school | call | position]
- **Status:** declared | inferred | genuinely open | link needed
- **Cycle:** [year / call reference, or "not published"]

## Sources
| Source | URL | Accessed | What it contributes |
|---|---|---|---|

## Declared theme
> [verbatim institutional wording, or "none published"]

## Decomposition — research activities actually covered
- [Activity / method / domain] — evidence: [which source shows it]
- ...
- Genuinely broad in: [where the container was not narrowed]

## Operative theme (only when status = inferred)
- **Hypothesis:** [one sentence]
- **Converging sources:** [source 1, tier N] + [source 2, tier M] — different tiers, at least one from tier 1 or 2
- **Recency:** [dates of the evidence relied on]
- **Excludes:** [what this scope rules out — if nothing, the status is `genuinely open`, not `inferred`]
- **Not published by the institution** — may inform emphasis, must never be quoted as the programme's declared scope, and cannot drop this target.

## Pathways (multi-pathway targets)
| Pathway | Declared scope | Status |
|---|---|---|

## Programme profile (only when requested — pass C)
- **Positioning (advertised):** [one sentence, in the programme's own frame — not handed downstream]

### Differentiators (passed swap test and backing check)
| Claim | Authority | Backing page | Accessed |
|---|---|---|---|
<!-- authority: declared / evidenced / advertised (backed) -->
- Unbacked, not handed downstream: [advertised claims with no backing page]
- Dropped as generic: [claims every programme makes]

### Intended graduate
- **Declared profile:** [specialisations, capabilities, target destinations — or "none published"]
- **Evidenced destinations:** [data, year, source — or "none published"]
- **Mismatch:** [where declared and evidenced disagree, or "none found"]

### Expected outcomes
- **Learning outcomes:** [formal list, verbatim or close — or "none published"]
- **Compulsory components:** [modules, thesis, internship, mobility]

## Hard constraints found
- [topic restrictions, eligible research areas, mandatory specialisation choice, or "none found"]

## Not answered here
- Applicant fit. Route to `apply-program-fit-mapper` with this dossier and its status.
- How to use the programme profile in prose. Route differentiators and outcomes to `apply-sop-writer` or `apply-interview-prep`, and the intended graduate profile to `apply-program-fit-mapper` for the goal-fit check.
```

For a candidate list, precede the blocks with a one-row-per-target summary table (target, unit, status, one-line scope) so the user can triage before reading.

## Quality bar

A strong output lets the user say what each target selects for, and cite where that came from. Every theme traces to a fetched page with a date. No target carries a scope the institution did not publish without an `inferred` label attached, and no target is dropped on an inferred theme. Targets whose pages could not be found are visible as `link needed` rather than quietly missing. In a programme profile, no `advertised` claim is presented as a differentiator without the swap test, and no graduate profile appears that the institution did not publish.

Two counts are worth watching as a self-check. If `inferred` is firing on most targets, the exclusion test is not being applied and the dossiers are describing fields rather than scopes. If pass B ran on targets the user had already ruled out on country, funding, or deadline, the search budget was spent on nothing.

## Volatility

Themes, specialisation names, pathway lists, and topic restrictions change every cycle, and institutions differ within every country. This skill encodes the **extraction method only** — there is deliberately no catalogue of programmes and their themes, because such a catalogue would be wrong within a cycle. Re-extract per cycle.
