<!-- Playbook: status. Canonical text; the .claude/skills and .codex/skills wrappers point here. -->

# Status

Produce a short spoken summary from the documents. Store nothing; the documents are the source
of truth and this command only reads them.
Calibrate every message to the owner profile in `AGENTS.md`: explain once per project, default to
less.

Read `docs/roadmap.md`, `docs/product-index.md`, and search every document for `TBD(`.

Report, in this order, in plain language:

1. **Progress**: milestones done out of total, with the shipped dates of the last one or two.
2. **Now**: the milestone in progress and each of its features with its stage (Idea, Planned,
   PRD, Design, Spec, In build, In QA, Live).
3. **Waiting on the owner**: anything at a gate that needs their decision (PRD approval, mockup
   approval, acceptance, release approval), and every `TBD(owner):` line with its file.
4. **Next**: the next one or two milestones in roadmap order.
5. **Drift check**: any disagreement between index, roadmap, guides, and the regression list that
   you noticed (a row marked Live with no shipped date, a Live feature with no golden path, a
   guide that says "nothing yet" for a Live feature). Offer to fix it in one change.

Keep it under two hundred words unless the owner asks for detail.
