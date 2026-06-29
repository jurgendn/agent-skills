# Venue quality — tiers for *rating* (not counting) publications

Use this to judge the *strength* a publication signals in Dimension 4 (research
potential), so one strong first-author paper isn't outweighed by several
weak-venue entries. **Rate, don't count.**

Two complementary sources:

- **CORE / ICORE conference ranking** — assigns A* / A / B / C tiers to
  conferences across computing. Portal: <https://portal.core.edu.au/conf-ranks/>.
- **CSRankings selective-venue lists** — does *not* tier venues; instead it counts
  only a small, curated set of the **most selective** venues per area, precisely to
  resist gaming by volume. FAQ: <https://csrankings.org/faq.html>. Treat a venue on
  the CSRankings list for its area as top-tier regardless of its exact CORE letter.

> **Volatility / verify-live.** CORE re-rates on a multi-year cycle and individual
> placements shift between editions (and some are contested). Specific letters
> below are indicative of recent CORE editions — **confirm the current rating at
> the CORE portal** before relying on a borderline A/A* or B/A call. Tier
> *definitions* and the CSRankings *selectivity* principle are stable; exact
> per-venue letters are the volatile part.

## Tier definitions (CORE)

- **A\*** — flagship: the leading venue(s) of a field, highly selective, top
  reputation. A first-author A* paper is the strongest single output signal.
- **A** — excellent: well-regarded, selective, clearly above average.
- **B** — good/solid: reputable but not top; meaningful but not field-defining.
- **C** — recognized but modest; meets basic standards.
- *Unranked / workshop / non-archival* — counts as evidence of activity and
  involvement, **not** as a validated research result. Score as supporting, not
  lead, output in Dimension 4.

When CORE and CSRankings disagree, prefer CSRankings' selectivity judgment for the
*area's* flagships and use CORE for breadth across the long tail.

## Table of contents

- [General machine learning](#general-machine-learning)
- [Graph ML / graph learning](#graph-ml--graph-learning)
- [Computer vision](#computer-vision)
- [Natural language processing](#natural-language-processing)
- [Theory (CS theory / learning theory)](#theory-cs-theory--learning-theory)
- [Mathematics](#mathematics)
- [Cross-cutting / adjacent](#cross-cutting--adjacent)
- [How to apply in scoring](#how-to-apply-in-scoring)

## General machine learning

- **A\*** — NeurIPS, ICML, ICLR (CSRankings' core ML set; verify ICLR's current
  CORE letter, which has varied by edition).
- **A** — AISTATS, UAI, AAAI, IJCAI (AAAI/IJCAI are broad-AI A* in some editions —
  verify), COLT (also theory).
- **B** — ECML-PKDD, ACML, and solid regional/applied ML conferences.
- **Journals** — JMLR, TPAMI, TMLR (archival, rigorous review) read as A/A*-level
  signals; rate by selectivity and the work, not impact factor alone.

## Graph ML / graph learning

Graph ML usually publishes at the general-ML flagships rather than a separate
flagship, so tier by the host venue:

- **A\*** — graph-learning papers at NeurIPS / ICML / ICLR.
- **A** — LoG (Learning on Graphs; newer — verify current standing), WWW and KDD
  for graph-mining/web-graph work (both broad A* in many editions — verify),
  TheWebConf.
- **B** — specialized or regional graph/network-science venues; applied
  network-analysis conferences.
- Note: "graph neural network" work also lands in CV/NLP venues when applied —
  rate by the actual host venue's tier in that area.

## Computer vision

- **A\*** — CVPR, ICCV.
- **A** — ECCV, BMVC (verify; sometimes B), WACV (verify).
- **B** — solid regional/applied vision venues.
- **Journals** — IJCV, TPAMI read as top-tier.

## Natural language processing

- **A\*** — ACL, EMNLP (verify EMNLP's current letter; A or A* by edition).
- **A** — NAACL, EACL, COLING, Findings-of-* (Findings is selective but secondary
  to the main track — score a notch below the main venue).
- **B** — *CL workshops and regional NLP venues (supporting output).
- **Journals** — TACL, Computational Linguistics read as top-tier.

## Theory (CS theory / learning theory)

- **A\*** — STOC, FOCS, SODA.
- **A** — COLT, ITCS, ICALP, CCC.
- **B** — regional/topic theory venues.
- **Journals** — JACM, SICOMP, and for learning theory JMLR; archival journal
  versions of theory results carry strong weight.

## Mathematics

CORE covers computing, not math, and math prestige is journal-driven, not
conference-driven. Rate by **journal standing**, and verify against field norms
(e.g. MathSciNet reputation, society journals) rather than a CORE letter:

- **Top** — Annals of Mathematics, JAMS, Inventiones, Acta, Publications IHÉS.
- **Strong/specialist** — leading society and specialist journals in the subfield.
- Conference talks/proceedings are weaker signals in pure math than a journal
  acceptance; weight accordingly and verify the subfield's conventions.

## Cross-cutting / adjacent

- **Data mining / web:** KDD, WWW (A\*), CIKM, WSDM (A).
- **IR:** SIGIR (A\*), ECIR (A/B).
- **Systems/AI-systems:** MLSys (verify), OSDI/SOSP (A\* systems) when relevant.
- **HCI:** CHI, UIST (A\*) when the work is HCI-flavored.
Rate any interdisciplinary paper by the **host venue's tier in its own field**.

## How to apply in scoring

1. Identify each publication's venue and authorship role (first/lead vs. middle).
2. Look up the tier here; for any borderline or contested letter, **verify at the
   CORE portal / check the CSRankings area list** before finalizing.
3. Feed the *quality-weighted* picture into Dimension 4 anchors in
   `rubric-descriptors.md` — a single first-author A*/A result can reach the 5
   band; a stack of workshop/non-archival items does not.
4. Never present a count ("3 papers") as the signal; present tier + role + the
   independent-contribution evidence.
