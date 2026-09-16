# Design: Rehearsals and replies

Status: Approved · Approved on: 2026-09-16 · Build started on: not yet
PRD: [prd.md](prd.md) · Mockups: [mockups/index.html](mockups/index.html) · Design system: [../../design/system.md](../../design/system.md)

What the feature looks like and how it behaves on screen, agreed before any code. The mockups
are the contract; screen names here are used verbatim in the spec and the build. A record once
the build starts; deviations go in the guide. Features without a screen leave this file as is.

## Screens

| Screen | Purpose | How the user gets there | Primary action |
|---|---|---|---|
| Sign in | A singer or the conductor proves who they are | The link the conductor posts in WhatsApp, or the bookmark | Send me a link |
| My rehearsals | A singer sees the term and answers the next one without going anywhere else | After signing in, if they are on the choir list | I'm coming |
| Rehearsal | A singer sees one rehearsal in full: place, note, songs, how many are coming | Tapping any rehearsal in My rehearsals | I'm coming |
| Rehearsals | The conductor sees the term with the answer counts on each night | After signing in, as the conductor | New rehearsal |
| New rehearsal | The conductor creates a rehearsal, by typing or by pasting the WhatsApp message | New rehearsal, from Rehearsals | Create rehearsal |
| Who is coming | The conductor sees, by name, who is coming, who is not, and who has not answered | Tapping a rehearsal in Rehearsals | Open a singer who has not answered, to get their number |
| Singers | The conductor keeps the choir list: name, email, section | The Singers tab | Add singer |

The conductor has a two-tab bottom bar (Rehearsals · Singers). Singers have no tabs: they land
on My rehearsals and everything is one level deep from there.

## Flows on screens

The PRD's flows, step by step, naming the screen at each step.

1. **The conductor plans next Tuesday.** Rehearsals → New rehearsal → fills date, time, place,
   optional note, songs → **Create rehearsal** → Who is coming, with "Rehearsal created" and
   **Copy link** at the top, which the conductor pastes into WhatsApp.
2. **The same, by pasting.** Rehearsals → New rehearsal → pastes the WhatsApp message into
   **Paste a message** → **Read it** → the screen shows *Here is what I understood* with the
   date, time, place and songs filled in and anything uncertain marked → the conductor corrects a
   field or taps **Create rehearsal** → Who is coming. Nothing is saved before that tap.
3. **The singer answers.** The link → Sign in → My rehearsals, next rehearsal at the top with
   **I'm coming** / **Can't make it** → one tap → the card says "You're coming" and shows the
   counts. No further screen is needed.
4. **The singer looks closer.** My rehearsals → Rehearsal: place, note, songs to prepare, the
   counts by section, and the same two buttons, now showing their answer.
5. **The conductor sees the room.** Rehearsals → Who is coming: three groups in a fixed order,
   No answer yet, Coming, Can't make it → tap a name in No answer yet → a sheet with that
   singer's email and phone, and nothing else about them.
6. **The conductor adds a singer.** Singers → **Add singer** → name, email, section → the singer
   appears in the list as "Not signed in yet" until they first open the link.

## States

Every screen, every state. A state not listed here will be improvised in code.

| Screen | Empty | Loading | Error | Success | Denied | AI: thinking / correct-me / fallback |
|---|---|---|---|---|---|---|
| Sign in | n/a: one field | Button reads "Sending…", disabled | "That link has expired. Ask for a new one." | "Check your email. We sent a link to anna@…" | "You're not on this choir's list yet. Ask your conductor to add you." — shown straight after sign-in, before any choir data loads | n/a |
| My rehearsals | "No rehearsals yet. Your conductor will add the term soon." | Three skeleton rows | "We couldn't load your rehearsals." + Try again | The next card flips to "You're coming" with the counts | n/a: someone who is not on the list never reaches this screen — they are stopped at Sign in | n/a |
| Rehearsal | n/a: a rehearsal always has a date and a place | Skeleton title and rows | "Your answer didn't save. Tap to try again." — the previous answer stays on screen | "Saved. You're coming." under the buttons | Read-only banner: "This rehearsal has started. Answers are closed." | n/a |
| Rehearsals | "No rehearsals yet. Create the first one." + New rehearsal | Three skeleton rows | "We couldn't load the term." + Try again | New rehearsal appears at the top marked "Just created" | "Only the conductor can open this page." | n/a |
| New rehearsal | The blank form is the default state | "Creating…" on the button, fields disabled | Per field: "Add a date", "Add a place". On save: "That didn't save. Your text is still here." | Goes to Who is coming with "Rehearsal created" | n/a | **Thinking**: "Reading your message…" with the text visible above it. **Correct me**: confirmation card, each field shown, uncertain ones marked "Check this", Create rehearsal / Edit. **Fallback**: "I couldn't read that one. Here's the form with what I got." |
| Who is coming | "Nobody has answered yet. 24 singers have the link." + Copy link | Skeleton groups | "We couldn't load the answers." + Try again | Sheet opens with the singer's contact details | Read-only banner once the rehearsal has started | n/a |
| Singers | "No singers yet. Add the first one." + Add singer | Three skeleton rows | "Anna Kowalska already has that email." under the email field | "Anna Kowalska added" and the row appears | n/a | n/a |

## Copy

The real words, in the design system's tone.

| Where | Text |
|---|---|
| Sign in, title | Sing with us |
| Sign in, body | Enter the email your conductor has for you and we'll send a link. No password to remember. |
| Sign in, button | Send me a link |
| Not on the list | You're not on this choir's list yet. Ask your conductor to add you. |
| My rehearsals, title | Your rehearsals |
| Reply buttons | I'm coming · Can't make it |
| After answering | Saved. You're coming. · Saved. We'll miss you. |
| Counts line | 18 coming · S 5 · A 4 · T 4 · B 5 |
| Songs heading | To prepare |
| Rehearsal started | This rehearsal has started. Answers are closed. |
| Rehearsals (conductor), title | Autumn term |
| Rehearsal row, conductor | 18 coming · 3 can't · 3 no answer |
| New rehearsal, title | New rehearsal |
| Paste box label | Paste a message |
| Paste box helper | Paste what you wrote in WhatsApp and I'll fill this in. The message is sent to a language model to be read; nothing is saved until you confirm. |
| Paste box button | Read it |
| AI card title | Here is what I understood |
| AI uncertain marker | Check this |
| AI fallback | I couldn't read that one. Here's the form with what I got. |
| Create button | Create rehearsal |
| After creating | Rehearsal created. Copy the link and post it in the group. |
| Who is coming, groups | No answer yet · Coming · Can't make it |
| Contact sheet | Chase Anna · anna.kowalska@example.com · +48 601 234 567 |
| Contact sheet footnote | Only you can see this. Singers never see each other's details. |
| Singers, title | The choir |
| Singers, row status | Not signed in yet |
| Add singer button | Add singer |
| Duplicate email error | Anna Kowalska already has that email. |
| Empty, my rehearsals | No rehearsals yet. Your conductor will add the term soon. |
| Empty, conductor | No rehearsals yet. Create the first one. |
| Empty, who is coming | Nobody has answered yet. 24 singers have the link. |

## Responsive

Phone first at 390 px. What changes at desktop width:

- The content column stops at 560 px and centres; nothing stretches to the window width.
- The conductor's bottom tab bar moves to a row of two links under the title; the thumb is not
  the pointing device on a laptop.
- Who is coming puts the three groups side by side above 900 px, so the whole room is one glance.
- Nothing changes size: 44 px targets and 15/16 px text stay, because the same person uses both.

## Accessibility

Focus order, labels, 44 px touch targets, contrast against the floor in the design system.

- Focus order follows reading order: title, then content, then the primary action last on the
  screen but first in the group of actions. The read-only banner is the first thing announced on
  a closed rehearsal.
- The reply control is two real buttons with `aria-pressed`, not a segmented widget. The chosen
  one says "I'm coming, chosen", not just a colour: the label and a tick carry the meaning, green
  only repeats it.
- Every count has a text equivalent: "18 coming: 5 sopranos, 4 altos, 4 tenors, 5 basses".
- Every field has a visible label above it, never a placeholder as a label. Errors replace the
  helper text and are tied to the field.
- Touch targets: 44 px minimum, 52 px for the reply buttons because they are the one thing a
  singer does with a thumb while walking.
- Contrast: body text 15.78:1, muted text 5.65:1, white on the accent 5.96:1, field borders
  3.25:1. Dark mode is designed separately and checked to the same floor.
- The paste box says out loud that the text goes to a language model, before it is used.

## Mockups

| Screen | File | States shown |
|---|---|---|
| Sign in | [mockups/sign-in.html](mockups/sign-in.html) | Default · sending · link sent · expired link · not on the list |
| My rehearsals | [mockups/my-rehearsals.html](mockups/my-rehearsals.html) | With the term · answered · empty · loading |
| Rehearsal | [mockups/rehearsal-singer.html](mockups/rehearsal-singer.html) | Not answered · answered with counts · started (read-only) · save failed |
| Rehearsals | [mockups/rehearsals-conductor.html](mockups/rehearsals-conductor.html) | With the term · empty · not the conductor |
| New rehearsal | [mockups/new-rehearsal.html](mockups/new-rehearsal.html) | Blank form · filled · field errors |
| New rehearsal, paste | [mockups/new-rehearsal-paste.html](mockups/new-rehearsal-paste.html) | Pasted · thinking · here is what I understood · couldn't read it |
| Who is coming | [mockups/who-is-coming.html](mockups/who-is-coming.html) | Three groups · contact sheet · nobody answered yet · after it started |
| Singers | [mockups/singers.html](mockups/singers.html) | The choir · add a singer · duplicate email · empty |

Open `mockups/index.html` in a browser; it links all eight with a line each.

## Critique (the ten-point walk)

Each mockup was walked against the ten points in `docs/playbooks/design.md`. What it changed:

1. **Primary action obvious in two seconds.** The first draft of My rehearsals put the reply
   buttons only on the Rehearsal screen, so answering took two taps. The next rehearsal now
   carries the reply control on the list itself: the singer's whole job is one tap from the link.
2. **The screen says where you are and what just happened.** Added "Saved. You're coming." under
   the buttons rather than only turning one green, and "Just created" on the new rehearsal row.
3. **Words from the domain.** "Event", "attendee" and "RSVP" were removed in favour of
   rehearsal, singer, coming / can't make it. The banned-words list is now in the design system.
4. **Destructive actions confirmed.** Nothing here deletes, but removing a singer (Singers screen)
   asks first and says what happens to their past answers: they stay, the person goes.
5. **Same thing looks the same.** The three "no answer" states (a singer's row, a conductor's
   group, a count chip) all use the warning outline, never a filled colour.
6. **Errors prevented before reported.** Date and place are required, but the paste path fills
   them; the duplicate email is caught as the conductor types the email, not after saving.
7. **Nothing to remember from another screen.** Who is coming repeats the date, place and the
   rehearsal link, so the conductor never has to go back to copy it.
8. **Readable at arm's length.** Body text went from 14 to 15 px and the muted grey was darkened
   to 5.65:1; the counts use the display face at 24 px so the number reads from a distance.
9. **Thumb-sized targets.** The reply buttons are 52 px tall and half the screen wide; the whole
   list row is tappable.
10. **The empty state teaches.** Every empty state names the next action and who does it
    ("Your conductor will add the term soon", "Create the first one").

The walk also reordered the conductor's three groups. They were Coming, Can't make it, No
answer yet, which reads like a report; No answer yet now comes first, because it is the only
group the conductor can do anything about. And the paste box's button was demoted from an accent
fill to an outline, so the one filled button on New rehearsal is still Create rehearsal: typing
must never look like the punished path.

Two further changes came from the applied-AI guardrails rather than the list: the paste box now
says where the text goes before it is used, and the "here is what I understood" card marks the
fields it is unsure about instead of presenting everything with equal confidence.

## Before this passes

The gate for stage 4. The agent ticks the first five when they are true; only the owner ticks
the last.

- [x] Every PRD flow is covered by the screens above
- [x] Every screen has its empty, error, and denied states designed
- [x] Copy is real words in the design system's tone; no placeholders
- [x] Every mockup passed the ten-point critique in the design playbook
- [x] Tokens and components come from `docs/design/system.md`; anything new was added there
- [x] Owner has opened the mockups and said "approved"
