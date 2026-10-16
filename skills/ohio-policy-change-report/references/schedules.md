# Scheduled Invocation Patterns

A reusable skill can be invoked by a schedule but does not create a background subscription on installation. Configure a real automation with the Automations tool only when the user requests the schedule. Resolve cadence and timezone; default timezone here is America/New_York. Include actual connected-source access and publication authorization in the prompt.

## Refresh Prompt

Use @ohio-policy-change-report to refresh the specified dataset paths in BehavioralHealthBillingSolutions/ohio-bh-policy-reference. Resolve the latest successful dated baseline, retrieve authoritative current sources, and compare body text, metadata, and effective status. Preserve dated source snapshots/hashes and generate a dated linked change-and-impact report with full source text and return links. Update scoped working files and push to the repository under existing authorization; respect branch protection and concurrent changes. For unchanged sources, report no substantive change; for source failures, report the blocked source without replacing the last validated copy. Do not send email or Teams messages unless separately authorized.

## Proposed Package Prompt

Use @ohio-policy-change-report to compare current effective rules with the specified official proposed/BIA package and prior draft in BehavioralHealthBillingSolutions/ohio-bh-policy-reference. Check whether the package URL has changed bytes or internal dates, reconcile its actual rule inventory, and preserve proposal status. Produce current-versus-proposed and prior-draft revision findings, exact text links, full rule text, operational impacts, forecast-input changes, and unresolved dependencies. Preserve effective working law. Publish scoped report and proposed reference files to the repository under existing authorization. Do not assume adoption from a comment deadline or a future milestone inside a draft.

Fill dataset paths and package URLs from the user's current scope; do not schedule an unbounded scan unless requested. A schedule that lacks source access or publication access must report that blocker rather than fabricate a successful refresh.
