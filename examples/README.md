# Examples

## ChoirHub

A community-choir app, run through the skill with no human in the loop (every gate answered
"yes" or with the answers a plausible owner would give). It is left exactly where a real project
would pause for its owner: the spec is drafted and waiting for approval.

What to read, in order:

1. [`choirhub/CONVERSATION.md`](choirhub/CONVERSATION.md): everything the owner would have seen,
   from "start a new project" to the spec presentation.
2. [`choirhub/AGENTS.md`](choirhub/AGENTS.md): the router, with four tripwires that came straight
   out of the interview and the security pass.
3. [`choirhub/docs/vision.md`](choirhub/docs/vision.md), [`docs/roadmap.md`](choirhub/docs/roadmap.md),
   [`docs/product-index.md`](choirhub/docs/product-index.md), [`docs/decisions.md`](choirhub/docs/decisions.md):
   the planning stack at four altitudes.
4. [`choirhub/docs/products/rehearsals-and-replies/prd.md`](choirhub/docs/products/rehearsals-and-replies/prd.md):
   the PRD, with the applied-AI pass's four proposals and what was decided about each.
5. [`choirhub/docs/design/system.md`](choirhub/docs/design/system.md) and
   [`docs/products/rehearsals-and-replies/design.md`](choirhub/docs/products/rehearsals-and-replies/design.md):
   the design system created from five questions, and the feature's screens, states, and copy.
   Open `docs/products/rehearsals-and-replies/mockups/index.html` in a browser for the mockups.
6. [`choirhub/docs/products/rehearsals-and-replies/spec.md`](choirhub/docs/products/rehearsals-and-replies/spec.md):
   the spec, with the AI component and its evaluation set, the security threat pass (including the
   inference leak it found), and the CTO pass's technical review. Two one-way doors became
   decisions; two shortcuts went into [`docs/tech-debt.md`](choirhub/docs/tech-debt.md).

The three open `TBD(owner)` questions at the end of the spec are real: the spec found
contradictions between the approved PRD, the approved design, and `infra.md`, and raised them
instead of resolving them silently. That is the process working.

Generated 2026-09-16 with the skill at that date. Later versions of the skill may stamp slightly
different templates.
