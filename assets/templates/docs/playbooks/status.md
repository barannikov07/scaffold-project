<!-- Playbook: status. Canonical text; the .claude/skills and .codex/skills wrappers point here. -->

# Status

Produce a short spoken summary from the documents.
Calibrate every message to the owner profile in `AGENTS.md` (see workflow.md, "How Claude
talks to the owner"): explain once per project, default to less. Store nothing; the documents are the source
of truth and this command only reads them.

Read `docs/roadmap.md`, `docs/product-index.md`, and search every document for `TBD(`.

Report, in this order, in plain language:

1. **Progress**: milestones done out of total, with the shipped dates of the last one or two.
2. **Now**: the milestone in progress and each of its features with its stage.
3. **Waiting on the owner**: anything at a gate that needs their decision (PRD approval,
   acceptance, release approval), and every `TBD(owner):` line with its file.
4. **Next**: the next one or two milestones in roadmap order.
5. **Drift check**: any disagreement between index, roadmap, and guides that you noticed (a row
   marked Live with no shipped date, a guide that says "nothing yet" for a Live feature). Offer to
   fix it in one change.

Keep it under two hundred words unless the owner asks for detail.
