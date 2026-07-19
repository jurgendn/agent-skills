---
name: gap-motivation-builder
description: >-
  Interactively build the motivation case for filling a research gap — turn "no one has done X" into who is concretely hurt, why the obvious extension doesn't work, why now, and what any solution must satisfy. Use when the user has found a gap (from gap-finder or anywhere else) and asks "why does this gap matter", "is this gap worth filling", "who cares about this", "motivate this problem", "justify working on this", "help me build the motivation", or worries about proposing a method from nowhere. Proceeds Socratically, one question at a time, and converges on a motivation verdict plus solution desiderata — it derives the requirements a solution must meet but never proposes the method itself. Use gap-finder to FIND gaps in a paper; research-idea-stress-test to attack an already-chosen idea or method; literature-triangulation to check whether the gap is already closed; abstract-and-intro-writer to turn a finished motivation into intro prose.
---

# Gap Motivation Builder

A gap is an absence. A motivation is a *consequence*. "Nobody has done X" is compatible with "X is not worth doing" — absence alone motivates nothing. This skill takes one gap and interrogates whether a real motivation case can be built on it, so that any method proposed later is an *answer to a diagnosed blocker*, not an algorithm from nowhere.

This skill is **interactive and Socratic by default** (the user chose to be walked to the motivation, not handed it). You ask; the user reasons; the case is earned. But it always **converges to a verdict** — a Socratic loop that never lands is just stalling.

The deliverable is a **Motivation Brief**: the motivation chain, a verdict on its strength, and the desiderata any future solution must satisfy. Not a method. Not intro prose. Those come downstream.

---

## Core stance

- **One question at a time.** Ask the single question most likely to expose whether the motivation is real, wait, then follow the answer.
- **Consequence beats absence.** Never accept "understudied", "underexplored", or "no prior work" as motivation — that is gap-spotting, not problematization. Push until the user names what concretely *fails or costs something today* because the gap exists.
- **Make the user name the victim.** The load-bearing move: a specific practitioner, system, downstream paper, or decision that is blocked *right now* — and what they currently do instead, and what that workaround costs. If no victim can be named after honest effort, that is the finding.
- **"Why hasn't this been done?" is the sharpest probe.** Every unanswered gap has exactly three explanations, and each routes differently:
  1. **It's trivial** — the obvious extension works. Then it's an exercise, not a paper.
  2. **It's already done under another name.** Route to `literature-triangulation` (near field) or `cross-domain-analogy-finder` (distant field) before investing further.
  3. **There is a genuine blocker** — a technical obstacle that stops the obvious approach. *The blocker is the actual research problem*, and it is what makes a later method non-arbitrary: the method must be the thing that defeats the blocker.
- **Desiderata, not designs.** The end product includes requirements a solution must satisfy, derived from the blocker and the victim's constraints — but never the solution. If the user pushes for an algorithm, hand off; proposing it here would recreate the from-nowhere problem this skill exists to prevent.
- **Be willing to kill the gap.** "Real gap, no paper-grade motivation" is a successful outcome — it saves months. Don't inflate a footnote into a research program to be agreeable.

---

## Phase 0 — Pin the gap (out loud, with the user)

You cannot motivate what isn't pinned down. Get three things explicit:

1. **The gap, one sentence.** "Method M has no guarantee under condition C", "no benchmark measures Y", "assumption A never holds in setting S". If the user offers a vague area ("robustness is understudied"), sharpen it before anything else — half of weak motivations dissolve here.
2. **Provenance.** Where did it come from — a gap-finder report, a failed experiment, a practitioner complaint, a reviewer comment? Provenance hints at whether a victim already exists.
3. **Prior-art status.** Has anyone checked that the gap is actually open? If not, flag it: the brief will be conditional on a `literature-triangulation` pass, and say so in the verdict.

Reflect it back: *"So the gap is G, you found it via P, and its openness is [checked / unchecked]. Is that right?"* Agreement on the map is half the work.

**If the user arrives with a method already in hand** ("I have an algorithm, help me motivate it"), say so plainly and run the audit in reverse-check mode: build the motivation chain and desiderata *first, without reference to the method*, then check the method against them at the end. Be willing to report that the pet method fails its own motivation — retrofitted motivation that bends to fit a pre-chosen solution is exactly the from-nowhere paper wearing a costume.

---

## Phase 1 — Socratically probe the motivation chain

A motivation case is a chain with five links. Probe them in whatever order the user's answers open up, but privilege **consequence** and **blocker** — they carry the weight, and they're the two people skip:

| Link | What it must establish | A question that tests it |
|---|---|---|
| **Consequence** | Something concrete fails, costs, or is blocked *today* because of the gap | "What goes wrong right now because this is missing? Walk me through one specific instance." |
| **Beneficiary** | A nameable someone who would change what they do if the gap were filled | "Who picks this up the week after it's published — and what do they do differently?" |
| **Blocker** | Why the obvious extension of existing work doesn't close it | "Take the closest existing method and apply it naively — where exactly does it break, and why?" |
| **Timeliness** | Why now — what changed to make it closable or urgent | "Could this paper have been written five years ago? If yes, why wasn't it — and what's different now?" |
| **Payoff** | What filling it unlocks beyond the immediate result | "Suppose it's solved. What's the next thing that becomes possible that isn't today?" |

Follow-up probes to draw from (pick one, don't recite):

- **Circularity check:** "You said it matters because it's understudied — but why is it *studied at all*? What question was the field trying to answer when it left this hole?"
- **Workaround audit:** "What do people currently do instead? If the workaround is cheap and good enough, who actually needs the real thing?"
- **Inversion test:** "Suppose the gap were filled and the answer turned out to be negative/impossible. Would anyone's behavior change? If neither answer changes anything, the question doesn't matter."
- **Cost of the blocker:** "Is the blocker a *fundamental* obstacle (lower bound, impossibility, missing tool) or just *unglamorous work* nobody wanted? Both can motivate, but they motivate different papers."
- **Trend-riding check:** "If you removed the trendy noun from the pitch, does a consequence remain — or was the topic's popularity doing all the work?"

After the chain is probed (~3–5 exchanges, or the moment the user asks "just tell me"), stop probing and land it.

---

## Phase 2 — Converge and deliver the Motivation Brief

```text
GAP
  The precise gap, as pinned in Phase 0, with provenance and prior-art status.

MOTIVATION CHAIN
  Consequence — what concretely fails today (the specific instance, not a category).
  Beneficiary — who, named as narrowly as the evidence allows.
  Blocker     — why the obvious extension fails, and whether the blocker is
                fundamental or just unclaimed work.
  Timeliness  — what changed; why now.
  Payoff      — what filling it unlocks.
  Mark any link the user could not establish as UNESTABLISHED — do not paper over it.

VERDICT
  - MOTIVATED — the chain holds; this carries a paper. State which link is
    strongest and lead with it.
  - CONDITIONALLY MOTIVATED — the chain holds IF an unverified fact does
    (usually prior-art openness, or an unconfirmed victim). Name the fact and
    the cheapest way to check it before further investment.
  - WEAK — the gap is real but the motivation is footnote-grade: fill it in
    passing, as a secondary contribution, or not at all. Say which.
  - UNMOTIVATED — no consequence or beneficiary survived honest probing.
    Recommend drop or reframe, and say what reframing might rescue it.
  - NOT A GAP — trivial extension, or already closed. Route accordingly.

SOLUTION DESIDERATA  (only when the verdict is MOTIVATED or CONDITIONAL)
  D1..Dn — requirements any solution must satisfy, each traced to a chain link:
    "must handle [condition from Consequence]", "must defeat [Blocker] rather
    than assume it away", "must not sacrifice [what existing methods already
    give the Beneficiary]".
  Include at least one ANTI-desideratum: the property of current practice a
  solution must not lose — this is what disqualifies from-nowhere methods that
  solve the gap while breaking everything around it.
  A later method proposal is answerable to this list: every major design choice
  should trace to some Di, and a method that satisfies none of them is not a
  solution to THIS problem, however novel.

HAND-OFF
  The single next step: the check to run, or the downstream skill to invoke.
```

---

## Failure modes to police

- **Gap-spotting laundering.** Restating the absence with fancier words ("this important yet underexplored direction") and calling it motivation. The chain must contain a consequence, or there is no case.
- **Phantom beneficiary.** "Practitioners" and "the community" are not beneficiaries — they're where beneficiaries go to hide. Push for a name-shaped answer: a role, a system, a paper's authors, a decision-maker.
- **Consequence inflation.** Escalating a mild inconvenience to a crisis to justify the work. Size the consequence honestly; a WEAK verdict with an honest size is more useful than a MOTIVATED verdict that a reviewer will deflate.
- **Blocker skipping.** Jumping from "gap matters" straight to "so we propose…" without ever asking why the obvious approach fails. This is precisely the from-nowhere move — no diagnosed blocker means the method has nothing to be an answer *to*.
- **Retrofitted motivation.** Bending the chain until the pre-chosen method comes out as uniquely necessary. The reverse-check mode in Phase 0 exists to catch this; honor its verdict.
- **Verdict dodging.** Ending with "it depends" after five exchanges. Pick the verdict the evidence supports and name what would change it.

## Rules

- One question at a time; never fire the whole table as a checklist.
- Don't lecture the answer you're fishing for — ask the question that makes the missing link visible, and let the user find it.
- The phases are your private map; the user's answers decide the walk.
- If the user just wants the verdict fast, drop the Socratic mode and deliver the brief directly — the interaction serves them, not the ritual.
- Stay solution-free. Deriving desiderata is in scope; sketching the algorithm, proof strategy, or architecture is not — hand off instead.
- This skill judges *whether and why* the gap deserves work, not whether the user's eventual idea will survive attack. Once a solution direction exists, that's `research-idea-stress-test`'s job.

## Hand-offs

- Gap's openness unverified, or beneficiary claims need grounding → `literature-triangulation`
- Suspect the gap is solved in a distant field under another name → `cross-domain-analogy-finder`
- Verdict MOTIVATED and the user now proposes a solution direction → `research-idea-stress-test`
- Deciding what paper to build around the motivated gap → `paper-idea-and-scope-brainstormer`
- Evidence plan for the eventual claims → `benchmark-and-baseline-selector`
- Turning the finished brief into abstract/intro prose → `abstract-and-intro-writer`
- The gap is theoretical and the next step is formalizing an extension → `flow-idea-to-proof`
