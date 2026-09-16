<!-- Playbook: design. Canonical text; the .claude/skills and .codex/skills wrappers point here. -->

# Design

Turn an approved PRD into something the owner can see and approve before any code exists. Runs
at stage 4 for every feature with a screen, called by the new-feature playbook; also runs on its
own when the owner says "design", "mockup", "what will it look like", or "make it beautiful".
Calibrate every message to the owner profile in `AGENTS.md`: explain once per project, default to
less.

Read first: the feature's `prd.md`, `docs/design/system.md`, `AGENTS.md`.

## 1. First run only: create the design system

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
  the same face everywhere. Pick from Google Fonts so mockups and app can both load it.
- A spacing scale (4, 8, 12, 16, 24, 32, 48) and one radius. Use them everywhere; never eyeball.
- Real hierarchy: one thing on each screen is clearly the most important.
- Whitespace is a feature. When a screen feels crowded, remove; do not shrink.
- Motion only where it explains something: a state change, an arrival. Under 250 ms.
- Dark and light are both designed, not inverted.

Record the design system as a decision (type product) with the owner's adjectives and references,
so a future session knows why the palette is what it is.

## 2. Write `design.md` for the feature

The feature's `design.md` was stamped from the template. Fill it from the PRD's flows:

- **Screens.** One row each: name, purpose, how the user gets there, the one primary action.
  Screen names are the contract; the spec and the build use them verbatim.
- **Flows on screens.** The PRD's flows mapped onto screens, step by step.
- **States.** Every screen's empty, loading, error, success, and permission-denied states. If the
  feature has an AI step: thinking, streaming, "here is what I understood, correct me", and the
  manual fallback. A state that is not designed will be improvised in code, badly.
- **Copy.** The real words: titles, buttons, empty-state lines, error messages, in the design
  system's tone. No placeholder text anywhere.
- **Responsive.** Phone first (390 px), then what changes at desktop width.
- **Accessibility.** Focus order, labels, 44 px touch targets, contrast checked.

## 3. Build the mockups

One static HTML file per screen in `docs/products/<slug>/mockups/`, plus `index.html` that
links them all with a one-line description each.

- Start every file from `docs/design/mockup-base.html`. It carries the tokens as CSS variables
  and a phone frame. Its token block is replaced with the design system's values once, on the
  first run, so every later mockup inherits them.
- Real copy from `design.md`, real-looking data from the product's domain, never lorem ipsum.
- States are extra phone frames in the same file, or separate files suffixed `-empty`, `-error`.
- No frameworks, no build step, no JavaScript beyond toggling a state. These are pictures that
  happen to be HTML; they are never imported into the app.
- If the agent has a design canvas skill, also publish the screens there so the owner can nudge
  elements directly. The HTML files remain the record.

## 4. Critique before showing

Walk each screen against this list and fix what fails. Do not show the owner a screen that fails
a line here.

1. The primary action is obvious within two seconds.
2. The screen says where the user is and what just happened.
3. Words match the owner's domain, not the system's ("rehearsal", not "event record").
4. Every destructive action has an undo or a confirmation.
5. The same thing looks the same everywhere; different things look different.
6. Errors are prevented before they are reported.
7. Nothing requires remembering something from another screen.
8. Text is readable at arm's length on a phone; contrast meets the floor.
9. Touch targets are big enough for a thumb.
10. The empty state teaches what to do first.

If the agent has a design critique or accessibility review skill, run it on the mockups too and
fold its findings in.

## 5. Show the owner, iterate, approve

Tell the owner how to open `mockups/index.html` in a browser, which screens to look at in what
order, and the two or three questions you want their reaction on. Calibrate to the profile: a
beginner gets "tap the blue button, that is what a singer would do"; a product manager gets the
screen list.

Iterate until the owner says "approved". Record the date in `design.md`, tick the checklist, set
the index row to stage Design, and commit the design and mockups to `main`
(`docs(<slug>): design`).

## Rules

- Design is a record once the build starts, like the PRD. Deviations discovered in build go in
  the guide's "Where it differs from the plan"; a new direction is a new numbered design file.
- The build matches the mockup. The orchestrator's review compares screen by screen.
- The design system is living. A feature that adds a component or a token updates
  `docs/design/system.md` in the same change, with a changelog row.
- Never skip Design for a feature with a screen because it "is small". Small features have no
  new screen by definition; if there is a new screen, the feature is Full.
