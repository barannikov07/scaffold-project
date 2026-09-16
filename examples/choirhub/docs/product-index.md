# Product index: ChoirHub

The status dashboard. One row per feature, updated at every stage transition. If this table and
reality disagree, reality is wrong until the table is fixed in the same change.

Stages: Idea · Planned · PRD · Design · Spec · In build · In QA · Live · Deprecated · Dropped
(Planned means assessed with a go; Later means assessed and deferred.)

| Feature | Purpose | Milestone | Size | Tags | Stage | PRD | Design | Spec | Guide | Updated |
|---|---|---|---|---|---|---|---|---|---|---|
| Tech setup | Make the project runnable, deployable, and testable | 0 | Full | no UI · sign-in | Planned | [checklist](products/tech-setup/checklist.md) | — | same | [guide](products/tech-setup/guide.md) | 2026-09-16 |
| Rehearsals and replies | Plan a rehearsal, collect coming or not coming from every singer, see the list before the night | 1 | Full | has-UI · privacy · sign-in · external service | Design | [prd](products/rehearsals-and-replies/prd.md) | [design](products/rehearsals-and-replies/design.md) | [spec](products/rehearsals-and-replies/spec.md) | [guide](products/rehearsals-and-replies/guide.md) | 2026-09-16 |

## How to read this

- A feature is a unit of build with its own PRD, design (if it has a screen), spec, QA runs, and guide.
- Tags: has-UI decides whether the Design stage exists; risk tags (money, privacy, sign-in,
  external service) decide whether the security passes run. A milestone in the roadmap can
  contain several features.
- Small-size changes to a live feature do not get a row; they are noted in that feature's guide
  changelog.
- Open questions across all documents are found by searching for `TBD(`. `/status` lists them.
