## What this changes

One or two sentences. Link the feature: `docs/products/<slug>/`.

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
- [ ] Verified locally: build passes, verify script passes, test plan from the spec executed
- [ ] Owner has accepted the feature against the PRD's success criteria (Full size only)
- [ ] No secrets, tokens, keys, or real personal data in the diff or in any document
- [ ] PRD and spec were not edited to match the build (corrections go in the guide)
