---
name: gre-quant-coach
description: Coach GRE Quantitative Reasoning — quantitative comparison tactics, problem-solving and data-interpretation strategy, content-gap triage, careless-error elimination, and timed drilling. Use this skill whenever the user works on GRE math ("quantitative comparison", "numeric entry", "why did I get this quant question wrong", "I keep making silly mistakes on quant", "GRE geometry/probability/percent review"), wants GRE-style quant practice sets, or asks how to get from a 160s score to a 168–170. Also use for quant pacing and calculator strategy. This is GRE test math (no calculus, no proofs) — for research-level math or ML theory use the theory-* or professor-mentor skills; for the verbal sections use gre-verbal-reasoning / gre-reading-comprehension.
---

# GRE Quantitative Reasoning Coach

GRE Quant tests high-school content under adversarial conditions: trap answers, deliberately awkward numbers, and time pressure. For most users — especially STEM/research users — the score gap is not mathematical ability but *test behavior*: unexamined assumptions in quantitative comparison, arithmetic slips, and answering a different question than the one asked. Diagnose which one before prescribing content review.

## Use this when

- The user shares a quant question and wants the fast, intended solution path (not just *a* solution).
- The user wants practice sets by topic, format, or difficulty.
- The user scores below their ability and wants to find out why ("careless mistakes", stuck at 162–166).
- The user wants a content review checklist or targeted topic drills.

## Do not use this when

- The math is beyond GRE scope (calculus, linear algebra, proofs, research math) — use `professor-mentor-technical-teaching` or the `theory-*` skills.
- The user wants a full multi-week study schedule — use `gre-learning-planner`.

---

## Format facts (stable since the Sept 2023 shortened GRE)

- Two Quant sections: 12 questions in 21 minutes, then 15 in 26 minutes; second section adapts to first-section performance. Scored 130–170.
- Question formats: **Quantitative Comparison** (fixed options: A greater / B greater / equal / cannot be determined), **multiple choice — one answer** (5 options), **multiple choice — one or more answers** (select all that apply, no partial credit), **Numeric Entry** (type the value), plus **Data Interpretation** sets (3ish questions on shared charts/tables).
- On-screen calculator (basic four-function + √). Skipping, marking, and returning within a section is allowed.
- Content scope: arithmetic, algebra, geometry (no proofs; figures NOT necessarily drawn to scale unless stated), data analysis (descriptive stats, probability, counting, normal distribution, chart reading). No trigonometry-heavy problems, no calculus.

---

## The score diagnosis — always run this first

When a user says "I want to improve quant", classify their misses from a recent practice set into:

1. **Content gap** — didn't know the fact/technique (e.g., forgot how normal-distribution percentages work). → Targeted topic review + drills.
2. **Trap taken** — knew the math, assumed something the problem didn't grant. → QC tactics and assumption hygiene below.
3. **Careless execution** — sign slips, misread numbers, answered the wrong quantity. → Error-proofing protocol below.
4. **Time pressure** — ran out, rushed the last stretch. → Pacing and triage below.

At 160+, categories 2–4 dominate; content review is mostly wasted time there. Below ~155, category 1 usually dominates and the content checklist matters. Say which regime the user is in.

## Quantitative Comparison tactics

QC is ~⅓ of the section and where strong-math users lose the most points, because it rewards *comparison* over *computation*.

- **Compare, don't compute.** Simplify both quantities together: add/subtract the same thing from both sides, divide both by a *known-positive* value, square both only when both are known non-negative. Stop the moment the relationship is forced.
- **Test adversarial numbers.** When variables are underconstrained, the burden is to *break* consistency. Standard battery: **0, 1, −1, a fraction between 0 and 1, a large number** — plus any boundary the constraints allow. Two different outcomes → answer D, immediately.
- **D-discipline**: if quantities contain no variables (pure numbers), D is impossible — eliminate it. If they do, actively hunt for D before trusting A/B/C.
- **Geometry QC**: figures are not to scale. Redraw the figure in at least two legal extreme configurations before comparing anything visual (lengths, angles, areas).
- The classic trap: assuming variables are positive integers. Write down the actual constraints given; everything else is up for grabs.

## Problem-solving and format tactics

- **Read the question stem last-line first** on word problems: know what is being asked (x? 2x? the difference? "how many are NOT…?") before parsing the setup. Underline/write down the asked-for quantity.
- **Ballpark before computing.** An estimate brackets the answer and catches slips; on Data Interpretation, estimation frequently *is* the intended path (answer choices are spread wide).
- **Backsolve and plug in.** MC answers are information — for "which value of x" problems, testing choices (start with the middle value) beats algebra when the algebra is messy.
- **Select-all**: evaluate each choice independently against the condition; never stop early. Check whether the condition can bound the possible values (min/max reasoning) instead of testing exhaustively.
- **Numeric Entry** has no elimination safety net: always sanity-check units, scale, and the exact form asked (fraction vs decimal vs percent; "nearest tenth").
- **Calculator discipline**: the on-screen calculator is slow and error-prone for multi-step work. Use it for one ugly arithmetic step, not as a thinking substitute. GRE numbers are usually chosen to cancel — if the arithmetic is getting ugly, suspect the path, not the calculator.

## Careless-error elimination protocol

"Careless" errors are systematic and fixable. Prescribe mechanically:

1. Keep an error log where every careless miss is written out to its *exact* mechanism ("dropped the negative when moving −3x", "solved for x, question asked x+y").
2. After ~15–20 logged errors, the top 2 mechanisms cover most of them. Install a *targeted check* for those only (e.g., a 3-second "what did they ask?" re-read before confirming) — global "be careful" advice does nothing; per-mechanism checks work.
3. Write intermediate steps on scratch paper even when the step feels trivial; most slips happen in mental steps.

## Pacing and triage

- Average ~1.7 min/question, but budget unevenly: QC ≈ 1 min, Data Interpretation ≈ 2+ min.
- Two-pass strategy: first pass answers everything answerable in ≤2 min, marks the rest; second pass returns with the remaining time. Never sink 4 minutes into one question on the first pass — every question is worth the same point.
- The last-5-questions rush is a pacing failure, not a math failure; it shows up in the error log as clustered end-of-section carelessness.

## Content checklist (for gap triage)

Arithmetic: integer properties (divisibility, primes, remainders, even/odd), fractions/decimals, exponents & roots, percent change, ratio & proportion.
Algebra: linear & quadratic equations, inequalities & absolute value, exponent rules, functions & compound functions, coordinate geometry (slopes, intercepts, distance).
Geometry: angles & parallel lines, triangles (special right triangles, similarity, triangle inequality), circles (arc/sector), polygons, area/perimeter/volume of standard solids.
Data analysis: mean/median/mode/range/standard deviation (conceptual), quartiles & boxplots, normal distribution (approximate 68–95 areas), counting (permutations/combinations), probability (independent, mutually exclusive, conditional basics), overlapping sets, chart/table interpretation.

Drill the *weak rows only* — confirmed by missed questions, not by self-report.

---

## Workflow

**Explaining a question**: get the user's approach first; show the intended fast path; if their path was valid but slow, say so and show the time difference; classify the miss into the four categories; log it.

**Generating practice**: GRE-style items in the requested format mix (default: 3 QC, 3 problem-solving of mixed formats, 2 data-interpretation on one dataset). Wrong answers must encode real traps (the sign-slip result, the solved-for-x-not-y value). Withhold solutions until answers are committed.

**Session end**: report accuracy by format and topic, the miss-category distribution, the top careless mechanism if any, and one concrete next-session instruction. Persistent content gaps → topic drill plan; persistent traps/carelessness → the protocols above, not more content review.
