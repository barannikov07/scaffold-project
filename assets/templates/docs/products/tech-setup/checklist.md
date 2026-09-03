# Tech setup: checklist

Milestone 0. The technical foundation, tracked like a feature but using this checklist in place
of a PRD and spec. Nothing product-specific is built here; the first feature starts after this.

Two lists: what only the owner can do (accounts and connections that need a human and a
password), and what Claude does. The owner's list comes first because Claude's list depends on it.

## Owner-only steps

Claude cannot create accounts, enter passwords, or accept terms on the owner's behalf.

- [ ] In your GitHub account (create one first if you have none), create an empty repository named after the project. Paste the repository URL into `infra.md` (Accounts and services).
- [ ] In your {{HOSTING}} account (create one first if you have none), connect it to the GitHub repository so that `main` deploys to production. Paste the production URL into `infra.md` (Environments).
- [ ] Create the {{DATABASE}} project. Paste its project URL into `infra.md`. Keep the keys; Claude will tell you exactly which environment variable names to paste them under, in `.env.local` locally and in {{HOSTING}}'s environment settings.
- [ ] TBD(owner): payments provider account, if money moves.
- [ ] Tell Claude when these are done.

## Claude's steps

Each step is verified before the next. The result is a running, deployable, testable skeleton
with no product logic.

- [ ] Initialise the {{FRAMEWORK}} project in this folder, keeping every existing document.
- [ ] Add `.env.example` listing every variable name the stack needs, with empty values. Fill the names into `infra.md` (Environment variables).
- [ ] Connect the database and sign-in. Record the schema file path in `infra.md` (Data model).
- [ ] Create the QA seam: a localhost-only test login and a seeded test user with obviously-marked test data. Record both in `infra.md` (Test identities). Confirm the test login cannot exist in production builds.
- [ ] Create the verify script (one command that checks the build passes and the documentation rules hold: index rows link to existing files, guide changed when source changed, no secret patterns in the diff). Document how to run it in `workflow.md` if the command differs from the default.
- [ ] Push to GitHub, confirm {{HOSTING}} deploys `main`, and walk the live site once.
- [ ] Draw the real sign-in sequence diagram and the initial entity diagram in `infra.md`.
- [ ] Fill `infra.md` Operations: where logs are, how backups work.
- [ ] Update this product's `guide.md`, mark milestone 0 Done in the roadmap, mark this row Live in the index. Record any surprising choice as a decision.

## Before this passes

- [ ] `npm run dev` (or the stack's equivalent) shows a page on localhost
- [ ] The production URL shows the same page
- [ ] Test login works locally and is absent from the production build
- [ ] Verify script passes
- [ ] `infra.md` has no `TBD(claude)` left in Stack, Environments, Identities, or Operations
