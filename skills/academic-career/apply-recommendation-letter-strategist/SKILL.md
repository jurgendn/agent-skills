---
name: apply-recommendation-letter-strategist
description: >-
  Plan PhD and research-application recommendation letters: choose recommenders, assess letter strength and risk, draft request or reminder emails, and prepare recommender packets. Use this skill whenever the user asks who should write their letters, whether a recommender is strong enough, how to ask for a recommendation, what materials to send, or how to coordinate letters for PhD programs, fellowships, research internships, RA roles, or lab applications. Establishes the target's declared theme or track from its live official page first, since it decides which recommender's observed evidence matters most and what the packet must supply.
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

### 2. Check the target's declared theme, then choose the letter set

Where the target declares a **theme, specialisation, track, or topic scope**, the committee reads the letters against it too. Establish the theme before comparing recommenders.

Get it from the live source: if the target is not one you already have text for in this conversation, **search the web for the programme's or call's official page** (and the specific track page where there are several) and read the declared scope in the programme's own words. Never infer it from the programme's name. If the page cannot be found, ask the user for the link rather than assuming a theme. Where none is declared, note `no declared theme — N/A` and choose on the general criteria alone.

The theme affects **who is asked** and **what evidence the packet supplies** — never what the letter is asked to claim:

- Prefer, among otherwise comparable recommenders, the one who **personally observed** work inside the declared theme. A supervisor who watched the applicant do the theme-relevant project is worth more here than a more senior writer who did not.
- Cover the theme across the set where possible, but never at the cost of a writer with real evidence: three theme-adjacent generic letters lose to two specific ones.
- If **no recommender** has observed theme-relevant work, say so plainly. That is a finding about the package — and sometimes about the target — not a gap to be papered over in the request email.

Hard rule: **never ask a recommender to mention the theme, use its vocabulary, or frame work as theme-relevant when they did not observe it that way.** The packet supplies real evidence and lets the writer choose; anything further is putting words in their mouth.

Then prefer recommenders who can provide:

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
- the declared theme or track per target, in the programme's own words, where one exists
- short summary of work with the recommender
- 3-6 specific evidence points they could mention truthfully, flagging which of them the writer observed inside the declared theme
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
## Declared theme per target
<!-- Theme in the programme's own words + source page and date checked, or "no declared theme — N/A".
     Where the official page could not be located, write "page not located — link needed". -->

## Recommender assessment
| Recommender | Likely strength | Evidence they can cite | Observed theme-relevant work? | Risks | Recommendation |
|---|---|---|---|---|---|

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

A strong output improves the odds of specific, credible, timely letters. It should be candid about risk, avoid prestige bias, and never help fabricate or overstate a recommender's knowledge of the applicant — including by steering a writer toward a declared theme they did not observe the applicant working in.
