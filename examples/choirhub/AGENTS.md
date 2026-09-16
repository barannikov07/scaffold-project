# ChoirHub

Helps a community choir's conductor manage members, rehearsals and attendance, so nobody has to chase people on WhatsApp.

This file is a map, not a manual. Every fact lives in exactly one document and this file only
points to it. If you are about to add detail here, it belongs in one of the documents below.
It is named AGENTS.md so every coding agent reads it; `CLAUDE.md` is a one-line import of this
file for Claude Code. Edit this file, never that one.

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
| Designing a screen or changing how anything looks | docs/design/system.md, the feature's design.md, docs/playbooks/design.md |
| Adding AI to a feature | docs/playbooks/ai-native.md, the feature's prd.md |
| Testing anything | docs/playbooks/qa.md, docs/qa/regression.md, the feature's spec.md |
| Anything with money, privacy, sign-in, or an external service | docs/playbooks/security.md, infra.md (Identities and access) |
| Deciding how something should be built, or whether it will scale | docs/playbooks/cto.md, infra.md, docs/tech-debt.md |

## Tripwires

Hard rules that must never break. One line each, pointing to the document that owns the detail.
This list only grows; never remove a line, mark it superseded with a decision link instead.

- Attendance and replies are append-only: once a rehearsal has happened, a record is never edited or deleted, only superseded by a new entry → infra.md (Data model)
- A singer never sees another singer's email or phone number; only the conductor sees contact details → infra.md (Identities and access)
- Card details never touch this app or its logs; when fees arrive they are handled by the payments provider → infra.md (Identities and access)
- A singer never sees who answered what: only the counts. A name against an answer is the conductor's view alone → infra.md (Identities and access)

The reasoning behind each line lives in [docs/decisions.md](docs/decisions.md).

## Golden rules

One line each. The full text and the reasoning live in [workflow.md](workflow.md).

1. PRD before spec, spec before code. Once built, the PRD and spec are a record; guides stay true; the roadmap moves.
2. Done includes docs: the guide, product index, and roadmap change in the same pull request.
3. Ship only via git and Vercel. Never deploy from the command line, never patch production by hand.
4. Database changes are additive and applied before the code that needs them merges.
5. Secrets live only in environment variables, never in the repository or in any document.
6. Small reversible steps: one feature per branch, branches live days not weeks.
7. Changing the vision is a decision. Record it; never let a PRD quietly drift from it.
8. The strongest model plans and reviews; builders build from briefs; two review rounds, then stop and tell the owner.
9. Anything with a screen is designed and approved as a mockup before it is built; the build matches the mockup.
10. AI inside the product must remove a step; it proposes, a person confirms, and the manual path stays.
11. No spec reaches build without the CTO pass; one-way doors are decisions, shortcuts are logged debt with a due date.

## Owner profile

Read this before writing anything to the owner. It sets how Claude talks, never what the process
requires. The owner edits these two lines when they change.

- Technical: understands how apps work, doesn't code
- Product: worked alongside product managers for years

The behaviour each level buys is the table "How Claude talks to the owner" in
[workflow.md](workflow.md). The short version: explain once per project, not once per session;
default to less; a beginner gets the why of each gate, a product manager gets the gate.

## Who does what

Sasha owns the product: decides what to build, approves PRDs, mockups, and specs, accepts
features, and approves releases. The agent drafts, designs, builds, tests, verifies, and keeps
every document true.

## Commands

The process is carried by nine playbooks in `docs/playbooks/`. Claude Code and Codex expose
them as slash commands through thin wrappers in `.claude/skills/` and `.codex/skills/`. Any other
agent follows the playbook directly when the owner says the trigger phrase. The first four are
the spine; the last five are specialists the spine calls at fixed points (see workflow.md,
"Specialists, and when they fire").

| Owner says | Follow |
|---|---|
| "new feature", "let's build X", "I want a PRD for X" | `docs/playbooks/new-feature.md` |
| "ship it", "release", "is it ready", "let's go live" | `docs/playbooks/ship.md` |
| "where are we", "status", "what's next" | `docs/playbooks/status.md` |
| "we'll go with", "record that", "let's decide" | `docs/playbooks/decision.md` |
| "design", "mockup", "what will it look like", "make it beautiful" | `docs/playbooks/design.md` |
| "where can AI help", "make it smarter", "AI features" | `docs/playbooks/ai-native.md` |
| "test it", "QA", "does it work", "check everything" | `docs/playbooks/qa.md` |
| "security", "is this safe", "who can see this", "review permissions" | `docs/playbooks/security.md` |
| "is this built right", "tech review", "will it scale", "ask the CTO" | `docs/playbooks/cto.md` |

## Directory map

```
AGENTS.md                     this map, read by every agent
CLAUDE.md                     one line: @AGENTS.md (Claude Code import; never edit)
workflow.md                   the process, branch, deploy, QA, migration rules
infra.md                      technical knowledge base (living)
docs/vision.md                north star (changes only via a decision)
docs/roadmap.md               ordered milestones with status and shipped dates
docs/product-index.md         one row per feature with stage and links
docs/decisions.md             append-only decision log, D-001 onward
docs/design/system.md         design system: tokens, type, components, copy rules (living)
docs/design/mockup-base.html  the base every mockup starts from
docs/qa/regression.md         golden paths of every shipped feature (living, appended at Close)
docs/tech-debt.md             deliberate shortcuts with a pay-by milestone (living, reviewed at Close)
docs/products/<slug>/         prd.md, design.md, spec.md (records), guide.md (living), qa.md (runs), mockups/
docs/products/_template/      copy this for each new feature
docs/products/tech-setup/     day-one technical setup, tracked like a feature
docs/playbooks/               the nine commands, canonical text
.claude/skills/ .codex/skills/  thin wrappers that expose the playbooks as slash commands
.github/pull_request_template.md   merge checklist mirroring the rules
```
