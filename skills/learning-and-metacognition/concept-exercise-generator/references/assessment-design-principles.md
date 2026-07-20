# Assessment Design Principles

Use this file when writing exercise stems and answer options. It changes how problems are constructed; it is not a citation list.

## Scope and Calibration

- These rules are for assessment after exposure to material, not teaching the concept for the first time.
- They work best for concepts with causal, logical, mathematical, or procedural structure. For arbitrary facts, use short recall checks rather than elaborate misconception diagnosis.
- When borrowing from self-explanation research, state claims cautiously: Chi et al. 1989 is small-N, and cross-domain confidence rests on later work by Chi 1994 in biology, Renkl in probability, Aleven and Koedinger in geometry tutoring, Bielaczyc in programming, and Bisra et al. 2018 as meta-analysis.
- Applying these principles to AI-assisted expert work is an extrapolation from studies of learners acquiring new material. Use them as design heuristics, not as a direct empirical guarantee.

## FCI / Mazur: Distractors Diagnose Misconceptions

Decision rule: multiple-choice questions are allowed only when the wrong answers are plausible wrong mental models.

Do:

- write each distractor to encode a named misconception;
- make a wrong choice diagnose which model the learner is using;
- include solution feedback that maps each distractor to the misconception and the source section to revisit;
- prefer misconception distractors for Tier 1-3 conceptual checks where the field has known confusions.

Do not:

- use random wrong answers;
- use obviously impossible answers just to fill options;
- ask "which looks right?" without requiring reasoning;
- treat a missed multiple-choice item as merely incorrect when it can diagnose a specific wrong model.

Minimum option format:

- Correct: the target model.
- Distractor A: misconception 1.
- Distractor B: misconception 2.
- Distractor C: misconception 3, or omit the option if no real misconception exists.

## CRT / Frederick: Intuitive-But-Wrong Verification Trap

Decision rule: include an exercise archetype where a fast intuitive answer is attractive but wrong, and the learner must deliberately verify.

Use this archetype when the concept has a common shortcut, symmetry assumption, base-rate neglect, sign error, quantifier slip, missing normalization, or off-by-one style trap.

Problem shape:

1. Present a compact scenario where the tempting answer is easy to compute mentally.
2. Ask for the answer and a verification step.
3. In the solution, name the intuitive wrong answer, explain why it attracts, and show the deliberate check that defeats it.

This is especially useful in Tier 2-3 problems: it tests whether the learner can slow down and audit a fluent first impression before building on it.

## Construction Checklist

- If a question is multiple choice, every distractor must diagnose a misconception.
- If a topic has a known intuitive trap, include one CRT-style verification problem in the ladder.
- If no real misconception or intuitive trap is known, use open-ended computation, derivation, diagnosis, or counterexample problems instead of fake options.
- In `solutions.md`, every diagnostic option or intuitive trap must map to a revisit pointer.
