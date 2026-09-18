# Product index: {{PROJECT_NAME}}

The status dashboard. One row per feature, updated at every stage transition. If this table and
reality disagree, reality is wrong until the table is fixed in the same change.

Stages: Idea · Planned · PRD · Spec · In build · In QA · Live · Deprecated · Dropped
(Planned means assessed with a go; Later means assessed and deferred.)

| Feature | Purpose | Milestone | Size | Tags | Stage | PRD | Spec | Guide | Updated |
|---|---|---|---|---|---|---|---|---|---|
| Tech setup | Make the project runnable, deployable, and testable | 0 | Full | no UI · sign-in | Planned | [checklist](products/tech-setup/checklist.md) | same | [guide](products/tech-setup/guide.md) | {{DATE}} |
| {{FIRST_FEATURE_NAME}} | TBD(claude): one line from the interview | 1 | Full | TBD(claude): has-UI · risk tags, set at Assess | Planned | [prd](products/{{FIRST_FEATURE_SLUG}}/prd.md) | [spec](products/{{FIRST_FEATURE_SLUG}}/spec.md) | [guide](products/{{FIRST_FEATURE_SLUG}}/guide.md) | {{DATE}} |

## How to read this

- A feature is a unit of build with its own PRD, spec, QA runs, and guide.
- Tags: has-UI decides whether the PRD lists screens, the spec designs their states, and QA runs
  the screen checks; risk tags (money, privacy, sign-in,
  external service) decide whether the security passes run. A milestone in the roadmap can
  contain several features.
- Small-size changes to a live feature do not get a row; they are noted in that feature's guide
  changelog.
- Open questions across all documents are found by searching for `TBD(`. `/status` lists them.
