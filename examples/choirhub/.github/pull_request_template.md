## What this changes

One or two sentences. Link the feature: `docs/products/<slug>/`. Tags from Assess: has-UI yes/no · risk: none / money / privacy / sign-in / external.

## Size

- [ ] Small (no new screen, table, permission, or money path): guide updated, no PRD or spec needed
- [ ] Full: PRD and spec were approved before this build started

## Merge checklist

Nothing merges with an unticked box. These mirror the rules in `workflow.md`.

- [ ] `docs/products/<slug>/guide.md` describes the feature as it now works
- [ ] `docs/product-index.md` row updated (stage, links)
- [ ] `docs/roadmap.md` updated if a milestone changed state
- [ ] `infra.md` updated if the stack, data model, a key flow, or an external service changed
- [ ] Any database change is additive, was applied to the live database before this merge, and is mirrored in the schema file
- [ ] `docs/products/<slug>/qa.md` has a completed run with evidence per line; zero open blockers
- [ ] Verified locally: build passes, verify script passes
- [ ] Design approved and every screen matches its mockup (features with a screen)
- [ ] Security diff checklist completed in the QA run (risk-tagged features)
- [ ] AI evaluation set run and passing; fallback and correction paths tested (features with AI)
- [ ] `docs/design/system.md` updated if a token or component was added
- [ ] `docs/qa/regression.md` gets this feature's golden path at Close
- [ ] Owner has accepted the feature against the PRD's success criteria (Full size only)
- [ ] No secrets, tokens, keys, or real personal data in the diff or in any document
- [ ] PRD and spec were not edited to match the build (corrections go in the guide)
