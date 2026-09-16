# Tech setup: checklist

Milestone 0. The technical foundation, tracked like a feature but using this checklist in place
of a PRD and spec. Nothing product-specific is built here; the first feature starts after this.

Two lists: what only the owner can do (accounts and connections that need a human and a
password), and what Claude does. The owner's list comes first because Claude's list depends on it.

## Owner-only steps

Claude cannot create accounts, enter passwords, or accept terms on the owner's behalf.

- [ ] In the GitHub account you already have, create an empty repository called `choirhub`. Paste the repository URL into `infra.md` (Accounts and services).
- [ ] In the Vercel account you already have, connect it to that GitHub repository so that `main` deploys to production. Paste the production URL into `infra.md` (Environments).
- [ ] Create a free Supabase project (this is the database and the sign-in in one). Paste its project URL into `infra.md`. Keep the keys somewhere safe; Claude will tell you exactly which environment variable names to paste them under, in `.env.local` locally and in Vercel's environment settings. Claude cannot see or paste them for you.
- [ ] Optional, only if singers should be able to sign in with Google: create a free Google OAuth client and give Supabase the two values it asks for. Email sign-in works without this.
- [ ] Payments: nothing to do. A payments provider account is needed at milestone 3 (membership fees), not now.
- [ ] Tell Claude when these are done.

## Claude's steps

Each step is verified before the next. The result is a running, deployable, testable skeleton
with no product logic.

- [ ] Initialise the Next.js project in this folder, keeping every existing document.
- [ ] Add `.env.example` listing every variable name the stack needs, with empty values. Fill the names into `infra.md` (Environment variables).
- [ ] Connect the database and sign-in. Record the schema file path in `infra.md` (Data model).
- [ ] Create the QA seam: a localhost-only test login and a seeded test user with obviously-marked test data. Record both in `infra.md` (Test identities). Confirm the test login cannot exist in production builds.
- [ ] Create the verify script (one command that checks the build passes and the documentation rules hold: index rows link to existing files, guide changed when source changed, no secret patterns in the diff). Document how to run it in `workflow.md` if the command differs from the default.
- [ ] Security baseline per `docs/playbooks/security.md`: secrets only in the host and `.env.local` with none in repository history, row-level rules default-deny, sign-in expiry, HTTPS and headers, backups on with a restore tried, dependency audit in the verify script, no personal data in logs. Record evidence in `infra.md` (Security baseline).
- [ ] Push to GitHub, confirm Vercel deploys `main`, and walk the live site once.
- [ ] Draw the real sign-in sequence diagram and the initial entity diagram in `infra.md`.
- [ ] CTO pass in setup mode (`docs/playbooks/cto.md`): confirm the stack still fits, fill `infra.md` Operations (where logs are, how backups restore, what to check first), and start `docs/tech-debt.md` if any shortcut was taken.
- [ ] Update this product's `guide.md`, mark milestone 0 Done in the roadmap, mark this row Live in the index. Record any surprising choice as a decision.

## Before this passes

- [ ] `npm run dev` (or the stack's equivalent) shows a page on localhost
- [ ] The production URL shows the same page
- [ ] Test login works locally and is absent from the production build
- [ ] Verify script passes
- [ ] Security baseline in `infra.md` ticked with evidence
- [ ] `infra.md` has no `TBD(claude)` left in Stack, Environments, Identities, or Operations
