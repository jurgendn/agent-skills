---
name: gre-issue-essay
description: Draft, score, and improve GRE Analytical Writing "Analyze an Issue" essays against the 0–6 rubric. Use this skill whenever the user shares a GRE Issue prompt or essay ("score my GRE essay", "AWA feedback", "how do I structure the Issue task", "what does a 5.0 essay need that a 4.0 doesn't"), wants a model essay, asks about the 30-minute timing, or wants targeted practice on position-taking, examples, or counterargument handling. Covers all six official instruction variants (agree/disagree, recommendation, claim-with-reason, two views, consequences). For IELTS essays use ielts-writing-task2; for auditing whether an argument's logic actually holds use argument-audit; for SOP/application essays use apply-sop-writer.
---

# GRE Issue Essay Coach (Analytical Writing)

The Issue task gives 30 minutes to take a position on a general-interest claim and defend it with reasons and examples. Since the Sept 2023 shortened GRE it is the *only* essay (the "Analyze an Argument" task was removed). It is scored 0–6 in half-points by a human rater plus ETS's automated scorer; what separates 4 from 5 from 6 is depth of position and quality of development, not vocabulary display.

## Use this when

- The user shares an Issue prompt and wants a plan, a model essay, or a timed-practice setup.
- The user shares their essay and wants a score estimate with rubric-anchored feedback.
- The user asks about structure, examples, counterarguments, or the 30-minute clock.

## Do not use this when

- The essay is IELTS — use `ielts-writing-task2` (different rubric, different task logic).
- The user wants their own real argument checked for validity — use `argument-audit`.
- The essay is a statement of purpose or application essay — use `apply-sop-writer`.

---

## Task facts

- 30 minutes, one prompt, typed in a plain editor (no spellcheck). No minimum length, but scored essays at 5+ are almost always ≥ 500 words because development takes space — length is a byproduct of development, never the goal.
- Every possible prompt is in the published ETS Issue pool (searchable on ets.org) — practice from the real pool.
- Each prompt carries one of six standard instruction stems. **The stem changes what a complete response is** — ignoring it caps the score:

| Stem asks for | A complete response must |
|---------------|--------------------------|
| Agree/disagree with a statement | Take a position AND consider ways the statement might or might not hold |
| Agree/disagree with a recommendation | Discuss specific circumstances where adopting it would or wouldn't be advantageous |
| Which of two views aligns with yours | Choose one AND address both views |
| Claim + underlying reason | Evaluate the claim AND the reason offered for it |
| Consequences of adopting a policy | Argue from predicted outcomes |
| Statement with a qualification | Discuss when it holds and when it doesn't |

> Score anchors: [`references/awa-scoring-rubric.md`](references/awa-scoring-rubric.md) — the 0–6 levels in compact form with the official-source pointer. Consult it before assigning any score so feedback stays anchored to the rubric, not impression.

---

## What actually moves the score

The 4→5→6 gradient, in order of leverage:

1. **A position with texture.** A 4 asserts a side; a 5–6 stakes a claim *and* marks its limits ("X is generally true, but fails precisely when…"). The instruction stems explicitly invite this — the qualification IS the response to "consider ways it might not hold".
2. **Developed reasons, few in number.** Two or three reasons argued deeply beat five asserted. Each body paragraph: claim → reasoning → *specific* example → link back to the thesis. "Many historical figures show that…" is a 4; a named case examined in two or three sentences is a 5–6. Examples may come from history, science, current events, literature, or well-drawn hypotheticals — specificity matters, domain doesn't, and invented statistics are unnecessary risk.
3. **An honest counterargument.** One paragraph that states the strongest opposing consideration and *answers* it (concede scope, then show why the thesis survives). Straw men read as a 4.
4. **Organization that carries the logic.** Paragraph order should be an argument, not a list; transitions signal logical relation ("this holds even when…", "the deeper problem is…") rather than enumeration ("Secondly…").
5. **Language: varied, precise, and controlled.** Errors matter only when frequent enough to obscure meaning; thesaurus decoration lowers precision and reads as a weaker essay. Fix clarity before fanciness.

## The 30-minute protocol

| Minutes | Do |
|---------|-----|
| 0–4 | Read the stem twice. Brainstorm both sides (fastest route to a nuanced thesis and a real counterargument). Pick position, jot 2–3 reasons + one example each + the counterargument. |
| 4–26 | Write: intro (context sentence + thesis with its qualification) → 2–3 reason paragraphs → counterargument paragraph → short conclusion that restates the qualified thesis. Intro and conclusion stay short; the middle is where points live. |
| 26–30 | Proofread for typos, dropped words, sentence boundaries. No restructuring. |

If time collapses: a complete essay with a conclusion outscores a longer torso that stops mid-thought — always land the ending.

---

## Workflow

### Scoring a user's essay

1. Identify the prompt's instruction stem and check the essay answered *that* task — stem-mismatch is the first thing to flag, before any prose feedback.
2. Read against the rubric reference and assign a half-point score with a one-line justification per rubric dimension (position, development, organization, language).
3. Give feedback in leverage order (the list above): the 1–2 changes worth the most points first, each illustrated by quoting the user's own sentences and showing the upgraded version.
4. End with:

```
Estimated score:  X.X / 6
Biggest lever:    <one sentence>
Next drill:       <one concrete practice instruction>
```

Calibration honesty: text-only scoring can't see the timed conditions; say the estimate assumes the essay was written in 30 minutes without tools, and ask if it wasn't.

### Producing a model essay or plan

- Under timed-realistic constraints: ~500–650 words, achievable structure, no encyclopedic examples the user couldn't produce live.
- Label the parts (thesis, reasons, counterargument) and annotate *why* each paragraph earns its keep, so the user learns the skeleton, not the specific essay.

### Timed practice

Offer prompts from Issue-pool themes (society, education, technology, government, intellectual life), enforce 30 minutes, then score as above. Track scores and recurring feedback across sessions; recurring grammar-level issues in a Vietnamese-L1 user can be drilled with `ielts-grammar-coach`'s general-English mode.
