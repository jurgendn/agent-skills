# Research immersion strategy

Use this when the task is not "find papers on X" but "get up to speed on X"
or "enter this unfamiliar research area." The goal is a working mental map
without drowning in the paper flood.

Grounding:
- Mysore et al., *How Data Scientists Review the Scholarly Literature*,
  arXiv:2301.03774.
- Baltes and Ralph, *Teaching Literature Reviewing for Software Engineering
  Research*, arXiv:2406.08369.
- Zheng et al., *DiscipLink: Unfolding Interdisciplinary Information Seeking
  Process via Human-AI Co-Exploration*, arXiv:2408.00447.
- Li et al., *A Survey Forest Diagram*, arXiv:2407.17081.
- Zou et al., *Real Deep Research for AI, Robotics and Beyond*,
  arXiv:2510.20809.
- Salatino et al., *A Survey on Knowledge Organization Systems of Research
  Fields*, arXiv:2409.04432.
- Iyer et al., *pathfinder: A Semantic Framework for Literature Review and
  Knowledge Discovery in Astronomy*, arXiv:2408.01556.
- Kreutz and Schenkel, *Scientific Paper Recommendation Systems*,
  arXiv:2201.00682.
- Agarwal et al., *LitLLM*, arXiv:2402.01788.

## Start exploratory, become systematic later

Do not begin a new field with a full systematic literature review unless the
user explicitly needs one. Early onboarding needs orientation, vocabulary,
and candidate clusters; formal inclusion/exclusion criteria are more useful
after the researcher knows what the clusters are.

Practical sequence:
1. Seed with 2-4 survey/canonical papers and one recent paper.
2. Extract vocabulary, benchmark names, dataset names, and recurring authors.
3. Search outward with multiple query families, including synonyms from adjacent
   disciplines.
4. Build a provisional map of method families and disagreements.
5. Only then decide whether a systematic review protocol is warranted.

## Escape disciplinary bubbles

Data scientists and interdisciplinary researchers often miss relevant work
because the same idea has different names across communities. For unfamiliar
or cross-field topics:
- search the problem name, not just the method name;
- ask which neighboring disciplines would care about the same phenomenon;
- translate terms across communities before declaring "no prior work";
- record query terms that failed, because failed searches show boundary lines.

## Use surveys, forest diagrams, and recommenders as maps, not evidence

Survey papers and visual maps are useful for orientation but clean up the messy
history. They can hide dead ends, disputes, weak replications, and changes in
benchmark practice. Use them to choose where to read, then verify load-bearing
claims in the original papers.

Knowledge organization systems (taxonomies, thesauri, ontologies, field
classification schemes) are also maps, not ground truth. Use them to discover
subareas, terms, venues, and neighboring fields, but check whether the taxonomy
is current, field-specific, and aligned with the user's question. A field's
official categories often lag emerging work and can hide interdisciplinary edges.

Recommendation systems and LLM literature tools are accelerators, not judges.
They can reinforce citation centrality, miss fringe or new work, and homogenize
related-work narratives. Counteract that by:
- running at least one keyword search outside the recommended cluster;
- following negative or critical citations;
- checking recent workshop/preprint work in fast fields;
- marking any tool-suggested synthesis as inferred until primary papers support it.

For semantic-search tools, log the query framing and retrieval bias explicitly.
Natural-language search can bridge jargon gaps, but it also smuggles in the
user's framing. Run at least one alternate framing: problem-first, method-first,
benchmark/dataset-first, and one adjacent-discipline vocabulary pass.

## Control breadth-depth tradeoff

Breadth-first mapping prevents early rabbit holes, but too much breadth produces
shallow familiarity. After the provisional map exists, force depth:
- choose 1-2 load-bearing papers per method family;
- read method/experiment/proof sections, not just abstracts and intros;
- reproduce a key derivation, table interpretation, or experimental contrast;
- write what would falsify the central claim.

For very fast fields, include the search date and assume anything older than
12 months may need a freshness check before being treated as current.
