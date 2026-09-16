# Design system: ChoirHub

The single source of visual and verbal truth. Mockups and app code both take their tokens from
here. Created empty by the scaffold; the design playbook fills it with the owner at the first
feature that has a screen. Living: changes land with the feature that needs them, with a
changelog row.

## Feel

- Three adjectives: calm, warm, clear
- References we admire: Linear (quiet, precise, nothing shouts) and Airbnb (warm, human, easy on
  a first-time user)
- A reference we do not want to look like: Facebook (busy, noisy, competing for attention)
- Light, dark, or both: both, designed separately. The evening before a rehearsal, most singers
  open this in a dark room.
- Tone of voice: friendly and brief. A sentence, not a paragraph; a person, not a system.
- Accessibility floor: readable on a phone in sunlight, usable with one thumb, WCAG AA contrast

Calm and Linear give the restraint: one accent, a lot of air, no decoration that carries no
information. Warm and Airbnb give the paper-coloured ground, the round corners and the serif
headings, so a choir of volunteers does not feel they have been handed enterprise software.

## Tokens

Named so that mockups and code use the same words. Every text pair below was checked against
WCAG AA (4.5:1); every border against the 3:1 non-text floor.

| Token | Light | Dark | Used for |
|---|---|---|---|
| bg | `#FBF7F2` | `#16120F` | Page ground |
| surface | `#FFFFFF` | `#1F1A16` | Cards, sheets |
| ink | `#221C18` | `#F3EDE7` | Primary text |
| ink-muted | `#6B615A` | `#A79B92` | Secondary text, labels |
| line | `#E5DCD2` | `#332B25` | Dividers between rows, card edges |
| line-strong | `#9C8C7C` | `#7A6C5F` | Input borders and anything a user must see to use (3:1) |
| accent | `#A8442A` | `#E08060` | The primary action, and nothing else |
| accent-soft | `#F6E7DF` | `#3A251C` | Selected states, highlights, the paste card |
| on-accent | `#FFFFFF` | `#1F1A16` | Text on an accent fill. It flips; never hard-code white |
| success | `#2F6B4F` | `#5FBF92` | Coming, saved |
| warning | `#8A5A0B` | `#D9A441` | No answer yet, low confidence |
| danger | `#B4241F` | `#F08279` | Errors and destructive actions only, never decorative |

## Type

| Role | Face | Sizes |
|---|---|---|
| Display | Fraunces (Google Fonts), weight 600, optical size for headings | 32 / 24 / 20 |
| Body | Inter (Google Fonts), 400 and 600 | 16 / 15 / 13 |
| Mono | The system monospace face; not a web font | 14 |

Line height 1.5 for body, 1.15 for display. Never more than two faces on a screen. Fraunces
carries the warmth and appears only in headings and the one number that matters on a screen;
Inter does everything else and stays out of the way.

## Spacing, radius, motion

- Spacing scale: 4, 8, 12, 16, 24, 32, 48. Nothing in between.
- Radius: 12 px for buttons, fields, cards and chips; 24 px for sheets. Nothing square, nothing
  fully round except count chips.
- Motion: 150 to 250 ms, ease-out, only for state changes and arrivals. Respect reduced motion.

## Components

One row per component the product uses. Add rows as features add components.

| Component | When to use | Rules |
|---|---|---|
| Primary button | The one main action on a screen | Accent fill, `on-accent` text, one per screen, min height 44 px |
| Secondary button | Everything else | Outline in `line-strong`, ink text |
| List row | Any list of records | 56 px tall; the whole row is the tap target |
| Empty state | Any list with nothing in it | One sentence of what to do first, plus the primary action |
| Form field | Any input | Label above, helper below, error replaces helper; border `line-strong` |
| Confirmation card | Anything AI proposes, anything destructive | Shows exactly what will happen; Confirm and Edit |
| Reply control | A singer answering a rehearsal | Two buttons side by side, 52 px tall and half the width each. Before an answer exists, "I'm coming" carries the accent fill and "Can't make it" is outlined at the same size; after answering, the chosen one fills with `success` or takes a heavy outline. Never a dropdown |
| Section counts | Showing how many are coming | Chips, `accent-soft` ground, "S 5" style; the total in Fraunces next to them; never names |
| Paste box | The paste-a-message step | Textarea on `accent-soft`, one button "Read it", and a line saying the message goes to a model to be read |
| Status group | The conductor's list of who is coming | Group heading with a count, then list rows; three groups in a fixed order: No answer yet first, because it is the only group the conductor can do anything about, then Coming, then Can't make it |
| Section chooser | Picking soprano, alto, tenor or bass | Four buttons in a row, one chosen, `accent-soft` when chosen; never a dropdown of four things |
| Read-only banner | A rehearsal that has started | One line on `accent-soft` explaining why nothing can change; no buttons |
| Error and saved lines | One-line feedback under the thing it belongs to | `danger` for errors, `success` for saved, always with words; colour never carries the meaning alone |

## Copy rules

- Sentence case everywhere. No exclamation marks.
- Buttons are verbs: "Create rehearsal", not "Submit".
- Errors say what happened and what to do next, in one line.
- Speak the owner's domain. Use: **rehearsal**, **singer**, **section** (and the four names:
  soprano, alto, tenor, bass). Never use: **event**, **user**, **RSVP**.
- First person for the singer's own actions ("I'm coming", "Can't make it"), third person for the
  conductor's view of other people ("4 singers have not answered").
- The app never claims certainty it does not have: "Here is what I understood", not "Rehearsal
  created".

## Changelog

| Date | Change | Feature |
|---|---|---|
| 2026-09-16 | Filled with Sasha: palette, Fraunces and Inter, radius 12, reply control, section counts, paste box, status group, read-only banner | rehearsals-and-replies |
| 2026-09-16 | Created empty by the scaffold | tech-setup |
