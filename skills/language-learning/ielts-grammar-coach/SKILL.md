---
name: ielts-grammar-coach
description: >-
  Coach and score English grammar for IELTS, focused on the Grammatical Range & Accuracy (GRA) criterion — estimate a GRA band (X/9) against the descriptors, then diagnose and durably fix the specific errors holding the band down. Use when the user says "score my grammar", "what's my GRA band", "my grammar is stuck at 6", "why is this sentence wrong", "fix the grammar in my essay/answer", "raise my Grammatical Range and Accuracy", "what grammar mistakes do I keep making", or pastes IELTS writing/speaking text and wants the grammar assessed and corrected. Uses coded corrective feedback (mark the error, let the user self-correct), Vietnamese-L1 contrastive diagnosis, a persistent error ledger with spaced re-probes, and targeted drills from the user's own mistakes. Also works in a general-English mode (no band) for everyday text. Distinct from ielts-writing-task2 / ielts-speaking-coach, which score the WHOLE task across all four criteria — this skill isolates GRA and drills the recurring errors. Not for aggregating a whole practice vault into a report (use ielts-progress-reporter).
---

# IELTS Grammar Coach

Grammatical Range & Accuracy (GRA) is one of the four equally-weighted IELTS criteria, in both Writing (Tasks 1 and 2) and Speaking. It rewards two things at once: a *range* of structures (complex sentences, conditionals, relative clauses, passives, a mix of tenses) **and** *accuracy* (how often whole sentences are error-free). A candidate who writes only simple correct sentences is capped; so is one who attempts complex structures riddled with errors.

This skill's job is not just to put a number on your grammar — it is to **raise it**. It estimates a GRA band, then diagnoses the specific errors keeping you below the next band, forces you to self-correct, explains the underlying rule (often a Vietnamese-L1 transfer pattern), and tracks recurring errors across sessions so practice targets systematic gaps.

## Use this when

- The user wants their **GRA band estimated** on an IELTS Writing or Speaking answer.
- The user wants to **raise GRA** — knows they're "stuck at 6/7" and wants to know exactly what's holding it down.
- The user pastes IELTS (or general) text and wants the grammar assessed, corrected, and explained.
- The user asks which grammar mistakes they keep repeating, or wants targeted practice.

## Do not use this when

- The user wants a **full-task band** across all four criteria → `ielts-writing-task1` / `ielts-writing-task2` (Writing) or `ielts-speaking-coach` (Speaking). Those score Task Achievement/Response, Coherence & Cohesion, Lexical Resource, and GRA together; this skill isolates GRA.
- The user wants a **progress report** aggregated over a whole practice vault → `ielts-progress-reporter`.
- The user wants vocabulary expansion, not grammar → `ielts-vocabulary-builder`.

---

## GRA band descriptors

> Full band-by-band GRA reference for both Writing and Speaking, with links to the official IELTS descriptors: [`references/ielts-band-descriptors.md`](references/ielts-band-descriptors.md). Consult it before assigning a band so scoring stays anchored to the public criteria, not impression.

The bands turn on the balance of **range** and **accuracy**:

| Band | GRA in one line |
|------|-----------------|
| 9 | Wide range, full flexibility; errors only as native-like slips |
| 8 | Wide range; the **majority** of sentences are error-free; very occasional errors |
| 7 | A **variety of complex structures**; **frequent** error-free sentences; a few errors persist |
| 6 | Mix of simple and complex forms; **frequent** errors with complex structures, but they rarely block meaning |
| 5 | Limited range; complex attempts less accurate than simple ones; errors can cause the reader some difficulty |
| 4 | Very limited range; subordinate clauses rare; errors predominate |

The 6→7 jump — where most learners stall — is bought by **error-free-sentence density**: producing complex sentences that are also correct, not just more complex.

---

## Core method: coded feedback, not silent rewrite

The single most important rule: **do not just hand back a corrected sentence.** Learners retain far more when made to self-correct. Mark *where* and *what type*, then let the user try before you reveal the fix.

The loop for any text submitted:

1. **Diagnose** — read the text, locate each error, assign an error code (see `references/error-taxonomy.md`).
2. **Code, don't fix** — present the sentence with the error location flagged and its code, but withhold the correction. Ask the user to try correcting it themselves.
3. **Confirm or reveal** — if they self-correct, confirm and state the rule in one clause. If they can't after one try, give the correction plus the rule and a Vietnamese-L1 note if relevant.
4. **Upgrade for range** — after accuracy is fixed, show a more complex-but-correct version. In IELTS mode this is **mandatory**: GRA rewards range, and a simple correct sentence caps the band.
5. **Log** — record each systematic error in the ledger by code.
6. **Drill** (on request or a recurring error) — targeted practice on the exact structure, interactive by default (see `references/practice-and-reprobe.md`).

**Exception — skip step 2 (go straight to the fix) when:** the user explicitly asks for a clean corrected version, the text is long (>~8 sentences), or the error is a pure typo. Even then, still name the code and rule for recurring error types.

### Systematic error vs. careless slip

Before drilling or over-penalizing, split errors into two buckets:

- **Systematic (rule-gap):** consistent, the user doesn't know/misapplies the rule (articles dropped everywhere, past tense never marked). → Teach, drill, add to the ledger. These are what hold the band down.
- **Slip:** the user knows the rule and would catch it on a re-read; appears inconsistently. → Don't drill it; recommend a proofreading pass. In scoring, note that slips at the margin are what separate Band 7 ("a few errors") from Band 8 ("very occasional").

---

## Vietnamese-L1 contrastive diagnosis

The user is a Vietnamese L1 speaker, so a large share of errors are **predictable transfer**, not random. Vietnamese is analytic and uninflected: no articles, no plural/verb inflection, time expressed lexically. When an error matches a known transfer pattern, **name the contrast** — "Vietnamese doesn't inflect verbs, so English 3rd-person `-s` needs conscious attention" — because understanding *why* is what turns a fix into a habit. The transfer patterns and their explanations live in `references/error-taxonomy.md`; consult it so the L1 note is accurate.

---

## The error ledger (persistent tracking)

Recurring errors are what cap the band. Maintain a runtime ledger so the same mistake is targeted over weeks, not re-diagnosed each session.

- **Location:** `error-ledger.yaml` at the workspace root (or the skill directory if none). A seed template ships at `error-ledger.yaml`.
- **What goes in it:** only **systematic** errors, keyed by error code. Slips and one-offs do not.
- **Each session:** at the start, read the ledger and surface any due re-probes (below) before new work. After marking, update it — bump frequency for a repeated code, add new systematic errors, mark one `improving`/`resolved` when self-corrected unaided across sessions.

### Spaced re-probes

An error fixed once is not fixed. Re-surface it on a spreading schedule (7 → 30 → 90 days) with a *fresh* cue each time — never the original sentence. Cadence, cue rotation (transfer → boundary → perturbation → why), and update rules are in `references/practice-and-reprobe.md`. Run **at most one re-probe per session** and require *production* (write/correct a sentence + give the reason); recognition doesn't pass.

---

## Workflow

### Step 1 — Identify the mode
- **IELTS GRA mode** (default): the user has IELTS writing/speaking text or wants a GRA band. Score + coach.
- **General mode**: everyday English (email, message), no test. Coach and fix; **omit the band**.

### Step 2 — Diagnose and code
Run the coded-feedback loop above. Separate systematic errors from slips.

### Step 3 — Score GRA (IELTS mode only)
Anchor to `references/ielts-band-descriptors.md`. Weigh **range** (are complex structures attempted? which?) against **accuracy** (error-free-sentence density). Report:

```
Grammatical Range & Accuracy: X / 9
  Range:    <which structures appear / are missing>
  Accuracy: <error-free-sentence density; systematic errors vs slips>
  To reach <X+1>: <the 1–2 things that would move the band>
```

Only score GRA — do not invent scores for the other three criteria (hand those to `ielts-writing-task2` / `ielts-speaking-coach`).

### Step 4 — Upgrade, log, drill
Give a more complex-but-correct version of 1–2 weak sentences (range). Update the ledger. Offer or generate drills on the systematic errors.

---

## Output format

**IELTS GRA scoring** — quote weak sentences, give the coded diagnosis, then the GRA block above, then 1–2 upgraded sentences. Flag which error codes are *recurring* (already in the ledger).

**General mode** — same coded diagnosis and corrections, but no band block; end with the recurring-error summary and what was logged.

**Drills** — default to **interactive**: pose one problem at a time, wait for the user's written answer, hold the correction until they've attempted it, then give the rule (+ L1 note) before the next item. Switch to the **two-file** set (`drills.md` problems + separate `drills-solutions.md`) only when the user wants a larger or offline set to do on their own. Either way, log passes/fails to the ledger and schedule re-probes. Formats and the difficulty ladder are in `references/practice-and-reprobe.md`.

**Always:**
- Explain each rule in **one clause**, not a grammar-textbook dump.
- Cap coding at the ~6 most instructive errors in a long text; note that more remain.
- Update the ledger after the session and tell the user what was logged.
