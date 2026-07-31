---
name: note-method
role: Everyday note protocol — capture, expand, store, query — for notes below the pipeline's size gate.
---

# Note method — capture → expand → store → query

The counterpart to `pipeline.md`. The pipeline governs **substantial artifacts** a reader will rely on; this file governs everything below that gate — reading notes, captures, log entries, definitions, meeting notes. Those are the majority of the vault, and "skip the pipeline" does not mean "no method."

Like the pipeline, this protocol names capabilities rather than a runtime's tools, so it is agent-portable.

## What the evidence actually supports

Encode these at the strength the sources carry, not stronger. Each claim below is flagged **supported**, **efficiency-only**, or **contested**; do not silently promote one.

- **Structure beats medium — supported.** In a randomized trial (Yıldırım 2026, *Frontiers in Psychology* 16:1697151, n=134, five weeks), structured formats (Cornell, Parallel) scored higher than unstructured linear notes, and only Cornell-vs-linear survived correction. Meta-analytic work agrees that what you do with the notes dominates the recording medium (Voyer et al. 2022, *Contemporary Educational Psychology*; Flanigan et al. 2024, *Educational Psychology Review*). **Read this as an overall achievement difference, not a retention mechanism:** the same trial found the time×group interaction non-significant (F(3,129) = 1.82, p = 0.146), so no method decayed more slowly than another. A structured note is better from the moment it is written; it does not decay less.
- **Reviewing the notes is what earns the advantage — supported.** Flanigan et al.'s meta-analysis (24 studies) found handwriting's achievement advantage small (Hedges' g = 0.248) *and conditional on students reviewing their notes over time*; without review it vanishes, even though typing produces more volume (g = 0.919). More notes are not better notes. This is the single best-supported reason the expand pass below ends in **your** review rather than at the model's output.
- **Motivation predicted retention; cognitive load did not — supported.** In the same trial, motivation was the strongest predictor across all four methods (β = 0.50–0.60, p < 0.01) while cognitive load showed no significant association with retention. A method the user will actually keep using beats a theoretically superior one they abandon. When a rule here would make the vault tedious, that is a cost against retention, not a neutral tradeoff.
- **The "digital feels easy, so it must be shallow" story is contested.** It is an interpretation the source study's own regression contradicts. Do not use it to justify adding friction. The defensible version is narrower: *verbatim transcription* is the failure mode, whatever the medium.
- **LLM expansion buys effort, not proven learning — efficiency-only.** Micronote capture with LLM expansion cut text written by ~47% and completion time by ~44% at 93% factual correctness (NoTeeline, IUI 2025), but n=12 and **retention was never measured**. Whether automated expansion preserves the encoding benefit of writing it yourself is an open question. Treat expansion as a time saver whose learning cost is unmeasured — which is exactly why the review step below is not optional.

## The loop

### 1. Capture — fast, rough, yours

Write fragments, abbreviations, and keywords while reading, listening, or thinking. Do not write full sentences and do not format. Speed and honesty matter more than completeness; a capture that never got written is worth nothing.

### 2. Expand — after the session, never during

Turn the fragments into full notes: complete sentences, key terms defined, a summary, and questions the note raises. An agent may do this pass, but under two conditions:

- **Expansion is grounded in the capture plus a source actually read** — the same integrity rules as the pipeline apply (never fabricate a source, never describe an unread one, gaps become `TODO` not filler).
- **The user reviews and edits the result.** This is the step that substitutes for the traditional rewrite-your-notes pass, and it is the only part of the loop with a plausible claim on learning. An unreviewed expansion is a transcript, not a note.

A note is not done growing after its first pass. When you come back later — a new session's fragments, a new handwritten page, a line typed straight into the note — that is a new increment on the same note, not a new note and not a sync problem between two copies: the vault file is the only copy there ever was. Expand only the new increment. Never regenerate the whole expansion, since the earlier prose already carries your edits and a full re-expansion would silently overwrite them.

### 3. Store — structured so it can be found

Write the reviewed note to its destination with the frontmatter and headers its template specifies (see *Retrieval contract*).

### 4. Query — to locate, then re-derive

Ask questions across the vault instead of scanning it. **An LLM's answer is a candidate, not your recall.** Retrieval practice is well-supported when *the human* retrieves; delegating the retrieval delegates the benefit too. So use a query to find what to re-derive, then close it and reconstruct the idea yourself. If you cannot, that is the gap to study — route it to `knowledge-debt-audit` rather than reading the answer again.

## Preserve the raw capture

**Never delete the original messy version.** Keep it under a `## Raw capture` heading in the same note (this vault does not create per-stage side files — the same one-file rule the pipeline follows).

It earns its space three ways: expansions are better when the model sees both the fragment and the cleaned text; it is the fallback when an expansion turns out to be wrong or hallucinated; and it preserves what *you* actually thought, which the cleaned prose quietly overwrites.

**If the note later grows past the size gate** and enters `pipeline.md`, `## Raw capture` stays where it is. It is not evidence, so pass 1 does not fold it into the `## Evidence` table, and pass 4 does not compress it away with that table — a raw capture is what *you* observed or thought, which is exactly what the final file should still be able to show. It is the one section exempt from needing a citation.

Mark provenance whenever the two are mixed: what you wrote, and what was expanded or supplied for you. A note that reads as yours but was largely generated is a debt, not understanding — the same distinction `knowledge-debt-audit` tracks, and the same one the learn-flows' discussion mode records with `[USER]`/`[PEER]`/`[MENTOR]` tags.

When a note grows across more than one sitting, append each new increment under its own dated sub-heading inside `## Raw capture` (e.g. `### 2026-07-31`) rather than editing or merging into what is already there. This keeps every past increment intact for the next expansion pass to check against, and keeps "what did I actually write, and when" answerable by reading the section rather than by memory.

## Retrieval contract

The vault is queried by machine, so a few conventions are load-bearing rather than cosmetic:

- **Frontmatter is metadata, not decoration.** Valid YAML from line 1. Whatever fields the template defines (`title`, `tags`, `source`, `date`, `status`, `confidence`) are what filtering runs on — an omitted `confidence` makes a note invisible to a "what am I unsure about" query. For a note that grows across sittings, add `updated` alongside the template's birth-date field (`date` or `created`): the birth date is when the note was born, `updated` is its most recent increment, and only the second stays true once the note has been added to more than once.
- **Section headers are stable because retrieval chunks on them.** Renaming `## Summary` to `## Overview` in one note silently breaks every query that targets it. Follow the template's headers; add new ones rather than renaming existing ones.
- **Links are the graph.** `[[wikilinks]]` let a query about one concept surface neighbours that never mention it by name. Link when you write, not in a later cleanup pass that will not happen.

## Sensitivity gate

Before sending note content to a remote model, check what is in it. Public material (published papers, public talks) is unrestricted. Unpublished research ideas, personal reflection, third-party confidential material, or anything under an agreement is not: expand it locally or by hand. If you are unsure, do not send it — the check is cheap and irreversible in only one direction.

## Done means

One file at its destination; the raw capture preserved inside it; the expansion reviewed by the user rather than accepted as written; frontmatter valid and headers matching the template; anything uncertain marked rather than smoothed away. A later increment meets the same bar for that increment: its capture dated and preserved, its expansion reviewed, `updated` bumped — and the previously reviewed prose left intact.
