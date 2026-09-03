# Decisions: {{PROJECT_NAME}}

Append-only. A decision earns an entry when a future owner or a fresh Claude session would
otherwise wonder "why is it like this?": stack choices, scope cuts, vision amendments, roadmap
reorders, tripwires, anything hard to reverse. Reversals are new entries that supersede the old
one; nothing is edited or deleted.

Format: ID · date · type (product / tech / process / scope) · status (Active / Superseded by D-nnn).
One paragraph: what was decided, why, and what was rejected.

---

## D-001 · {{DATE}} · tech · Active

**Stack: {{FRAMEWORK}}, {{DATABASE}}, {{AUTH}}, hosted on {{HOSTING}}.**

TBD(claude): why each part was chosen given the interview answers, and what was rejected
(for example a separate auth provider, a different host, a native app). Note anything the owner
already had that decided the choice.

## D-002 · {{DATE}} · process · Active

**Adopt the documented product process, planning stack, and deploy rules.**

The project follows the nine-stage pipeline in `workflow.md` with size-tiered ceremony, keeps
PRDs and specs as records once built, guides living, the roadmap fluid, treats docs as a merge requirement, ships only via git to
{{HOSTING}}, and tracks work in the four-altitude planning stack (vision, roadmap, product index,
decisions). Rejected: ad-hoc building without written plans, which is fast for a week and
unrecoverable after a month; a single "status" document mixing plan, history, and reasoning,
which drifts.
