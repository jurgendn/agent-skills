---
name: gre-vocabulary-builder
description: Build, drill, and retain GRE-level vocabulary the way the test actually uses it — meaning clusters, charge (positive/negative), secondary meanings of common words, and recall drills embedded in Text Completion / Sentence Equivalence contexts. Use this skill whenever the user wants to learn GRE words ("GRE word list", "help me memorize vocab", "quiz me on these words", "what does 'protean' mean and how is it tested"), keeps forgetting words, wants a spaced review routine, or wants practice sentences for new words. Also use when TC/SE practice reveals vocabulary gaps. For solving actual TC/SE questions use gre-verbal-reasoning; for IELTS topic vocabulary use ielts-vocabulary-builder.
---

# GRE Vocabulary Builder

The GRE tests vocabulary in one narrow way: can you judge whether a word fits a determinate slot in an academic sentence. That means recognition + nuance discrimination, not production, spelling, or definition recital. Everything here optimizes for that use: words are learned in sentence context, in meaning clusters, with charge attached — because that is exactly the information TC/SE questions interrogate.

## Use this when

- The user wants to learn new GRE words or work through a word list.
- The user keeps forgetting specific words and wants a retention routine.
- The user met unknown words in TC/SE practice (handed over from `gre-verbal-reasoning`).
- The user wants drills: quizzes, cloze sentences, charge-sorting, cluster discrimination.

## Do not use this when

- The user is solving TC/SE questions — use `gre-verbal-reasoning` (it routes vocabulary gaps back here).
- The user needs IELTS topic vocabulary or academic collocations for essays — use `ielts-vocabulary-builder`.

---

## What GRE vocabulary actually is

1. **High-frequency test words** — the recycled core (~800–1200 words) of academic/literary vocabulary: *laconic, prosaic, equivocate, venerate, intransigent…* Frequency-ranked lists exist in every major prep resource; working through a high-frequency deck is genuinely worth it, unlike memorizing a 3,500-word dictionary.
2. **Secondary meanings of ordinary words** — the highest-value, most-neglected category. The GRE loves the meaning you don't know of a word you do: *qualify* (= limit), *check* (= restrain), *flag* (= weaken), *appropriate* (v., = seize), *wanting* (= deficient), *economy* (= efficiency of expression), *arrest* (= stop), *telling* (= revealing). When one appears anywhere in practice, capture it explicitly — the familiar spelling actively blocks relearning.
3. **Charge and register** — many TC/SE eliminations run on polarity alone (is this word approving or critical?). Every word entry must carry its charge.

## The word entry format

Never record a bare word–definition pair; record what the test will ask about:

```
**equivocate** (v.) — to use deliberately ambiguous language to avoid committing
charge: negative (evasive)
cluster: hedge, prevaricate, temporize | ≠ lie outright (that's mendacity)
GRE-style: Pressed for a timeline, the minister ___ed, offering answers
          notable chiefly for their strategic vagueness.
hook: equi-voc — "equal voices," saying two things at once
```

The **cluster line** does discrimination work: GRE answer choices routinely put near-neighbors side by side, so learn *hedge vs. prevaricate vs. equivocate* together, with the distinguishing edge stated. The **hook** (root, image, or mnemonic — whatever sticks) is memory aid, not etymology lesson; roots (*ben-, mal-, -loq-, -phil-, e-/ex-*) are recognition boosters for unseen words, not a primary learning method.

## Learning protocol

- **Batch size**: 10–20 new words per session, always introduced *in sentences first* — give the GRE-style sentence, let the user infer, then confirm. Inference-then-confirmation encodes far better than definition-first.
- **Cluster by meaning, not alphabet**: teach *frugal / parsimonious / penurious / thrifty* (and their charge differences) as one unit; alphabetical lists scatter the discriminations the test asks for.
- **Spaced retrieval**: re-probe new words at roughly 1 day → 3 days → 1 week → 3 weeks, retiring words after two clean, spaced hits in *different* cue formats. Always test retrieval (blank first), never recognition-by-rereading.
- **Leeches** (words failed 3+ times): stop repeating the same card. Change the encoding — new hook, new cluster contrast, or a self-written sentence about the user's own research/life. Repetition of a failing encoding just rehearses the failure.

## Drill formats (rotate; vary the cue)

1. **Cloze (primary)** — a GRE-register sentence with a blank, 4–6 choices drawn from the user's own studied words including near-neighbors from the same cluster. This is the closest proxy to the real task.
2. **Charge sort** — 10 words, sort into positive/negative/neutral in 60 seconds. Fast, high-yield.
3. **Cluster discrimination** — two near-synonyms, one sentence where only one fits; the user must say *why* the other fails.
4. **Odd one out** — 4 words, 3 share a cluster.
5. **Reverse cloze** — the user writes a sentence in which the target word is forced (a road-sign structure that only that meaning satisfies). Production is not tested on the GRE, but it is the strongest encoding drill.

Vary cue format across re-probes of the same word — a word only ever tested by the same cloze sentence has memorized the sentence, not the word.

## Session ledger

Track per word: date introduced, probe history (format + result), status (learning / review / retired / leech). If the user has a practice vault, keep this as a `vocab-ledger` file there and open sessions by pulling due re-probes *before* introducing new words — due reviews outrank new material.

## Workflow

- **New-words session**: pull due re-probes → introduce the new batch in sentence context → immediate mixed drill (formats 1–2) covering new + due words → update ledger → end with the 3 shakiest words named.
- **"Quiz me"**: mixed drill from the ledger (or a user-supplied list), weighted toward due and leech words; report accuracy by cluster and any word due for encoding change.
- **Word lookup** ("what does X mean"): give the full entry format above — including how the GRE tends to use it — not a dictionary line. Offer to add it to the ledger.
- **Handoffs from TC/SE practice**: words arriving from `gre-verbal-reasoning` error logs enter as high-priority; they have proven test relevance for this user.
