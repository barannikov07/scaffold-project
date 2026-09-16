# Design system: {{PROJECT_NAME}}

The single source of visual and verbal truth. Mockups and app code both take their tokens from
here. Created empty by the scaffold; the design playbook fills it with the owner at the first
feature that has a screen. Living: changes land with the feature that needs them, with a
changelog row.

## Feel

- Three adjectives: TBD(owner)
- References we admire: TBD(owner)
- A reference we do not want to look like: TBD(owner)
- Light, dark, or both: TBD(owner)
- Tone of voice: TBD(owner)
- Accessibility floor: readable on a phone in sunlight, usable with one thumb, WCAG AA contrast

## Tokens

Named so that mockups and code use the same words.

| Token | Light | Dark | Used for |
|---|---|---|---|
| bg | TBD(claude): filled by the design playbook | | Page ground |
| surface | | | Cards, sheets |
| ink | | | Primary text |
| ink-muted | | | Secondary text, labels |
| line | | | Borders, dividers |
| accent | | | The primary action, and nothing else |
| accent-soft | | | Selected states, highlights |
| success / warning / danger | | | Semantic only, never decorative |

## Type

| Role | Face | Sizes |
|---|---|---|
| Display | TBD(claude): a face with character, from Google Fonts | 32 / 24 / 20 |
| Body | TBD(claude): a quiet face that pairs with it | 16 / 14 |
| Mono | For codes, amounts, IDs | 14 |

Line height 1.5 for body, 1.15 for display. Never more than two faces on a screen.

## Spacing, radius, motion

- Spacing scale: 4, 8, 12, 16, 24, 32, 48. Nothing in between.
- Radius: TBD(claude): one value (8 is a safe default), doubled for sheets.
- Motion: 150 to 250 ms, ease-out, only for state changes and arrivals. Respect reduced motion.

## Components

One row per component the product uses. Add rows as features add components.

| Component | When to use | Rules |
|---|---|---|
| Primary button | The one main action on a screen | Accent fill, one per screen |
| Secondary button | Everything else | Outline, ink text |
| List row | Any list of records | 56 px tall; the whole row is the tap target |
| Empty state | Any list with nothing in it | One sentence of what to do first, plus the primary action |
| Form field | Any input | Label above, helper below, error replaces helper |
| Confirmation card | Anything AI proposes, anything destructive | Shows exactly what will happen; Confirm and Edit |

## Copy rules

- Sentence case everywhere. No exclamation marks.
- Buttons are verbs: "Create rehearsal", not "Submit".
- Errors say what happened and what to do next, in one line.
- Speak the owner's domain: TBD(owner): three words that must be used and three that must not.

## Changelog

| Date | Change | Feature |
|---|---|---|
| {{DATE}} | Created empty by the scaffold | tech-setup |
