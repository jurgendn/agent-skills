# OpenReview-era reviewer norms

Use this reference when reviewing for modern ML/NLP/CV/AI venues that use
OpenReview-style workflows, including ICLR, NeurIPS, CVPR, AAAI, ACL/ARR, and
ICML-like conferences.

This is a distilled calibration reference, not a substitute for the current
venue instructions. When the user names a specific current venue, check that
venue's live reviewer guide and review form before finalizing scores, policy
claims, LLM-use handling, or ethics requirements.

Last checked: 2026-07-08.

Sources:
- ICLR 2026 Reviewer Guide: https://iclr.cc/Conferences/2026/ReviewerGuide
- NeurIPS 2025 Reviewer Guidelines: https://neurips.cc/Conferences/2025/ReviewerGuidelines
- CVPR 2026 Reviewer Guidelines: https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelines
- AAAI-26 Reviewer Instructions: https://aaai.org/conference/aaai/aaai-26/instructions-for-aaai-26-reviewers/
- ACL Rolling Review Reviewer Guidelines: https://aclrollingreview.org/reviewerguidelines
- ACL Rolling Review Review Form: https://aclrollingreview.org/reviewform

## Core reviewer obligations

- Review the submitted work, not the paper you wish existed.
- Identify the paper's central claim, contribution type, and target community.
- Check whether the evidence actually supports the claims, including empirical,
  theoretical, resource, benchmark, and position-paper claims.
- Separate decision-critical weaknesses from optional improvement suggestions.
- Make novelty objections specific: name the closest prior work and explain the
  actual overlap. Vague "this is known" criticism is not enough.
- Make baseline objections specific: name the missing baseline, benchmark, or
  protocol and say what conclusion it would test.
- Ask actionable, rebuttal-relevant questions. Prefer questions whose answers
  could raise or lower the score.
- Calibrate confidence honestly. If proofs, appendices, code, related work, or
  parts of the experiments were not checked, say so.
- Revisit the assessment after author response and reviewer discussion based on
  what was actually clarified, corrected, or newly surfaced.

## Tone and phrasing

- Critique claims, methods, evidence, and presentation, not author competence or
  intent.
- Prefer "the paper", "the work", or "the submission".
- Avoid "you"; usually avoid "the authors" when the sentence can be written
  about the work instead.
- Phrase criticism as if it were being delivered respectfully face to face.
- State what would resolve the concern: evidence, analysis, proof detail,
  baseline, clarification, narrowed claim, or limitation statement.

## What to check in the paper

- **Claim support:** Do the main results, proofs, or analyses support the
  headline claims, or do conclusions outrun the evidence?
- **Novelty and positioning:** Is the delta over closest prior work clear and
  correctly attributed?
- **Baselines and protocol:** Are strong incumbents, closest prior methods,
  lower bounds, and self-ablations included where the claim requires them?
- **Metrics and benchmarks:** Do the chosen metrics and datasets match the
  claimed property, such as accuracy, efficiency, robustness, generalization,
  fairness, interpretability, or sample efficiency?
- **Reproducibility:** Are data, splits, preprocessing, seeds, configs, tuning
  budget, hardware assumptions, code, and evaluation protocol described enough
  for the main result to be reproduced or used as a baseline?
- **Statistical support:** Are variance, confidence intervals, significance
  tests, or repeated runs reported when the claim depends on small differences?
- **Limitations and scope:** Are known limits, failure modes, and
  generalizability boundaries stated honestly?
- **Ethics and societal impact:** Are personal data, human-subjects data, dual
  use, bias, exclusion, safety, and harmful failure modes handled according to
  the venue's policy?
- **Data and artifact attribution:** Are datasets, codebases, models, and other
  assets cited and licensed appropriately?
- **Citation reliability:** Are references real, correctly attributed, and
  aligned with the claims they are attached to?

## Review form calibration

Modern forms often separate several axes. Do not let one axis silently stand in
for another.

- **Soundness:** Are the claims technically and methodologically supported?
- **Significance / impact / excitement:** Who would care or act differently if
  the result is true? State whether the impact is broad or narrow.
- **Originality / novelty:** What is new relative to named prior work?
- **Clarity:** Can a competent reader understand, reimplement, or rederive the
  work?
- **Reproducibility:** Is there enough information to reproduce the main
  result, use the result as a baseline, or build on the artifact?
- **Overall recommendation:** Tie the score to the few load-bearing reasons,
  not to a count of minor issues.
- **Confidence:** Reflect expertise overlap and what was checked, not how
  strongly worded the review is.

## LLM use and confidentiality

- The reviewer remains responsible for every sentence submitted under their
  name, including any LLM-assisted text.
- Do not paste confidential manuscripts, reviews, rebuttals, or discussions into
  third-party systems unless the venue policy explicitly permits it.
- Disclose LLM use when the review form or venue policy asks for it.
- Watch for fabricated facts, fabricated citations, or overconfident summaries
  in LLM-assisted text.
- Do not copy content from other reviews, including AI-generated reviews. It is
  acceptable to state agreement or disagreement with a point in your own words.

## Discussion and rebuttal behavior

- Read the author response against the concerns actually raised in the review.
- Acknowledge resolved concerns explicitly.
- Update the score when the response changes the evidence, not to preserve the
  initial position.
- Do not move the goalposts by replacing answered concerns with unrelated new
  objections unless the new issue is genuinely decision-critical.
- During reviewer discussion, weigh arguments by evidence rather than by vote
  count or reviewer confidence alone.

## Common low-quality review patterns to avoid

- Terse reviews that give a score without a decision-relevant rationale.
- "Not novel" without references and overlap analysis.
- "Missing baselines" without naming which baselines and what they test.
- Rejecting because the paper is not the contribution type you expected.
- Treating lack of SOTA as fatal when the paper does not claim SOTA and offers a
  different contribution.
- Focusing on typos or writing polish while leaving the central claim unevaluated.
- Asking for unreasonable experiments without saying whether they are essential
  or optional.
- Harsh, sarcastic, personalized, or accusatory wording.
- Overstating certainty when major parts of the work were not checked.
