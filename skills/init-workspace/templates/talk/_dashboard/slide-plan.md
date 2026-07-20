# Slide Plan

One row per slide — the spec the `deck-*` builder renders. Fill this from the approved `narrative/` using `references/slide-design-principles.md`. Keep the **claim title** (not a topic label) and the **one signal** for each slide.

## Per-slide spec

| # | Claim title (one sentence) | One signal | Visual | Time | Status |
|---|---|---|---|---|---|
| 1 | | | | | todo |
| 2 | | | | | todo |
| 3 | | | | | todo |

Status: `todo` → `drafted` → `built` → `final`. Visual: chart / figure / diagram / bullets / none.

## Checks before building

- [ ] `narrative/` has an approved message + arc.
- [ ] Slide count fits the time budget (`talk-structure-patterns.md`).
- [ ] Every title is a claim, not a label.
- [ ] Each slide carries exactly one signal.
- [ ] Builder chosen for the audience (academic / proposal-report / business).

## Dataview (optional, if slides become per-note)

If you later split slides into one note each under `slides/notes/` with frontmatter `slide`, `status`, `signal`:

```dataview
TABLE WITHOUT ID slide AS "#", signal AS Signal, status AS Status
FROM "slides/notes"
SORT slide ASC
```
