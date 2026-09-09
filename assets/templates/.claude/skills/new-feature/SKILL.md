---
name: new-feature
description: Start a new feature or product the right way: assess it against the vision, then draft the PRD and the spec stage by stage with the owner's approval at each gate. Use whenever the owner wants to build, add, or plan something new, says "let's build X", "I want a feature that...", "start on X", or asks for a PRD or spec, even if they do not say "new feature".
---

# New feature

Take one idea through Assess → PRD → Spec as defined in `workflow.md`. Stop at each gate for the
owner's decision. Do not write code in this flow; building starts only after the spec is approved.

## Before anything

Read, in this order: `CLAUDE.md`, `docs/vision.md`, `docs/roadmap.md`, `docs/product-index.md`.
Calibrate every message to the owner profile in `CLAUDE.md` (see workflow.md, "How Claude
talks to the owner"): explain once per project, default to less.
The vision is the prism for everything below; if you have not read it in this session, you cannot
assess.

## 1. Assess

Write a short assessment in the conversation, not a document:

- **Size**: Small or Full, per the tiers in `workflow.md`. If Small, skip the rest of this flow,
  say so, and go straight to building on a branch with a guide update.
- **Risk tags**: money, privacy, data loss, external service, or none.
- **Vision fit**: the specific vision goal or principle it advances, quoted. If nothing,
  recommend Later or Dropped and say why.
- **Depends on**: features or milestones that must exist first.
- **Recommendation**: go now, later, or no.

Ask the owner for the decision in one question. Record it: add or update the row in
`docs/product-index.md` (stage Planned, Later, or Dropped) and, if go, add or confirm the
milestone row in `docs/roadmap.md`.

## 2. PRD

The first feature's folder already exists from the scaffold. For any later feature, create
`docs/products/<slug>/` by copying `docs/products/_template/`, replacing the `FEATURE_NAME` and `FEATURE_SLUG` placeholders (in double braces) with the
feature's name and slug in all three files. Draft `prd.md` fully, in the owner's language, using what you know from the conversation
and the vision. Paste the assessment at the top. Mark every gap as `TBD(owner): <question>`
rather than guessing.

Then present it to the owner as a draft: summarise problem, scope, non-goals, and success
criteria in a few sentences, list the open questions, and ask for answers and approval. Iterate
until the owner says "approved" and every box in "Before this passes" is ticked. Record the
approval date in the PRD header, set the index row to stage PRD, and commit the PRD and the
index change directly to `main` (`docs(<slug>): PRD`). Plans are documents, not code; they land on
`main` before any branch exists, so the build starts from an agreed plan.

## 3. Spec

Read `infra.md` and `docs/decisions.md` first. Draft `spec.md`: data model changes (additive
only), functions, screens, permissions, edge cases, migration plan, work items for delegation,
test plan covering every success criterion, rollback. Open each technical section with one plain sentence.

Present the plain sentences and the test plan to the owner; the technical tables are for
you. Iterate until "approved" and the checklist is ticked. Record the date, set the index row to
stage Spec, and commit to `main` (`docs(<slug>): spec`).

## 4. Hand off to build

Tell the owner what happens next: a branch `feat/<slug>`, the migration if any, the build (by
you directly if small, by builder agents from the spec's work items if not, with you reviewing),
then `/ship` when ready. Update `docs/product-index.md` "Updated" date. Ask whether to start building
now.

## Rules

- Never edit a PRD or spec after the build has started. Corrections go in `guide.md`; a changed
  plan is a new numbered PRD in the same folder.
- If the PRD conflicts with the vision, offer two paths: drop or narrow the feature, or record a
  decision with `/decision` that amends the vision. Never proceed silently.
- One feature at a time through this flow.
