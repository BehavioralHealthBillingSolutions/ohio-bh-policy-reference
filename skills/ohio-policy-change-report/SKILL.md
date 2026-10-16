---
name: ohio-policy-change-report
description: Create linked change-and-impact reports for Ohio policy datasets, including OAC and ORC chapter refreshes, historical manual or agreement revisions, current-versus-proposed rules, BIA/CSI referral packages, and draft-to-draft comparisons. Use for on-demand or scheduled comparisons in the BHBS ohio-bh-policy-reference repository, with full source text, reciprocal links, source hashes, operational impacts, and forecast-engine actions.
---

# Ohio Policy Change Report

This public distribution excludes complete manuals and complete agreement PDFs. Do not publish
uncleared source material or omitted Milliman reports. Follow the omission register and public
contribution rules; analyze restricted inputs locally and link to their official publisher.

Produce the repository's standard report structure: preserve the change summary and likely impact beneath each rule/section title; include the full updated or proposed text beneath that analysis; link to the full chapter, baseline, official source, and return to the report. Support refresh, proposal, and draft-revision modes. Read [repository and modes](references/repository-and-modes.md) and [report contract](references/report-contract.md) before producing outputs. Use [scheduled invocation patterns](references/schedules.md) only when scheduling or configuring recurring work.

## Resolve the Comparison

1. Default to `BehavioralHealthBillingSolutions/ohio-bh-policy-reference` when the user's context identifies that repository. Use the connected GitHub tools unless a local checkout is accessible in this runtime. Read the current tree, applicable AGENTS.md, README, source manifests, and relevant source files. Preserve repository conventions and filenames.
2. Record the baseline and target identities, source URLs, internal dates, retrieval timestamps with timezone, effective dates, policy status, file hashes, and repository head. Select the comparison explicitly: historical-to-current, current-to-proposed, or previous-draft-to-revised-draft. Add a secondary draft comparison when it materially updates an existing forecast.
3. Resolve versions from file contents and authoritative sources rather than filenames or memories. Check whether a stable PDF URL was overwritten. A BIA submission date or printed deadline is not an effective date. A missing rule in a narrower packet is not a rescission.
4. Verify live Ohio Laws text for current-law comparisons using ohio-laws-to-markdown when available; use a fresh cache or bypass old caches. Prefer regulatory/payer primary sources for current requirements. Distinguish a successfully fetched snapshot from verified current policy and disclose retrieval failures. Do not silently relabel an archived baseline as live-verified.
5. Extract proposed PDFs from the official packet. Preserve proposed additions and retained text, exclude deletions and predecessor copies marked for rescission, and retain separately the fact of rescission/replacement. Validate color/strikeout interpretation visually. Never delete numeric-only content without checking its page position. Preserve draft errors as source evidence and flag material cross-reference, threshold, or internal conflicts. Use PDF conversion skills where appropriate; do not treat a generic text dump containing both old and new text as the proposed rule.

## Compare and Interpret

1. Inventory every rule, section, appendix, and relevant table. Match by identifier and subject, including rescinded-and-reissued counterparts; build a service crosswalk when identifiers or titles change.
2. Compare substantive text independently from retrieval timestamps, headings, formatting, and supplemental metadata. Classify additions, removals, substantive amendments, metadata-only edits, newly operative prepublished provisions, unchanged items, replacements, out-of-scope items, and unverified items. Report coverage gaps.
3. Generate reproducible text diffs. Use the bundled `scripts/build_report.py` after preparing a JSON comparison specification; it renders the report, diffs, and hashes from source files and reviewed analysis. Read its `--help` and the report-contract example. Automated diffs locate evidence; they do not determine legal significance.
4. Write grounded summaries with paragraph citations, before/after examples, and likely operational impact. Keep fact, interpretation, and payer/system implementation distinct. State `⚠️ Risk Flag.` for material ambiguity or compliance, enrollment, authorization, documentation, credentialing, system, or reimbursement risk. Do not infer exact rates, utilization thresholds, adoption dates, or savings without the governing appendix or evidence.
5. Address Ohio Medicaid behavioral-health workflows: agency versus rendering provider versus member; ODM FFS versus MCO/OhioRISE/MyCare applicability; service definitions and activity remapping; eligibility, supervision, staffing tiers, units/time/group ratios, bundles, authorizations, treatment plans, claim edits, and forecast-engine scenario inputs. Assign owner-ready actions without inventing named owners. Qualify impacts until proposal adoption and implementation details are verified.

## Assemble and Validate

1. Put the dated report under `Ohio Rules/` for rule comparisons. Preserve immutable dated source copies under `Reference MD Files/All Historical and Current/`; use a clearly labeled proposed subfolder under `Ohio Rules/Comparisons/` for navigable proposal copies. Never overwrite effective working law with a proposal. Add return links without changing statutory body text.
2. Include an executive summary, source-status table, rule coverage, per-rule summary/likely impact, current and target full text or direct appendix anchors, operational/forecast actions, differences from any prior draft, unresolved questions, validation, and provenance. Use relative links encoded for spaces in repository documents. Keep source text distinct from analysis and label whether full updated sections include unchanged context. Large texts may be in a linked appendix; make every rule entry reach its exact text.
3. Validate source-body preservation, expected coverage, effective dates, all relative links and fragments, no truncation/placeholders, source hashes, PDF boundaries, and representative material paragraphs. Check extraction anomalies against the PDF; retain genuine source errors and flag them. Do not invent verified counts. For rates/tables, confirm row-column relationships against the PDF before numerical interpretation.
4. Run the renderer on actual inputs. Review summaries against both sides; test the diff output, hashes, and link targets. Treat an incomplete extraction or contradictory draft as an explicit review item, not evidence for a definitive implementation action.

## Save and Publish

Honor task and recurring-run authorization. The user's request to update this repository authorizes a scoped commit/push; a report-only request does not implicitly authorize changing unrelated files or enabling schedules. On an already authorized recurring repository refresh, proceed without repeat confirmation. Follow branch protection and repository instructions; preserve concurrent changes, use expected-head checks, and never force-push. Verify changed remote paths and content hashes before claiming completion. Keep historical source states immutable.

Save repository-backed artifacts in the repository; do not duplicate them in Library. For standalone requested artifacts, use the Library workflow. Report the saved report URL, source status, material findings, and outstanding blocker. Do not claim a local Windows checkout updated merely because GitHub was updated.

A skill is not itself a scheduler. Create/update an automation only when the user requests an actual schedule or future check and its cadence is known or reasonably inferred. Configure the invocation with dataset scope, source-status rules, repository destination, timezone, and write authorization. Do not hardcode dates or factual policy conclusions from a prior run.
