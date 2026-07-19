---
name: ielts-learning-planner
description: Build a personalised IELTS study plan with weekly schedules, skill-specific drills, and progress milestones. Use this skill when the user wants a study plan, asks how to prepare for IELTS, wants to know how to allocate study time across the four skills, or asks how to improve from their current band to their target band. Also use when the user asks how to use academic paper reading to improve IELTS Reading, wants to integrate reading research papers into their IELTS prep, or asks for a paper-reading routine. Integrates with ielts-reading-strategies, ielts-writing-task1, ielts-writing-task2, ielts-speaking-coach, and ielts-vocabulary-builder.
---

# IELTS Learning Planner

A study plan is only useful if it is calibrated to the gap between the current band and the target, the time available, and the user's weakest skills. Generic plans waste time on strengths and ignore real gaps.

## Use this when

- The user wants a structured IELTS study plan.
- The user asks how to allocate study time across Listening, Reading, Writing, Speaking.
- The user wants to integrate academic paper reading into their IELTS preparation.
- The user asks how to move from a specific current band to a target band.
- The user asks for a daily or weekly schedule.

## Do not use this when

- The user wants feedback on a specific essay or speaking response — route to the relevant writing or speaking skill.
- The user wants vocabulary for a specific topic — use `ielts-vocabulary-builder`.
- The user wants strategy for a specific question type — use `ielts-reading-strategies`.

---

## Step 1 — Diagnostic

Before building a plan, establish:

| Question | Why it matters |
|----------|----------------|
| Current band (overall and per skill) | Identifies the gap and which skills to prioritise |
| Target band | Determines how aggressive the plan needs to be |
| Test date / weeks available | Sets the timeline and intensity |
| Study hours available per week | Determines what is realistic |
| Weakest skill | Gets the most allocated time |
| Academic or General Training | Different Reading/Writing demands |

If the user has not taken a test, ask them to estimate based on a practice test, or assume Band 5 as a starting point.

**Typical band gaps and realistic timelines:**

| Gap | Realistic timeframe (full-time study ~15 hrs/week) |
|-----|----------------------------------------------------|
| +0.5 band | 4–6 weeks |
| +1.0 band | 8–12 weeks |
| +1.5 bands | 16–20 weeks |
| +2.0 bands | 6–12 months |

Progress is rarely linear — Reading and Listening tend to respond faster than Writing and Speaking.

---

## Step 2 — Skill Prioritisation

### Overall band score calculation

The four skills (Listening, Reading, Writing, Speaking) are averaged and rounded to the nearest 0.5. A gain in any single skill lifts the overall band.

> To set realistic per-skill targets and explain what each band requires, use the band-descriptor reference: [`references/ielts-band-descriptors.md`](references/ielts-band-descriptors.md) (bands 5–9 across the Writing and Speaking criteria, with links to the official IELTS descriptors).

**Triage logic:**

1. Find the skill(s) furthest below the target — these get the most time.
2. Never completely neglect any skill, even strong ones — they decay without practice.
3. Writing improves slowest (requires examiner feedback cycles); start writing early.
4. Reading responds well to volume and strategy work — high ROI per hour.
5. Listening responds to regular exposure; daily short sessions beat weekly marathons.
6. Speaking improves with frequency — short daily practice beats one long weekly session.

**Suggested time allocation by weak skill:**

| Weakest skill | Suggested weekly split |
|---------------|----------------------|
| Writing | Writing 35% / Reading 25% / Listening 25% / Speaking 15% |
| Reading | Reading 35% / Writing 25% / Listening 25% / Speaking 15% |
| Speaking | Speaking 35% / Writing 25% / Listening 25% / Reading 15% |
| Listening | Listening 35% / Writing 25% / Reading 25% / Speaking 15% |
| Balanced | 25% each |

---

## Step 3 — Weekly Plan Template

### Sample plan: 15 hrs/week, target +1 band, weak in Reading and Writing

| Day | Activity | Duration | Skill |
|-----|----------|----------|-------|
| Mon | Academic paper reading session (see below) | 45 min | Reading |
| Mon | IELTS Reading practice — 1 passage + question type drill | 30 min | Reading |
| Tue | Writing Task 2 draft | 40 min | Writing |
| Tue | Task 2 vocabulary + collocation study | 20 min | Vocabulary |
| Wed | Academic paper reading session | 45 min | Reading |
| Wed | Listening practice — 1 section with transcript review | 30 min | Listening |
| Thu | Writing Task 1 draft + self-score | 30 min | Writing |
| Thu | Speaking Part 2 + Part 3 practice | 30 min | Speaking |
| Fri | IELTS Reading — full passage timed (20 min) + analysis | 30 min | Reading |
| Fri | Vocabulary drill — topic bank (rotate topics weekly) | 20 min | Vocabulary |
| Sat | Full mock: Reading (60 min) or Writing (60 min) | 60 min | Mixed |
| Sat | Review mock answers — score and error analysis | 30 min | Mixed |
| Sun | Light review — vocabulary cards, Speaking Part 1 Q&A | 20 min | Mixed |

Adjust proportions based on the diagnostic. The structure above is a skeleton, not a prescription.

---

## Step 4 — Reading Papers for IELTS Reading

### Why academic papers help

IELTS Academic Reading passages are drawn from journals, magazines, and reports written for a non-specialist educated audience. They share key features with academic papers:

- Long, complex sentences with multiple clauses
- Academic vocabulary (AWL words in natural context)
- Argumentative structure: claim → evidence → qualification → conclusion
- Hedging language: "suggests", "may indicate", "it appears that"
- Dense information in a short space

Reading papers regularly trains the same skills the IELTS Reading test examines: identifying main claims, distinguishing fact from opinion, locating specific information, and understanding how arguments are constructed.

### What to read

**Ideal sources** (accessible, not overly technical):
- Review articles and survey papers (they explain fields rather than assume expertise)
- Science journalism derived from research (e.g., Nature News, Scientific American)
- Working papers and policy reports (World Bank, OECD, IMF)
- arXiv papers in areas the user finds interesting — particularly introductions and conclusions

**Topic match to IELTS themes:**

| IELTS Reading topic | Good paper domains |
|---------------------|--------------------|
| Environment / Climate | Environmental science, ecology, climate policy |
| Technology | Computer science surveys, AI ethics, human-computer interaction |
| Health / Medicine | Public health reviews, epidemiology |
| Society / Education | Sociology, education research, psychology |
| Economy | Economics working papers, development economics |
| History / Archaeology | Humanities review articles |

**Tip:** The user does not need to understand every technical detail. The goal is to practise reading strategies and absorb vocabulary in context — not to master the field.

### The paper-reading session (45 minutes)

This is a structured session, not free reading. Follow this protocol every time:

#### Phase 1 — Skim (5 min)

Read only:
- Title
- Abstract
- Section headings
- First and last sentence of each section

Goal: build a mental map of what the paper argues and how it is structured. Do not read body paragraphs yet.

After skimming, write one sentence: *"This paper argues that… by…"*

This mirrors the IELTS skill of identifying the main idea before engaging with detail.

#### Phase 2 — Targeted reading (20 min)

Pick 2–3 sections that seem most relevant or interesting and read them carefully. While reading:

- Underline claims (what the authors argue).
- Circle evidence markers ("demonstrated that", "data suggest", "findings indicate").
- Mark hedging language ("may", "appears to", "it is possible that").
- Flag any unfamiliar vocabulary.

After this phase, try to answer: *"What evidence does the paper use to support its main claim? Is there any limitation or counterargument mentioned?"*

This mirrors True/False/Not Given and Yes/No/Not Given logic.

#### Phase 3 — Vocabulary harvest (10 min)

From the sections you read, collect:
- 5 new academic words or phrases
- Their collocations (how they are used in the sentence, not just the word alone)
- One example sentence you could use in an IELTS essay

Record these in a vocabulary notebook or flashcard system.

#### Phase 4 — Reflection (10 min)

Write 3–5 sentences summarising the paper in your own words. This is low-stakes Writing Task 1 practice: selecting key information and expressing it accurately and concisely.

Then ask: *"If this were an IELTS passage, what question types would fit it?"* (E.g., would the argument structure lend itself to YNNG? Would the process lend itself to flow-chart completion?)

### Frequency recommendation

| Band target | Recommended paper sessions per week |
|-------------|-------------------------------------|
| Band 6.0    | 2 sessions/week |
| Band 7.0    | 3 sessions/week |
| Band 7.5+   | 4–5 sessions/week |

Start with review articles and science journalism. Move to primary research papers as comfort grows.

---

## Step 5 — Skill-Specific Weekly Routines

### Reading

- 3–4 paper-reading sessions per week (see above).
- 2–3 IELTS Reading passages per week with question type focus (rotate types weekly).
- Weekly: 1 timed full-section mock (60 min, 3 passages, 40 questions).
- Daily: 10 min vocabulary review from paper harvest.

### Writing

- Task 2: write 2 essays per week. Score yourself immediately using the band descriptor table. If possible, get one reviewed by a teacher or use `ielts-writing-task2`.
- Task 1: write 1 report per week, rotating visual types (line graph one week, map the next).
- Weekly: study 1 model answer — analyse its structure, vocabulary choices, and cohesive devices.
- Daily: 10 min vocabulary/collocation study from `ielts-vocabulary-builder`.

### Speaking

- Daily: 5–10 min Speaking Part 1 Q&A (speak aloud, not in writing).
- 3×/week: timed Part 2 cue card (1 min prep, 2 min talk, record if possible).
- 1–2×/week: Part 3 abstract discussion using topics from recent paper sessions.
- Weekly: review one recorded answer for vocabulary range and fluency patterns.

### Listening

- Daily: 20–30 min exposure (podcast, lecture, documentary — not just IELTS tests).
- 2–3×/week: official IELTS Listening section with transcript review after answering.
- Weekly: transcribe 2 minutes of audio — builds ear for natural speech patterns.

---

## Step 6 — Progress Milestones

Set a checkpoint every 3–4 weeks:

1. Take a full timed mock test (use official Cambridge IELTS books or equivalent).
2. Score each section.
3. Compare to the previous checkpoint.
4. Identify which question types or skill areas still show errors.
5. Adjust the plan: increase time on stagnant skills, reduce time on skills already at target.

**Signs a skill is improving:**
- Reading: fewer NOT GIVEN errors; finishing sections within time; raw score increasing.
- Writing: less repetitive vocabulary; overview included in Task 1; position clearer in Task 2.
- Speaking: longer answers without pausing to search for words; more varied connectives.
- Listening: catching more specific details; fewer mishearings on section 3 and 4.

---

## Plan Output Format

When generating a plan for the user, produce:

1. **Diagnostic summary** — current band, target band, gap, weeks available, weak skills identified.
2. **Weekly time allocation table** — hours per skill per week.
3. **7-day schedule** — specific daily activities with durations.
4. **Paper-reading session schedule** — days and target domains.
5. **4-week milestone** — what a successful checkpoint looks like for this user.
6. **Resources to use from this skill set** — which other IELTS skills to invoke for each activity.

Keep the plan realistic. A plan the user will not follow is worse than no plan. If they only have 5 hours per week, say so clearly and set a longer timeline.
