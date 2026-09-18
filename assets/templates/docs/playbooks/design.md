<!-- Playbook: design. Canonical text; the .claude/skills and .codex/skills wrappers point here. -->

# Design system

One rule governs how anything looks: every screen is built from the design system, and when a
screen needs a component or token the system lacks, it is added to the system first, then used.
No one-off UI. There is no design stage and there are no mockups: the PRD says which screens
exist, the spec designs every state, and the owner sees real screens on the pull request preview.

This playbook runs at three moments in a project's life: at tech setup, to create the system with
the owner; during build, whenever a screen needs something the system lacks; and before the
owner's acceptance look, to critique the built screens. It also runs on its own when the owner
says "design", "design system", "what will it look like", "make it beautiful", or "add a
component". Calibrate every message to the owner profile in `AGENTS.md`: explain once per
project, default to less.

Read first: `docs/design/system.md`, `AGENTS.md`, and the feature's `spec.md` when there is one.

## 1. Tech setup: create the system with the owner

If `docs/design/system.md` still has `TBD(owner)` lines, the project has no design system yet.
Ask the owner five questions, one at a time, each with an example and a "you decide":

1. Three adjectives for how it should feel. ("calm, warm, precise")
2. Two apps or sites whose look they admire, and one they dislike.
3. Light, dark, or both.
4. Tone of voice in the interface. ("friendly and brief", "formal")
5. Accessibility floor. Default: readable on a phone in sunlight, usable with one thumb, WCAG AA
   contrast.

Then fill `docs/design/system.md`: palette as tokens, type pairing, spacing, radius, motion,
components, copy rules. The choices that make it look designed rather than generated:

- One accent colour, used for the primary action and nothing else. Neutrals carry the rest.
- A display face with character paired with a quiet body face. Not the framework default, not
  the same face everywhere.
- A spacing scale (4, 8, 12, 16, 24, 32, 48) and one radius. Use them everywhere; never eyeball.
- Real hierarchy: one thing on each screen is clearly the most important.
- Whitespace is a feature. When a screen feels crowded, remove; do not shrink.
- Motion only where it explains something: a state change, an arrival. Under 250 ms.
- Dark and light are both designed, not inverted.

Make it real code in the same step, in the stack's idiom: the tokens as variables the whole app
reads; the base components from the Components table (top bar, list row, empty state, form
field, primary and secondary button, segmented control, confirmation card, banner, skeleton,
bottom tabs, sheet, toast); and a gallery page that renders every component in every state, light
and dark, at phone width. The gallery is reachable on localhost and in preview builds only, never
in production. It is how the owner sees the system before any feature exists and how a future
session checks a component without reading its code.

Show the owner the gallery, iterate until it feels like their three adjectives, and record the
system as a decision (type product) with the adjectives and references, so a future session knows
why the palette is what it is.

## 2. Describing a screen, for the PRD and the spec

The PRD's Screens section is one line per screen in the owner's words: what it is for and the
one thing the user does there. Written to be pictured, not parsed: "the week view, where the
conductor sees who is coming and taps a rehearsal to change it", not "rehearsal list view".
This list is the owner's main say in how the product will look, so it goes to them with the PRD
and changes with their answer.

The spec's Screens section is the design:

- **Screens.** One row each: name, purpose, how the user gets there, the one primary action.
  Screen names are the contract; the build and the QA run use them verbatim.
- **States.** Every screen's empty, loading, error, success, and permission-denied states. If the
  feature has an AI step: thinking, streaming, "here is what I understood, correct me", and the
  manual fallback. A state that is not written down will be improvised in code, badly.
- **Copy.** The real words: titles, buttons, empty-state lines, error messages, in the design
  system's tone. No placeholder text anywhere.
- **Responsive and accessible.** Phone first (390 px), then what changes at desktop width. Focus
  order, labels, 44 px touch targets, contrast checked.
- **Components.** Everything above named against the Components table in `system.md`. Anything
  missing is listed there so the build adds it to the system before the screen uses it.

## 3. Build: add to the system first, then use it

When a work item needs a component or token the system lacks:

1. Prefer composing what exists. A new component earns its place by being needed in a way no
   composition covers, not by being convenient.
2. Add it to the app's component set and to the gallery, in every state, light and dark, at
   phone width, on the tokens and the spacing scale. Name it in the product's words.
3. Add its row to the Components table in `docs/design/system.md` and a changelog row, in the
   same change.
4. Then use it in the screen.

A component used by one screen is still a component, with a row and a gallery entry. There is no
"just this once": a one-off style is how a product stops looking like one product.

## 4. Critique before the owner looks

Before the owner's acceptance walk, open each built screen on localhost or the preview and walk
it against this list; fix what fails. Do not show the owner a screen that fails a line here.

1. The primary action is obvious within two seconds.
2. The screen says where the user is and what just happened.
3. Words match the owner's domain, not the system's ("rehearsal", not "event record").
4. Every destructive action has an undo or a confirmation, and anything that can be created
   can be corrected before it matters.
5. The same thing looks the same everywhere; different things look different. Nothing on the
   screen is outside the design system.
6. Errors are prevented before they are reported.
7. Nothing requires remembering something from another screen, and every value shown on any
   screen has a screen where it is entered. Check this across the set, not screen by screen.
8. Text is readable at arm's length on a phone; contrast meets the floor.
9. Touch targets are big enough for a thumb.
10. The empty state teaches what to do first.
11. Every state in the spec's Screens section is reachable and looks designed.

If the agent has a design critique or accessibility review skill, run it on the built screens
too and fold its findings in. If the agent has a skill that runs the app and takes screenshots,
attach one screenshot per screen and state to the QA run.

## 5. The owner's look

The owner sees the screens for the first time at acceptance, on the preview link (anything
public) or on localhost (anything behind sign-in). Tell them which screens to look at in what
order and the two or three questions you want their reaction on, calibrated to the profile: a
beginner gets "tap the blue button, that is what a singer would do"; a product manager gets the
screen list. A screen the owner sends back is ordinary work: nothing is in production, and the
fix goes on the same branch. Iterate until "accepted".

## Rules

- Every screen is composed from the design system. Anything new goes into the system first: the
  app's component set, the gallery, and the Components table, in the same change.
- The design system is living. A feature that adds a component or a token adds a changelog row;
  the Close stage checks it.
- The system is real code. `docs/design/system.md` describes it; the app and the gallery are it.
  When they disagree, the code is fixed or the document is, in the same change, never neither.
- Never skip the state list for a feature with a screen because it "is small". Small features
  have no new screen by definition; if there is a new screen, the feature is Full.
