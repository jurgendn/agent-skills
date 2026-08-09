# Calibration example — the first-person gap and STAR/AR

One worked contrast. The point is not the wording; it is what the assessor can and cannot score.

---

## Question (asked by a DAAD-style committee, assessor type A)

*"Tell me about a time an experiment or project did not work out."*

---

## Weak answer

> "In my master's project we were working on a segmentation model for medical images. We had a lot of problems with the data — the annotations were inconsistent between hospitals, so the results were not good at first. We tried different approaches and eventually we got it working. It taught me that data quality is really important in machine learning."

**Why this fails, precisely:**

- **No individual action.** Every verb is "we." The committee is scoring one person and has been given nothing to score. This is the most common correctable weakness, and structured protocols are specifically designed to surface it.
- **No task.** What was this person responsible for? Unclear.
- **The result is vague.** "Eventually we got it working" — by what measure, how much better, over what baseline?
- **The lesson is a platitude.** "Data quality is important" is not a finding; every assessor already believes it. Nothing here distinguishes the candidate.
- **No alternative.** Nothing indicates the candidate's practice actually changed.

---

## Restructured with STAR/AR

> **(Situation)** "In my master's project I was building a segmentation model on chest imaging pooled from three hospitals. **(Task)** I owned the data pipeline and the evaluation setup. **(Action)** Validation performance was strong but the model failed on the third hospital's scans. I suspected the annotations rather than the model, so I pulled a sample of 200 cases and re-checked them against the protocol — the third site had labelled a boundary differently, systematically. I re-specified the labelling rule, had the affected subset re-annotated, and re-ran the comparison. **(Result)** Cross-site performance gap dropped from about 11 Dice points to under 3, and the ablation showed the earlier result had been measuring annotation drift, not model quality.
>
> **(Alternative Action)** What I should have done was check label consistency across sites *before* training anything — I lost about six weeks. **(Alternative Result)** I would have caught it in the first week, and I would have had a cleaner story about which differences were real. I now run an inter-site agreement check as the first step of any pooled-data project, before I fit anything."

**Why this works:**

- **The first-person gap is closed.** "I owned", "I suspected", "I pulled", "I re-specified". The committee can now attribute specific judgement to this candidate.
- **The diagnosis is the content.** The interesting part is not that something failed — it is that the candidate suspected the *labels* rather than the model. That is the judgement being assessed.
- **The result is measured.** 11 → 3 Dice points, plus what the ablation established. Falsifiable, and it shows the candidate knows what their own numbers mean.
- **AR converts the failure into evidence.** The cost is admitted plainly (six weeks), and the change in practice is concrete and permanent. Admitting the cost is what makes the lesson credible.
- **It survives follow-up.** Every claim opens a door the candidate can walk through — why 200 cases, why Dice, what the protocol said. A memorised answer has no such doors.

---

## Calibration note

The restructured answer says "I" repeatedly and states a measured improvement. For an applicant trained in a modesty-valuing setting this can feel like boasting.

It is not — every claim is work the candidate actually did, and the six-week cost is stated openly rather than hidden. Understating a real contribution to a committee that expects direct claims is a transmission failure, not modesty: the assessor's estimate of the contribution ends up lower than the truth.

The rule is accuracy, in both directions. Do not inflate, and do not deflate.

---

## Adapting by assessor type

- **Type B (prospective supervisor):** compress the numbers, expand the reasoning. A supervisor cares more about *why you suspected the labels* than about the final Dice figure, and will probably interrupt to ask.
- **Type C (administrative/embassy panel):** strip the jargon entirely. "The data from one hospital had been labelled to a different standard, which made the results look better than they were. I found it, fixed it, and changed how I start projects." Depth is not the exam; clarity is.
