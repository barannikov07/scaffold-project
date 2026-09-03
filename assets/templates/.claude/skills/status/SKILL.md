---
name: status
description: Report where the project stands: milestones done and remaining, what is in progress and at which stage, what is next, open questions marked TBD, and anything blocked on the owner. Use whenever the owner asks "where are we", "what's the status", "what's next", "what's left", "how far along are we", or opens a session wanting orientation.
---

# Status

Produce a short spoken summary from the documents. Store nothing; the documents are the source
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
