---
name: flow-phd-application
description: >-
  Orchestrate a complete PhD / research-program application package end-to-end — from reading the applicant's materials through CV, program & faculty fit, SOP, recommender strategy, professor outreach, and a final package audit. Use whenever the user wants to drive the whole application rather than one piece: "help me with my PhD applications", "where do I start with my application", "manage my application process", "I'm applying to PhD programs, what's the plan", "get my materials ready", or hands over a folder of CV/transcripts/notes and asks for the path to submission. This is a ROUTER that sequences existing singleton skills with stage gates; it does not write the SOP, CV, or emails itself. For a single piece, invoke that skill directly (e.g. apply-sop-writer, apply-cv-builder). For driving a research paper use flow-paper-lifecycle.
---

# PhD Application Orchestrator

Drive a research-program application from raw materials to a submission-ready, internally consistent package. The job is to know **which piece comes next, what depends on what, and which singleton to hand to** — gating so later pieces build on a settled foundation (no SOP before fit is mapped; no submission before the package is audited for consistency). This file owns sequencing and gates only; it never writes the CV, SOP, or emails itself.

For one isolated piece, skip the orchestrator and invoke that skill directly. Use this when the user wants the *whole package* managed.

## Before You Start: Locate the Applicant

Ask only what you can't infer. You need:
- **Where they are** — just starting, has a CV, has a draft SOP, mid-cycle, etc. Sets the entry stage.
- **Materials on hand** — CV, transcripts, research writeups, publication list, target schools. If these exist, stage 1 ingests them; if not, note the gaps.
- **Targets & timeline** — fields/programs of interest and deadlines. Drives shortlisting and pacing.

If motivation or direction is wobbly (the "should I even do a PhD" layer), route to `apply-motivation-keeper` before the package work — a package built on an unclear why reads hollow.

## The Pipeline

Run in order; **enter at the applicant's actual stage** and resume from the last unmet gate. The early stages produce a reusable profile that every later piece draws on, so the order matters.

```text
1 Read the profile → 2 Build the CV → 3 Map program & faculty fit
→ 4 Write the SOP → 5 Plan recommenders → 6 Professor outreach
→ 7 Audit the package
```

**Conditional route (not in the linear order):** for a graded scorecard, a
cross-border **eligibility** verdict, or **scholarship**-mission fit
(VEF/DAAD/Fulbright/Erasmus/MSCA), hand to `apply-dossier-evaluator` — see Router
Rules. Check eligibility *early* (before stage 4) when a degree-equivalence
question exists, since an "ineligible as-is" verdict reshapes the whole plan.

### Stage 1 — Read the profile → `apply-profile-reader`
Ingest CV, transcripts, research statements, project writeups, publication list, GitHub, target-school materials into one reusable structured profile. **Everything downstream reads from this** — do it first.
**Gate:** a structured profile exists capturing background, research experience, and targets.

### Stage 2 — Build the CV → `apply-cv-builder`
Turn the profile into a research-oriented academic CV; surface missing evidence of research readiness while it can still be addressed.
**Gate:** a research-framed CV exists; gaps in research evidence are named.

### Stage 3 — Map program & faculty fit → `apply-program-fit-mapper`
Convert interests into searchable research themes; shortlist programs and identify specific faculty/labs with fit evidence and per-school fit notes.
**Gate:** a shortlist with named faculty and concrete fit evidence per target. **The SOP depends on this.**

### Stage 4 — Write the SOP → `apply-sop-writer`
Draft/critique the Statement of Purpose, connecting prior work → future direction → program fit, using the stage-3 fit notes per school.
*Optional reader's-eye pass:* once a draft exists, hand it to `professor-critic` with the named reader "an admissions reader skimming 200 SOPs" and the bar "shortlist / discard" — a verdict the author-side drafter doesn't give.
**Gate:** an SOP whose research narrative and program-fit paragraphs are grounded in the fit map, not generic.

### Stage 5 — Plan recommenders → `apply-recommendation-letter-strategist`
Decide who should write, what each letter should emphasize, and assemble the recommender packet so letters complement (not echo) the SOP.
**Gate:** recommenders chosen with a per-letter emphasis plan and packet materials.

### Stage 6 — Professor outreach → `apply-cold-email-drafter`
Where appropriate, draft concise cold emails to prospective advisors, converting stage-3 fit notes into specific, non-generic outreach.
*Optional reader's-eye pass:* before sending, hand the email to `professor-critic` with the named reader "a busy PI triaging a full inbox" and the bar "reply / delete" — it predicts whether the email actually earns a response.
**Gate:** outreach emails drafted and tied to real fit evidence (skip if the programs don't expect pre-application contact).

### Stage 7 — Audit the package → `apply-package-auditor`
Check the assembled package for completeness, internal consistency (CV ↔ SOP ↔ letters tell one coherent story), and per-program requirements before submission.
**Gate:** the package passes a consistency-and-completeness audit for each target program.
For a *scored* read of the same package — per-dimension 1–5, tier, and the highest-leverage gap — also run the conditional route `apply-dossier-evaluator` (the auditor checks coherence; the evaluator assigns numbers).

## Router Rules

- **Delegate, don't duplicate.** Each stage hands to a singleton; this file owns sequencing and gates.
- **Profile first, always.** Stage 1 feeds everything; don't draft pieces from scratch when a structured profile would unify them.
- **Hard dependency: fit before SOP.** No SOP drafting (4) until the fit map (3) exists — a generic SOP is the most common failure.
- **Resume, don't restart.** Enter at the applicant's real stage; reuse the profile across cycles and schools.
- **Per-school, not one-size.** Stages 3–7 vary by target program; the audit (7) is per-program.
- **Motivation underneath.** If the "why" is unstable, route to `apply-motivation-keeper` before or alongside the package work.
- **Score, eligibility & scholarships → `apply-dossier-evaluator`.** Conditional, not a linear stage: route here when the user wants a graded scorecard, a cross-border eligibility verdict (e.g. a 4-year BSc against a master's-required EU PhD — check *early*, before stage 4), or scholarship-mission fit (VEF/DAAD/Fulbright/Erasmus/MSCA). Re-score before stage 7 to surface the highest-leverage gaps. Always verify cutoffs/limits/deadlines against the live official call.
