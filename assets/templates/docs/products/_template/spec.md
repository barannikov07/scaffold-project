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

What the user sees. One line per screen with what it shows and what can be done there.

- 

## Permissions

Who may see and do what. Reference the roles in `infra.md`.

| Action | Allowed for | Denied for |
|---|---|---|
| | | |

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

## Rollback

What reverting the merge commit leaves behind (data, external state) and whether any of it needs
cleanup.

## Before this passes

The gate for stage 4. Claude ticks the first seven when they are true; the owner ticks the last.

- [ ] Every PRD flow has the screens and functions that serve it
- [ ] Permissions cover every action for every role
- [ ] Edge cases include the empty state and at least one failure
- [ ] Migration plan is additive only, or "none"
- [ ] Work items are independent, file-scoped, and together cover every screen and function above
- [ ] Test plan covers every success criterion in the PRD
- [ ] Rollback section is honest about data left behind
- [ ] Owner has read the plain-language sentences and said "approved"
