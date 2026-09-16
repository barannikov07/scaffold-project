# scaffold-project

A [Claude Code](https://claude.com/claude-code) skill that sets up a brand-new project the way a
strong product team would, for an owner who is not an engineer and builds with Claude.

It works with **Claude Code and Codex** out of the box, and with any agent that reads `AGENTS.md`.

It creates **documents and process only, no application code**: the router `AGENTS.md`, a vision,
a milestone roadmap, a product index, a decisions log, a ten-stage workflow, the technical
knowledge base, a design system, a QA regression list, PRD / design / spec / guide templates, a
pull request checklist, and nine playbooks that carry the process: four for the spine
(new-feature, ship, status, decision) and five specialists the spine calls at fixed points
(design, applied AI, QA, security, and a CTO pass). Then it starts the first PRD with you.

## See it work

**[How it works → barannikov07.github.io/scaffold-project](https://barannikov07.github.io/scaffold-project/)** walks through a real run (ChoirHub, an app for a community choir): the interview replayed, the generated documents, sequence diagrams of the scaffold session and of one feature's life, the ten-stage pipeline, and the orchestrator-and-builders loop.

## Read a finished example

[`examples/choirhub`](examples/choirhub) is a full run on a community-choir app, left where a real
project pauses for its owner: vision, roadmap, decisions, a PRD with the applied-AI pass, a design
system and HTML mockups, and a spec with the security threat pass and the CTO pass. Start with
[`examples/choirhub/CONVERSATION.md`](examples/choirhub/CONVERSATION.md), which is everything the
owner would have seen.

## What you get

```
AGENTS.md                     map for every future session, any agent, with tripwires and golden rules
CLAUDE.md                     one line, @AGENTS.md, so Claude Code reads the same map
docs/playbooks/               nine playbooks (canonical): new-feature, ship, status, decision, design, ai-native, qa, security, cto
.claude/skills/ .codex/skills/ thin wrappers exposing them as slash commands in Claude Code and Codex
workflow.md                   idea → assess → PRD → design → spec → migrate → build → QA → release → close
infra.md                      stack, environments, identities, security baseline, data model, key flows, operations
docs/design/system.md         design system: tokens, type, components, copy rules (living)
docs/design/mockup-base.html  the base every mockup starts from
docs/qa/regression.md         golden paths of every shipped feature (living)
docs/tech-debt.md             deliberate shortcuts with a pay-by milestone (living)
docs/vision.md                north star; changes only through a recorded decision
docs/roadmap.md               one ordered milestone table: planned, delivered, next
docs/product-index.md         one row per feature with its stage and links
docs/decisions.md             append-only decision log, D-001 onward
docs/products/<slug>/         prd.md, design.md, spec.md (records), guide.md (living), qa.md (runs), mockups/
docs/products/tech-setup/     day-one technical setup, tracked like a feature
.github/pull_request_template.md
```

## The ideas behind it

- **AGENTS.md is a router, not an encyclopedia.** Every fact lives in one document; everything else links to it.
- **Records are kept, guides are living, the roadmap is fluid.** A feature's PRD and spec become a record of what was agreed once its build starts. Guides carry current truth. The roadmap and vision change whenever you learn something, with the change and its reason written down.
- **Done includes docs.** Nothing merges until the guide, index, and roadmap reflect the change.
- **Tripwires over tribal knowledge.** Every hard invariant gets one line in AGENTS.md pointing to its owner.
- **Size decides ceremony.** Small changes go straight to build; anything with a new screen, table, permission, or money path gets the full path.
- **The owner decides at three moments**, four when there is a screen: approving the PRD, approving the mockup, accepting the feature, approving the release. The agent does the rest.
- **Design is a gate, not a garnish.** Anything with a screen is designed on a project design system and approved as a static HTML mockup the owner opens in a browser, before any code. The build must match it.
- **AI in the product removes a step.** An applied-AI pass runs on every PRD draft and proposes two to four places where AI takes the tedious part (voice or paste to record, auto-mapping, drafted messages, drift signals). It proposes, a person confirms, the manual path stays.
- **QA, security, and architecture are playbooks, not hopes.** Every QA line is executed with evidence in a recorded run; risk-tagged features get a threat pass at spec and a diff checklist at QA; every spec gets a CTO pass that names the simplest build, the biggest risk, and the one-way doors, and logs shortcuts as debt with a due date. All prefer stronger built-in skills when the agent has them.
- **Light by default.** Playbooks load only when they fire (about 5,000 tokens of process per session, not the whole set), specialists only when their tag is set, and the CTO pass is three sentences unless the spec adds a table, a service, an AI component, or a risk.
- **Calibrated to the owner.** Two interview questions set how technical and how product-savvy the owner is. A beginner gets the why of each gate once; a product manager gets the gate. The process itself never changes.
- **Orchestrator and builders.** The strongest model plans, writes the PRD and spec, and reviews. Cheaper models build from file-scoped briefs. Two review rounds, then stop and report.

## Install

Claude Code:

```bash
git clone https://github.com/barannikov07/scaffold-project.git ~/.claude/skills/scaffold-project
```

Codex (same repository, same skill format):

```bash
git clone https://github.com/barannikov07/scaffold-project.git ~/.codex/skills/scaffold-project
```

Then, in any empty folder, tell your agent "start a new project" or "scaffold this project".

Projects it creates are agent-agnostic too: the router is `AGENTS.md`, which Codex and most agents
read natively, and `CLAUDE.md` is a one-line import of it for Claude Code. The playbooks live
as plain playbooks in `docs/playbooks/` with wrappers for both `.claude/skills/` and
`.codex/skills/`, and `AGENTS.md` maps the trigger phrases to the playbooks for any agent without
slash commands. The specialist playbooks use a stronger built-in skill when the agent has one (a
design canvas, a security review, a code review, a skill that runs the app) and fall back to
their own checklists when not, so the process is complete on any agent.

## How it runs

1. Interviews you in plain language, one question at a time. No "which stack?"; it asks what the product does, who uses it, whether people sign in, whether data or money is involved, and what to build first. Claude picks the stack and explains it in one sentence.
2. Shows a plain-English summary and asks one yes/no.
3. Stamps the templates (`scripts/scaffold.py`) and fills the content that needs judgment.
4. Commits everything in one commit on `main`.
5. Hands you the list of things only you can do (accounts, repository, hosting connection) and starts the first PRD.

## Layout of this repository

```
SKILL.md              the procedure Claude follows
references/           why the structure is shaped this way, the interview, the filling guide
scripts/scaffold.py   stamps assets/templates into a target folder
assets/templates/     every generated file, with {{PLACEHOLDERS}}
evals/                a test scenario used while developing the skill
```

## License

MIT
