# Metacognition Foundations

Use this file only to construct and grade the single knowledge-debt probe. It is a decision skeleton, not a literature review.

## Scope and Calibration

- Fire probes only on dependency-structured material: proofs, derivations, mechanisms, algorithms, code paths, experimental claims with causal logic. Do not use this machinery for arbitrary facts, labels, trivia, or glossary recall.
- Treat the learning-science evidence as strongest for people acquiring new material. Using these probes to audit whether an expert has internalized AI-assisted work is an extrapolation. The mechanism plausibly transfers because both cases require generative reconstruction, but the studies do not directly test expert audit of AI-assisted output.
- State effect-size claims cautiously. Chi et al. 1989 is small-N. Cross-domain confidence comes from later self-explanation evidence: Chi 1994 in biology, Renkl in probability, Aleven and Koedinger in geometry tutoring, Bielaczyc in programming, and Bisra et al. 2018 as meta-analysis. Do not present the 1989 study alone as decisive.

## Rozenblit and Keil: Rate, Generate, Re-rate

Decision rule: the reactive circuit-breaker is a three-step loop.

1. **Rate:** ask the learner for a quick self-rating of understanding before the probe.
2. **Generate:** require a no-lookback, step-by-step explanation of the load-bearing dependency.
3. **Re-rate:** ask for the self-rating again after generation.

The debt signal is the gap between pre-generation confidence and post-generation confidence, plus the quality of the generated answer. A large downward re-rate after forced explanation means the learner had an illusion of explanatory depth. A high rating that survives generation is not enough by itself; the answer still must pass the grading rules below.

Use this loop when the user is about to build on an AI-produced result. Do not use it as a general teaching routine.

## Koriat and Bjork: Fluency Is Not Knowledge

Decision rule: no-lookback is mandatory for ownership checks.

Reading the source, recognizing familiar phrases, or seeing that an answer "looks right" can feel like knowledge while leaving retrieval and reconstruction untested. Therefore:

- Ask the probe before giving hints, summaries, or worked steps.
- Require the learner to answer without looking back at the assistant's prior derivation, source text, notes, or solution.
- Ban recognition-style probes: "does this look right?", "which answer seems correct?", "spot the familiar definition", and multiple choice unless each wrong answer is a misconception distractor that diagnoses a specific wrong model.
- Do not pass an answer because it is fluent, familiar, or close to the source wording.

## Chi et al.: Self-Explanation Probe Taxonomy

Every probe must be one of these three types and must target the load-bearing step.

1. **Justification probe:** "Why does step N follow from step N-1?"
   - Use when the risk is a hidden inference, algebraic move, causal link, or code invariant.
2. **Anticipation probe:** "Without looking, what must the next step accomplish?"
   - Use when the risk is surface following rather than knowing the proof, derivation, or algorithm's direction.
3. **Violation probe:** "If assumption A is dropped, which step fails first?"
   - Prefer for proofs, derivations, theoretical claims, algorithms with preconditions, and paper claims. It forces a model of dependency structure rather than a memorized sequence.

Never issue a generic probe such as "explain your understanding of X." Pick the dependency, then pick the probe type.

## Chi Grading Rule: Paraphrase Fails

Passing requires an inference not already present in the source text.

Fail answers that only:

- restate the relevant sentence in different words;
- summarize the proof or mechanism without adding a dependency claim;
- list steps without explaining why one step licenses the next;
- name a theorem, assumption, or property without showing how it does work.

Pass answers that add at least one checkable inference, such as:

- a reason the step is forced;
- the first failure point under a violated assumption;
- a concrete counterexample or minimal instance;
- an invariant, dependency, or causal mechanism not merely copied from the source.

## Gardner-Medwin: Optional Confidence Elicitation

When useful, ask for confidence with the answer, not after grading.

- **Confident-wrong:** toxic debt. The learner is likely to build on a false model.
- **Hesitant-wrong:** strategic debt or ordinary learning gap, depending on whether an exposure moment is imminent.
- **Confident-right:** pass only if the answer also adds a valid inference.
- **Hesitant-right:** pass, but recommend one short repayment action if the material is about to be used in an exposure moment.

Confidence is a risk classifier, not a replacement for grading.
