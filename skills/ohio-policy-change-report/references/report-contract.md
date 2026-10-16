# Report Contract and Renderer Inputs

Use professional, direct BHBS language. Lead with status, material change, and next action. Include current authority, proposed authority, and likely impact as distinct elements.

Each entry must have an identifier/title, change classification, source status, change summary with paragraph references, likely impact, owner-ready action, and a link to current text and full target text. Keep the summary concise and link each entry to an exact full-text appendix anchor. For proposals, show current and proposed text independently; never blend them into an apparent operative rule. Preserve source metadata and annotate source errors outside the quoted law.

Use `python3 scripts/build_report.py spec.json --output /absolute/report.md`.
All source paths in the JSON resolve relative to the JSON location. Source files should contain the exact rule/section text under a `## Rule Text` heading. The renderer compares only that body and verifies that it is included unchanged in the full-text companion. Prepare per-rule source copies from the complete authoritative chapter while preserving source and effective-date fields; a full-chapter link may be added in `context_links`.

Minimum JSON example (values are illustrative, not Ohio policy facts):

```json
{
  "title": "Dataset Current Versus Proposed Change and Impact Report",
  "mode": "current-versus-proposed",
  "as_of": "YYYY-MM-DD America/New_York",
  "baseline_label": "Current effective source",
  "target_label": "Proposed draft, not operative",
  "overview": "Reviewed status, scope, dates, key findings and limitations.",
  "context_links": [{"label": "Official proposed packet", "href": "https://example.gov/package.pdf"}],
  "coverage_notes": "Enumerate matched, replaced, unchanged, out-of-scope and unverified items.",
  "entries": [{
    "id": "rule-id",
    "title": "Rule subject",
    "classification": "Substantive proposal",
    "current_path": "current/rule-id.md",
    "target_path": "proposed/rule-id.md",
    "summary": "Current paragraph X permits A; proposed paragraph Y changes B.",
    "impact": "Explain agency, rendering-provider, member and revenue-cycle implications.",
    "action": "Operational owner: verify and prepare the relevant change.",
    "risk": "Optional material ambiguity or implementation dependency."
  }],
  "afterword": "Forecast actions, unresolved questions, validation evidence, provenance and limitations."
}
```

Renderer outputs: concise report, a `.text.md` exact full-source companion, a `.diff.md` text-diff companion, and a `.sources.json` hash/coverage companion. Text diffs compare normalized whitespace and Markdown list indentation; this is a locator rather than a paragraph-renumbering-aware legal redline. Keep GFM table rows contiguous with a single newline; escape pipes in cells. Validate rendered table structure and links outside the renderer against the entire repository tree if targets are not materialized locally. Add reciprocal source links only after generation so report links can target stable anchors. Never use raw content hashes after adding navigation without recomputing them; preserve an immutable source hash separately.
