---
name: apply-interview-prep
description: >-
  Prepare for academic selection interviews and conversations — PhD admissions, funded-project or DAAD-style panels, scholarship/embassy panels, MSc admissions, and prospective-supervisor calls. Use when the user says "I have a PhD interview", "DAAD interview next week", "my supervisor wants a call", "what will they ask me", "mock interview me", or has been shortlisted and wants to prepare. Always triage who is across the table first: funder committees, prospective supervisors, and administrative panels assess different things. Distinct from apply-sop-writer (written essays), apply-cold-email-drafter (first contact), and professor-critic (grades the finished rehearsal). If the programme selects on documents only, route out rather than inventing interview prep.
---

# Academic Interview Preparation

An academic interview is not one thing. The same applicant, the same research, and the same question — "why this programme?" — demand different answers depending on who is asking. A funder's academic committee is testing whether your plan is feasible and whether their money is well spent. A prospective supervisor is testing whether they want to work with you for four years. An embassy panel is testing eligibility, motivation, and whether you will do what the programme was funded to make you do.

Preparing one generic set of answers and delivering it to all three is the most common failure mode. This skill triages first, then builds prep specific to the assessor.

## Use this when

- The user has been shortlisted or invited to an interview, call, or selection panel for a research programme, PhD position, MSc programme, or scholarship.
- A prospective supervisor has replied to outreach and proposed a conversation.
- The user wants a mock interview, an answer bank, or questions to ask the interviewer.
- The user is unsure what a specific programme's interview will actually assess.

## Do not use this when

- No interview exists yet and the user is making first contact — use `apply-cold-email-drafter`.
- The task is a written essay, motivation letter, or research statement — use `apply-sop-writer`.
- The user wants a whole-package consistency check — use `apply-package-auditor`.
- The user wants a graded scorecard of their profile — use `apply-dossier-evaluator`.
- The programme selects on documents alone (see Step 0) — there is nothing to rehearse.

## Step 0 — Triage: who is across the table?

**Do this before anything else.** Everything downstream depends on the answer. Ask the user, or determine from the programme, which of these applies. `references/who-is-across-the-table.md` carries the full profile of each type.

| Assessor | Typical settings | What they are actually testing |
|---|---|---|
| **A. Funder's academic committee** | DAAD research grants and study scholarships; some Erasmus Mundus consortia | Is the plan feasible, is the host well chosen, is this person a good bet |
| **B. Prospective supervisor** | Direct PhD via cold email; Australian RTP; MSCA/EURAXESS positions | Can I work with this person, do they think independently, will they finish |
| **C. Administrative / embassy panel** | MAECI and similar national scholarships | Eligibility, motivation, benefit to home country, follow-through |
| **D. No interview — documents only** | SISGP, Italian DSU, IYT, many EMJM consortia | Nothing. Route out. |

**If the answer is D, say so plainly and stop.** Do not generate interview prep for a selection process that has no interview. Route the user to `apply-sop-writer` for the motivation letter and reference-letter strategy, since in a document-only process those carry the entire load. If a programme mentions a recorded video presentation instead of a live interview, treat it as assessor type A or C with no follow-up questions — prepared delivery matters more, improvisation matters less.

**When the type is genuinely unclear**, say so and tell the user what to check: the invitation email itself (who is copied, and their titles), the programme's selection-procedure page, and whether the funder or the university issued the invitation. Do not guess. A wrong triage produces confidently wrong preparation.

**Mixed panels exist.** A DAAD committee may include a subject specialist who interviews like a supervisor. Prepare for the dominant type and hold the second type's material in reserve.

## Step 1 — Ground in what already exists

Interview answers must match the written application. A story that contradicts the SOP is worse than a weak story.

Pull from whatever the user already has: the structured profile from `apply-profile-reader`, per-school fit notes from `apply-program-fit-mapper`, the supervisor's current direction from `apply-research-direction-mapper`, and the submitted SOP and CV. If none exist, gather the equivalent by asking — but note that the interview answers you build are then unanchored to what the committee has actually read.

Flag any contradiction you find between what the user says aloud and what their application claims. Committees do read the file before the interview.

## Step 2 — Build the answer bank

Five answers carry most interviews regardless of assessor type. Build these first, in the user's own words, drawn from real experience.

1. **The two-minute research summary.** Question, approach, what was found, why it mattered. Deliverable aloud without notes. This is the single highest-leverage artifact — it opens most interviews and sets the frame for everything after.
2. **Why this programme, this host, this group.** Must contain something that could not be said about any other programme. Generic answers here are the most commonly cited weakness.
3. **Why this degree, and what after.** Phrase it for the actual level. For a doctoral application: why a PhD, why now, and what research career follows. For a master's application: why this specific programme, why it is the right next step from your background, and what you will do with it — for master's scholarships with a development, bilateral, or leadership mission, "what after" is a **scored criterion**, not a closing pleasantry. Assessor types A and C weight this heavily in both cases. You are expected to have thought that far ahead.
4. **A failure or setback.** Structure with STAR/AR (see Step 3). The result must include what changed in the user's practice afterwards.
5. **Your questions for them** (Step 6).

Then add assessor-specific material per `references/who-is-across-the-table.md` — feasibility and timeline defence for type A, research-conversation depth for type B, eligibility and home-country benefit for type C.

**Do not script answers verbatim.** Build the load-bearing points and let the phrasing vary. Memorised answers fail under follow-up questions, and follow-up is where assessors actually discriminate between candidates.

## Step 3 — Structure the behavioural answers

For any "tell me about a time…" question, use **STAR**: Situation and Task (context), Action (what *you* specifically did), Result (what was achieved and why it worked). For failure and weakness questions use **STAR/AR**, which appends Alternative Action and Alternative Result — what you would do differently and what that would have produced. This converts a setback into evidence of judgement rather than a confession.

`references/structured-answer-evidence.md` carries the provenance and what the supporting evidence does and does not establish. Read it before making claims to the user about effectiveness.

The most common failure is a first-person gap: the user narrates what the *team* did and never says what *they* did. Assessors are evaluating one person. Probe for the individual contribution whenever an answer stays in "we."

## Step 4 — Sharpen: make every answer concrete

Structure alone produces answers that are organised but still vague. This step is where most of the real gain is. **Run every answer in the bank through the following pass, and do not accept the user's first version.**

### The five tests

Each answer must survive all five. Name which test an answer fails, quote the offending phrase, and ask for the replacement — do not silently rewrite it for them.

1. **Named, not categorised.** Every generic noun gets replaced by the actual thing. "A machine learning model" → "a 3D U-Net." "A large dataset" → "14,000 scans from three hospitals." "Some issues with the data" → "the third site labelled the boundary differently." Category words are where assessors stop believing you were there.
2. **Quantified or bounded.** Attach a number, or an honest bound, to every claim of change. "It improved a lot" → "Dice went from 0.71 to 0.86." If the user genuinely does not remember, "roughly a third faster" or "about six weeks" beats "significantly." Never invent a number — an invented figure collapses on the first follow-up.
3. **First-person and specific.** Every load-bearing verb has "I" as its subject and names an actual action: *I checked, I re-specified, I re-ran, I argued for*. "I was involved in" and "I helped with" are not actions.
4. **So-what stated.** Every answer ends with why the result mattered — what it enabled, what it ruled out, what changed afterwards. An answer that stops at the number leaves the assessor to supply the significance, and they may not.
5. **Deliverable in the time available.** The two-minute summary is two minutes, spoken. Answers to single questions land at roughly 60–90 seconds. Longer means the point is buried. Have the user say it aloud and time it; do not assess length by reading.

### Strip these

- **Hedges that weaken a true claim**: "kind of," "I guess," "a bit," "I just," "sort of." Distinguish these from *honest* uncertainty ("I'm not certain the effect holds beyond this dataset"), which is a strength and must stay.
- **Filler openers**: "That's a good question," "Basically," "So yeah."
- **Trailing dilution**: strong answers ending in "...or something like that" / "...but anyway."

### Set the jargon dial by assessor

Clarity is audience-relative — the same answer is not clear to all three types.

- **Type A (committee)**: field-adjacent but not sub-field. Assume they know the discipline, not your specific corner. Define your one core technical term as you use it.
- **Type B (supervisor)**: full technical depth. Under-explaining here wastes the conversation.
- **Type C (administrative panel)**: zero jargon. Have a version a smart non-specialist follows completely. Practise this one aloud — it is the hardest and the most often skipped.

### The sharpening loop

For each of the five core answers: have the user give it → name the failing tests with the quoted phrase → ask the question that extracts the missing specific → have them redeliver → time it. Repeat until it passes all five. **Two answers sharpened properly beat five answers left vague.**

Worked before-and-after: `examples/answer-calibration.md`.

## Step 5 — Calibrate self-presentation

How explicitly a candidate claims credit is culturally variable, and mismatches are penalised. An applicant trained to attribute results to circumstance and to the group can read to a German or Australian committee as not having contributed. The same applicant's directly-stated claims can read as arrogant to a panel with strong modesty norms.

`references/structured-answer-evidence.md` covers the research and its limits. The operating rule:

**Calibrate how explicitly the user claims work they actually did. Never invent claims, and never coach a personality.** The target is that an assessor's estimate of the user's contribution matches reality. If the user did it, say "I did it" — in most Western academic settings, understating a real contribution is not modesty, it is a transmission failure. Panels also detect performed personality reliably, so the fix is precision about facts, not manufactured confidence.

Ask the user what feels uncomfortable to say aloud. That discomfort usually marks exactly where the calibration gap sits.

## Step 6 — Prepare questions for them

Two or three per interviewer, specific enough that they could not have been asked of another group. Derive them from the interviewer's recent work — `apply-research-direction-mapper` output is the right input. Good questions ask about direction and open problems, not facts recoverable from the website.

For assessor type B this is not a courtesy — a supervisor is assessing whether a research conversation with the user is worth having, and the questions are a large part of that evidence.

Also prepare the questions the *user* needs answered to decide: funding duration and conditions, group size and supervision style, what happens if the project direction changes, employment status and terms where the position is a contract rather than a stipend.

## Step 7 — Rehearse

Run a live mock. Play the assessor type from triage, ask follow-ups, and push when an answer is vague, over-general, or stays in "we." Do not accept a first answer that would not survive a real committee.

Follow-ups are the point of the rehearsal: they are where memorised answers break and where the Step 4 tests get re-applied under pressure. After any answer that drifts back toward the generic, name the failing test and take it again.

Then hand the rehearsal to `professor-critic` with the named reader set to the triaged assessor and the acceptance bar set to the real decision — "advance to funding / reject" for type A, "offer a position / pass" for type B, "award / decline" for type C. That skill delivers a verdict; this one builds the material. Do not grade the rehearsal here.

## Step 8 — After the interview

Thank-you message within a day, referencing something specific from the conversation. Send any material promised during the interview. Record — while fresh — what was asked, what landed, what did not, and the user's own read on fit, since the user is also deciding. Feed recurring weak answers back into Step 2 before the next interview.

## Volatility

Interview format, panel composition, duration, language, whether a presentation is required, and whether an interview exists at all are **programme- and cycle-specific and change**. Deadlines, stipend amounts, age caps, and eligibility rules likewise. Treat every such specific as something to **verify against the live official call and the invitation email**, and say so to the user rather than asserting it. The durable content of this skill is the assessor taxonomy and the answer craft, not any particular programme's current procedure.

## Output

- A triage verdict naming the assessor type and what it implies.
- The answer bank: five core answers plus assessor-specific material, in the user's own words, each sharpened until it passes all five concreteness tests and timed aloud.
- Questions for each interviewer, and questions the user needs answered.
- A rehearsal transcript with follow-ups, and a pointer to `professor-critic` for the verdict.
- A short list of what to verify against the official call before the interview.
