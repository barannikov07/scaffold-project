<!-- Playbook: qa. Canonical text; the .claude/skills and .codex/skills wrappers point here. -->

# QA

Prove the feature works the way the PRD, the design, and the spec say, before the owner is asked
to accept it. Runs at stage 8, called by the ship playbook; also on its own mid-build when the
owner says "test it", "QA", "does it work", or "check everything". Calibrate every message to the
owner profile in `AGENTS.md`.

Read first: the feature's `spec.md` (test plan, permissions, AI components), `design.md`
(states), `AGENTS.md` (tripwires), `docs/qa/regression.md`, and the PRD's success criteria.

## 1. Write and execute the run

Create or append to `docs/products/<slug>/qa.md`: one run per attempt, dated, with the sections
below as tables of line · steps · expected · result · evidence. Every line is executed and its
evidence written down (what was on screen, what the database held). A line nobody executed is
not a pass; it is a lie in a document, and the owner will find it in production.

Prefer a skill that runs the app and takes screenshots; otherwise run the app locally and walk
each line by hand in the browser. Never mark a line from reading the code.

| Section | What it covers | Source |
|---|---|---|
| Functional | Every line of the spec's test plan: the happy path and each edge case | spec.md |
| Permissions | One row per role and action from the spec's permission table; every "denied" is actually denied, including by direct request, not only by a hidden button | spec.md |
| Tripwires | One check per tripwire line in AGENTS.md that this feature could touch | AGENTS.md |
| Design conformance | Each screen against its mockup; each state in design.md reachable and correct | design.md |
| Responsive | Every screen at 390 px and at desktop width | design.md |
| Accessibility floor | Keyboard reaches everything; labels present; contrast at the floor; 44 px targets | design system |
| Data safety | The QA guardrail in workflow.md was followed; test records carry the TEST- marker | workflow.md |
| Regression | Every golden path in docs/qa/regression.md still passes | regression.md |
| AI components | The evaluation set runs and passes; the fallback works with the model unavailable; the correction path works | spec.md |
| Security | The diff checklist from the security playbook, when the feature is risk-tagged | security.md |

Small-size changes use the short form: Functional, Tripwires, Regression.

## 2. Triage

Every failed line is one of two things:

- **Blocker**: breaks a success criterion, a tripwire, or a permission; loses or exposes data;
  crashes. Fixed before anything else, then the affected section is re-run from the top.
- **Later**: cosmetic, or an edge the PRD did not promise. One line in the roadmap under Later,
  linked to this run. Never silently dropped.

## 3. Exit criteria

The run is complete when all of these hold; only then does the owner get the acceptance
checklist:

- Every functional line executed with evidence.
- Permission matrix complete; every denied action denied.
- Every tripwire check green.
- Regression green.
- Zero open blockers.

## 4. The owner's acceptance checklist

Turn the PRD's success criteria into numbered steps the owner can follow: where to click, what to
type, what should appear. Calibrate to the profile: a beginner gets every tap; a product manager
gets the criteria. Say where to run it: localhost for anything behind sign-in, the preview link
for anything public. The owner replies "accepted" or lists issues; issues are triaged the same
way.

## 5. At Close

Append the feature's golden path to `docs/qa/regression.md`: the shortest sequence of steps that
proves the feature works, with the expected result. Every later QA run walks it.
