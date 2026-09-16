<!-- Playbook: ship. Canonical text; the .claude/skills and .codex/skills wrappers point here. -->

# Ship

Move one feature from Build through QA → Release → Close as defined in `workflow.md`. The owner
has two decisions here: accepting the feature and approving the release. Everything else is the
orchestrator's.
Calibrate every message to the owner profile in `AGENTS.md`: explain once per project, default to
less.

## 1. Verify (the orchestrator)

This is the orchestrator's job, never a builder's. If builders produced the code, their reports
are inputs, not evidence: read the diff. If the review loop in `workflow.md` ("How the agent
builds") has already used its two rounds and blockers remain, stop here and tell the owner.

On the feature branch:

- Build passes and the verify script passes.
- **Run the QA playbook** (`docs/playbooks/qa.md`) in full: functional, permissions, tripwires,
  design conformance, responsive, accessibility floor, data safety, regression, AI components.
  The run is recorded in `docs/products/<slug>/qa.md` with evidence per line. Report what was
  run and what happened, not "tests pass".
- **If the feature is risk-tagged, run the security diff checklist**
  (`docs/playbooks/security.md`) as the run's Security section.
- Every blocker fixed and its section re-run. "Later" items are roadmap lines.
- `docs/products/<slug>/guide.md` describes the feature as built, including "Where it differs
  from the plan".
- `docs/product-index.md` row, `docs/roadmap.md`, `infra.md` (if anything cross-cutting
  changed), and `docs/design/system.md` (if a token or component was added) are updated on this
  branch.
- Any migration was applied to the live database and mirrored in the schema file before this
  point.
- No secrets or real personal data in the diff. Search for key-like strings before pushing.

If anything fails, fix it and re-verify before going further.

## 2. Acceptance (owner)

The QA playbook's step 4: the PRD's success criteria as numbered steps with exact actions and
expected results, calibrated to the owner's profile. Tell the owner where to run it: localhost
for anything behind sign-in, the preview link for anything public. Set the index row to In QA.

Wait for the owner. "Accepted" moves on. A list of issues is triaged with the owner: blocker (fix
now, re-run the affected QA section, re-run acceptance) or later (one line under Later in the
roadmap). No release with an open blocker.

## 3. Release (owner approves, orchestrator executes)

Pre-flight, with evidence for each:

- Migration applied and mirrored, if any.
- Every environment variable the feature needs exists in the host's settings.
- The rollout and rollback section of the spec read once; anything it says needs cleanup is
  noted.
- For risk-tagged features: a feature flag or a staged rollout is in place, per the spec.

Push the branch, open the pull request using `.github/pull_request_template.md`, and tick only
the boxes that are true. Show the owner the checklist and ask for release approval in one
question. On "yes": merge to `main`. Do not deploy by any other means.

After the host reports the deploy done, walk the acceptance checklist's happy path on the live
site. If it fails, revert the merge commit and push, then investigate. Report faithfully.

## 4. Close (orchestrator)

- Index row: stage Live, updated date.
- Roadmap: milestone status Done with the shipped date, if this completed the milestone.
- Guide "Outcome": two or three lines on whether the success criteria were met, what was
  learned, and, for any AI step, whether it saved the time the PRD claimed.
- `docs/qa/regression.md`: append this feature's golden path.
- `docs/design/system.md` changelog row, if the feature changed the system.
- The CTO pass's debt review: anything in `docs/tech-debt.md` due by this milestone is scheduled
  as a Small change or a roadmap row; nothing is silently rolled forward.
- `/decision` for anything surprising that a future session should know.
- Ask the owner one question: does the order of the remaining milestones still hold, and does
  the vision still hold? Update the roadmap "Last reviewed" date either way.
