---
name: research-proposal-writer
description: >-
  Write or refine a forward-looking research proposal — a plan for work not yet
  done, judged on plausibility and feasibility rather than results. Two modes:
  a PhD research proposal for a prospective supervisor, admissions committee, or
  fellowship (what you will do over the next several years), or a next-paper
  proposal pitched to your current advisor (what the next paper is and how you
  will get there). Trigger on "refine my research proposal", "research plan for
  my PhD application", "proposal for my professor about the next paper", "what
  I'll work on for the next N years", "pitch my next project to my advisor",
  "is my research plan convincing". NOT the SOP essay (apply-sop-writer), not
  grading a finished draft against a named reader (professor-critic), not
  stress-testing the idea itself (research-idea-stress-test), and not building
  defense slides (deck-beamer-proposal-report).
---

# Research Proposal Writer

A proposal is not a paper: there are no results to defend, so it is judged entirely on plausibility and feasibility. The register this forces is specific — you promise **questions and deliverables**, never outcomes. "We will determine whether X holds under Y, and either answer is publishable" is fundable; "we will improve SOTA by 3%" is a red flag, because nobody can promise a result they haven't produced.

Condensed source material (Heilmeier Catechism, SSRC, MIT Comm Lab, Peyton Jones, Ten Simple Rules) lives in `references/proposal-sources.md`. Consult it when drafting; the durable principles are baked into this file.

## When NOT to use this skill (route out first)

- The gap itself is shaky or unmotivated → `gap-motivation-builder` first; there is nothing to propose yet.
- The solution direction hasn't survived any attack → `research-idea-stress-test` before investing in prose.
- The user wants the evaluation/comparison plan designed in depth → `benchmark-and-baseline-selector`.
- The draft is finished and the user wants a verdict as their real reader would give it → `professor-critic`.
- The user needs the SOP/personal essay for an application → `apply-sop-writer`.
- The proposal is done and needs defense slides → `deck-beamer-proposal-report`.

## Intake (one batch, then proceed)

Ask once, together:

1. **Mode** — PhD proposal (prospective supervisor/committee/fellowship, multi-year horizon) or next-paper pitch (current advisor, one paper cycle)?
2. **Reader and constraints** — who reads it, page/word limit, any mandated sections (e.g., NSF Intellectual Merit / Broader Impacts; EU Excellence / Impact / Implementation). Treat program-specific limits and criteria wording as volatile: use what the user provides, and mark anything uncertain "verify against the live call" rather than asserting it.
3. **What exists** — a draft to refine, rough notes, or just an idea?

**Precondition:** if the user cannot state the research question and why current approaches fail at it, stop — route to `gap-motivation-builder` and say why. A proposal written around an unmotivated gap wastes the polish.

## The three reviewer questions

Every reviewer scans the proposal for exactly three answers (Przeworski & Salomon):

1. **What will we learn that we do not know now?**
2. **Why is it worth knowing?**
3. **How will we know the conclusions are valid?**

Reviewers are overloaded and often outside your subfield; they will not dig for hidden answers. The opening paragraph — first page at most — must answer question 1 crisply, with no jargon. A clearly posed non-rhetorical question or a bold central claim both work. Leave the reader one memorable message: you want to be "the one who claims X" in the committee discussion, not "the one from that university."

## The shared skeleton

Both modes fill the same skeleton, which maps onto the Heilmeier Catechism:

| Section | Answers (Heilmeier) |
|---|---|
| 1. Problem & objective | What are you trying to do, in plain language? Why is it hard? |
| 2. State of the art & gap | How is it done today; what are the limits of current practice? |
| 3. Proposed approach | What is new, and why do you think it will succeed? |
| 4. Workplan & milestones | How long will it take? What are the mid-term and final "exams"? |
| 5. Evaluation plan | How will success be measured? |
| 6. Risks & fallbacks | What are the risks — and what still gets learned if the main idea fails? |
| 7. Expected contributions & payoff | Who cares; what difference does success make? |
| 8. Fit & resources *(PhD mode only)* | Why this supervisor/lab/program specifically? |

Methodology (sections 3–5) is **an argument, not an agenda**: a list of tasks does not prove the tasks add up to the best attack on the problem. Say what you will actually *do* — the datasets, instruments, proofs, experiments, analysis techniques — and why that sequence answers the question. Most proposals fail because they leave the reviewer wondering what the applicant will actually do.

## Mode calibration

### PhD mode (multi-year, prospective reader)

- **Scope:** roughly 3–4 connected publishable units under one thesis question — a thread, not a list of disconnected projects and not one paper stretched over four years.
- **Certainty gradient:** year 1 concrete (specific first study, named data/methods), later years directional (questions that depend on early findings). A plan equally detailed in year 4 as in year 1 reads as naive.
- **It's a demonstration, not a contract:** committees fund the *person*; nobody holds you to the plan. What's being graded is whether you can pose an important question, know the field, and design a credible attack.
- **Fit is dependency, not flattery:** name what in the supervisor's expertise, equipment, data, or collaborations the plan actually *requires*. "I admire your work on X" carries no information; "WP2 needs the longitudinal cohort your lab maintains" does.
- **Write for a tired, interdisciplinary panel:** first page jargon-free; technical depth later or in an appendix.
- **Bibliography is a seriousness signal:** reviewers use it to check you won't duplicate existing work; one missing directly-relevant reference is costly.

### Next-paper mode (one cycle, your own advisor)

- **Scope:** one falsifiable claim plus the minimal experiment set that would establish it. If it needs three claims, it's two papers.
- **Length:** 1–2 pages. Your advisor reads it in minutes; density beats completeness.
- **Timeline in weeks/months** with explicit decision points: "if the pilot doesn't show the effect by week 6, we pivot to the fallback or kill it."
- **End with the ask:** what you need from the advisor — compute, data access, a go/no-go, co-author time — stated explicitly.
- **Skip** the fit section and most background; your advisor knows the field. Spend the space on the claim, the evidence plan, and the risks.

## Failure-mode checklist

Run this on every draft (refine mode) and on your own output (draft mode):

1. **Promised outcomes.** Any sentence guaranteeing a result ("will outperform", "will achieve") → rewrite as a question or deliverable where either answer is informative.
2. **"We will explore / investigate / look at X."** Not a research operation. Replace with the actual operations: which experiment, which proof strategy, which dataset, which analysis.
3. **Task list without argument.** The workplan must argue *why these tasks are the best attack*, not just enumerate them.
4. **Single point of failure.** If WP2–4 all die when WP1's idea fails, the plan is a bet, not a plan. Decouple work packages; give each risk a fallback that still yields a contribution.
5. **Ambition miscalibration** — both directions: one paper's worth stretched over years (too thin) or a career's worth in one proposal (not credible). Calibrate to the mode's scope rule above.
6. **Nothing at stake.** The plan tendentiously marches to a preconceived conclusion. There must be a genuine unknown; say what would prove the idea wrong.
7. **Vague timeline.** Milestones must be checkable events ("working prototype evaluated on X by month 9"), and pivots must be named in advance.
8. **Jargon on page one.** The opening must survive a reader from an adjacent field.
9. **Fit as flattery** (PhD mode). See calibration above.
10. **No evaluation plan.** Every proposal carries a minimal + suggested comparison set (baselines/benchmarks or, for theory, the validity test). Route to `benchmark-and-baseline-selector` when this needs real design work.
11. **Buried lede.** The three reviewer questions not answerable from the first page.

## Process

### Draft mode (from notes or an idea)

1. Intake batch.
2. Produce a **skeleton outline**: each section from the table above with a 1–2 sentence commitment of what it will say. Flag any section where information is missing with `[NEEDED: ...]` — never invent gap claims, resources, or timelines.
3. Get the user's approval on the skeleton (this is where scope and ambition get corrected cheaply).
4. Write the prose, then run the failure-mode checklist on it and report anything that survives.

### Refine mode (existing draft)

1. Read the whole draft first.
2. Run the failure-mode checklist; rank findings by severity (kills the proposal / weakens it / polish).
3. **Report the diagnosis before rewriting** — never silently rewrite. The user decides what to accept.
4. Revise the affected sections, preserving what already works.

### Handoffs

Weak gap → `gap-motivation-builder`. Untested direction → `research-idea-stress-test`. Evaluation design → `benchmark-and-baseline-selector`. Finished draft, named-reader verdict → `professor-critic`. Slides → `deck-beamer-proposal-report`.

## Output format

```markdown
# [Proposal title]

[Sections per the skeleton, mode-calibrated]

---

## Notes

**Missing information ([NEEDED] items):** ...
**Claims requiring citations or verification:** ...
**Volatile program details to verify against the live call:** ...
**Checklist items that survived (with severity):** ...
```

Refine mode additionally opens with the ranked diagnosis before any revised text.

## Quality bar

After the first page, the reader can state the question, why it matters, and what you will actually do. After the full read, they can name the milestones, the biggest risk and its fallback, and how success will be measured — and they remember one sentence of it the next day.
