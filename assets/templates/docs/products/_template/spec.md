# Spec: {{FEATURE_NAME}}

Status: Draft · Approved on: not yet · Build started on: not yet
PRD: [prd.md](prd.md)

A spec says how the feature will be built. Written after the PRD is approved, before any code.
Once the build starts it is a record and is not edited. Each technical section opens with one plain sentence for the owner.

## Data model changes

What the system will start remembering. Additive only: new tables, new nullable columns, new
indexes. Nothing renamed or dropped here.

| Entity / table | Change | Why |
|---|---|---|
| | | |

Update `infra.md` Data model when this ships.

## Functions and endpoints

What the app does behind the screens.

| Name | Input | Output | Who may call it |
|---|---|---|---|
| | | | |

## Screens

What the user sees. One row per screen, named exactly as in `design.md`; the mockup is the
contract for how it looks. Features without a screen write "none".

- 

## Permissions

Who may see and do what. Reference the roles in `infra.md`.

| Action | Allowed for | Denied for |
|---|---|---|
| | | |

## AI components

Write "none" if no AI opportunity was chosen. Otherwise one row per component, plus the
evaluation set that QA will run.

| Component | Input | Output | Model tier | Latency class | Cost per use | Data leaves the app to | Fallback | A person confirms |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Evaluation set: ten real examples with expected outputs.

1. 

## Security

Write "not risk-tagged" if the assessment set no risk tag. Otherwise filled by the security
playbook's threat pass: data classification, denied actions, the rules that enforce them, input
surfaces, abuse cases, external services, logging.

## Edge cases

What could go wrong and what happens then. Empty states, bad input, double submits, lost
connection, permission failures.

- 

## Migration plan

Leave "none" if the data model does not change. Otherwise: the script name, what it adds, why it
is safe to run twice, and confirmation that it is applied before the code merges.

none

## Work items

How the build is split for delegation (see `workflow.md`, "How Claude builds"). Each item is
independent, names the files it may touch, the contract it must satisfy, and how to know it is
done. Three files or fewer in total: one item, built by the orchestrator.

| # | Item | Files it may touch | Contract | Done when |
|---|---|---|---|---|
| 1 | | | | |

## Test plan

Every line is executed on localhost before push. Written so a person could follow it.

1. 

## Rollout and rollback

How it goes live: to everyone at once, behind a feature flag, or staged (which users first).
Risk-tagged features need a flag or a stage. Then: what reverting the merge commit leaves behind
(data, external state) and whether any of it needs cleanup.

## Before this passes

The gate for stage 5. The agent ticks every box but the last when they are true; the owner
ticks the last.

- [ ] Every PRD flow has the screens and functions that serve it
- [ ] Screens are named exactly as in design.md (features with a screen)
- [ ] Every AI component has a fallback, a confirmation point wherever a tripwire applies, and an evaluation set (features with AI)
- [ ] Security section complete and every denial has an enforcing rule (risk-tagged features)
- [ ] Permissions cover every action for every role
- [ ] Edge cases include the empty state and at least one failure
- [ ] Migration plan is additive only, or "none"
- [ ] Work items are independent, file-scoped, and together cover every screen and function above
- [ ] Test plan covers every success criterion in the PRD
- [ ] Rollout and rollback section is honest about how it goes live and what is left behind
- [ ] Owner has read the plain-language sentences and said "approved"
