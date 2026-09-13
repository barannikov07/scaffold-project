---
name: scaffold-project
description: Scaffold a brand-new project's documentation and product process the way a top-tier product builder at a top-tier company would, for a non-technical owner who builds with Claude. Docs and process only, no application code. Interviews the owner in plain language, then creates the router AGENTS.md, vision, roadmap, product index, decisions log, workflow (idea → assess → PRD → spec → migrate → build → QA → release → close), infra.md, PR checklist, PRD/spec/guide templates, and the /new-feature, /ship, /status, /decision playbooks for Claude Code and Codex, commits them in one commit, and moves straight into the first PRD. Use this whenever the user wants to start a new project, app, product, or repository from scratch, or asks to "scaffold", "bootstrap", "set up the docs", "set up the process", "kick off a new project", or wants a vision doc, roadmap, or PRD for something that does not exist yet, even if they never say the word scaffold.
---

# Scaffold a project

You are setting up a NEW project for someone who may not be technical. When you are done they
will have a folder of documents that lets any future Claude session build the product the way a
strong product team would: a north-star vision, an ordered roadmap, a status dashboard, a decision
log, a written process with gates, and the technical knowledge base. No application code is
created here. The technical setup becomes the first tracked task inside the process.

Read `references/principles.md` once before starting. It explains why the structure is shaped the
way it is, so you can defend it to the owner and fill the files with intent rather than filler.

## The flow

### 1. Check the target folder

Work in the current working directory unless the owner names another. If the folder already
contains files other than `.git`, stop and show what is there before writing anything. This skill
creates a fresh scaffold; it must not overwrite someone's existing work.

### 2. Interview the owner

Follow `references/interview.md`. Ask one question at a time, in plain language, with an example
answer and a "you decide" option. Do not ask for a "stack"; ask what the product does, who uses it,
whether people sign in, whether it stores data, whether money moves, and what the first thing to
build is. You translate those answers into technical choices, not the owner.

Roughly eight questions, plus two at the start about the owner: how technical they are and how
familiar with product work. Those two set the explanation depth for the whole project and go
into the owner profile in AGENTS.md. Stop early if the owner gives you everything in one go.

### 3. Decide the stack and state it back

Use the decision guide at the end of `references/interview.md`. Pick a default when the owner says
"you decide". State the choice back in one plain sentence with a one-line reason for each part. The
reasoning goes into the decisions log as D-001, so it is never lost.

### 4. Show the summary and get one confirmation

Before creating anything, show a short plain-English summary: project name, purpose, the stack in
one sentence, the first feature, and the list of documents you will create with a five-word
purpose each. Not a file tree; a non-technical owner cannot read a file tree. Ask one yes/no
question, then proceed.

### 5. Stamp the templates

Run the stamping script. It copies every template into the target folder and fills the
placeholders it knows. Anything unknown becomes a marked TBD.

```bash
python3 <skill-dir>/scripts/scaffold.py --target <project-dir> \
  --set PROJECT_NAME="..." --set PURPOSE="..." --set OWNER="..." \
  --set FRAMEWORK="..." --set DATABASE="..." --set AUTH="..." --set HOSTING="..." \
  --set FIRST_FEATURE_NAME="..." --set FIRST_FEATURE_SLUG="..." \
  --set TECH_LEVEL="never coded | understands, doesn't code | reads code" \
  --set PRODUCT_LEVEL="new to product work | worked with PMs | product manager" \
  --set TRIPWIRES="- <invariant> → infra.md (<section>)
- <invariant> → infra.md (<section>)"
```

`DATE` is filled automatically. Pass `TRIPWIRES` whenever the interview surfaced a hard
invariant (data that must never be lost or edited, data that must never be seen by the wrong
person, money rules); one line each, arrow to the owning doc. Omit it only when there are none,
and the script writes "None yet". The script refuses to overwrite existing files, and it copies
the product template into `docs/products/<first-feature-slug>/`.

### 6. Fill the content that needs judgment

The templates carry structure and quality bars; you supply the substance. Follow
`references/filling-guide.md` file by file. The important ones:

- `docs/vision.md`: draft the end state, audience, principles, and non-goals from the interview.
  Write it as a first draft for the owner to react to, and say so.
- `docs/roadmap.md`: milestone 0 is "Tech setup", milestone 1 is the first feature. Add later
  milestones only if the owner described them; each is one line.
- `docs/product-index.md`: two rows, tech setup and the first feature.
- `docs/decisions.md`: D-001 stack choice with reasoning, D-002 adopting this process, and
  D-003 with the reasoning behind the tripwires if there are any (the tripwire lines themselves
  are one-liners and have nowhere else to hold the why).
- `infra.md`: stack, environments, the accounts the owner will need, env var names for the chosen
  stack. Data model and key flows stay as placeholders for the tech setup task.
- `AGENTS.md`: the map paragraph and directory map. Check the tripwire block reads well and
  points at the right `infra.md` sections.

Never invent facts. A TBD is written as `TBD(owner): <the question>` so it can be found and
answered later. Every fact lives in exactly one document; if you are about to write the same fact
twice, link instead.

### 7. Commit

Initialise git if the folder is not a repository. Make one commit on `main`:

```
docs: project scaffold (process, index, roadmap, workflow)
```

Do not push. Pushing needs a remote the owner has to create.

### 8. Hand off and start the first PRD

Tell the owner, in this order, then wait for their reaction to the vision before drafting the
PRD (the vision-fit section depends on it):

1. What was created, in three or four sentences.
2. The human-only checklist from `docs/products/tech-setup/checklist.md`: accounts to create,
   the GitHub repository, the hosting connection. You cannot do these for them.
3. That the next step is the PRD for the first feature, and that you are starting it now.

Then run the new-feature flow from the freshly created `docs/playbooks/new-feature.md`
for the first feature, with the reacted-to vision as the prism. The PRD draft
stays uncommitted until the owner approves it; approved plans are committed straight to `main`,
as the new-feature flow describes.

## Writing rules for every generated document

- Plain language first. Each section that carries technical detail opens with one sentence a
  non-technical owner understands, then the detail. Technical terms get a short gloss in
  parentheses the first time they appear in a file.
- Calibrate to the owner profile from the moment it is known, including during this scaffold.
  A beginner gets the "why" of each step once; a product manager gets the step and the question.
  Overexplaining to a senior owner is as much a failure as underexplaining to a beginner.
- Who does what is explicit. The owner decides, approves, accepts, and releases. Claude drafts,
  builds, verifies, and keeps docs true. Say which is which wherever a step needs a person.
- Quality bars stay in the files. Each template ends with a "Before this passes" checklist. Leave
  those in place; they are how future sessions know when a document is good enough.
- Dates are absolute, ISO format. No "next week".

## Before you finish

- Every placeholder is filled or converted to a `TBD(owner):` line. Search for `{{` outside
  `docs/products/_template/` to be sure; that folder keeps its placeholders on purpose.
- `AGENTS.md` links resolve to files that exist.
- The product index, roadmap, and decisions log agree with each other.
- One commit exists on `main` with the message above.
- The owner has the human-only checklist and knows the first PRD is starting.
