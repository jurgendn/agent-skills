# Logistics Reference

Use for Phase 4 draft handoff logistics: venue-aware formatting checks, coauthor sign-off, cover letters, and clean handoff to downstream audit skills. Distills Krantz, "How to Write Your First Paper" (Notices of the AMS, 2007), adapted for mathematics, applied mathematics, and graph ML venues.

## Operational Rules

- [EXPERT] Choose the venue before final formatting. Scope, audience, page limits, style files, anonymity rules, and supplement policies affect what the paper can say.
- [EXPERT] Do not use prestige as the only venue criterion. A technically correct paper can fail if the venue's readers do not care about the problem framing.
- [EXPERT] For mathematics venues, check theorem novelty, proof completeness, relation to known results, journal scope, notation style, and whether examples/counterexamples are expected.
- [EXPERT] For ML venues, check empirical standard, baseline expectations, reproducibility checklist, ethics/limitations requirements, page budget, and artifact policy.
- [EXPERT] Do not run full venue selection here. If the venue is undecided, hand off to `venue-targeting`; if the paper is near-final, hand off to `submission-readiness-audit`.
- [EXPERT] Freeze a submission candidate before asking for coauthor sign-off. The request should include the draft version, target venue, deadline, known risks, and exact approval request.
- [EXPERT] Discuss authorship and author order explicitly before submission. Do not let the submission deadline become the first time hidden assumptions surface.
- [EXPERT] For journal submissions, write a short cover letter that states the paper's fit, central contribution, and confirmation that the manuscript is not under review elsewhere if required.
- [EXPERT] Treat referee reports as information, not as a referendum on the author's worth. Separate required changes, optional improvements, misunderstandings caused by the draft, and disagreements with the referee.
- [EXPERT] When responding to referees, answer every substantive point with a location in the revised draft, a concise explanation, or a respectful reason for not changing.
- [EXPERT] Before submission, hand off the full draft to `argument-audit`, `submission-readiness-audit`, and `citation-auditor`; if LLM-assisted prose was used, also run `ai-writing-detector`.

## Venue Fit Checklist

```markdown
| Item | Math venue | ML venue | Status |
| --- | --- | --- | --- |
| Scope | theorem/problem fit | task/community fit | pass/fail |
| Page/style | journal class or template | conference template/supplement | pass/fail |
| Evidence norm | complete proof | baselines/ablations/seeds | pass/fail |
| Reproducibility | proof details/examples | code/data/hyperparameters | pass/fail |
| Review mode | editorial/referee | double-blind/area chair | pass/fail |
```

## Coauthor Sign-Off Protocol

```markdown
Subject: Sign-off request for <paper title> to <venue>

Draft version:
Target venue:
Deadline:
Known risks:
Requested action: approve / approve with minor edits / block submission until issue resolved
Response deadline:
```

## Reproducibility Handoff

- [EXPERT] For ML venues, check only that the draft names the code/data artifact path, experiment-note sources, and unresolved reproducibility gaps.
- [EXPERT] Do not duplicate the full reproducibility audit here. Use the paper workspace's `references/reproducibility-checklist.md` during drafting, then run `reproducibility-audit` or `artifact-release-packager` for release-level work.
- [EXPERT] If a reported result cannot be traced to an experiment note, command, seed/config, or code commit, mark it as a draft-handoff blocker and route back to the experiment/result-writing stage.

## Draft Handoff Risks

- [EXPERT] Blocking: venue style/page limit impossible without removing core evidence.
- [EXPERT] Blocking: a coauthor has not approved the submission.
- [EXPERT] Blocking: an empirical claim depends on unavailable or undocumented results.
- [EXPERT] Blocking: a theorem depends on an unproven lemma or undefined assumption.
- [EXPERT] Nonblocking but risky: related work is structurally placed but not source-grounded; route to `literature-triangulation`.
