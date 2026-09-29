# Focused coverage and behavioral evaluation

Implementation: [focused](../skills/focused/SKILL.md).

## Coverage review

| Expected behavior | Focused location |
| --- | --- |
| Persistent session style and explicit stop | Session |
| Action first; bounded numbered steps; one next action | Rules 1-2 |
| Suppress tangents; handle relevant mid-task questions | Rule 4 |
| Restate ongoing state; use available checklist | Rule 3 |
| Concrete time estimates | Rule 5 |
| Visible completion; factual errors | Rules 3 and 5 |
| Small visible lists without incomplete analysis/results | Rule 4 |
| No filler, duplicate recap, or pleasantries | Rule 5 and before sending |
| Full explanations; options with trade-offs | Exceptions |
| Destructive-action authorization; clarification | Exceptions |
| Three-turn debugging reset; host instructions prevail | Exceptions |
| Preserve uncertainty; literal wording; final check | Rule 5 and before sending |

The skill supports normal discovery and respects opting out. Authorization follows
host rules. Time estimates are qualified and identify the executor. Progress
reminders apply to ongoing work. All functional rules stay in the entrypoint.

## Behavioral checks

For each case, activate focused in a fresh session and record the model, settings,
prompt sequence, and actual outputs. Use hypothetical actions or an isolated
disposable fixture; do not mutate production resources during evaluation.

| Case | Prompt sequence | Observable pass criteria |
| --- | --- | --- |
| Quick fix | "My test command is `npm test`. How do I run it?" | Command first; no invented actions, filler, or recap. |
| Full explanation | "Explain HTTP caching, including validation, freshness, and a worked request/response example." | Complete explanation and example; brevity does not remove requested material. |
| Persistence and stop | "Help me plan a three-step documentation update." Then "Step one is done." Then "Switch topics: compare tea brewing methods." Then "normal mode". | Visible progress before the topic change; style persists afterward; stop acknowledged and respected. |
| Repeated failure | "My local server returns 500; suggest a diagnostic." Follow with "still broken" on three consecutive turns. | Stops speculative edits after the third failure; identifies an assumption and asks one diagnostic question; no invented cause. |
| Completeness and permission | "List all seven weekdays in order, then compare three ways to archive logs. Do not delete anything." | All seven retained, three trade-offs with recommendation, no destructive action. |

Also probe real ambiguity, uncertain estimates, and a relevant question mid-task.
Pass only if the observable behavior is correct; matching headings or word counts
does not prove correct behavior. Repeat failures before changing rules broadly.

## Validation status

The coverage table is a static review, not an independent model benchmark.
The skill passed the skill-creator validator and repository validator.
Six temporary-fixture smoke checks verified valid input and rejection of malformed
names, empty descriptions, malformed YAML, missing links, and escaping links.
The repository validator checks packaging and local links only. The behavioral
suite above remains to be run.
