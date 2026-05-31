---
name: citation-auditor
description: Audit a paper's bibliography and inline citations for correctness — verifying papers exist, claims match what the cited paper actually says, attribution is accurate, and no citations are hallucinated or misattributed. Use whenever the user wants to check their references before submission, suspects a citation is wrong, wants to verify a specific claim is supported by the cited source, or has received a reviewer comment about incorrect citations. Also use when writing literature-heavy sections and needing to verify that a cited paper actually says what you think it says. This skill catches hallucinated titles/authors, citation telephone (claims distorted through secondary sources), missing citations on factual claims, and wrong-paper citations (citing a follow-up when the original should be cited).
---

# Citation Auditor

A citation error is not a formatting problem — it is a factual error. Citing a paper that doesn't exist, or claiming a paper says something it doesn't, undermines the credibility of the entire work.

The two most dangerous citation errors are:
1. **Hallucinated citations**: a paper that sounds plausible but doesn't exist, or exists with different authors/title/year/venue.
2. **Claim-citation mismatch**: the cited paper does not actually support the specific claim being made.

Both are common, both survive casual review, and both are caught by careful reviewers and editors.

---

## Workflow

### 1. Inventory what needs checking

Gather from the user:
- The bibliography (BibTeX, reference list, or inline citations).
- The paper text, or at minimum the sentences containing each citation.
- Any specific citations the user suspects are wrong.

If the full text is not available, focus on the bibliography entries themselves for existence checks, and ask for the specific claim sentences for claim-alignment checks.

---

### 2. Existence check (verify each paper is real)

For each entry in the bibliography, verify:

| Field | What to check |
|---|---|
| Title | Exact title matches a real paper — not a plausible paraphrase |
| Authors | Author list and order match — especially first author |
| Year | Publication year is correct |
| Venue | Conference/journal name and abbreviation are correct |
| Volume/pages | For journals: these match the actual publication |
| arXiv ID | If cited as arXiv, the ID exists and matches the paper |
| URL/DOI | If provided, resolves to the correct paper |

**Use the available search tools** (Alphaxiv MCP, web search) to look up each paper. Do not rely on memory alone — LLM training data contains hallucinated citation patterns that sound authoritative.

Flag as **unverified** any paper you cannot confirm through a direct search. Do not assume a paper exists because the title sounds reasonable.

Common hallucination patterns to watch for:
- Author names from real researchers combined with titles they didn't write.
- Real venue + plausible title + wrong year.
- Real paper title with wrong first author.
- Slightly wrong venue name (e.g., "Proceedings of NeurIPS 2020" when it was ICML).

---

### 3. Claim-citation alignment check

For each inline citation, extract the specific claim it is supposed to support and check whether the cited paper actually makes that claim.

Work through each claim-citation pair:

```
Claim: "Transformer models scale predictably with compute [Smith et al., 2020]."
→ Does Smith et al. (2020) actually report scaling laws for transformers?
→ Is this the original source of the scaling law claim, or a secondary citation?
```

Common misalignment patterns:

**Citation telephone**: Paper A introduces a result. Paper B cites A with a slight paraphrase. Paper C cites B's paraphrase as if it were A's original claim. By paper D, the claim has drifted significantly from what A actually proved. Always trace back to the original source.

**Over-broad attribution**: Citing a paper that mentions X in passing as if it established X as a result.

**Scope mismatch**: The cited paper showed X on dataset Y, but the claim says "X holds in general."

**Negative result cited as positive**: Citing a paper that actually argues against the claim, or that showed mixed results.

**Wrong paper for a well-known result**: Citing a survey or tutorial for a result that belongs to a specific original paper.

For each misalignment found, state:
- What the claim says.
- What the cited paper actually says.
- The correct citation to use (if known) or that a citation needs to be found.

---

### 4. Attribution accuracy check

For foundational or well-known results, verify the citation is to the original source:

- **Methods**: The paper that introduced the method, not a follow-up that made it famous.
- **Datasets**: The dataset paper, not a paper that happens to use the dataset.
- **Algorithms**: The original algorithmic paper, not a library or implementation.
- **Results / empirical findings**: The paper that first reported the finding, not one that replicated it.

It is acceptable to cite a later paper when it is the most accessible or clear description of the method — but the original should be cited alongside it when credit matters.

---

### 5. Missing citation check

Scan the paper text for:

- Factual claims about prior work with no citation ("Transformers outperform RNNs on language modeling").
- Numerical claims with no source ("accuracy above 90% on ImageNet").
- Named methods, datasets, or benchmarks with no citation (first mention of BERT, ImageNet, BLEU, etc.).
- "It is known that..." or "It is well established that..." — these require a citation or the hedge must be removed.

For each flagged location, note what citation is missing and suggest search terms to find it.

---

### 6. Format and consistency check

Check for:

- **Duplicate entries**: same paper cited under two different keys.
- **Inconsistent venue names**: "NeurIPS" vs. "Advances in Neural Information Processing Systems" vs. "NIPS" — pick one convention.
- **arXiv vs. published version**: if a published version exists, prefer it over the preprint. Note cases where only the arXiv version is cited but a published version is available.
- **Author name inconsistency**: same author cited as "J. Smith" in one entry and "John Smith" in another.
- **Missing required fields**: journal articles missing volume/pages, conference papers missing booktitle.

---

## Output format

```markdown
# Citation Audit Report

## Summary
- Total citations checked: [n]
- Verified: [n]
- Unverified / potentially hallucinated: [n]
- Claim-citation mismatches: [n]
- Missing citations: [n]
- Format issues: [n]

---

## Unverified or hallucinated citations

### [Key: AuthorYear]
- Claimed: [title, authors, venue, year]
- Finding: [could not verify / found different title / found different authors / etc.]
- Action: [search for correct paper / remove / replace with verified alternative]

---

## Claim-citation mismatches

### Claim: "[exact quote from paper]" [Key]
- What the cited paper actually says: [description]
- Problem: [telephone distortion / scope mismatch / wrong paper / etc.]
- Suggested fix: [correct citation / revised claim / both]

---

## Missing citations

### "[quote from paper]"
- Problem: factual claim with no citation
- Suggested search: [query terms to find the right paper]

---

## Attribution issues

### [Claim]
- Currently citing: [Key] ([secondary source / follow-up / survey])
- Should cite: [original paper — if known]

---

## Format issues

- [Key]: [specific problem and fix]

---

## Verified (no issues)
[List of keys confirmed correct — or "all remaining entries"]
```

---

## Using search tools

When verifying a citation, search in this order:

1. **Alphaxiv / arXiv search**: for ML, NLP, CV, statistics papers. Search by title, then cross-check authors and year.
2. **Web search**: for papers outside arXiv, or to find the published venue of an arXiv preprint.
3. **Semantic Scholar / Google Scholar**: for citation counts and linked metadata.

If a paper cannot be found after two independent search attempts with different query strategies, flag it as **unverified** and recommend the user locate the original source manually.

Never confirm a citation exists based on training-data familiarity alone. A confident memory of a citation is not verification.

---

## Quality bar

A clean citation audit means: every reference in the bibliography corresponds to a real, locatable paper; every inline claim is supported by what the cited paper actually demonstrates; and no factual claim goes uncited. The reader should be able to follow every citation and find exactly what the paper claims they will find.
