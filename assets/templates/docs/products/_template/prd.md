# PRD: {{FEATURE_NAME}}

Status: Draft · Approved on: not yet · Build started on: not yet

A PRD says what we are building and why, in the owner's language. It is a draft until the build
starts and a record of what was agreed after that. If reality turns out different, the guide
records it; if you change your mind, that is a new PRD in this folder, not an edit of this one.

## Assessment

| | |
|---|---|
| Size | Full |
| Has UI | yes / no |
| Risk tags | none / money / privacy / sign-in / external service |
| Depends on | |
| Decision | go / later / no, by the owner, with the date |

## Vision fit

Which part of [the vision](../../vision.md) this advances, in one or two sentences, quoting the
goal or principle. If it strains a vision principle, say which and why it is worth it. A feature
that advances nothing in the vision does not get built; it gets Later or Dropped.

## Problem

What is hard or impossible today, for whom, and what it costs them. Two or three sentences.

## Users

Who uses this and in what situation. If roles differ, one line per role.

## Scope

What this feature does. Short bullets, each one observable.

- 

## Non-goals

What this feature deliberately does not do, even though someone will ask. This is the section
that keeps the build small.

- 

## Flows

The main path and the important alternatives, as numbered steps the owner can picture. One
flow per heading.

### Main flow

1. 

### When things go wrong

- 

## Success criteria

How we will know it worked. Each line is something a person can check by using the product, and
it becomes the owner's acceptance checklist in QA.

- 

## AI opportunities

Filled by the applied-AI pass after the first draft. Every row gets a decision: chosen (now in
Scope and Flows, with the confirmation step shown), deferred (a roadmap Later row), or rejected
(in Non-goals with the reason).

| # | Opportunity | Step it removes | Gain | Risk | Cost class | Decision |
|---|---|---|---|---|---|---|
| | | | | | | |

## Open questions

`TBD(owner):` lines that must be answered before approval.

- 

## Before this passes

The gate for stage 3. The agent ticks the first four when they are true; only the owner ticks
the last two. The owner approves only when every box is ticked.

- [ ] Vision fit names a specific goal or principle
- [ ] Non-goals section has at least one real exclusion
- [ ] Every success criterion is checkable by using the product
- [ ] AI opportunities considered, each with a decision; chosen ones visible in Scope and Flows
- [ ] Every open question is answered or moved to the spec as a design question
- [ ] Owner has read it and said "approved"
