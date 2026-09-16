<!-- Playbook: cto. Canonical text; the .claude/skills and .codex/skills wrappers point here. -->

# CTO pass

The technical review a staff engineer gives a spec before anyone builds it. Runs at stage 5,
after the spec draft and before the owner approves, called by the new-feature playbook; also at
tech setup (setup mode) and at Close (debt review), and on its own when the owner says "is this
built right", "tech review", "will it scale", "architecture", or "ask the CTO". Calibrate every
message to the owner profile in `AGENTS.md`: the owner gets two sentences; the table is for the
builders.

It is deliberately small. It is one section in the spec, written by the same orchestrator in the
same session, not a new document and not a new agent. Its job is to catch the handful of
choices that are expensive to reverse, and to say what can be left out.

Read first: the feature's `spec.md`, `infra.md`, `docs/decisions.md`, `docs/tech-debt.md`.

## Light or full

**Light** when the spec adds no table or column, no external service, no AI component, and the
feature carries no risk tag. Three questions, three sentences in the spec's Technical review:

1. What is the simplest build that meets every success criterion, and what does this spec add
   beyond it?
2. What is the single biggest technical risk?
3. Is any choice here a one-way door? If yes, it becomes a decision entry.

**Full** in every other case. Fill the table in the spec's Technical review section:

| Check | Question it answers |
|---|---|
| Fit | Does this belong in the existing structure, or is it quietly a new module? Name where it lives |
| Data | Tables and columns right; indexed for the queries the screens make; additive; immutable or append-only where a tripwire says so |
| Contracts | Every function has clear inputs, outputs, and failure behaviour |
| Scale and cost | Users and records in a year; the first place it gets slow; what each AI call or external service costs per month at that size |
| Reliability | What the user sees when each external service is down; what is retried, what is queued |
| Observability | What is logged (no personal data); how we would know it is broken before a user tells us |
| Simplicity | The simpler way, if there is one; what can be left out; whether any new dependency is worth its weight |
| One-way doors | Choices that are hard to reverse; each recorded as a decision |
| Debt | What is deliberately shortcut, added to `docs/tech-debt.md` with a "pay by" milestone |

Two rules for filling it: write "fine" where a row has nothing to say rather than inventing a
concern, and never add a requirement the PRD did not ask for. The pass removes and de-risks; it
does not grow the feature.

## What the owner sees

Two sentences, in their words: the biggest technical risk and what the spec does about it, and
the simplest way to build this. If a one-way door exists, one more sentence saying what it is
and that it is being recorded. Nothing else unless they ask.

## Setup mode (tech setup, once)

- Confirm the stack fits the interview answers now that the checklist is being executed; if it
  does not, say so before anything is installed, and record the change as a decision.
- Fill the Operations section of `infra.md`: where logs are, how backups restore, what to check
  first when something breaks.
- Create the first rows of `docs/tech-debt.md` if the setup took any shortcut.

## Debt review (Close)

Read `docs/tech-debt.md`. Any row whose "pay by" milestone is the one just shipped or earlier
is due: tell the owner in one line each, and offer to schedule it as a Small change or a roadmap
row. Debt is paid on a schedule, not discovered in a crisis.

## Prefers, when the agent has it

A code review or simplification skill helps at Build, not here. At this stage nothing extra is
needed; the pass is judgment over the spec and `infra.md`.
