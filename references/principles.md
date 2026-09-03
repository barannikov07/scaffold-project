# Why the scaffold is shaped this way

Read this once before scaffolding. It is the reasoning behind the structure, so you can explain
it to the owner in their words and fill each file with intent.

## The owner is not an engineer

Everything in the scaffold is written for someone who will read these documents to steer Claude,
not to write code themselves. That changes three things:

- The owner answers questions about the product (who, what, whether money moves). Claude turns
  those into technical choices and explains them back in one sentence each.
- The process names a human gate only where a human's judgment is genuinely needed: approving a
  PRD, accepting a feature, approving a release. Everything else Claude does.
- Rules that live only in prose get forgotten. So the process is also installed as project
  commands (`/new-feature`, `/ship`, `/status`, `/decision`) and as a pull request checklist. The
  tooling carries the discipline, not the owner's memory.

## Five principles the generated docs must obey

1. **CLAUDE.md is a router, not an encyclopedia.** It is a map with pointers, tripwires, and rules
   of the road. Every fact lives in exactly one document; everything else links to it. A
   CLAUDE.md that repeats facts drifts the moment one copy changes.
2. **Plans are frozen, guides are living.** PRDs and specs record what was decided and are never
   edited to match reality after the build. Guides carry current truth and must match reality at
   every merge. Keeping the two apart is what lets you see later where reality diverged from the
   plan, which is the most useful thing a project history can tell you.
3. **Done includes docs.** Nothing merges until the guide, product index, and roadmap reflect the
   change. It is a merge requirement, not a courtesy. Docs updated "later" are docs never updated.
4. **Tripwires over tribal knowledge.** Every hard invariant (immutable records, append-only
   integrations, privacy boundaries, money rules) gets one line in CLAUDE.md pointing to the
   owning doc. The list only grows. A fresh session reads the tripwires before touching anything.
5. **Small reversible steps.** Short-lived branches, additive migrations, one feature per pull
   request. Rollback is reverting one merge commit.

## The planning stack: four altitudes

Progress tracking fails when one document tries to hold plan, status, history, and reasoning at
once. So they are split by altitude, each owning one kind of fact:

| Altitude | Document | Owns |
|---|---|---|
| Why | `docs/vision.md` | The end state, who it serves, principles for trade-offs, non-goals |
| What, in what order | `docs/roadmap.md` | Numbered milestones with a "done when" line and a status |
| Where each piece stands | `docs/product-index.md` | One row per feature, its milestone, stage, links |
| Why it is this way | `docs/decisions.md` | Numbered, append-only decisions with reasoning |

The roadmap is one ordered table rather than Now/Next/Later lists, so shipped milestones stay in
view with their dates and total progress is visible at a glance. The first row not marked done is
"now". PRDs are written just in time, one milestone ahead at most, so later milestones stay cheap
one-liners that learnings can reshape.

The vision is a prism, not decoration. Three mechanisms make it bite: CLAUDE.md sends every
assess or PRD task to it first; every PRD has a mandatory vision-fit section; and a conflict
between a PRD and the vision is resolved by dropping the PRD or by recording a decision that
amends the vision, never by silently ignoring it.

## infra.md is the system-level living guide

It holds what is true about the system right now and crosses more than one feature: stack,
environments, identities and access, the data model at entity level, sequence diagrams for the
critical flows, external services, operations, and known gotchas. Per-feature guides hold what is
specific to one feature. Schema files hold exact columns. The decisions log holds the why. If a
section outgrows a screen it moves to its own file and infra.md keeps a pointer.

## Ceremony is sized

A full PRD and spec for a button colour change will get skipped, and once skipped once the
discipline is gone. So the assess stage sets a size, and size decides ceremony. Small changes go
straight to build with a guide update. Anything with a new screen, table, permission, or money
path takes the full path. See the size tiers in the workflow template.
