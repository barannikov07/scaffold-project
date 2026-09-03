---
name: ship
description: Take a built feature through QA, release, and close: verify locally, produce the owner's acceptance checklist, open the pull request with the merge checklist ticked, merge on approval, check production, and update the index, roadmap, and guide. Use whenever the owner says "ship it", "release", "deploy", "merge", "is it ready", "let's go live", or asks to finish a feature.
---

# Ship

Move one feature from Build through QA → Release → Close as defined in `workflow.md`. The owner
has two decisions here: accepting the feature and approving the release. Everything else is yours.

## 1. Verify (the orchestrator)

This is the orchestrator's job, never a builder's. If builders produced the code, their reports
are inputs, not evidence: read the diff. If the review loop in `workflow.md` ("How Claude
builds") has already used its two rounds and blockers remain, stop here and tell the owner.

On the feature branch:

- Build passes and the verify script passes.
- Every line of the spec's test plan is executed on localhost. Report what was run and what
  happened, not "tests pass".
- `docs/products/<slug>/guide.md` describes the feature as built, including "Where it differs
  from the plan".
- `docs/product-index.md` row, `docs/roadmap.md`, and `infra.md` (if anything cross-cutting
  changed) are updated on this branch.
- Any migration was applied to the live database and mirrored in the schema file before this point.
- No secrets or real personal data in the diff. Search for key-like strings before pushing.

If anything fails, fix it and re-verify before going further.

## 2. Acceptance (owner)

Turn the PRD's success criteria into a numbered checklist with exact steps: where to click, what
to type, what should appear. Tell the owner where to run it: localhost for anything behind
sign-in, the preview link for anything public. Set the index row to In QA.

Wait for the owner. "Accepted" moves on. A list of issues is triaged with the owner: blocker
(fix now, re-run acceptance) or later (one line under Later in the roadmap). No release with an
open blocker.

## 3. Release (owner approves, Claude executes)

Push the branch, open the pull request using `.github/pull_request_template.md`, and tick only
the boxes that are true. Show the owner the checklist and ask for release approval in one
question. On "yes": merge to `main`. Do not deploy by any other means.

After the host reports the deploy done, walk the acceptance checklist's happy path on the live
site. If it fails, revert the merge commit and push, then investigate. Report faithfully.

## 4. Close (Claude)

- Index row: stage Live, updated date.
- Roadmap: milestone status Done with the shipped date, if this completed the milestone.
- Guide "Outcome": two or three lines on whether the success criteria were met and what was
  learned.
- `/decision` for anything surprising that a future session should know.
- Ask the owner one question: does the order of the remaining milestones still hold, and does the
  vision still hold? Update the roadmap "Last reviewed" date either way.
