# Spec: {{FEATURE_NAME}}

Status: Draft · Approved on: not yet · Build started on: not yet
PRD: [prd.md](prd.md) · Design system: [../../design/system.md](../../design/system.md)

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

What the user sees, composed from the design system. Screen names are the contract; the build
and the QA run use them verbatim. Features without a screen write "none".

| Screen | Purpose | How the user gets there | Primary action |
|---|---|---|---|
| | | | |

### States

Every screen, every state. A state not listed here will be improvised in code.

| Screen | Empty | Loading | Error | Success | Denied | AI: thinking / correct-me / fallback |
|---|---|---|---|---|---|---|
| | | | | | | n/a |

### Copy

The real words, in the design system's tone: titles, buttons, empty-state lines, error messages.
No placeholder text.

| Where | Text |
|---|---|
| | |

### Responsive and accessible

Phone first at 390 px; what changes at desktop width. Focus order, labels, 44 px touch targets,
contrast against the floor in the design system.

- 

### Components

Everything above is composed from `docs/design/system.md`. Anything a screen needs that the
system lacks is listed here and added to the system, in the app and in its Components table,
before the screen uses it.

| Needed by | Component or token | Added to the system on |
|---|---|---|
| | | |

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

Evaluation set: ten real examples with expected outputs. Before there are users, ten written
ones in the users' voice (including one adversarial and one that is not the thing at all), with a
Close item to replace them with real ones from the first weeks.

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

## Technical review

Filled by the CTO pass (`docs/playbooks/cto.md`) after the draft, before approval. Light (three
sentences) when nothing below applies; the full table when the spec adds a table, an external
service, an AI component, or carries a risk tag. "Fine" is a valid answer for a row; an invented
concern is not.

| Check | Finding |
|---|---|
| Fit | |
| Data | |
| Contracts | |
| Scale and cost | |
| Reliability | |
| Observability | |
| Simplicity | |
| One-way doors | none, or decision IDs |
| Debt | none, or rows added to docs/tech-debt.md |

## Before this passes

The gate for stage 4. The agent ticks every box but the last two when they are true; the owner
ticks the last two.

- [ ] Every PRD flow has the screens and functions that serve it
- [ ] Every screen has its states and its real copy, and anything the design system lacks is listed under Components (features with a screen)
- [ ] Every AI component has a fallback, a confirmation point wherever a tripwire applies, and an evaluation set (features with AI)
- [ ] Security section complete and every denial has an enforcing rule (risk-tagged features)
- [ ] Permissions cover every action for every role
- [ ] Edge cases include the empty state and at least one failure
- [ ] Migration plan is additive only, or "none"
- [ ] Work items are independent, file-scoped, and together cover every screen and function above
- [ ] Test plan covers every success criterion in the PRD
- [ ] Rollout and rollback section is honest about how it goes live and what is left behind
- [ ] Technical review done; every one-way door is a decision entry; shortcuts are in docs/tech-debt.md
- [ ] Every `TBD(owner)` in this spec is answered, and the answer is written where the question was
- [ ] Owner has read the plain-language sentences and said "approved"
