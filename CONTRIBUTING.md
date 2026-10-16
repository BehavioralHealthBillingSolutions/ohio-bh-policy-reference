# Contributing

Use a branch and pull request. Report extraction errors with the document version and original
PDF viewer page number. Never include member data, claims, credentials, or private agency contracts.

- Never commit complete provider-agreement PDFs, omitted Milliman content, full BH manuals,
  or private repository history. Link to the official publisher instead.
- Existing archived sources, comparison snapshots, and versioned agreement excerpts are immutable.
  Correct errors with a new dated/versioned copy and a clear explanation.
- Keep source text, BHBS interpretation, and editorial omission notices visibly separate.
- Every new preserved source needs an entry in `PUBLICATION_MANIFEST.json` with its exact-byte
  SHA-256, source URL, status, and curation date. Preserve the source's own document dates.
- Do not silently substitute new bytes fetched from an old stable URL. Hash and date the new version.
- Update `OMISSIONS.json` and its explanation when adding a new agreement version. Page ranges
  are PDF viewer positions. Inspect the boundaries and associated attachments, not just the copyright page.
- Review `.github/` changes carefully. Required checks and branch rules must be activated separately
  in GitHub settings; importing files does not activate a ruleset.
