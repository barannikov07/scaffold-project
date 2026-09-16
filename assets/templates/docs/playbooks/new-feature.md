<!-- Playbook: new-feature. Canonical text; the .claude/skills and .codex/skills wrappers point here. -->

# New feature

Take one idea through Assess → PRD → Design → Spec as defined in `workflow.md`, calling the
applied-AI, design, and security playbooks at their fixed points. Stop at each gate for the
owner's decision. No code is written in this flow; building starts only after the spec is
approved.
Calibrate every message to the owner profile in `AGENTS.md` (see workflow.md, "How the agent
talks to the owner"): explain once per project, default to less.

## Before anything

Read, in this order: `AGENTS.md`, `docs/vision.md`, `docs/roadmap.md`, `docs/product-index.md`.
The vision is the prism for everything below; if you have not read it in this session, you
cannot assess.

## 1. Assess

Write a short assessment in the conversation, not a document:

- **Size**: Small or Full, per the tiers in `workflow.md`. If Small, skip the rest of this flow,
  say so, and go straight to building on a branch with a guide update.
- **Has UI**: yes or no. Yes means the Design stage exists for this feature.
- **Risk tags**: money, privacy, sign-in, external service, or none. Any tag means the security
  playbook runs at Spec and at QA.
- **Vision fit**: the specific vision goal or principle it advances, quoted. If nothing,
  recommend Later or Dropped and say why.
- **Depends on**: features or milestones that must exist first, including the hidden ones
  (people or records that must exist before this feature means anything).
- **Recommendation**: go now, later, or no.

Ask the owner for the decision in one question. Record it: add or update the row in
`docs/product-index.md` (stage Planned, Later, or Dropped) and, if go, add or confirm the
milestone row in `docs/roadmap.md`.

## 2. PRD

The first feature's folder already exists from the scaffold. For any later feature, create
`docs/products/<slug>/` by copying `docs/products/_template/`, replacing the `FEATURE_NAME` and
`FEATURE_SLUG` placeholders (in double braces) with the feature's name and slug in every file.
Draft `prd.md` fully, in the owner's language, using what you know from the conversation and the
vision. Paste the assessment at the top. Mark every gap as `TBD(owner): <question>` rather than
guessing.

**Then run the applied-AI pass** (`docs/playbooks/ai-native.md`) on the draft. It fills the
PRD's "AI opportunities" table with two to four proposals and a recommendation each.

Present the PRD to the owner as a draft: summarise problem, scope, non-goals, and success
criteria in a few sentences, then the AI opportunities one line each, then the open questions.
Ask for answers, the AI decisions, and approval. Fold chosen AI items into scope and flows,
deferred ones into the roadmap, rejected ones into non-goals with the reason. Iterate until the
owner says "approved" and every box in "Before this passes" is ticked. Record the approval date
in the PRD header, set the index row to stage PRD, and commit the PRD and the index change
directly to `main` (`docs(<slug>): PRD`). Plans are documents, not code; they land on `main`
before any branch exists, so the build starts from an agreed plan.

## 3. Design (only if has-UI)

Run the design playbook (`docs/playbooks/design.md`). On the first UI feature in the project it
creates the design system with the owner first. It fills `design.md`, builds the mockups, runs
the critique, and stops at the owner's mockup approval. On "approved": stage Design in the
index, commit to `main` (`docs(<slug>): design`).

## 4. Spec

Read `infra.md` and `docs/decisions.md` first. Draft `spec.md`: data model changes (additive
only), functions, screens named exactly as in `design.md`, permissions, AI components for any
chosen AI item, edge cases, migration plan, work items for delegation, test plan covering every
success criterion and every designed state, rollout and rollback. Open each technical section
with one plain sentence.

**If the feature is risk-tagged, run the security playbook's threat pass**
(`docs/playbooks/security.md`) and fill the spec's Security section before presenting.

**Then run the CTO pass** (`docs/playbooks/cto.md`): light unless the spec adds a table, a
service, an AI component, or a risk tag. It fills the Technical review section, records one-way
doors as decisions, and logs shortcuts in `docs/tech-debt.md`.

Present the plain sentences, the test plan, the CTO pass's two sentences (biggest risk,
simplest build), and, when present, the security summary in terms of who can see and do what. Iterate until "approved" and the checklist is ticked. Record the date,
set the index row to stage Spec, and commit to `main` (`docs(<slug>): spec`).

## 5. Hand off to build

Tell the owner what happens next: a branch `feat/<slug>`, the migration if any, the build (by you
directly if small, by builder agents from the spec's work items if not, with you reviewing, and
screen by screen against the mockups for UI features), then `/ship` when ready. Update
`docs/product-index.md` "Updated" date. Ask whether to start building now.

## Rules

- Never edit a PRD, design, or spec after the build has started. Corrections go in `guide.md`; a
  changed plan is a new numbered file in the same folder.
- If the PRD conflicts with the vision, offer two paths: drop or narrow the feature, or record a
  decision with `/decision` that amends the vision. Never proceed silently.
- One feature at a time through this flow.
- The specialist playbooks are not optional when their tag is set. Skipping design for a feature
  with a screen, or the threat pass for a feature that touches money, is a process failure to
  report, not a shortcut to take.
