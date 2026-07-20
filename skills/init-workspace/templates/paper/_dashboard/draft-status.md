# Draft Status

Track the state of each paper section. Update the table by hand as sections move from `todo` → `drafting` → `revising` → `done`. The writer skills (`abstract-and-intro-writer`, `method-section-writer`, `results-writeup`, `related-work-writer`) produce the prose in `drafts/`.

| Section | File | Status | Owner skill | Notes |
|---|---|---|---|---|
| Abstract | `drafts/abstract.md` | todo | abstract-and-intro-writer | write last, from the spine |
| Introduction | `drafts/intro.md` | todo | abstract-and-intro-writer | must match abstract's promises |
| Related Work | `drafts/related-work.md` | todo | related-work-writer | from `related-work/` map |
| Method | `drafts/method.md` | todo | method-section-writer | consistent notation |
| Results | `drafts/results.md` | todo | results-writeup | every number → an experiment |
| Discussion | `drafts/discussion.md` | todo | — | limitations stated honestly |

## Pipeline status

Which drafts have been through the four-pass pipeline (`agents/pipeline.md`). Requires the Obsidian **Dataview** plugin; each pass records itself in the draft's frontmatter `pipeline:` key (`evidence` → `drafted` → `reviewed` → `verified`). A draft missing here never entered the pipeline.

```dataview
TABLE WITHOUT ID file.link AS Draft, pipeline AS "Last pass"
FROM "drafts"
WHERE pipeline
SORT file.name ASC
```

## Section spine check

Before drafting, confirm `ideas/` holds an agreed argument spine (`paper-argument-planner`). Each section should advance one part of that spine; if a section has no job in the spine, cut it.
