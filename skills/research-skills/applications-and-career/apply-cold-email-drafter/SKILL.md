---
name: apply-cold-email-drafter
description: Draft, critique, and revise concise cold emails to professors for PhD applications, research internships, RA opportunities, lab rotations, or prospective-supervisor outreach. Use this skill whenever the user wants to contact a professor, ask about PhD openings, request a meeting, introduce their research background, mention a paper, follow up politely, or convert professor-fit notes into an email. This skill should trigger even if the user says "email a PI", "message a potential advisor", "reach out to faculty", or "cold mail" rather than "cold email".
---

# Professor Cold Email Drafter

A good professor cold email is short, specific, and easy to answer. It should prove the sender has done enough homework to be credible, while avoiding a long autobiography or generic praise.

## Use this when

- The user wants to draft, review, shorten, or personalize an email to a professor or PI.
- The user is asking about PhD supervision, lab openings, research internships, RA roles, rotations, or meetings.
- The user has professor-fit notes and wants an outreach message.
- The user needs a follow-up after no response.
- The user wants subject lines or alternative tones for academic outreach.

## Do not use this when

- The user has not yet figured out what the professor currently works on. Use `apply-research-direction-mapper` first.
- The user wants a full SOP or application essay. Use `apply-sop-writer`.
- The user is comparing many faculty or programs. Use `apply-program-fit-mapper`.
- The user needs recommender strategy. Use `apply-recommendation-letter-strategist`.

## Workflow

### 1. Gather the minimum context

Identify:

- sender status: prospective PhD applicant, master's student, undergraduate, industry researcher, RA applicant, etc.
- target professor, department, institution, and program cycle if relevant
- purpose: ask about openings, request meeting, seek feedback, express fit before applying, or ask about RA/internship
- professor-specific evidence: recent paper, project, talk, grant, or lab theme
- sender-specific evidence: 1-2 strongest research experiences, technical skills, publications, or projects
- constraints: desired tone, word limit, attachments, CV link, deadline, country/program norms

If professor-specific evidence is missing, ask for it or draft a clearly marked placeholder version. Do not fabricate paper titles or claims.

### 2. Choose the email strategy

Select one primary ask:

- **PhD fit / openings**: ask whether they are considering students in the cycle and whether your direction fits.
- **Research meeting**: ask for a short conversation around a specific shared topic.
- **RA / internship**: ask whether there are opportunities and state availability or relevant skills.
- **Follow-up**: briefly restate context and make it easy to ignore if busy.

Avoid combining too many asks. Professors should be able to decide what to do after one quick read.

### 3. Build the message

Use this structure:

1. **Subject**: specific, searchable, and not gimmicky.
2. **Opening**: who the sender is and why they are writing.
3. **Professor-specific hook**: one recent work/theme and what genuinely interests the sender.
4. **Sender fit**: one compact evidence-backed bridge from the sender's background.
5. **Ask**: one clear, low-friction request.
6. **Close**: mention CV/materials if attached, thank them, and sign off.

Keep the main email around 120-220 words unless the user requests otherwise. Prefer concrete details over flattery.

### 4. Calibrate tone and risk

Check for:

- generic praise such as "your esteemed research" without evidence
- excessive biography or paragraph-long project summaries
- overclaiming fit or implying guaranteed supervision
- asking the professor to do work the applicant should do
- mentioning outdated research if recent directions differ
- unclear program cycle or opportunity type
- attachments or links referenced but not included

When useful, provide both a polished version and a shorter version.

### 5. Add follow-up guidance

For follow-ups:

- wait a reasonable interval unless there is a deadline
- keep it under 100 words
- forward or reply in the same thread
- add one new useful detail only if it materially changes the request
- avoid guilt, urgency pressure, or repeated chasing

## Output formats

For drafting:

```markdown
## Subject options
1. [Specific subject]
2. [Alternative]

## Draft email
Dear Professor [Last Name],

[Email body]

Best regards,
[Name]

## Why this works
- Professor-specific hook: ...
- Applicant fit bridge: ...
- Ask: ...

## Optional edits
- Shorter version: ...
- If attaching CV: ...
- If no reply: ...
```

For review:

```markdown
# Cold Email Review

## Overall assessment

## Main risks

## Revised email

## Line-level fixes
```

## Quality bar

A strong email should sound like a serious junior researcher, not a mass-mail template. It should be specific enough to show fit, short enough to respect the professor's time, and clear enough that the professor can reply with a simple yes, no, or suggestion.
