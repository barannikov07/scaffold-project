# Applied-AI pattern catalogue

Reference for the applied-AI playbook. Each pattern says when it earns its place and when it
does not. "Guardrail" is the minimum a design must include when the pattern is chosen.

## Capture: getting information in without typing

| Pattern | Good when | Bad when | Guardrail |
|---|---|---|---|
| Voice to structured record | The user is on the move, or the record has many fields | The record is one field; typing is faster | Show the transcript and the mapped fields; one tap to edit |
| Photo or PDF to fields | Receipts, business cards, forms, spec sheets | The data is already digital elsewhere | Confidence per field; low-confidence fields highlighted |
| Paste anything to a record | Users already have the information in a message or email | The structure is trivial | Show what was extracted next to the source |

## Understand: making sense of what is there

| Pattern | Good when | Bad when | Guardrail |
|---|---|---|---|
| Extraction and auto-mapping | Importing spreadsheets or exports with unknown columns | A fixed template already exists | Mapping preview before import; nothing written until confirmed |
| Classification and tagging | Many items, a stable set of categories | Categories change weekly; humans disagree | Tag is editable; the model's reason is one tap away |
| Dedup and matching | People, companies, products entered by many hands | Records are few | Merge is proposed, never automatic |
| Summarise a thread | Long chats, tickets, meeting notes | The thread is short | Verbatim quotes alongside the summary |

## Assist: doing the boring half

| Pattern | Good when | Bad when | Guardrail |
|---|---|---|---|
| Smart defaults from history | The same values recur (place, time, people) | First-time use; no history | Defaults are visibly defaults; one tap to change |
| Natural-language command | Users know what they want and hate forms ("move Tuesday to 7pm") | Precision matters more than speed | Echo the interpreted command before executing |
| Drafted message | Reminders, replies, descriptions the user would write anyway | The message is legally or emotionally sensitive | Draft is editable; nothing sends without a tap |
| Translation | Mixed-language users | Single language | Original visible on request |

## Decide: seeing what a person would miss

| Pattern | Good when | Bad when | Guardrail |
|---|---|---|---|
| Anomaly and drift signals | Patterns over time matter (attendance dropping, spend spiking) | Data is too thin to have a pattern | Show the evidence, never just the verdict |
| Prioritisation | More items than attention | Items are few | Order is a suggestion; the user can pin |
| Recommendation with reasons | Choices with many options | One obvious option | The reason is shown; declining is easy |

## Act: doing the thing, with permission

| Pattern | Good when | Bad when | Guardrail |
|---|---|---|---|
| Agentic step behind a confirmation card | Multi-step tasks the user does often | Irreversible actions without a card; money, privacy, immutable records | Card shows exactly what will happen; Confirm and Edit |
| Scheduled digest | Users check the same thing daily | Real-time matters | Digest links to the source; unsubscribe in one tap |

## Surface: where the user meets it

| Pattern | Good when | Bad when | Guardrail |
|---|---|---|---|
| Conversational entry point (chat, messenger bot) | Users already live in a messenger; tasks are short | Tasks need a screen (tables, comparisons) | Thin adapter over the same functions; same permissions as the app |
| Inline suggestion | The user is already on the right screen | It interrupts | Dismissible; remembers the dismissal |

## Always

- The AI step is optional; the manual path stays.
- The user sees what the model read and what it concluded.
- Correction is one tap, and nothing changes silently.
- Money, privacy, and immutable records: propose, confirm, then act.
- Ten real examples in the spec's evaluation set before the pattern is built.
