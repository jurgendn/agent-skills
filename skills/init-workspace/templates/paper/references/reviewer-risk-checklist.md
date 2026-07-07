# Reviewer-risk checklist

Use this author-facing checklist before submission and during major revisions.
It translates common OpenReview-era reviewer expectations into paper risks to
fix before real reviewers find them.

This is not a venue policy file. For a named venue, also check the current author
and reviewer guides.

## Claim and contribution risk

- [ ] The central claim is stated in one sentence and is falsifiable.
- [ ] Each major claim points to a specific figure, table, proof, experiment, or
      citation.
- [ ] Conclusions do not exceed the tested setting, theorem assumptions, or
      available evidence.
- [ ] The contribution type is clear: method, theory, dataset, benchmark,
      empirical finding, analysis, position paper, or resource.
- [ ] The paper does not rely on "SOTA" unless the protocol and baselines really
      support a SOTA claim.

## Novelty and related-work risk

- [ ] The closest prior work is named, not vaguely gestured at.
- [ ] The delta over prior work is explicit: what is new, what is reused, and
      what remains the same.
- [ ] Any "not previously studied" or "first" claim has been checked against the
      literature.
- [ ] Missing citations are not being used as a substitute for missing novelty.
- [ ] Factual claims about prior work are supported by sources that actually say
      what the paper claims.

## Evidence and evaluation risk

- [ ] The minimal strong baseline set is present: lower bound, strong incumbent,
      closest prior method, and self-ablation where relevant.
- [ ] Every baseline is fairly tuned under a comparable protocol.
- [ ] Metrics match the claim type: accuracy, efficiency, robustness,
      generalization, calibration, fairness, interpretability, or cost.
- [ ] Ablations isolate the claimed mechanism rather than decorating the table.
- [ ] Statistical uncertainty is reported where small differences matter.
- [ ] Failure modes, slices, or negative cases are described when averages hide
      important behavior.

## Reproducibility and artifact risk

- [ ] Data source, version, split, preprocessing, and filtering are specified.
- [ ] Seeds, configs, hyperparameters, hardware assumptions, and tuning budgets
      are recorded.
- [ ] Main paper numbers map to experiment notes and reproducible commands.
- [ ] Code, data, models, or supplementary artifacts are anonymized when required
      and attributed/licensed when disclosed.
- [ ] "Code available" is not treated as equivalent to "main result
      reproducible."

## Ethics, limitations, and data risk

- [ ] Limitations state scope and generalizability boundaries honestly.
- [ ] Societal impact or ethics discussion covers who benefits, who may be
      harmed, and what happens under failure.
- [ ] Personal data, human-subjects data, consent, IRB/equivalent approval, and
      privacy are handled if relevant.
- [ ] Dataset, model, and code assets are cited like research contributions, not
      treated as infrastructure with no attribution.
- [ ] Dual-use, bias, safety, exclusion, or misuse concerns are flagged rather
      than hidden.

## Rebuttal readiness

- [ ] The likely top 3 reviewer objections are written down.
- [ ] For each objection, the paper already contains the best available answer or
      a clear limitation.
- [ ] The authors can say what evidence would change the claim, score, or
      interpretation.
- [ ] Optional improvements are separated from decision-critical gaps.
- [ ] The paper can be defended without inventing new claims during rebuttal.
