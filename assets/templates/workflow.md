# How work flows in {{PROJECT_NAME}}

This document governs all feature work. The agent (Claude Code, Codex, or any other) follows it;
{{OWNER}} decides at the gates. If a situation is not covered here, the golden rules in AGENTS.md
decide, and the gap gets fixed here in the same change.

## Who does what

| | {{OWNER}} (the owner) | The agent |
|---|---|---|
| Ideas | Has them, captures them in one line | Captures them when they come up in conversation |
| Assess | Decides go / later / no | Drafts the assessment: size, has-UI, risk tags, vision fit |
| PRD | Approves, including the screen list | Drafts with the vision as the prism; lists the screens in the owner's words; runs the applied-AI pass |
| Spec | Approves | Drafts, with every screen state and its copy, test plan, work items, rollout and rollback; runs the security threat pass when the feature is risk-tagged |
| Migrate | Nothing | Applies the additive change, mirrors it in the schema file |
| Build | Nothing | Builds on a branch from the design system, adding to it first when a screen needs something new; updates the guide, index, roadmap, infra |
| QA | Accepts against the PRD's success criteria, on the preview or localhost. For a feature with a screen this is the owner's first look; sending a screen back is ordinary work | Runs the QA playbook, and the security checklist when tagged; fixes blockers |
| Release | Approves | Pre-flight, merge to main, production check |
| Close | Reads the outcome | Marks Live, records the outcome, appends the regression path, prompts a roadmap review |

The owner's work is concentrated in three moments: approving the PRD, accepting the feature, and
approving the release. Everything else is the agent's.

## How the agent talks to the owner

The owner profile in AGENTS.md has two axes. Technical level decides whether terms are glossed and
whether code is ever shown. Product level decides how much of the process is explained and who
drafts the plans. Neither axis changes a gate; they change the words around it.

| | Never coded / new to product work | Understands, doesn't code / worked with PMs | Reads code / product manager |
|---|---|---|---|
| Terms | Gloss every term in one sentence, the first time it appears in the project | Gloss only unusual terms | No glossing |
| Options | One recommendation and the reason | Recommendation plus one alternative | All options, one line each |
| Gates | Say why the gate exists, once, the first time it is reached | Name the gate | Ask the question. "PRD ready, approved?" |
| Code | Never shown; described in words | File names only | Diff on request |
| PRD and spec | The agent drafts everything, owner reacts | The agent drafts and marks where the owner could add | Owner may draft, the agent reviews and fills gaps |
| Screens | "Tap the blue button; that is what a singer would do" | Screen list with one line each | Screen list |
| Acceptance checklist | Every step as "tap here, expect this" | Steps without interface detail | Criteria only |

Rules that stop this becoming a lecture:

- **Once per project, not once per session.** An explanation given in an earlier session is not
  repeated. If in doubt, the decisions log and the guides show what the owner has already seen.
- **Default to less.** When unsure which column applies, use the one to the right. The owner can
  ask "why?"; they cannot un-read a paragraph.
- **The owner can turn it down or up in one sentence.** "Skip the explanations" or "explain more"
  updates the profile lines in AGENTS.md, and every later session follows.
- **Tripwires are the exception.** A tripwire is always named when a task touches it, whatever the
  level. One line, not a paragraph.

## The pipeline

Every feature moves through these stages in order. The "passes when" column is the gate; a stage
is not done until its gate holds. Two tags set at Assess decide what fires downstream: **has-UI**
(the feature has a screen: the PRD lists its screens, the spec designs every state, QA runs the
screen checks, and the owner's acceptance walk is screen by screen) and **risk** (money, privacy,
sign-in, external service, or none: the security passes).

| # | Stage | Who | Produces | Passes when |
|---|---|---|---|---|
| 1 | Idea | Owner | One line in the roadmap under "Later", or a row in the index with stage Idea | Captured; nothing else required |
| 2 | Assess | Agent drafts, owner decides | Size (Small / Full), has-UI, risk tags, vision fit, dependencies, go / later / no | Row in `docs/product-index.md` with stage Planned, Later, or Dropped |
| 3 | PRD | Agent drafts, owner approves | `docs/products/<slug>/prd.md`, including the AI opportunities the applied-AI pass found and the decision on each | Owner says "approved"; the "Before this passes" checklist is all ticked; committed to `main` |
| 4 | Spec | Agent drafts, owner approves | `spec.md`: data model, functions, screens with every state and the real copy, permissions, AI components, security section when tagged, edge cases, migration plan, work items, test plan, rollout and rollback | Owner says "approved"; checklist ticked; committed to `main` |
| 5 | Migrate | Agent, only if the spec has a migration plan | Additive change applied to the live database; mirrored in the schema file | Applied and mirrored before any dependent code merges |
| 6 | Build | Agent | Branch `feat/<slug>` with code plus guide, index, roadmap, and infra updated; every screen built from the design system, with anything new added to it first | Build passes, verify script passes, docs match the code |
| 7 | QA | Agent runs, owner accepts | The QA playbook executed and recorded in `qa.md`; the security checklist when tagged; the owner's acceptance checklist, walked on the preview or localhost, screen by screen for features with a screen | Zero open blockers; owner says "accepted" |
| 8 | Release | Owner approves, agent executes | Pre-flight; pull request merged to `main`; production smoke check | The live site passes the acceptance happy path |
| 9 | Close | Agent | Stage Live; shipped date in the roadmap; outcome vs success criteria; golden path appended to `docs/qa/regression.md`; roadmap review | Index, roadmap, and regression list match reality; owner has seen the outcome note |

### Stage notes

**Idea.** Cheap to capture, free to drop. Do not write a PRD for an idea. Ideas that arrive
mid-conversation go into the roadmap's "Later" rows or the index as stage Idea so nothing is lost.

**Assess.** The assessment is a short note, not a document: size, has-UI, risk tags, which vision
goal it advances, what it depends on (including the hidden dependencies: people or records that
must exist before the feature means anything), and a recommendation. If it advances no vision
goal, recommend Later or Dropped. The two tags are not bureaucracy: has-UI is what makes the
screen list, the state design, and the screen checks exist, and risk is what makes the security
passes exist. Get them right here and
nothing downstream has to be remembered. The owner's decision is recorded in the index row.
Assessments for Full-size features are pasted at the top of the PRD.

**PRD.** Problem, users, scope, non-goals, flows, screens (one line each, for features with a
screen), success criteria, vision fit. One page for most features. The screen list is the owner's
main say in how the product will look, so it is written to be pictured, not parsed; the
design-system playbook, "Describing a screen", shows how. After the draft and before approval, the applied-AI pass (`docs/playbooks/ai-native.md`)
proposes where AI inside the product removes a step from the flow; the owner chooses, and every
proposal ends in scope, in the roadmap, or in non-goals with a reason. Written just in time: the
PRD for a milestone is written when that milestone is next, not before. A draft until the build
starts; from then on it is a record of what was agreed and is not edited. Corrections go in the
guide, and a genuine change of mind is a new PRD (`prd-2-<short>.md`) in the same folder, so the
history of thinking is kept.

**Screens.** There is no design stage and there are no mockups. Which screens exist is decided in
the PRD, in the owner's words; every state and the real copy are decided in the spec; and every
screen is built from the design system (`docs/design/system.md`), which is real code in the app
from tech setup on. One rule governs the look: use the design system, and when a screen needs a
component or token the system lacks, add it to the system first, then use it. No one-off UI. The
owner sees screens for the first time on the pull request preview or on localhost at acceptance;
sending one back is ordinary work, not a failure, because nothing is in production and rework by
an agent is cheap. The design-system playbook (`docs/playbooks/design.md`) creates the system
with the owner at tech setup and governs every addition.

**Spec.** Data model changes, functions or endpoints, screens with every state (empty, loading,
error, success, denied; for an AI step also thinking, correct-me, and the manual fallback) and the
real copy, phone first, permissions, edge cases, migration plan, work items, test plan, rollout
and rollback. Written after the PRD is approved, before any code. A state that is not written
down here will be improvised in code, badly. For risk-tagged features the security playbook's
threat pass fills the Security section: what data is sensitive, who may see it, which rule
enforces each denial, what a malicious user would try. For chosen AI items, the AI components
section names inputs, outputs, model tier, cost, what data leaves the app, the fallback, who
confirms what, and an evaluation set of real examples. Before the owner approves, the CTO pass
(`docs/playbooks/cto.md`) adds the Technical review: the simplest build, the biggest risk,
one-way doors recorded as decisions, and any deliberate shortcut logged in `docs/tech-debt.md`.
A record once built.

**Migrate.** Only additive changes: add tables, add nullable columns, add indexes. Never rename or
drop in the same change that adds. The change is applied to the live database out of band and
mirrored in the repository's schema file before the code that depends on it merges, so a rollback
of the code never leaves the database inconsistent.

**Build.** One feature per branch, branch named `feat/<slug>`, days not weeks. The same branch
updates `guide.md`, the product index, the roadmap, and `infra.md` if anything cross-cutting
changed. Verified locally before push. Anything larger than a few files is built by delegation:
the orchestrator splits the spec's work items across builder agents and reviews the result. For
UI features the review includes a screen-by-screen check against the spec's Screens section and
the design system: every state present, nothing one-off. See "How the agent builds" below.

**QA.** Two halves. The agent's half is the QA playbook (`docs/playbooks/qa.md`): every line of
the test plan, the permission matrix, one check per tripwire, every state in the spec, phone width,
the accessibility floor, the data-safety guardrail, the regression list, the AI evaluation set,
and the security diff checklist when tagged, each line executed and recorded with evidence in
`docs/products/<slug>/qa.md`. Failures are triaged blocker (fix before release) or later (one
line in the roadmap). The owner's half is the acceptance checklist: the PRD's success criteria as
exact steps, walked on localhost (anything behind sign-in) or on the preview link (anything
public), answered with "accepted" or a list of issues. For a feature with a screen this is the
owner's first look at the screens; issues go back to the branch as ordinary work. No release with
an open blocker.

**Release.** Pre-flight first: migration applied and mirrored; every environment variable the
feature needs present in the host; the spec's rollback section read once; a feature flag or staged
rollout in place for risk-tagged features. Then merging the pull request to `main` is the
release; the host deploys it. After deploy, the agent walks the acceptance happy path on the live
site. If it fails, roll back (below) before investigating.

**Close.** Mark the index row Live, add the shipped date to the roadmap, write two or three lines
in the guide's "Outcome" section on whether the success criteria were met (and whether any AI
step saved the time the PRD claimed), append the feature's golden path to
`docs/qa/regression.md`, add a design-system changelog row if the feature changed it, run the
CTO pass's debt review so anything in `docs/tech-debt.md` that has come due is scheduled, add a
decision entry if anything surprising was learned, and ask the owner whether the order of the
remaining milestones still holds.

## Specialists, and when they fire

Five playbooks carry the professional practice. They are called by `new-feature` and `ship` at
fixed points, driven by the tags from Assess, so the owner never has to remember them. Each also
works as a standalone command for a re-run. Every playbook prefers a stronger built-in skill when
the agent has one and falls back to its own checklist when not, so the process is complete on any
agent and better on the agents that have more.

| Playbook | Fires at | For | Prefers, when the agent has it |
|---|---|---|---|
| `docs/playbooks/ai-native.md` | PRD, after the draft, before approval | Every Full feature | Nothing extra needed |
| `docs/playbooks/design.md` | Tech setup (create the system with the owner); Build, whenever a screen needs a component or token the system lacks; QA (critique before the owner's look) | Every project once; then has-UI features | A design canvas or design critique skill; an accessibility review skill |
| `docs/playbooks/security.md` | Spec (threat pass), QA (diff checklist), tech setup (baseline) | Risk-tagged features; the baseline once | A built-in security review skill |
| `docs/playbooks/qa.md` | QA, before the owner's acceptance | Every feature; Small in short form | A skill that runs the app and takes screenshots; a code review skill |
| `docs/playbooks/cto.md` | Spec (technical review), tech setup (setup mode), Close (debt review) | Every Full feature; light unless the spec adds a table, a service, an AI component, or a risk tag | Nothing extra; judgment over the spec and infra.md |

Skipping a specialist whose tag is set is a process failure to report, not a shortcut to take.

## How the agent builds: orchestrator and builders

Thinking and building are different jobs and deserve different models. The most capable model
available acts as the **orchestrator**: it interviews, assesses, writes the PRD and the spec,
splits the work, reviews the code, and decides what ships. Faster, cheaper models act as
**builders**: each takes one self-contained work item and implements it. The owner only ever
talks to the orchestrator. This works in any agent: in Claude Code the orchestrator spawns
builders as sub-agents; in an agent without sub-agents, the orchestrator builds the work items
itself, one at a time, and still reviews each against the spec before starting the next.

| Role | Model tier | Does | Never does |
|---|---|---|---|
| Orchestrator | The strongest model available (Claude Opus or Fable, GPT-5 class with high reasoning) | Plans, writes PRD and spec, splits work into items, briefs builders, reviews every diff against the spec, the design system, and the tripwires, fixes docs, ships | Trusts a builder's own report of success |
| Builder | A fast model (Claude Sonnet, a GPT-5 mini class model; the strong model for hard items) | Implements one work item from its brief on a branch or worktree, runs the tests it was given, reports what it changed | Touches files outside its brief, changes the spec, merges |

The loop, for every Full-size feature:

1. **Plan.** The orchestrator writes the spec's "Work items" section: independent items, each with
   the files it may touch, the contract it must satisfy, and its done-criteria. Items that touch
   the same files are merged into one or given separate worktrees.
2. **Delegate.** One builder per item, in parallel, each with a self-contained brief: the item, the
   relevant spec sections, the spec's Screens section for its screen and the design system's
   component list, `infra.md` pointers, the tripwires, and how
   to verify. Small features (three files or fewer, or nothing parallel) are built by the
   orchestrator itself; say so.
3. **Review.** The orchestrator reads the combined diff against the spec, the design system, and the
   tripwires, runs the verify script and the test plan, and lists findings. Only correctness and
   security findings go back to builders; style is fixed inline or noted.
4. **Fix.** Confirmed findings return to the builder that wrote the code, as file-anchored
   instructions. Scope only shrinks in a fix round: no new features, no refactors.
5. **Stop.** At most two review-and-fix rounds. If blockers remain after the second, the
   orchestrator stops and tells the owner: the plan is probably wrong, not the builders.

Done means the verify script passes, the QA run is complete, zero confirmed critical findings,
and the docs are true. Not "the reviewer ran out of things to say".

## Size decides ceremony

| Size | When | Path |
|---|---|---|
| Small | No new screen, table, permission, external service, or money path. Copy changes, styling, bug fixes, small tweaks to an existing feature | Build → QA (short form: functional, tripwires, regression) → Release → Close. Built by the orchestrator directly. Guide updated. No PRD or spec. Noted in the guide's changelog |
| Full | Anything else | All nine stages. The security passes only if risk-tagged; the applied-AI pass always; the screen list, the state design, and the screen checks if has-UI |

When in doubt, it is Full. The cost of a one-page PRD is an hour; the cost of an unplanned schema
change is a week.

## Branch and release rules

- `main` is production. Every merge to `main` is a release.
- Ship only via git → GitHub → {{HOSTING}}. Never deploy from the command line; never edit
  anything in production by hand.
- Approved PRDs and specs are committed straight to `main` before the branch exists;
  they are documents, and the build must start from an agreed plan.
- One feature per short-lived branch for code. Branch → pull request → merge. Preview deployments
  come free with the pull request; anything behind sign-in is verified on localhost, not on
  previews.
- Rollback is reverting the merge commit and pushing. Nothing else. Then investigate.
- Secrets live only in the host's environment settings and in the gitignored `.env.local`. Never
  in the repository, never in any document. Documents list variable names only.

## QA guardrail once real data exists

Before real users exist, QA can write anything. From the day real data exists:

- QA only ever signs in as the seeded test user and touches records that belong to it.
- Seeded test records carry an obvious marker (a `TEST-` prefix in their name or title) so they
  can be found and cleaned.
- Nothing in QA modifies or deletes a real user's record. If a test needs a real-looking case,
  seed a copy under the test user.
- The localhost-only test login never exists in production builds.

## Migration protocol

1. The spec carries the migration plan: what is added and why nothing is renamed or dropped.
2. The agent writes one idempotent script per change (safe to run twice), named
   `migration/apply-<slug>-<n>-<short>.<ext>` per the stack's tooling.
3. The script is run against the live database before the dependent code merges.
4. The repository's schema file is updated in the same pull request so it always mirrors the live
   database.
5. Removals happen in a separate, later change, after the code that needed the old shape is gone.

## Docs are a merge requirement

The pull request template lists the documents that must be true before merge. A pull request
with an unticked box does not merge. This is not bureaucracy: the documents are how the owner
steers and how the next session understands the system. Docs updated "later" are docs never
updated.

## Commands

| Command | What it does |
|---|---|
| `/new-feature <name>` | Assess, then PRD with the applied-AI pass, spec with the security pass if tagged, each with owner approval |
| `/ship <slug>` | Run the QA playbook, prepare the acceptance checklist, pre-flight, open the pull request, merge on approval, close |
| `/status` | Summarise where everything stands from the index and roadmap; list open TBDs |
| `/decision` | Record a decision in the log with reasoning and rejected alternatives |
| `/design <slug>` | Create the design system with the owner at tech setup; add a component or token before a screen uses it; critique built screens before the owner's look |
| `/ai-native <slug>` | Propose where AI inside the product removes a step; record the decisions in the PRD |
| `/qa <slug>` | Execute the full QA run with evidence; triage; write the acceptance checklist |
| `/security <slug>` | Threat pass at spec, diff checklist at QA, or the project baseline |
| `/cto <slug>` | Technical review of a spec: simplest build, biggest risk, one-way doors, tech debt; setup mode at tech setup; debt review at Close |
