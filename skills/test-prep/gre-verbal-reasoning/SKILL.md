---
name: gre-verbal-reasoning
description: Coach GRE Verbal Reasoning Text Completion and Sentence Equivalence — explain items, generate practice sets, diagnose recurring error patterns, and drill the predict-then-match method. Use this skill whenever the user works on GRE fill-in-the-blank questions, shares a Text Completion or Sentence Equivalence item ("why is the answer B", "I picked the trap again"), asks for TC/SE practice questions, wants strategy for two- and three-blank questions, or asks why they keep missing verbal questions despite knowing the words. Also use for GRE verbal timing strategy and section-adaptive pacing. For GRE reading passages and critical-reasoning questions use gre-reading-comprehension; for learning and retaining vocabulary itself use gre-vocabulary-builder; for IELTS (not GRE) use the ielts-* skills.
---

# GRE Verbal Reasoning Coach (Text Completion & Sentence Equivalence)

TC and SE are logic questions wearing vocabulary costumes. The sentence always contains enough structural evidence to determine the blank before looking at the choices; a miss is either a vocabulary gap, a misread of that evidence, or a trap taken. The coaching goal is to make the user identify which of the three happened, every time.

## Use this when

- The user shares a TC or SE item and wants the reasoning, not just the answer.
- The user wants a practice set of TC/SE items (by difficulty, blank count, or target vocabulary).
- The user keeps missing TC/SE and wants a diagnosis of why.
- The user asks how to handle two- and three-blank questions or how to pace the verbal sections.

## Do not use this when

- The question has a passage — use `gre-reading-comprehension` (including short critical-reasoning arguments).
- The user wants to learn or retain word lists — use `gre-vocabulary-builder`.
- The user wants a full study schedule — use `gre-learning-planner`.

---

## Format facts (stable since the Sept 2023 shortened GRE)

- Two Verbal sections: 12 questions in 18 minutes, then 15 questions in 23 minutes. The second section's difficulty adapts to first-section performance.
- **Text Completion**: 1–3 blanks. Single-blank items have 5 choices; two- and three-blank items have 3 choices per blank. No partial credit — all blanks must be right.
- **Sentence Equivalence**: one sentence, one blank, 6 choices; select exactly the 2 that each complete the sentence AND produce sentences alike in meaning. No partial credit.
- Within a section you can skip, mark, and return freely — pacing strategy matters.
- Scored 130–170, combined with RC questions in the same sections.

---

## The core method: predict, then match

Never read the choices first. Choices are written to sound plausible; the sentence is written to be determinate. The sequence is:

1. **Read the sentence for structure, ignoring the blank.** Find the *clue* (the phrase the blank must agree or contrast with) and the *road sign* (the connective that says which).
2. **Predict a fill** — your own word or phrase, even a clumsy one ("something like 'stubborn'", or just "a negative word about his honesty").
3. **Match choices against the prediction.** Eliminate anything that contradicts the road-sign logic, regardless of how sophisticated it sounds.
4. **Re-read the completed sentence.** It must be coherent as a whole, not just blank-locally.

### Road signs to train until automatic

| Type | Signals | Effect on blank |
|------|---------|-----------------|
| Contrast | although, but, yet, despite, however, paradoxically, far from, once…now | Blank opposes the clue |
| Continuation | and, indeed, moreover, likewise, just as, semicolon with no pivot | Blank agrees with the clue |
| Cause/effect | because, thus, therefore, so…that, given | Blank follows logically from the clue |
| Negation stack | not un-, hardly, scarcely, fails to, belies | Flip polarity — count the negatives explicitly |
| Punctuation | colon, semicolon, apposition commas | What follows restates or defines — strong agreement signal |

Double negatives and irony ("his critics conceded that…") are where high-difficulty items live. When a user misses these, the fix is mechanical: mark every polarity flip in the sentence before predicting.

### Multi-blank strategy

- Blanks are not attacked in order — attack the blank with the strongest local clue first (often the second or third). Solving it constrains the others.
- Each blank's 3 choices are independent; do not look for "theme" answers across blanks.
- After filling all blanks, always re-read the full sentence. Multi-blank traps are locally fine, globally incoherent.

### Sentence Equivalence specifics

- The two correct answers usually form a near-synonym pair, but the test is *sentence meaning equivalence*, not word synonymy — occasionally two non-synonyms both work, and a synonym pair can both be wrong.
- Predict first, then scan for a pair matching the prediction. A choice with no partner is almost never correct even if it fits — use this to eliminate, not to pick (a lone perfect-fit word means re-examine your prediction).
- Charge (positive/negative/neutral) eliminates fast: if the sentence needs a critical word, cross out all approving choices before weighing nuance.

---

## Trap taxonomy — name the trap when explaining a miss

1. **Opposite trap** — the choice fits the clue but with inverted polarity; caused by missed road signs or negation stacks.
2. **Word-you-know trap** — a familiar word that is topically related but logically wrong; chosen over an unfamiliar correct answer. Rule to teach: *never eliminate a word solely because you don't know it; eliminate words you know don't work.*
3. **Half-right multi-blank** — one blank forced an interpretation the other blanks contradict.
4. **Secondary-meaning miss** — the correct answer uses a less common sense ("qualify" = limit, "flag" = weaken, "check" = restrain). Send recurring cases to `gre-vocabulary-builder`.
5. **Sophistication bait** — the hardest-looking word chosen because the item felt hard. Difficulty lives in sentence logic more often than in word rarity.

---

## Workflow

### Explaining an item the user shares

1. Ask what they picked and *why*, before revealing anything — the diagnosis is in their reasoning, not their answer.
2. Walk the method: clue → road sign → prediction → elimination. Show why each wrong choice is wrong (name the trap).
3. Classify the miss: **vocabulary gap / structure misread / trap taken / careless**. State the classification explicitly.
4. If vocabulary gap: give the word's meaning, charge, and one TC-style example sentence; suggest adding it to the user's `gre-vocabulary-builder` rotation.

### Generating practice

- Default set: 6 items — 2 single-blank TC, 2 multi-blank TC, 2 SE — at the requested difficulty; answers and explanations withheld until the user commits answers.
- Write items GRE-style: academic register, a determinate clue + road sign per blank, wrong answers that are attractive for a *specific* nameable reason.
- On request, build sets around the user's weak vocabulary or weak trap types.
- Track results across the session in a running error table (see below).

### Drilling and pacing

- **Accuracy before speed**: untimed drills until ~85% accuracy at a difficulty level, then timed (TC single-blank ~45s, multi-blank ~90s, SE ~60s).
- TC/SE are the section's time bank — banking time here funds the RC passages. A user consistently over ~90s per item should practise predicting on a 30-second timer even at the cost of accuracy for a week; prediction speed is trainable, verification speed is not.
- In-section: first pass takes every TC/SE and short RC; mark and return to long-passage stragglers.

---

## Error log format

Keep a per-session (or per-user, if a practice vault exists) table:

```
| # | Item type | Result | Miss class | Detail |
|---|-----------|--------|------------|--------|
| 1 | TC 2-blank | ✗ | structure misread | missed "far from" contrast |
| 2 | SE | ✓ | — | — |
| 3 | TC 1-blank | ✗ | vocab gap | "protean" |
```

End every practice session with: accuracy by item type, the dominant miss class, and one concrete instruction for the next session (e.g., "circle every negation before predicting"). A dominant *vocab gap* pattern routes to `gre-vocabulary-builder`; a dominant *structure misread* pattern means more untimed drills here.
