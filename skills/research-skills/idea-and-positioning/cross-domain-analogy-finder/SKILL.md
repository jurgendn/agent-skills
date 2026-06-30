---
name: cross-domain-analogy-finder
description: Find a concept's structural twin in a distant field — to borrow a solution, or to check whether the idea already exists under another name. Use when stuck on a problem and wanting to widen the search ("has anyone solved this shape of problem", "find precedent in another field", "what field has this same structure", "I'm stuck, where else does this appear"), or when checking novelty before investing ("is my idea actually new", "has this been solved elsewhere", "am I reinventing something"). Two modes — OFFENSE borrows a portable solution from a far domain; DEFENSE checks whether your idea already exists. This is high-variance foraging: use it when genuinely stuck or vetting novelty, NOT as a daily driver. Grounds prior-art claims through literature-triangulation; hands the residual mismatch to gap-finder. Do NOT use for finding papers or precedent inside your own field or surveying an area (literature-triangulation), or stress-testing one chosen idea (research-idea-stress-test).
---

# Cross-Domain Analogy Finder

Two problems can be the same problem speaking different languages.

The job is to find a concept's **structural twin** in another field — then decide,
honestly, which of four things you are actually holding. The entire value of this
skill is the verification gate. Without it, this is an analogy fountain with good
production values.

This skill is **supposed to disappoint you most of the time.** A run that returns
three exciting transferable analogies is lying. Real structural transfer across
distant domains is rare; that rarity is what makes the hits worth anything.

---

# When NOT to use this

- As a way to *feel* productive while avoiding a hard problem. This has the texture
  of deep work while deferring the grind. Deploy it when genuinely stuck or vetting
  novelty — not as a default.
- For precedent **inside or near** your own field → `literature-triangulation`.
- To survey a research area → `literature-triangulation`.
- To vet one already-chosen idea → `research-idea-stress-test`.

If you cannot name the *problem you are stuck on* or the *idea you are vetting*,
stop and get that first. This skill needs a concrete seed.

---

# The two modes

Pick one before starting. They differ on **distance**, on **spirit**, and on what
counts as success. The postures are *not* symmetric.

| | OFFENSE (borrow a solution) | DEFENSE (check novelty) |
|---|---|---|
| Goal | import a tool from elsewhere | confirm your idea is (not) already solved |
| Where to walk | **distant** domains — distance is a *reward* | **adjacent first**, then **distance-complete** |
| Retrieval net | loose (chase any promising lead) | loose (alien vocabulary hides the twin) |
| Acceptance | structural: *"can I take something from this?"* | skeptical: *"am I caught by this?"* |
| One win is | one portable tool | one tight identity match |
| Stop when | a result transfers and passes the import test | the skeleton's instances are cleared, near AND far |

Both modes **retrieve loosely and judge structurally.** What differs is the question
the structural judge asks. Offense is expansive (one carry-able result is a win).
Defense is contractive and distrusts your own originality (one twin is a verdict).

**Offense → distant nodes.** Near neighbors already talk to each other; an analogy
you find there is probably in a textbook. The gold is far: the source domain's
people never noticed the shared structure, so the transfer is both novel and likely
to carry a genuinely different technique. Bias the walk *toward* distance.

**Defense → adjacent-first but distance-complete.** Start near (cheapest place the
twin usually lives), but **adjacency is a search order, not a stopping rule.** A
novelty claim is only valid once the *distant* instances sharing your skeleton are
also cleared. Stopping at adjacency is how you fabricate false confidence in your
own originality — and how a reviewer finds the 1987 paper you missed.

---

# Procedure

## 1. Abstract — strip the vocabulary

The hardest step, and the one that fails quietly. Reduce the concept to its skeleton:

- **objects** — what are the things?
- **operator** — what acts on them?
- **invariant** — what quantity/property is controlled?
- **dynamics** — how does it evolve / what is optimized?

Calibration: **abstract until the invariant survives but the vocabulary dies.**
- Too shallow → you search the *name* and match the name. Useless.
- Too deep → everything is "a dynamical system on a state space" and the search
  goes vacuous.

Diagnostic from the store (§5): if your skeleton already has dozens of instances
across unrelated domains, you abstracted too shallow — it has become a useless hub.
If it has exactly one, you went too deep, or it is genuinely new. The sweet spot is
a *handful* of instances from *distant* domains.

## 2. Search the abstraction, not the name

Search the skeleton's *signature*, not its label. "Spectral gap" returns spectral
gap; "the scalar governing exponential relaxation to a dominant eigenmode" returns
Kuramoto thresholds, Cheeger constants, adiabatic gaps, stat-mech relaxation time —
none of which say "spectral gap," all of which *are* it.

- OFFENSE: walk toward far domains and unfamiliar vocabulary.
- DEFENSE: enumerate the skeleton's instances near→far; the set is finite once the
  abstraction is right, which is what makes "distance-complete" achievable rather
  than "search all of science."

Use the skeleton store (§5) as a retrieval prior. **The store proposes; it never
verifies.** The moment a stored edge stands in for evidence, you launder a
surface-match as real.

## 3. Classify each hit — the four-way gate

Every candidate is exactly one of these. They **all feel identical at first glance**
("huh, that looks related"). Telling them apart is the whole job, because acting on
a surface-match as portable wastes a month, and dismissing a twin-with-a-delta as
"already exists" wastes a paper.

- **Identical** → the same problem, already solved. STOP. Read their literature,
  inherit their toolbox, their failure modes, their counterexamples. (Defense win —
  a *gift*, not a death sentence.)
- **Portable** → the solution transfers. State the precondition it smuggles in
  (a metric? a symmetry? a conservation law?) and check it holds in your setting.
  (Offense win.)
- **Twin-with-a-delta** → matches everywhere except one structural place. The
  mismatch **is** your open problem, pre-located. (The jackpot → hand to `gap-finder`.)
- **Surface-only** → resemblance with nothing carry-able. DISCARD. This is the
  bucket the gate exists to fill; most honest runs should land here.

## 4. The import-a-result test — the teeth

For every candidate that is not Surface-only, **name the specific thing that crosses
over**: a theorem, a bound, an algorithm, or a proof technique — and check it says
something nontrivial back home.

> If you cannot name the carry-able result, it is Surface-only. No exceptions.

"They're both kinda about flow" fails. An analogy is a partial functor between two
domains; keep it only if it preserves the load-bearing morphisms.

## 5. Provenance — non-negotiable for a research skill

The catastrophic failure is not a *missed* analogy. It is a *confabulated* one:
"stat-mech solved this in 1987" with a hallucinated paper that makes you abandon a
real contribution out of false humility.

- Every DEFENSE claim ("field X already solved this") needs a real, checkable source
  or it is stamped **`unverified`**.
- Treat all retrievals as *leads*, never facts, until a source is in hand.
- Ground prior-art through **`literature-triangulation`** — do not assert citations
  from memory. This skill proposes the analogy; that skill confirms the prior art.

## 6. Accrete

Append what you found to the skeleton store (§ store file): the skeleton, the
concrete instances, their carry-able results with provenance, and any delta. The
store compounds — over months it becomes a concept-graph centered on *your* research
neighborhoods. Build it emergent, never global. Do **not** try to pre-map all of
science; that is the years-long, dangerously-fun version that eats your timeline.

---

# Output contract

For each surfaced hit:

1. **Skeleton** — objects / operator / invariant / dynamics.
2. **The hit** — concept, domain, distance from source.
3. **Verdict** — Identical / Portable / Twin-with-a-delta / Surface-only.
4. **Carry-able result** — the named theorem/bound/algorithm/technique, or "none → discard."
5. **Provenance** — source, or `unverified`.
6. **Delta** (if twin) — the single structural mismatch → `gap-finder`.
7. **Precondition** (if portable) — the smuggled assumption to check.

End with an honest tally. If everything came back Surface-only, **say so plainly** —
that is a successful run, not a failed one.

---

# Companion files

- `skeleton-store.yaml` — the accreting concept↔skeleton index (retrieval prior + schema).
- `calibration-set.md` — graded worked examples; the skill's ground truth.

# Hand-offs

- Prior-art grounding → `literature-triangulation`
- The delta from a twin → `gap-finder`
- A chosen borrowed idea, to vet → `research-idea-stress-test`
