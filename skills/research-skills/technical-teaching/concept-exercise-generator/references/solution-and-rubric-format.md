# Solution & Rubric Format

Solutions live in their own file (`solutions.md`), never interleaved with the problems. The split is the whole point: the learner must commit to an answer before checking. A solution that is just "the answer" is useless for self-verification — each one carries a rubric so the learner can grade a *near-miss* honestly, and a revisit pointer so a miss turns into targeted re-study instead of passive reading.

## Required fields per solution

For every problem, mirror the exercise number and tag, then provide:

1. **Answer** — the correct result, stated plainly.
2. **Why** — the reasoning/working that produces it. For Tier 2+ show the steps; the learner checks their *process*, not just the final value.
3. **✅ You've got it if** — the rubric for a pass. Describe what a correct understanding looks like, including acceptable alternative phrasings/approaches.
4. **⚠️ Common wrong turn** — the specific mistake learners make here. This lets someone who got it "almost right" recognize their error instead of rationalizing it as correct.
5. **↩ Revisit if missed** — name the exact concept, section, toy case, or learning-flow stage to restudy. Not "review the material" — point at the thing.

## Template

```text
# Solutions — <topic>

1. [Tier 1 · <concept>]
   Answer: <plain answer>
   Why: <one or two lines>
   ✅ You've got it if: <pass rubric>
   ⚠️ Common wrong turn: <the typical error>
   ↩ Revisit if missed: <specific thing to restudy>

2. [Tier 3 · <concept>]
   Answer: <plain answer>
   Why:
     - <step / reason 1>
     - <step / reason 2>
   ✅ You've got it if: <names the trade-off / mechanism, not just the verdict>
   ⚠️ Common wrong turn: <e.g., "describing what happens without saying why">
   ↩ Revisit if missed: <concept + where it was taught>
```

## Scoring guidance to include for the learner

- **Tier 1–2:** pass = correct answer by the correct procedure. A right answer reached by a wrong method is a miss — flag it.
- **Tier 3:** pass = the *reasoning* matches the rubric, even if phrased differently. "Right verdict, hand-wavy why" = miss.
- **Tier 4:** pass = a correct, self-generated construction/derivation/critique. Partial credit doesn't clear the gate; note it and restudy.

## The gate rule

Understanding is verified only when **Tier 3+ problems pass unaided**. State this explicitly in `solutions.md`. Clearing Tiers 1–2 while missing Tier 3+ means the learner can recite and run the method but not yet reason about it — the orchestrator should route back to teaching, not forward.
