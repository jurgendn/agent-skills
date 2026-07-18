---
name: pipeline
role: Four-pass research pipeline — evidence, draft, review, verify — run inside ONE file.
---

# Research pipeline — four passes, one file

The vault's quality pipeline. The four roles (researcher, reviewer, verifier,
writer) are **passes over a single working file**, not separate agents with
separate output files.

## When to run it

Run the full pipeline only for **substantial artifacts**: a synthesis or summary
note, a paper-section draft, a proof writeup, a report — anything a reader will
rely on, roughly a page or more. Small artifacts (a reading note, a log entry, a
glossary line, a status update) skip the pipeline entirely; the vault's Operating
contract (source-grounded, mark uncertainty, report faithfully) still applies in
a single pass.

## One file, no stage files

Every pass edits the artifact's own file at its final destination path. Never
create per-stage side files (`research.md`, `draft.md`, `review.md`,
`cited.md`). The evidence table and any open review items live *inside* the
working file while the pipeline runs and are compressed or resolved by the final
pass. Net result of the pipeline: **exactly one file**.

This protocol is agent-portable: it names capabilities (search, fetch a URL,
read a file), not a specific runtime's tools. If a capability you need is
unavailable, mark the affected check `not performed` — never guess to fill the
gap.

## Pass tracking

At the end of each pass, set `pipeline:` in the working file's YAML frontmatter
to the pass just completed — `evidence`, `drafted`, `reviewed`, or `verified` —
creating the key if needed. An interrupted pipeline is then resumable by any
agent (the next pass is whatever follows the recorded value), and the vault
dashboard can query which artifacts actually reached `verified`. A file with no
`pipeline:` key never entered the pipeline.

## Integrity rules (bind every pass)

1. **Never fabricate a source.** No verifiable URL or vault note → do not
   mention it.
2. **Never describe a source you have not read.** You may note that it exists;
   you may not summarize its contents, metrics, or claims from the title alone.
3. **Write only from gathered evidence.** Missing content becomes a `TODO`,
   never plausible-looking filler; no invented tables, charts, or numbers.
4. **Preserve caveats and disagreements.** Separate claims read directly,
   claims inferred, and unresolved questions — never smooth them away.
5. **No fake certainty.** Do not write "verified"/"confirmed"/"reproduced"
   unless the pass actually performed the check and can point to it.

## Pass 1 — Evidence

Gather what the artifact will be built from: the relevant vault notes,
definitions, results, and/or external sources. Search wide with varied queries
first, then narrow using the terminology you find; prefer primary sources
(papers, official docs, primary data) over aggregators and undated blogs. Write
an `## Evidence` section at the bottom of the working file — a table with stable
IDs the later passes cite:

| # | Source | Where (URL / vault note) | Key claim | Confidence |
|---|--------|--------------------------|-----------|------------|

Close the pass with one line listing what remains unresolved or unchecked.

## Pass 2 — Draft

Write the artifact's prose above the Evidence section, using only what Evidence
supports. Structure: summary up top, sections by theme or question, open
questions at the end. No inline citations yet (pass 4 adds them). Flag gaps as
`TODO` rather than writing around them.

## Pass 3 — Review

If your runtime can spawn a fresh agent instance, hand this pass and pass 4 to
one that receives only the working file and this protocol — not the drafting
conversation. A reviewer that did not write the draft critiques it more
honestly; running all passes in one context is the acceptable fallback, not the
ideal.

Reread the whole draft as a skeptical reader: claims that outrun the evidence,
missing baselines/ablations/caveats, conflated ideas, notation drift,
conclusions stated more strongly than the support warrants. **Fix directly
whatever you can.** Anything you cannot fix now gets one callout directly under
the offending passage —

> [!warning] REVIEW FATAL|MAJOR|MINOR
> What is wrong and what would fix it.

— never a separate review document. The callout renders visibly in Obsidian's
reading view, so unresolved items jump out when skimming. Keep looking after
the first problem.

## Pass 4 — Verify

- Anchor every factual claim to an Evidence ID with an inline `[N]`; hedged or
  opinion statements need none.
- Check that each cited source supports the specific wording (meaning, not
  topic overlap); fetch URLs to confirm they resolve, else mark `unchecked`.
- Provenance-audit every number, benchmark, figure, and improvement claim back
  to a source or artifact path; remove or `TODO` whatever has none.
- Resolve remaining `REVIEW` callouts: fix the text or downgrade the claim;
  only a FATAL item may be left standing, so the reader sees it.
- Compress `## Evidence` into a final `## Sources` list (every `[N]` appears in
  Sources, every Sources entry is cited — no orphans either way).

## Done means

One file at its final path; every factual claim cited; Sources verified; no
per-stage side files; no silently dropped `REVIEW` items.
