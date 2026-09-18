<!-- Playbook: new-feature. Canonical text; the .claude/skills and .codex/skills wrappers point here. -->

# New feature

Take one idea through Assess → PRD → Spec as defined in `workflow.md`, calling the applied-AI,
security, and CTO playbooks at their fixed points. Stop at each gate for the
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
- **Has UI**: yes or no. Yes means the PRD lists the screens, the spec designs every state, QA
  runs the screen checks, and the owner's acceptance walk is screen by screen.
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
guessing. For a feature with a screen, fill the Screens section: one line per screen in the
owner's words, what it is for and the one thing the user does there (design-system playbook,
"Describing a screen"). It is the owner's main say in how the product will look.

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

## 3. Spec

Read `infra.md` and `docs/decisions.md` first. If tech setup (milestone 0) has not shipped,
`infra.md` is still mostly placeholders: the spec then names what `infra.md` will record (schema
path, environment variable names, the provider) and says so, and `infra.md` itself is updated
when the feature or the setup ships. A living document describes what exists, never a plan.
Draft `spec.md`: data model changes (additive
only), functions, screens with every state and the real copy, composed from the design system
(design-system playbook, "Describing a screen"), permissions, AI components for any
chosen AI item, edge cases, migration plan, work items for delegation, test plan covering every
success criterion and every state in the Screens section, rollout and rollback. Open each technical section
with one plain sentence.

**If the feature is risk-tagged, run the security playbook's threat pass**
(`docs/playbooks/security.md`) and fill the spec's Security section before presenting.

**Then run the CTO pass** (`docs/playbooks/cto.md`): light unless the spec adds a table, a
service, an AI component, or a risk tag. It fills the Technical review section, records one-way
doors as decisions, and logs shortcuts in `docs/tech-debt.md`.

Present the plain sentences, the test plan, the CTO pass's two sentences (biggest risk,
simplest build), and, when present, the security summary in terms of who can see and do what. Iterate until "approved" and the checklist is ticked. Record the date,
set the index row to stage Spec, and commit to `main` (`docs(<slug>): spec`).

## 4. Hand off to build

Tell the owner what happens next: a branch `feat/<slug>`, the migration if any, the build (by you
directly if small, by builder agents from the spec's work items if not, with you reviewing, and
screen by screen against the spec's Screens section and the design system for UI features),
then `/ship` when ready. Update
`docs/product-index.md` "Updated" date. Ask whether to start building now.

## Rules

- Never edit a PRD or spec after the build has started. Corrections go in `guide.md`; a
  changed plan is a new numbered file in the same folder.
- If the PRD conflicts with the vision, offer two paths: drop or narrow the feature, or record a
  decision with `/decision` that amends the vision. Never proceed silently.
- One feature at a time through this flow.
- The specialist playbooks are not optional when their tag is set. Skipping the threat pass for a
  feature that touches money, or the state design for a feature with a screen, is a process
  failure to report, not a shortcut to take.
