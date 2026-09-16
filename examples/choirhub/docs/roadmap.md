# Roadmap: ChoirHub

The plan, in order. One row per milestone; order is priority; the first row not marked Done is
what we are working on now. Shipped rows stay with their dates so progress is visible at a glance.
PRDs are written one milestone ahead at most, so later rows are cheap one-liners that can change.

Last reviewed: 2026-09-16

## Current focus

Milestone 0 comes first because nothing can ship until the project exists, deploys to Vercel, and
can be tested: it is plumbing, not product. Then milestone 1, rehearsals and replies, because it
is the smallest thing you can actually use on a Tuesday, and it is the part that removes the job
you called the most tedious: counting replies in WhatsApp and chasing the people who never
answered. Everything else in the vision (the register, the fees, the drift signal) needs the
rehearsal to exist first, so it waits.

## Milestones

| # | Milestone | Done when | Status | Features | Shipped |
|---|---|---|---|---|---|
| 0 | Tech setup | The app runs locally and on Vercel, test login and seed data exist, verify script passes | Planned | [tech-setup](products/tech-setup/checklist.md) | |
| 1 | Rehearsals and replies | A rehearsal exists in the app with its date, place and songs, every singer has answered coming or not coming, and the conductor sees the full list before the night without asking anyone | Planned | [rehearsals-and-replies](products/rehearsals-and-replies/prd.md) | |
| 2 | Attendance record | Who actually turned up is recorded during the rehearsal and cannot be changed afterwards | Later | | |
| 3 | Membership fees | A singer pays their term fee in the app and the conductor sees who has paid without a spreadsheet | Later | | |
| 4 | Drift signal | The conductor is shown which singers have stopped coming, with the evidence, while there is still time to keep them | Later | | |

Status values: Later · Planned · In progress · Done · Dropped

## Later (unordered ideas)

One line each. Promote to a numbered row when it is assessed.

- Section leader role: a singer who can see and chase their own section, and nothing else.
- What to prepare: parts, notes or a link attached to each song on a rehearsal.
- Draft the nudge for the singers who have not answered, ready to send or copy into WhatsApp. Deferred from the [rehearsals and replies PRD](products/rehearsals-and-replies/prd.md); it needs a way to deliver a message, which milestone 1 deliberately does not have.
- Pre-fill a new rehearsal from the last few: same night, same time, same place. Deferred from the [rehearsals and replies PRD](products/rehearsals-and-replies/prd.md); it needs a few rehearsals to learn from.

## Changes

Reorders, drops, and additions, newest first, each linked to its decision.

| Date | Change | Decision |
|---|---|---|
| 2026-09-16 | Roadmap created with milestones 0 and 1; milestones 2 to 4 added as Later from the end state in the vision | D-002 |
