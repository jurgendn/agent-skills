# Venue conventions (reference)

Workspace-local crib sheet for submission norms. This is a *starting* checklist, not a substitute for the call-for-papers — always read the target venue's CFP and formatting instructions, which override anything here. Use the `venue-targeting` skill to choose and prioritise venues.

## Things that vary by venue — confirm each from the CFP

- **Page limit** and whether references/appendix count toward it.
- **Anonymisation** (double-blind vs single-blind): no author names, no self-identifying "our prior work [12]" phrasing, anonymised repo links.
- **Template** (LaTeX style file / Word template) and font/margin rules.
- **Supplementary material** policy and size limits.
- **Reproducibility / ethics / broader-impact** statements — increasingly mandatory; see `reproducibility-checklist.md`.
- **Dual submission / preprint (arXiv)** policy and embargo windows.
- **Abstract registration** deadline (often a week before the full deadline).

## Rough archetypes (verify before relying on them)

- **ML conferences** (NeurIPS / ICML / ICLR): 8–10 pages + unlimited references, double-blind, mandatory reproducibility checklist, supplementary allowed.
- **NLP conferences** (ACL / EMNLP, ARR): fixed page count, responsible-NLP / limitations section required, ARR review cycle.
- **Vision** (CVPR / ICCV / ECCV): strict page limit, double-blind, supplementary PDF/video.
- **Journals** (JMLR / TPAMI / TMLR): no hard page limit, rolling or longer review, revision rounds rather than a single rebuttal.

## Pre-submission gate

Run `submission-readiness-audit` and `citation-auditor`. Record the chosen venue, deadline, and checklist state in `submission/`.
