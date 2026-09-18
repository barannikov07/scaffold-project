# Filling guide: what to write in each file after stamping

The stamping script fills names and dates. The substance comes from the interview and from you.
Go file by file. Where the interview gave nothing, leave the `TBD(owner):` line and move on; do
not invent. The `TBD(claude):` lines are yours to fill now if you can, or to leave for the tech
setup task if they need the running system.

## AGENTS.md

- The purpose line is the owner's one-sentence answer, lightly edited.
- Tripwires are passed to the stamping script as `TRIPWIRES`, one line each, and the script
  writes "None yet" when the value is omitted. The interview questions on data that must not be
  lost or seen, and on money, are the usual sources. Format:
  `- Payment records are append-only, never edited or deleted → infra.md (Data model)`.
  The template already says the reasoning lives in the decisions log; put it in D-003.
- Owner profile: the two interview answers, stamped as `TECH_LEVEL` and `PRODUCT_LEVEL`. Use
  the owner's own words if they gave a fuller answer ("I built a Shopify store once") rather
  than forcing the three labels; the table in workflow.md is read by column, and a fresh session
  can map a sentence to a column.
- Directory map: keep as is; it describes the scaffold accurately.

## docs/vision.md

Draft every section from the interview, in the owner's words where possible, and say plainly in
the hand-off that it is a first draft for them to react to. The end state comes from question 3;
push it to the ambitious version. Principles are the trade-off rules you heard between the lines
("must be simple for tenants", "never lose a payment"). Non-goals are what the owner said they do
not want, plus one or two obvious temptations you would rule out. "How we know we have won"
comes from the follow-up "what would make it worth building?". If the owner's answers describe a
workflow full of tedious steps, propose one principle of the form "the app does the tedious part;
the person keeps the decision", and mark it as a suggestion; it is what makes the applied-AI
pass fit the vision later.

## docs/roadmap.md

- Current focus: two or three sentences: tech setup first because nothing can ship without it,
  then the first feature because it is the smallest thing the owner can use.
- Milestone 1's "done when" is one observable sentence, the same as the first success criterion
  you expect the PRD to carry.
- Add milestones 2 and up only if the owner described them, including capabilities named in
  their end-state answer. One line each, status Later, Features and Shipped columns empty. The
  "Done when" column is filled even for Later rows, since it is what makes the milestone a
  milestone rather than a wish. Example row:
  `| 2 | Attendance record | Who actually turned up is recorded and cannot be changed afterwards | Later | | |`

## docs/product-index.md

Two rows. The first feature's purpose is one line. Both rows Planned. The Tags column for the
first feature stays TBD until Assess sets has-UI and the risk tags; do not guess it. Leave PRD, spec, and
guide links pointing at the stamped files; they exist.

## docs/decisions.md

- D-001: the stack, with the reason for each part from the interview reference, and what was
  rejected. If the owner already had accounts or preferences, say those decided it.
- D-002 is complete as stamped.
- D-003, only if tripwires exist: what the invariants are, why each is cheap now and expensive
  to retrofit, and what was rejected (usually "remember it during review").

## infra.md

Fill Stack at a glance (the "why" column, one line each), Environments (production URL stays
TBD until the owner has it), Accounts and services (the exact accounts the chosen stack needs),
Roles inside the app (from the users question), and the tripwire-related lines under Data model.
Environment variable names: fill them if you know the stack's standard names (for Supabase and
Next.js you do), otherwise leave the TBD for tech setup. Diagrams and the Operations section
(logs, backups) stay as `TBD(claude)` for the tech setup task; they need the running system.

## docs/design/system.md and docs/qa/regression.md

Leave both as stamped. The design system is filled by the design-system playbook, with the owner,
at tech setup (milestone 0); guessing a palette now would be invented. The regression list
is empty until the first feature ships.

## docs/products/<first-feature>/prd.md

Do not fill it during the scaffold. It is created empty from the template on purpose; the
new-feature flow fills it with the owner in the loop, right after the scaffold commit.

## docs/products/tech-setup/checklist.md

Adapt the owner-only steps to what the owner already has: if they said they have a GitHub or
hosting account, say so in the line rather than telling them to create one. Replace the payments
line with "nothing yet; a <provider> account is needed at milestone <n>" if money moves later, or
remove it if money never moves. An owner-only checklist must contain only things the owner can
actually do today.

## Consistency pass before committing

- Milestone rows in the roadmap match feature rows in the index (names, numbers, links).
- The decision IDs cited in the vision changelog and roadmap changes exist in the log.
- Every `{{` is gone. Every remaining `TBD(` has an owner and a question.
- Every relative link in AGENTS.md, the index, and the roadmap resolves.
