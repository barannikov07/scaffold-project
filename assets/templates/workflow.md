# How work flows in {{PROJECT_NAME}}

This document governs all feature work. Claude follows it; {{OWNER}} decides at the gates. If a
situation is not covered here, the golden rules in CLAUDE.md decide, and the gap gets fixed here
in the same change.

## Who does what

| | {{OWNER}} (the owner) | Claude |
|---|---|---|
| Ideas | Has them, captures them in one line | Captures them when they come up in conversation |
| Assess | Decides go / later / no | Drafts the assessment: size, risks, vision fit |
| PRD | Approves | Drafts, using the vision as the prism |
| Spec | Approves | Drafts, including test plan and rollback |
| Migrate | Nothing | Applies the additive change, mirrors it in the schema file |
| Build | Nothing | Builds on a branch, updates the guide, index, roadmap, infra |
| QA | Accepts against the PRD's success criteria | Verifies locally, executes the test plan, fixes blockers |
| Release | Approves | Merges to main, checks production |
| Close | Reads the outcome | Marks Live, records outcome and learnings, prompts a roadmap review |

The owner's work is concentrated in three moments: approving the PRD, accepting the feature, and
approving the release. Everything else is Claude's.

## How Claude talks to the owner

The owner profile in CLAUDE.md has two axes. Technical level decides whether terms are glossed and
whether code is ever shown. Product level decides how much of the process is explained and who
drafts the plans. Neither axis changes a gate; they change the words around it.

| | Never coded / new to product work | Understands, doesn't code / worked with PMs | Reads code / product manager |
|---|---|---|---|
| Terms | Gloss every term in one sentence, the first time it appears in the project | Gloss only unusual terms | No glossing |
| Options | One recommendation and the reason | Recommendation plus one alternative | All options, one line each |
| Gates | Say why the gate exists, once, the first time it is reached | Name the gate | Ask the question. "PRD ready, approved?" |
| Code | Never shown; described in words | File names only | Diff on request |
| PRD and spec | Claude drafts everything, owner reacts | Claude drafts and marks where the owner could add | Owner may draft, Claude reviews and fills gaps |
| Acceptance checklist | Every step as "tap here, expect this" | Steps without interface detail | Criteria only |

Rules that stop this becoming a lecture:

- **Once per project, not once per session.** An explanation given in an earlier session is not
  repeated. If in doubt, the decisions log and the guides show what the owner has already seen.
- **Default to less.** When unsure which column applies, use the one to the right. The owner can
  ask "why?"; they cannot un-read a paragraph.
- **The owner can turn it down or up in one sentence.** "Skip the explanations" or "explain more"
  updates the profile lines in CLAUDE.md, and every later session follows.
- **Tripwires are the exception.** A tripwire is always named when a task touches it, whatever the
  level. One line, not a paragraph.

## The pipeline

Every feature moves through these stages in order. The "passes when" column is the gate; a stage
is not done until its gate holds.

| # | Stage | Who | Produces | Passes when |
|---|---|---|---|---|
| 1 | Idea | Owner | One line in the roadmap under "Later", or a row in the index with stage Idea | Captured; nothing else required |
| 2 | Assess | Claude drafts, owner decides | Size (Small / Full), risk tags, vision fit, go / later / no | Row in `docs/product-index.md` with stage Planned, Later, or Dropped |
| 3 | PRD | Claude drafts, owner approves | `docs/products/<slug>/prd.md` | Owner says "approved"; the "Before this passes" checklist in the PRD is all ticked |
| 4 | Spec | Claude drafts, owner approves | `docs/products/<slug>/spec.md` incl. test plan, migration plan, rollback | Owner says "approved"; checklist ticked |
| 5 | Migrate | Claude, only if the spec has a migration plan | Additive change applied to the live database; mirrored in the schema file | Applied and mirrored before any dependent code merges |
| 6 | Build | Claude | Branch `feat/<slug>` with code plus guide, index, roadmap, and infra updated | Build passes, verify script passes, docs match the code |
| 7 | QA | Claude verifies, owner accepts | Test plan executed; acceptance checklist from the PRD's success criteria | Owner says "accepted" (or blockers are fixed and re-accepted) |
| 8 | Release | Owner approves, Claude executes | Pull request merged to `main`; production smoke check | The live site works for the acceptance checklist's happy path |
| 9 | Close | Claude | Stage Live in the index; shipped date in the roadmap; outcome vs success criteria recorded; roadmap review | Index and roadmap match reality; owner has seen the outcome note |

### Stage notes

**Idea.** Cheap to capture, free to drop. Do not write a PRD for an idea. Ideas that arrive
mid-conversation go into the roadmap's "Later" rows or the index as stage Idea so nothing is lost.

**Assess.** The assessment is a short note, not a document: size, risk tags (money, privacy,
data loss, external service), which vision goal it advances, what it depends on, and a
recommendation. If it advances no vision goal, recommend Later or Dropped. The owner's decision
is recorded in the index row. Assessments for Full-size features are pasted at the top of the PRD.

**PRD.** Problem, users, scope, non-goals, flows, success criteria, vision fit. One page for most
features. Written just in time: the PRD for a milestone is written when that milestone is next, not
before. A draft until the build starts; from then on it is a record of what was agreed and is not
edited. Corrections go in the guide, and a genuine change of mind is a new PRD
(`prd-2-<short>.md`) in the same folder, so the history of thinking is kept.

**Spec.** Data model changes, functions or endpoints, screens, permissions, edge cases, migration
plan, test plan, rollback. Written after the PRD is approved, before any code. A record once built.

**Migrate.** Only additive changes: add tables, add nullable columns, add indexes. Never rename or
drop in the same change that adds. The change is applied to the live database out of band and
mirrored in the repository's schema file before the code that depends on it merges, so a rollback
of the code never leaves the database inconsistent.

**Build.** One feature per branch, branch named `feat/<slug>`, days not weeks. The same branch
updates `guide.md`, the product index, the roadmap, and `infra.md` if anything cross-cutting
changed. Verified locally before push. Anything larger than a few files is built by delegation:
the orchestrator splits the spec's work items across builder agents and reviews the result. See
"How Claude builds" below.

**QA.** Two halves. Claude's verification: build passes, the verify script passes, every line of
the spec's test plan is executed on localhost. The owner's acceptance: Claude turns the PRD's
success criteria into a short checklist with exact steps, the owner walks through them on
localhost (anything behind sign-in) or on the preview link (anything public) and replies
"accepted" or lists what is wrong. Each issue is triaged as blocker (fix before release) or later
(one line in the roadmap). No release with an open blocker.

**Release.** Merging the pull request to `main` is the release; the host deploys it. After deploy,
Claude walks the acceptance happy path on the live site. If it fails, roll back (below) before
investigating.

**Close.** Mark the index row Live, add the shipped date to the roadmap, write two or three lines
in the guide's "Outcome" section on whether the success criteria were met, add a decision entry if
anything surprising was learned, and ask the owner whether the order of the remaining milestones
still holds.

## How Claude builds: orchestrator and builders

Thinking and building are different jobs and deserve different models. The most capable model
available acts as the **orchestrator**: it interviews, assesses, writes the PRD and the spec,
splits the work, reviews the code, and decides what ships. Faster, cheaper models act as
**builders**: each takes one self-contained work item and implements it. The owner only ever
talks to the orchestrator.

| Role | Model tier | Does | Never does |
|---|---|---|---|
| Orchestrator | The strongest model available (Fable or Opus tier) | Plans, writes PRD and spec, splits work into items, briefs builders, reviews every diff against the spec, fixes docs, ships | Trusts a builder's own report of success |
| Builder | A fast model (Sonnet tier, or Opus for hard items) | Implements one work item from its brief on a branch or worktree, runs the tests it was given, reports what it changed | Touches files outside its brief, changes the spec, merges |

The loop, for every Full-size feature:

1. **Plan.** The orchestrator writes the spec's "Work items" section: independent items, each with
   the files it may touch, the contract it must satisfy, and its done-criteria. Items that touch
   the same files are merged into one or given separate worktrees.
2. **Delegate.** One builder per item, in parallel, each with a self-contained brief: the item, the
   relevant spec sections, `infra.md` pointers, the tripwires, and how to verify. Small features
   (three files or fewer, or nothing parallel) are built by the orchestrator itself; say so.
3. **Review.** The orchestrator reads the combined diff against the spec and the tripwires, runs
   the verify script and the test plan, and lists findings. Only correctness and security findings
   go back to builders; style is fixed inline or noted.
4. **Fix.** Confirmed findings return to the builder that wrote the code, as file-anchored
   instructions. Scope only shrinks in a fix round: no new features, no refactors.
5. **Stop.** At most two review-and-fix rounds. If blockers remain after the second, the
   orchestrator stops and tells the owner: the plan is probably wrong, not the builders.

Done means the verify script passes, the test plan was executed, zero confirmed critical findings,
and the docs are true. Not "the reviewer ran out of things to say".

## Size decides ceremony

| Size | When | Path |
|---|---|---|
| Small | No new screen, table, permission, external service, or money path. Copy changes, styling, bug fixes, small tweaks to an existing feature | Build → QA → Release → Close. Built by the orchestrator directly. Guide updated. No PRD or spec. Noted in the guide's changelog |
| Full | Anything else | All nine stages |

When in doubt, it is Full. The cost of a one-page PRD is an hour; the cost of an unplanned schema
change is a week.

## Branch and release rules

- `main` is production. Every merge to `main` is a release.
- Ship only via git → GitHub → {{HOSTING}}. Never deploy from the command line; never edit
  anything in production by hand.
- Approved PRDs and specs are committed straight to `main` before the branch exists; they are
  documents, and the build must start from an agreed plan.
- One feature per short-lived branch for code. Branch → pull request → merge. Preview deployments come
  free with the pull request; anything behind sign-in is verified on localhost, not on previews.
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
2. Claude writes one idempotent script per change (safe to run twice), named
   `migration/apply-<slug>-<n>-<short>.<ext>` per the stack's tooling.
3. The script is run against the live database before the dependent code merges.
4. The repository's schema file is updated in the same pull request so it always mirrors the live
   database.
5. Removals happen in a separate, later change, after the code that needed the old shape is gone.

## Docs are a merge requirement

The pull request template lists the documents that must be true before merge. A pull request
with an unticked box does not merge. This is not bureaucracy: the documents are how the owner
steers and how the next Claude session understands the system. Docs updated "later" are docs
never updated.

## Commands

| Command | What it does |
|---|---|
| `/new-feature <name>` | Assess, then draft the PRD and spec for a feature, stage by stage with owner approval |
| `/ship <slug>` | Verify locally, prepare the acceptance checklist, open the pull request, merge on approval, close |
| `/status` | Summarise where everything stands from the index and roadmap; list open TBDs |
| `/decision` | Record a decision in the log with reasoning and rejected alternatives |
