# Targeted Drills + Spaced Re-probes

Two mechanisms that turn a one-time correction into a durable fix: **drills** built
from the user's own errors, and **spaced re-probes** that resurface an old error
before it's forgotten. Both operate on error codes from `error-taxonomy.md` and on
the `error-ledger.yaml` runtime state.

---

## Part 1 — Targeted drills

Generate drills from the structure the user actually got wrong, not a generic
worksheet. There are two delivery modes; **interactive is the default**.

### Mode A — Interactive (default)

Run the drill as a short back-and-forth in the conversation:

- Pose **one problem at a time**, tagged `[CODE]`, and **wait** for the user's
  written answer. Do not show the next item yet.
- **Hold the correction** until they have attempted it — this preserves the
  self-test. When they answer, confirm or correct, give the rule in one clause
  (+ an L1 note if relevant), then pose the next item.
- Keep a session to ~5–8 items so it stays a quick round.
- The chat naturally guards honesty (you withhold the answer), so no separate
  solutions file is needed.

### Mode B — Two-file set (offline / larger practice)

Use when the user wants a bigger set to do on their own, away from the chat:

- `drills.md` — problems only, each tagged `[CODE]` and a difficulty tier.
- `drills-solutions.md` — worked answer + the one-line rule for each item, in a
  **separate** file so the user can self-test without seeing the answers.

Both modes use the same design rules, difficulty ladder, and ledger/re-probe
updates below.

### Design rules

- 5–8 items per error code. More than one code per drill set is fine if the user has
  several active gaps, but keep each item single-focus.
- **Require production.** Every item must make the user *write or correct* a sentence.
  Multiple-choice and "name the rule" don't build the habit — they test recognition.
- **Ladder the difficulty:**
  1. **Recognize/correct** — a wrong sentence to fix (scaffolded, the target error
     is the only thing wrong).
  2. **Produce in a frame** — give a prompt/word set; the user forms a correct sentence.
  3. **Produce freely + boundary** — an open prompt that also hits a tricky case where
     the naive rule doesn't apply (e.g., zero article with uncountables; irregular past).
- Draw at least one item from the user's **own** erroneous sentence (reworded), so the
  practice connects to their real mistake.

### `drills.md` template

```markdown
# Grammar drills — <date>
Focus: [SVA], [ART]

## [SVA] — subject–verb agreement
1. (correct) The data show a trend, but the summary "show" the opposite. → fix it.
2. (frame) Make a present-tense sentence about your brother using "work".
3. (free+boundary) Write a sentence where the subject is "Everyone" — what verb form?

## [ART] — articles
...
```

### `drills-solutions.md` template

```markdown
# Solutions — <date>

## [SVA]
1. "…the summary shows the opposite." — 3rd-person singular subject ⇒ -s.
2. e.g. "My brother works at a bank." — he/she/it + present ⇒ -s.
3. "Everyone has a role." — "everyone" is grammatically singular ⇒ singular verb.
   (Boundary: notionally plural, grammatically singular.)
```

---

## Part 2 — Spaced re-probes

Store re-probe state inside `error-ledger.yaml` (see the seed template). An error the
user corrected once is not internalized; resurface it on a spreading schedule with a
**fresh cue** each time — never the original sentence.

### Schedule

- Stages by `interval_stage`: **1 = +7 days, 2 = +30 days, 3+ = +90 days.**
- Seed only the user's **systematic** errors (from the ledger), highest-frequency
  first. The re-probe queue is a retrieval schedule, not a copy of every error.
- Run **at most one re-probe per session**, at the session start, before new marking.
  Tell the user how many more are due.

### Cue rotation (never repeat a prompt)

Before writing a re-probe, read the item's `probe_history`. Rotate the angle by stage
so the user can't pattern-match a memorized answer:

1. **transfer** — same error type, new topic/structure.
2. **boundary** — a case where the usual correction does *not* apply.
3. **perturbation** — change one feature; ask what else must change.
4. **why** — produce the correction and state the load-bearing rule in one clause.

Cycle again after stage 4 with fresh language. Always require production.

### Updating the schedule

- **Pass (unaided correct + reason):** append the attempt, increment `interval_stage`,
  keep `status: scheduled`, set the next `due_date` from the pass date (30 days for
  stage 2, then 90). After several clean passes, mark the ledger error `resolved`.
- **Fail:** append the attempt, set `status: needs-work`, keep the current stage and
  due date so it stays visible. After a corrected unaided retry, increment and reschedule.
- **Same code reappears in new marked text:** treat as fresh failure — set
  `status: needs-work`, update the source fields, retain the stage, surface it before
  lower-priority items. Bump the error's `frequency` in the ledger.
