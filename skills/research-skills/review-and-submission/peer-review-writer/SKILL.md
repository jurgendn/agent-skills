---
name: peer-review-writer
description: >-
  Write a peer review of someone else's paper for a conference or journal — structured summary, evidenced strengths and weaknesses, calibrated scores, and constructive questions. Use whenever the user is the REVIEWER: "I have to review this paper", "help me write a review for NeurIPS/ICML/ACL/a journal", "is this weakness worth rejecting over", "how do I phrase this criticism", "draft my review from these notes", "what score should I give", or they share a manuscript they were assigned. Also use for meta-reviews, emergency reviews, and for serving on a program committee or as area chair — "I'm on the PC for X", "how does bidding/COI work", "how do I manage subreviewers", "I'm an area chair, how do I run the discussion". Do NOT use when the user is the AUTHOR: responding to reviews of their own paper is reviewer-response-strategist, pre-submission self-auditing is submission-readiness-audit, and mining a paper for research openings for their own work is gap-finder.
---

# Peer Review Writer

Write reviews that are useful to three audiences at once: the authors (what to fix and why), the area chair (a decision-relevant signal), and the community (quality control that is fair and calibrated).

A review's authority comes from evidence, not adjectives. Every weakness must point at something specific in the paper — a section, an equation, a table — and say why it matters for the paper's claims. "Not novel enough" and "experiments are insufficient" are verdicts, not reviews.

## Ground rules (ethics and stance)

- **Review the paper that was submitted**, not the paper you wish the authors had written. A different research question is not a weakness.
- **Confidentiality is absolute.** Never suggest actions that leak the manuscript, and do not attempt to deanonymize authors; if the user pastes a manuscript, work only within this conversation.
- **No citation-fishing.** Suggest missing references only when they genuinely undermine novelty or are load-bearing baselines — never the user's own work unless it clearly meets that bar, and flag the conflict if so.
- **Match severity to evidence.** If the user hasn't verified a suspected flaw (e.g. "I think this proof is wrong"), phrase it as a question to the authors, not an accusation.
- **A weakness must be either fixable or fatal — say which.** Fixable → frame as a request the rebuttal can address. Fatal → say plainly it determines your score, so the AC can weigh it.
- Most venues now require reviews to reflect the reviewer's own judgment. This skill structures, sharpens, and phrases the USER's assessment — when the user hasn't formed one yet, extract it by asking, don't invent one.

## Process

### 1. Establish the review context

Ask (or infer from the prompt) before drafting: the venue and its review form (scores, mandatory sections, rebuttal or not), the deadline pressure (full review vs. emergency review), and how far the user has gotten (haven't read it / read it with rough notes / know the verdict, need the writing). Enter the process at the matching step — a user with complete notes needs steps 4–5, not a reading plan.

### 2. Read for the claim–evidence map

Guide a two-pass read. Pass one (15 min): abstract, intro, figures, tables, conclusion — extract the paper's central claims and the contribution type (new method / new theory / new benchmark / new finding). Pass two: for each claim, locate the evidence offered and rate it: **supported / partially supported / unsupported / contradicted by the paper's own results**. This map is the skeleton of the entire review; every strength and weakness should trace back to a row in it.

For early-career reviewers who need help calibrating stance, fairness, and what a real referee report should contain, use `references/early-career-referee-primer.md` (grounded in Ntampaka et al., 2022, arXiv:2205.14270). It is especially useful when the user is unsure whether they are being too harsh, too lenient, or too formulaic.

For OpenReview-era ML/NLP/CV/AI venues such as ICLR, NeurIPS, CVPR, AAAI, ACL/ARR, or ICML-like conferences, use `references/openreview-era-reviewing.md` to calibrate review tone, specificity, LLM/confidentiality policy, ethics/limitations checks, rebuttal questions, and score/confidence behavior. Always check the live venue guide when the user names a current venue.

### 3. Assess along the four standard axes

- **Soundness:** do the methods/proofs/experiments actually support the claims? Check the classics: missing or weak baselines, no variance/seeds, test-set decisions, claims broader than the evidence (tested on 3 datasets, claimed "general"), proofs with unstated assumptions.
- **Novelty/contribution:** what is the delta over the closest prior work — *named*, not vibes? Distinguish "incremental but solid" (often acceptable) from "already exists" (fatal; must cite where).
- **Significance:** who acts differently if this is true? A correct, novel, useless result is a real category — say so honestly.
- **Clarity:** could a competent reader reimplement / re-derive it? Clarity issues are almost always fixable — never the headline reason to reject a sound paper.

### 4. Triage weaknesses before writing

Sort the raw weakness list into: **major-fatal** (sinks the paper if unanswered), **major-fixable** (rebuttal or revision can address), **minor** (typos, presentation, small requests). The review should foreground at most 2–4 major points — a review with twelve co-equal weaknesses gives the AC no signal and the authors no priorities. Minor points go in a compact list at the end.

### 5. Draft the review

Use the venue's form; when there is none, use this structure:

```
## Summary
[3–6 sentences proving you understood the paper: problem, approach,
key results — neutral tone, no evaluation yet. Authors should nod
reading this.]

## Strengths
[S1, S2, ...: specific and evidenced, same rigor as weaknesses.
"Clean ablation isolating X (Table 3)" not "well written".]

## Weaknesses
[W1, W2, ...: ordered by severity. Each = what (with section/table/eq
reference) → why it matters for the claims → what would resolve it.]

## Questions for the authors
[Numbered, answerable, decision-relevant — each tied to a weakness
whose resolution could move your score. Not rhetorical.]

## Minor comments
[Typos, notation, presentation — compact list.]

## Score and justification
[Score on the venue's scale + 2–3 sentences tying it to the major
weaknesses; state explicitly what rebuttal answer would raise it.]
```

### 6. Calibrate the score

Anchor to the venue's scale semantics, not gut feeling: a sound-but-incremental paper is typically borderline, not reject; unsupported central claims cap the score regardless of polish. Cross-check consistency: the score must follow from the stated weaknesses — a review listing only minor issues cannot justify a reject, and confidence should reflect actual expertise overlap (it is fine, and better for the AC, to mark low confidence outside one's area).

Two calibration facts from the PC side that reviewers routinely get wrong:
- **The accept/reject border is not the middle score — it's usually "weak accept".** A merely-average score is a soft reject at a selective venue; a paper often needs at least one genuinely enthusiastic champion to get in. Don't mistake "I don't object" for "accept."
- **Don't cluster around the mean — use the range.** Scores tend to bunch up; a clear strong or weak score is *more* useful to the AC than a hedge. If you love it or dislike it, say so decisively (you can revise after discussion). Judge the paper on whether its central contribution is worth the community's attention, not on flaw-count: a novel, useful idea can merit acceptance despite typos and sloppy references, while flawless execution of a boring result stays boring.

Before finalizing, run the fairness pass: would you consider this review fair and useful if you received it on your own paper?

## Special modes

- **Emergency review (hours, not days):** compress to pass-one reading + claim–evidence map on the central claim only; say honestly in confidence/limitations what was not checked (appendix proofs, supplementary experiments).
- **Meta-review / AC summary:** synthesize the reviews' points of agreement and disagreement, weigh them by evidence rather than by count or confidence scores, state the decision rationale in terms of the strongest surviving argument, and list what the camera-ready must fix.
- **Rebuttal-phase update:** re-score against what the rebuttal actually resolved; acknowledge answered points explicitly rather than going silent or moving the goalposts to new weaknesses.
- **Serving on a program committee (PC member / area chair):** when the user isn't writing a single review but is *responsible for a pile* of submissions — bidding, conflicts of interest, deciding what to review vs. delegate, managing subreviewers, driving discussion, and reaching decisions — use `references/pc-member-guide.md`. It covers the full PC timeline and mechanics (grounded in Dulek et al., 2021, arXiv:2105.02773). The per-review craft in the main workflow still applies to each paper the user reviews personally.
