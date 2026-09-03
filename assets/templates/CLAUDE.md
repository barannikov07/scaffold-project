# {{PROJECT_NAME}}

{{PURPOSE}}

This file is a map, not a manual. Every fact lives in exactly one document and this file only
points to it. If you are about to add detail here, it belongs in one of the documents below.

## Where things live

| Question | Document |
|---|---|
| What are we building and why? What is the end state? | [docs/vision.md](docs/vision.md) |
| What is the plan, in what order, and what has shipped? | [docs/roadmap.md](docs/roadmap.md) |
| Where does each feature stand right now? | [docs/product-index.md](docs/product-index.md) |
| Why is it this way? What did we decide and reject? | [docs/decisions.md](docs/decisions.md) |
| How does work flow, branch, deploy, and get tested? | [workflow.md](workflow.md) |
| How is the system built: stack, environments, accounts, data, key flows? | [infra.md](infra.md) |
| How does one specific feature work today? | `docs/products/<slug>/guide.md` |

## Read before working

| If the task is... | Read first |
|---|---|
| Assessing an idea or writing a PRD | docs/vision.md, docs/roadmap.md, docs/product-index.md |
| Writing a spec | the feature's prd.md, infra.md, docs/decisions.md |
| Building or changing code | the feature's spec.md and guide.md, infra.md, workflow.md |
| Changing data or the schema | infra.md (Data model), workflow.md (Migration protocol) |
| Shipping | workflow.md (Release and Close), .github/pull_request_template.md |
| Answering "where are we?" | docs/product-index.md, docs/roadmap.md |

## Tripwires

Hard rules that must never break. One line each, pointing to the document that owns the detail.
This list only grows; never remove a line, mark it superseded with a decision link instead.

{{TRIPWIRES}}

The reasoning behind each line lives in [docs/decisions.md](docs/decisions.md).

## Golden rules

One line each. The full text and the reasoning live in [workflow.md](workflow.md).

1. PRD before spec, spec before code. Plans freeze once built; guides stay true.
2. Done includes docs: the guide, product index, and roadmap change in the same pull request.
3. Ship only via git and {{HOSTING}}. Never deploy from the command line, never patch production by hand.
4. Database changes are additive and applied before the code that needs them merges.
5. Secrets live only in environment variables, never in the repository or in any document.
6. Small reversible steps: one feature per branch, branches live days not weeks.
7. Changing the vision is a decision. Record it; never let a PRD quietly drift from it.

## Who does what

{{OWNER}} owns the product: decides what to build, approves PRDs and specs, accepts features, and
approves releases. Claude drafts, builds, verifies, and keeps every document true. The commands
`/new-feature`, `/ship`, `/status`, and `/decision` carry the process; use them rather than
improvising.

## Directory map

```
CLAUDE.md                     this map
workflow.md                   the process, branch, deploy, QA, migration rules
infra.md                      technical knowledge base (living)
docs/vision.md                north star (changes only via a decision)
docs/roadmap.md               ordered milestones with status and shipped dates
docs/product-index.md         one row per feature with stage and links
docs/decisions.md             append-only decision log, D-001 onward
docs/products/<slug>/         prd.md (frozen), spec.md (frozen), guide.md (living)
docs/products/_template/      copy this for each new feature
docs/products/tech-setup/     day-one technical setup, tracked like a feature
.github/pull_request_template.md   merge checklist mirroring the rules
.claude/skills/               project commands: new-feature, ship, status, decision
```
