# AGENTS.md — Talk: <TALK TITLE>

Orientation for any agent operating on this talk/presentation vault. This file
is the map and the rules; narrative planning and slide building live in the
installed skills this file routes to. The vault separates *what you'll say*
(narrative) from *what's on screen* (slides) so the story is decided before any
slide is built.

## What this vault is

A workspace for one talk — conference, seminar, job talk, defense, lecture, or an
executive/industrial report. It optimises for *narrative first, slides second*:
the message and arc are settled in `narrative/` before the deck is opened.

## Layout

```text
narrative/        # the talk plan: message, audience, arc, timing, what to cut
slides/           # the deck source (.tex Beamer, or .pptx)
figures/          # figures adapted FOR slides (not paper figures verbatim)
assets/           # logos, images, icons, fonts
script.md         # speaker notes — what to say per slide
references/       # slide-design-principles, talk-structure-patterns
_dashboard/       # slide-plan (per-slide spec)
```

## Routing

| Folder | Skill to use |
|---|---|
| `narrative/` | `research-talk-planner` — settle message/arc/pacing **first** |
| `_dashboard/slide-plan.md` | `deck-design-principles` (per-slide spec schema + rules) |
| `slides/` (academic talk) | `deck-beamer-academic` |
| `slides/` (proposal / progress report) | `deck-beamer-proposal-report` |
| `slides/` (executive / industrial report) | `deck-business-report` |
| `figures/` | `figure-table-planner` (adapt for projection) |

## Default actions

- **Starting a talk:** run `research-talk-planner` and write the result to
  `narrative/` — message, audience, arc, time budget, and what to cut. Do **not**
  open a deck builder yet.
- **Once the narrative is approved:** fill `_dashboard/slide-plan.md` (one row
  per slide) using `deck-design-principles`, then render with the matching
  `deck-*` builder into `slides/`.
- **Per slide:** capture what you'll *say* in `script.md`, not on the slide.

## Rules

- **Narrative before slides.** No deck building until `narrative/` holds an
  agreed message and arc. Slides render a plan; they don't invent it.
- **One signal per slide.** Each slide makes a single point; the title states the
  claim, not the topic (`deck-design-principles`).
- **Slides are not the paper.** Don't paste paper figures or paragraphs; adapt
  figures for projection (`figures/`) and put prose in `script.md`.
- **Respect the time budget.** The arc in `narrative/` sets a slide count; if the
  deck exceeds it, cut from the plan, not from the clock.
- **Pick the builder by audience**, per the routing table — academic vs
  proposal/report vs executive are different decks.

## Obsidian formatting rules

Two silent failures: the file saves fine but renders broken in Obsidian. Follow
these whenever you write a note here.

- **Frontmatter must be valid YAML and start on line 1** — nothing before the
  opening `---`, not a title or even a blank line, and no `#` heading above it.
- **Quote wikilinks in frontmatter.** A bare `related: [[other-note]]` is invalid
  YAML and makes Obsidian render the whole block as raw text. Use a quoted list
  on one line: `related: ["[[other-note]]", "[[a-summary]]"]`.
- **Never put a raw `|` in a table cell.** The pipe is the column separator, so an
  aliased wikilink `[[a-note|label]]` splits the cell and corrupts the table
  (stray `label]]` leaks into a phantom column). In a table use an unaliased link
  `[[a-note]]` or escape the pipe as `\|`. Aliased links are fine in prose — just
  never inside a table.
