<!-- Playbook: decision. Canonical text; the .claude/skills and .codex/skills wrappers point here. -->

# Decision

Append one entry to `docs/decisions.md`.
Calibrate every message to the owner profile in `AGENTS.md` (see workflow.md, "How Claude
talks to the owner"): explain once per project, default to less. Never edit or delete an existing entry; a reversal is a
new entry that marks the old one "Superseded by D-nnn".

## Entry

Next ID in sequence. Format:

```
## D-nnn · YYYY-MM-DD · product|tech|process|scope · Active

**One-sentence statement of the decision.**

One paragraph: why, what was rejected and why, and what it affects.
```

## Then link it

- If it amends the vision: edit `docs/vision.md` accordingly and add a changelog row citing the ID.
- If it reorders or drops roadmap items: update `docs/roadmap.md` and add a Changes row.
- If it creates a hard invariant: add a tripwire line in `AGENTS.md` pointing to the owning doc.
- If it explains something odd in the system: add a line under `infra.md` Constraints and gotchas.

Confirm to the owner in one sentence what was recorded and where it is linked from.
