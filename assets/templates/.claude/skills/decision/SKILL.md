---
name: decision
description: Record a decision in the append-only decisions log with its reasoning, the alternatives rejected, and links from the documents it affects. Use whenever a choice is made that a future session would otherwise wonder about: stack or tool choices, scope cuts, vision changes, roadmap reorders, new tripwires, anything hard to reverse. Trigger when the owner says "let's decide", "we'll go with", "record that", or when you notice such a choice being made in conversation.
---

# Decision

Append one entry to `docs/decisions.md`. Never edit or delete an existing entry; a reversal is a
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
- If it creates a hard invariant: add a tripwire line in `CLAUDE.md` pointing to the owning doc.
- If it explains something odd in the system: add a line under `infra.md` Constraints and gotchas.

Confirm to the owner in one sentence what was recorded and where it is linked from.
