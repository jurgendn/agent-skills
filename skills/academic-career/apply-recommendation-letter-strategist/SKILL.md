---
name: apply-recommendation-letter-strategist
description: >-
  Plan PhD and research-application recommendation letters: choose recommenders, assess letter strength and risk, draft request or reminder emails, and prepare recommender packets. Use this skill whenever the user asks who should write their letters, whether a recommender is strong enough, how to ask for a recommendation, what materials to send, or how to coordinate letters for PhD programs, fellowships, research internships, RA roles, or lab applications.
---

# Recommendation Letter Strategist

Recommendation letters are third-party evidence. The goal is to help the applicant choose credible advocates and give them the context needed to write specific, research-relevant letters.

## Use this when

- The user is choosing recommenders for PhD, research master's, fellowship, research internship, RA, or lab applications.
- The user wants to compare possible letter writers.
- The user asks whether a letter is likely to be strong, generic, risky, or redundant.
- The user wants request, follow-up, reminder, or thank-you emails.
- The user needs a recommender packet, brag sheet, or program-specific talking points.

## Do not use this when

- The user asks you to write a fake recommendation letter or impersonate a recommender.
- The user wants to misrepresent a relationship, contribution, or achievement.
- The user wants SOP drafting. Use `apply-sop-writer`.
- The user wants detailed CV rewriting. Use `apply-cv-builder`.
- The user wants full application coherence review. Use `apply-package-auditor`.

## Workflow

### 1. Map recommender options

For each possible recommender, identify:

- role and relationship to applicant
- duration and recency of interaction
- research, coursework, work, teaching, or mentorship context
- evidence they personally observed
- likely specificity and enthusiasm
- title or field credibility for the target application
- possible risks: generic letter, weak relationship, missed deadlines, lukewarm support, mismatch with target field

### 2. Choose the letter set

Prefer recommenders who can provide:

- direct evidence of research ability
- intellectual independence and technical depth
- writing, communication, or collaboration signal
- resilience and follow-through
- comparison to other students or researchers when credible
- complementary perspectives rather than three duplicate letters

A famous but distant recommender is often weaker than a less famous recommender with detailed evidence.

### 3. Prepare the ask

A strong request should:

- ask whether they can write a **strong** letter
- give a clear deadline and application context
- include why their perspective matters
- make the logistics easy
- offer a recommender packet
- give them a graceful way to decline

Do not pressure the recommender or imply they should say things they did not observe.

### 4. Build the recommender packet

Include:

- CV
- SOP or research statement draft if available
- transcript or grade context when relevant
- target program list and deadlines
- short summary of work with the recommender
- 3-6 specific evidence points they could mention truthfully
- links to papers, posters, code, or project artifacts
- instructions for submission portals

### 5. Manage deadlines and follow-up

Recommend a timeline for:

- initial ask
- packet delivery
- portal entry
- polite reminders
- final confirmation
- thank-you note and outcome update

## Output format

Use:

```markdown
## Recommender assessment
| Recommender | Likely strength | Evidence they can cite | Risks | Recommendation |
|---|---|---|---|---|

## Recommended letter set
1. [Name/role]: [why]
2. [Name/role]: [why]
3. [Name/role]: [why]

## Request email draft
Subject: [Subject]

[Email]

## Recommender packet
- [Material]
- [Material]

## Follow-up schedule
- [Date or relative timing]: [Action]
```

If facts are missing, mark them as questions rather than inventing details.

## Quality bar

A strong output improves the odds of specific, credible, timely letters. It should be candid about risk, avoid prestige bias, and never help fabricate or overstate a recommender's knowledge of the applicant.
