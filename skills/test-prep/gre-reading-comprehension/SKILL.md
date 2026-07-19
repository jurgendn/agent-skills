---
name: gre-reading-comprehension
description: Coach GRE Reading Comprehension and paragraph-argument (critical reasoning) questions — passage mapping, question-type strategies, wrong-answer elimination, and timed drilling. Use this skill whenever the user works on GRE reading passages or shares an RC question ("why is this inference wrong", "main idea vs primary purpose", "select-in-passage", "select all that apply"), asks how to read dense GRE passages faster, or works on strengthen/weaken/assumption/paradox questions. Also use to generate GRE-style passages and question sets for practice. For fill-in-the-blank Text Completion / Sentence Equivalence use gre-verbal-reasoning; for IELTS Reading use ielts-reading-strategies; for auditing real research arguments use argument-audit.
---

# GRE Reading Comprehension Coach

GRE RC rewards reading for *architecture* — what the author claims, why, and how the parts relate — and punishes reading for detail retention. Every correct answer is provable from the passage text; every wrong answer is wrong for a nameable reason. Coaching means training the user to demand that proof.

## Use this when

- The user shares a GRE passage question and wants the reasoning behind right/wrong answers.
- The user wants practice passages and question sets (by passage type, question type, or difficulty).
- The user reads too slowly, re-reads constantly, or "understands the passage but misses the questions".
- The user works on paragraph-argument questions: strengthen, weaken, assumption, conclusion, paradox, boldface/role.

## Do not use this when

- The question is a sentence with blanks — use `gre-verbal-reasoning`.
- The user is preparing IELTS Reading — use `ielts-reading-strategies` (different test, different question logic).
- The user wants to check whether a real argument in their own work holds — use `argument-audit`.

---

## Format facts (stable since the Sept 2023 shortened GRE)

- RC questions appear in both Verbal sections mixed with TC/SE; roughly half of the ~27 verbal questions are passage-based.
- Passages: mostly one paragraph; a few 2–4 paragraphs; drawn from sciences, social sciences, humanities, and everyday topics. No outside knowledge is ever required or rewarded.
- Question formats: multiple choice with one answer (5 options); multiple choice with one *or more* answers (3 options, no partial credit); select-in-passage (click the sentence that…).
- Paragraph arguments: a short (3–6 sentence) argument followed by one critical-reasoning question.

---

## Reading method: map, don't memorize

For any passage longer than a few sentences, read once with the goal of producing a **passage map** — then answer questions by *returning to the text*, never from memory.

The map (mental for short passages, 1 line per paragraph for long ones):

1. **Main point** — the one thing the author wants you to walk away believing.
2. **Structure** — what each paragraph *does* (presents a view / attacks it / offers evidence / qualifies / proposes an alternative), not what it *says*.
3. **Tone/stance** — is the author neutral reporter, advocate, or critic? Most wrong answers on purpose/attitude questions violate stance.
4. **Flags** — pivots ("however", "yet recent work…"), attribution shifts ("critics contend" vs. the author's own voice), and hedges. Attribution errors (assigning a cited view to the author) power many trap answers.

Details (dates, names, mechanisms) get *located*, not learned — know which paragraph holds them.

## Question-type playbook

| Type | Ask yourself | Trap to expect |
|------|--------------|----------------|
| Main idea / primary purpose | What does the *whole* passage do? | A choice true of one paragraph only |
| Detail ("according to the passage") | Where is this stated? Re-find the line | Accurate-sounding paraphrase that distorts one word |
| Inference ("suggests", "implies") | What *must* be true given the text — smallest possible step | A reasonable real-world claim the passage never commits to |
| Function/role ("in order to") | What job does this sentence do for the argument? | Describes content correctly, function wrongly |
| Author's attitude | Which words carry evaluation? | Overstated stance (passage: mild reservation → choice: "vehement rejection") |
| Vocab-in-context | What does the word do *in this sentence*? | The word's most common meaning |
| Select-in-passage | Which sentence performs the named function? | A sentence about the right topic doing the wrong job |
| Multiple-answer (select all) | Judge each option independently, yes/no | Stopping after finding one good answer |

**The line-reference discipline**: before confirming any answer, point to the words in the passage that prove it. If the user can't quote the evidence, they are guessing — even when the guess is right. Enforce this in every explanation.

## Wrong-answer taxonomy

Teach elimination by name; the same five families cover nearly every trap:

1. **Out of scope** — introduces something the passage never discusses.
2. **Extreme** — "always/never/only/impossible" where the passage hedges.
3. **Distortion** — right elements, wrong relationship (cause↔effect swapped, view misattributed).
4. **Opposite** — contradicts the passage; catches speed-readers who missed a pivot.
5. **True but not asked** — accurate to the passage, unresponsive to the question.

## Paragraph arguments (critical reasoning)

First, always decompose: **conclusion** (what the author wants accepted) / **evidence** (what's offered) / **assumption** (the unstated bridge). Then:

- **Weaken**: attack the assumption — usually an alternative cause, a disanalogy, or a sampling flaw. Not: contradict the evidence.
- **Strengthen**: shore up the assumption — rule out the alternative, confirm the analogy holds.
- **Assumption**: the negation test — negate the choice; if the argument collapses, it's the assumption.
- **Paradox/explain**: find the choice that lets *both* stated facts stay true.
- **Boldface/role**: label each bold portion as evidence, conclusion, opposing view, or concession — match labels, ignore content.

## Timing and pacing

- Budget: TC/SE fast (see `gre-verbal-reasoning`), leaving ~1.5–2 min per RC question *including* first read. One-paragraph passage + 1 question ≈ 2.5 min total; a long passage with 3–4 questions earns its ~7–8 minutes.
- Read the passage once, properly. The "skim then hunt" habit imported from other tests fails on GRE inference-heavy questions and causes double reading.
- Chronic re-readers: the cause is usually reading for detail. Drill map-writing — one line per paragraph, then answer with the passage available. Speed follows structure.

---

## Workflow

### Explaining a question

1. Ask what the user picked and their reasoning first.
2. Rebuild the passage map together (or the conclusion/evidence/assumption breakdown for arguments).
3. Prove the correct answer with quoted text; name the trap family of each wrong answer, especially theirs.
4. Classify the miss: **map failure** (misread the passage) / **question misread** / **elimination failure** (had it down to two) / **time pressure**. Down-to-two misses deserve special attention: log which trap family keeps winning.

### Generating practice

- Write GRE-register passages (dense, argumentative, hedged; science/humanities/social-science rotation) with a mix of question formats, including select-in-passage and select-all.
- Every generated question must survive the line-reference discipline: the explanation quotes the proving text.
- Withhold answers until the user commits; end with the error table (same format as `gre-verbal-reasoning`: result, miss class, detail) and one instruction for next session.

### Session-end report

Accuracy by question type, dominant miss class, dominant trap family, and pacing observations. Recurring *map failures* → more untimed structural reading; recurring *elimination failures* on one trap family → targeted sets seeded with that trap.
