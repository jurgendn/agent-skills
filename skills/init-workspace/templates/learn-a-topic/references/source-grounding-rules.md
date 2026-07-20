# Source-grounding rules (reference)

The discipline that keeps this vault trustworthy: every non-trivial claim is traceable to a source. This is what separates a learning vault from a pile of half-remembered assertions.

## Rules

1. **Every claim in `summaries/` or `map/` links to a `sources/` note.** Use `[[sources/src-001-...|Vaswani et al.]]` inline. No link → it's an open question, not a fact. **Inside a table cell, drop the `|alias`** and write the bare `[[sources/src-001-...]]` (or escape the pipe as `\|`) — an unescaped `|` is read as a column separator and corrupts the table.
2. **Quote or locate.** When a claim is precise (a number, a bound, a definition), note *where* in the source it lives, so it can be checked.
3. **Separate source from interpretation.** In a reading note, keep "what the source says" distinct from "what I think it means". Don't let your gloss become a remembered fact.
4. **Flag unsourced beliefs.** If you believe something but can't cite it, put it in `open-questions.md` with "find a source" — don't promote it to a summary.
5. **Watch citation telephone.** If source A cites B for a claim, prefer reading B before repeating it; second-hand claims drift. (`citation-auditor` formalises this if the vault becomes a survey.)
6. **Record confidence.** Low-confidence understanding of a source is fine, but mark it (`confidence: low`) so summaries built on it stay provisional.

## Why it matters

- It makes the vault **reusable** — a grounded summary can become a Related Work section (`related-work-writer`) without re-checking everything.
- It surfaces **what you don't know** precisely, which is where learning happens.
- It prevents the most common failure: confidently repeating something you never actually verified.
