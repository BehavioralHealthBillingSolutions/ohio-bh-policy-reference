# Curated publication and maintenance

This repository starts with new Git history. Complete manual copies, complete agreement PDFs,
and the private archive's old branches/commits are not imported. Rules/proposals and the dated
BHBS rule-comparison outputs are included with their source/version caveats.

## Agreement method

The supplied builder pins three official PDFs by SHA-256 and page count, extracts retained pages
as plain text, and places editorial notices outside source-text blocks. It omits the entire
identified Milliman report including blank pages and supporting rate tables, not merely the
copyright notice. The Appendix M divider and the next Appendix N are retained.

The July 2026 OhioRISE source has no identified Milliman report in its text; this observation
does not certify completeness or clear every third-party right. Its transcription remains
prominently labeled as an incomplete reference, with original-page links and extraction caveats.

## Reproduce the content build

**Device:** Windows desktop. **Application:** Windows Terminal → PowerShell.
**Working folder:** this repository root. **Prerequisites:** Python 3.10+ and PyMuPDF installed.
The source-root argument points to a separately available reviewed source checkout. Input PDFs
must be downloaded from the official URLs listed in the builder and saved using its version IDs.
Keep those complete PDFs outside this repository. Do not commit them.

```powershell
py -3 .\scripts\build_public_reference.py --source-root "C:\path\to\reviewed-source-checkout" --agreement-pdfs "C:\path\to\private-input-pdfs" --output "C:\path\to\new-empty-build"
```

**Output:** a new local content tree. This does not push, publish, copy Git history, or enable
GitHub settings. It creates the rule/tool seed files and agreement excerpts/omission register;
repository-specific READMEs, workflow controls, publication manifest, and release annotations
are maintained separately. A changed source PDF must be independently reviewed and repinned.

## Protections and updates

- Import `.github/rulesets/bhbs-main-protection.json` in GitHub's repository Settings → Rules →
  Rulesets after the workflow is on main. The file does not activate settings on its own.
- The validator blocks changes/deletion/renames to preserved sources and versioned excerpts.
  Add a new dated version instead. It checks manifest byte hashes and omission page inventories.
- Known excluded complete-source hashes and full agreement PDFs are blocked. This catches the
  reviewed originals; it is not a complete copyright/privacy detector for arbitrary new content.
- Code-owner approval is optional while Chelsea is the only maintainer. Review control-file
  changes carefully; administrators can change GitHub settings.
- Keep fresh source bytes and historical interpretations separate. Do not silently replace a
  proposal with effective law or relabel an older report as a fresh review.

Source PDFs are linked to their publishers. The public repository does not include the omitted
Milliman pages or grant rights to other source-owned material. Full manuals remain link-only.

## Rebuild browser sections

**Device:** Windows desktop. **Application:** Windows Terminal → PowerShell.
**Working folder:** this repository root. **Prerequisites:** Python 3.10+.

```powershell
py -3 .\scripts\build_browser_views.py
```

**Output:** page-aligned agreement reading sections and updated manifest hashes.
The generator retains the curated omissions and incomplete-document notices.
Review generated changes before committing. Python runs this script directly; it does not invoke PowerShell.
