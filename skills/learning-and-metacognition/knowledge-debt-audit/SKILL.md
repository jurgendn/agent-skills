---
name: knowledge-debt-audit
description: Detect when AI assistance has produced output you cannot regenerate yourself, call the loan before it compounds, and re-probe repaid debt on a spaced, variable-cue schedule. "Get the work done" is not "I understand it." Trigger when the user is about to BUILD ON an AI-produced result ("before I extend this", "am I understanding this or just getting it done", "check whether I really get this"), wants a standing audit ("what am I in debt for", "what could I not rebuild alone"), or starts a session or periodic review in a workspace with `debt-ledger.yaml`. Two modes — REACTIVE (circuit breaker at the borrow moment) and PERIODIC (statement of account plus due re-probes). Probe UNDERSTANDING of the load-bearing step, never RECALL of incidentals. Do NOT use to generate practice (concept-exercise-generator) or teach a concept fresh (professor-mentor-technical-teaching).
---

# Knowledge Debt Audit

Using AI has real advantages, but *get the work done* is not *I understand it*.
Relying on it on a load-bearing concept creates **knowledge debt** — the gap between
what your output can do and what you can do without the tool. The danger is never a
single borrow. It is that the balance compounds silently and stays invisible until
the exposure moment: a qualifying exam, a whiteboard, a reviewer's question — every
one of them a debt audit with no AI in the room.

This skill makes the balance visible while it is still cheap to pay down, and calls
the toxic loans early. It is willing to do the uncomfortable thing a chat tool
rarely does: tell you to **stop asking and go derive it yourself.**

---

# The core: strategic vs. toxic debt

Not all debt is bad, and a version of this skill that pretends otherwise is a nag
you will disable within a day. The single load-bearing distinction:

- **Strategic debt** — borrowed on the *periphery*: things you will never need to
  regenerate. A plotting call, a library's internals, a curl flag, a one-off syntax.
  Carrying this is *efficiency*, not failure. **Leave it alone.** Probing it is the
  skill's own failure mode.
- **Toxic debt** — borrowed on a *load-bearing step you are about to build on*: the
  derivation under your next paper, the theorem your calibration depends on, the
  result a reviewer will ask you to defend. **Call this loan.**

The test for which bucket: *will you need to regenerate this, unaided, in an
exposure moment?* If no → strategic, stay silent. If yes → toxic, probe now.

Because the borrows are research borrows, the exposure moments are **named and
specific** — and naming them is what makes the classifier sharp rather than naggy. A
borrow is toxic when a *concrete* research exposure will call it: a qualifying exam,
an advisor whiteboard, a reviewer's "why this normalization," a conference Q&A, a
thesis defense. "You will defend this to your advisor" is a crisp toxic signal; "you
might need this someday" is not. If you cannot name the exposure, lean strategic.

---

# When NOT to fire

- First encounters. You cannot owe debt on something you are still learning. Gate on
  *building on*, not on *meeting*.
- Implementation, writing, logistics, code. The target is understanding of theory you
  will extend — not whether you memorized a constant or an API.
- Anything peripheral (see strategic debt). If you will never need to rebuild it, the
  borrow is correct and the skill is silent.
- Recall vs. understanding: forgetting a constant is fine. Not grasping *why the
  constant is there* is the target.

---

# The trigger: the borrow moment

The debt is incurred at one specific instant — when the user takes an AI-produced
result and moves to **extend it as if it were owned capital.** That is the initial
firing point. The detectable signal: "now that we have X, let's build Y on it" where
X is load-bearing and was produced by the assistant.

After a toxic debt is repaid, the ledger schedules deliberate re-probes. These are
not random interruptions: PERIODIC mode surfaces them when due.

---

# Probe construction

Mimicry is *good* at restating. Asking someone to explain a concept back catches
nothing — it rewards the exact failure mode. Probe from the angles fluency cannot
fake, and probe the **load-bearing step only**: one sharp, generative, no-lookback
question.

Before writing the probe, read `references/metacognition-foundations.md` and use its
rate → generate → re-rate loop, no-lookback rule, three probe types, and grading rule.
Never issue a generic probe ("explain your understanding of X"). Every probe must be
one of the three taxonomy types — justification, anticipation, or violation — targeted
at the load-bearing step.

Keep the ONE-probe constraint. Do not turn the gate into an interrogation; the point
is one sharp, opportunity-cost-aware circuit breaker, not a quiz session.

Because the borrows here are almost always *research* borrows, prefer the
research-native form of each angle — it is sharper, and (see grading) it gives the
grader something checkable instead of prose to judge.

1. **Justification.** Not "what is it" but "*why* must this step follow from the
   previous one?" Understanding knows which step is structural and which is
   incidental.
2. **Anticipation.** "Without looking, what must the next step accomplish?" Mimicry
   can recite the next line; understanding can name the job that line must do.
3. **Violation.** "If this assumption is dropped, which step fails first?" Prefer
   this for proofs and derivations; it tests dependency structure, not surface
   sequence.

**Demand a checkable answer, not a fluent one — this closes the grader's own
illusion.** An LLM grades by fluency and is structurally prone to passing an answer
that *sounds* like understanding. Defend against your own grading: where the material
allows, require a worked numerical instance, a derived line, or the specific input on
which a perturbation breaks — an object the grader cannot fake-judge — rather than an
assessment of the user's prose. Research material almost always allows this; use it.

---

# Spaced re-probes and variable cues

Passing once closes the immediate loan; it does not prove durable ownership. Schedule
each repaid toxic debt through `debt-ledger.yaml`:

- stage 1: due 7 days after repayment;
- stage 2: due 30 days after passing stage 1;
- stage 3 and later: due 90 days after the previous pass.

`interval_stage` is the stage of the **next** re-probe. Stage 0 means no re-probe is
scheduled. Use ISO dates and calculate the next date from the day the user passes,
not from the old due date.

Never reuse a probe verbatim. Before writing one, inspect that entry's
`probe_history`. Choose the cue angle from the stage, cycling every four stages:

1. **transfer** — apply the dependency in a structurally different case;
2. **boundary** — identify the weakest condition or a near-boundary case;
3. **perturbation** — change one input or assumption and derive what changes first;
4. **load-bearing-why** — reconstruct why the central step is necessary.

Then instantiate the angle as one of the existing probe types: justification,
anticipation, or violation. The angle varies the retrieval cue; the taxonomy still
defines what the probe tests. Require a new concrete instance or derivation, not a
paraphrase of the previous answer.

After every attempt, append the date, stage, angle, exact prompt, and verdict to
`probe_history`.

- **Pass / understands-differently:** keep `repaid: true`, increment
  `interval_stage`, set `status: probed-passed`, and schedule its next due date.
- **Fail:** set `status: outstanding` and `repaid: false`; retain the failed stage
  and due date so PERIODIC mode keeps it visible. After successful repayment,
  set `status: probed-passed`, increment the stage, and schedule the next re-probe.
- **Strategic debt:** keep `due_date: null`, `interval_stage: 0`, and never probe it.

Do not soften a re-probe because the item was previously passed. A repeated fluent
answer without a fresh checkable inference fails.

---

# Grading discipline

- **Refuse fluent-but-empty.** "Yeah, because of the spectral properties" is a
  **fail**, not a pass. The hardest job is not waving it through because it
  pattern-matches to a correct answer. A lenient audit issues false certificates of
  understanding — the exact counterfeit it exists to catch.
- **Distinguish "doesn't understand" from "understands differently."** A non-standard
  but correct mental model **passes**. Do not punish the user for not matching your
  phrasing.

---

# The inversion

Sometimes the correct output is not a probe — it is a refusal. This skill runs inside
the very tool that is the lender, and a frictionless lender is how the balance got
large. When the debt is toxic and outstanding, the right move can be:

> Stop asking me. Close the chat, get a pen, and regenerate this step yourself.
> Come back when you can produce it cold.

A comprehension check that *always* lets the conversation continue is failing. The
generation effect is real: a step you produce yourself is retained; a step you read
is not.

---

# Modes

- **REACTIVE (spine).** The circuit breaker. Watches for the borrow moment, classifies
  the debt, and on toxic debt runs one probe — or the inversion. This is the default.
- **PERIODIC (add-on).** At session start when the workspace contains the ledger,
  read it before continuing with new load-bearing research work. Also run this check
  at the start of every requested periodic review. Surface toxic outstanding entries
  and toxic repaid entries whose `due_date` is today or earlier. Run at most one
  overdue re-probe per turn, oldest due first; keep the rest visible in the queue.
  Then use past-chat search, when available, to reconcile borrows missing from the
  ledger.

---

# Output contract

For a reactive firing:

1. **The borrow** — the specific result being built on, and that it came from the AI.
2. **Classification** — strategic (→ stay silent, done) or toxic.
3. **Probe** — the one load-bearing question, probe type chosen.
4. **Verdict** — pass / fail / understands-differently, graded honestly.
5. **Repayment** (if toxic + fail) — the concrete action: re-derive step N unaided,
   or the inversion. Route by repayment type: targeted practice →
   `concept-exercise-generator`; rebuild the result from source →
   `theory-paper-to-theorem-distiller`; re-derive with guidance →
   `professor-mentor-technical-teaching`; repay by teaching →
   `naive-student`, then return its playback here for certification.

When grading the response, put **Verdict** first. Do not bury a fail beneath
explanation or encouragement.

For a periodic audit, lead with **DUE NOW**: oldest overdue re-probe and the count
still queued. Then show the statement — toxic outstanding, toxic repaid/scheduled,
and strategic carried — newest first. If nothing is due, say so explicitly and show
the next scheduled date.

Keep it to two buckets, three probe types, one ledger. No severity scores, no ornate
rubric. The moment this skill gets elaborate it becomes the brainrot it exists to
catch.

---

# Companion files

- `debt-ledger.yaml` — the accreting account (runtime state; powers the periodic mode).
- `debt-taxonomy.md` — worked strategic-vs-toxic examples; the classifier's ground truth.
- `references/metacognition-foundations.md` — decision rules for constructing and grading the single metacognitive probe.

# References (ground via literature-triangulation — do NOT assert from memory)

- **Illusion of explanatory depth** (Rozenblit & Keil) — people feel they understand a
  mechanism until forced to explain it in detail. Why "explain it back" fails as a probe.
- **Desirable difficulties** (Bjork) — fluency is a poor signal of learning; effortful
  retrieval consolidates it. Grounds the generative, no-lookback design.
- **Generation effect** — self-produced answers are retained far better than read ones.
  Grounds the inversion.
- **Cognitive offloading / Google effect** (Sparrow et al.) — outsourcing to an external
  store lowers internal retention. The literal mechanism of knowledge debt.
- **Metacognition and uncertainty communication** — useful AI assistance must expose
  what the user knows, guesses, and cannot yet regenerate; calibrated uncertainty is
  part of repayment, not a cosmetic hedge.
- **Feynman-style learning** — explaining a concept simply is useful only when paired
  with adversarial probes for mechanisms, assumptions, and boundaries; fluent summary
  alone is not evidence of ownership.

# Hand-offs

- Want practice to repay the debt → `concept-exercise-generator`
- Want the concept taught fresh → `professor-mentor-technical-teaching`
- Want to repay by teaching an honest novice → `naive-student`
