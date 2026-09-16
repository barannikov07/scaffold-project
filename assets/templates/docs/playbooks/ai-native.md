<!-- Playbook: ai-native. Canonical text; the .claude/skills and .codex/skills wrappers point here. -->

# Applied AI

Find where AI inside the product removes a step from the user's flow or a decision from the
owner's plate, propose it while the PRD is still a draft, and carry the chosen items through
design, spec, and QA. Runs after every Full PRD draft, called by the new-feature playbook; also
on its own when the owner says "where can AI help", "make it smarter", "AI features", or asks
what applied AI could do for a feature. Calibrate every message to the owner profile in
`AGENTS.md`.

This is AI *in* the product. It is not about the agent that builds the product.

Read first: the feature's `prd.md`, `docs/vision.md`, `AGENTS.md` (tripwires),
`docs/playbooks/ai-native-patterns.md`.

## 1. List the human steps

Go through the PRD's flows and write down every step where a person types, reads, copies, sorts,
chases someone, decides, or waits. Note who does it and how often. This list is the raw
material; an opportunity that does not map to a step here is a gimmick.

## 2. Match steps to patterns

For each step, check the pattern catalogue. Keep the two to four candidates with the biggest
gain, and for each write:

- **Pattern**, and a one-line description in the owner's words.
- **Step it removes**, and for whom, from the list in step 1.
- **Gain**: which PRD success criterion improves, and roughly by how much.
- **Risk tags**: privacy (what data leaves the app), money, a tripwire it touches, or none.
- **Cost class**: instant and cheap · a few seconds and cents · background job.
- **Recommendation**: now, later, or no, with the reason.

A feature that is itself an AI capability (a drift signal, a recommender) gets the same
treatment, focused on the human-in-the-loop points and the evaluation set rather than on finding
steps to remove.

## 3. Write it into the PRD

Fill the PRD's "AI opportunities" table with every candidate and a decision column. Then:

- **Chosen** items go into Scope and into the Flows, with the human confirmation step shown.
  Success criteria gain a measurable line ("a rehearsal is created from a pasted message in under
  ten seconds, with the conductor confirming once").
- **Deferred** items become one line in the roadmap's "Later (unordered ideas)" list with a link
  back to this PRD. Not a milestone row and not a Changes entry; a deferral is not a decision.
- **Rejected** items go into Non-goals with the reason, so no future session re-proposes them.
- **If a chosen item adds a risk tag** (usually external service, because text goes to a model
  provider, or privacy, because personal data does), update the PRD's Assessment block and the
  Tags column of the index row before presenting. The security passes are driven by those tags;
  a stale tag silently skips a threat pass.

## 4. Present to the owner

Two to four lines, one per opportunity, with the recommendation. Ask which they want. A beginner
gets one sentence on what each would feel like to use; a product manager gets the table.

## 5. Carry the chosen items through

- **Design**: every AI step gets its states designed: thinking, streaming if it takes seconds,
  "here is what I understood, correct me", and the manual fallback. The confirmation card
  component is the default surface.
- **Spec**: the "AI components" section: inputs, outputs, model tier, latency class, cost per use,
  what data leaves the app and to which provider, fallback when the model fails or is wrong, who
  confirms what, and an evaluation set of ten real examples with expected outputs. Record the
  model choice as a decision. Add the provider to `infra.md` external services.
- **Security**: data sent to a provider is a privacy item; user-supplied text inside a prompt is
  an input surface. Both go through the security playbook when the feature is risk-tagged.
- **QA**: the evaluation set is run; the fallback and correction paths are tested.
- **Close**: the guide records whether the AI step saved the time the PRD claimed.

## Rules

- **Remove a step or it is not added.** A chat box on the side of a feature removes nothing.
- **Name the gain.** If no success criterion improves, the recommendation is "no".
- **Tripwires bind AI harder than people.** For money, privacy, or immutable records, AI proposes
  and a person confirms. Always. The confirmation is designed, not implied.
- **Show the source, allow correction.** What the model read and what it concluded are both
  visible; fixing it is one tap.
- **Degrade to manual.** If the model is down or wrong, the feature still works by hand.
- **Two to four, ranked.** Not a brainstorm.
- **Provider-neutral.** Use the provider the stack already has; pick the cheapest tier that
  passes the evaluation set; record the choice.
