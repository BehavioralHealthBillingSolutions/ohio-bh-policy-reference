---
name: ohio-laws-to-markdown
description: "Extract verbatim rule or statute text from codes.ohio.gov (Ohio Administrative Code and Ohio Revised Code) and output clean Markdown with paragraph hierarchy, effective dates, and supplemental history preserved. Use when the user pastes an OAC chapter, OAC rule, ORC chapter, or ORC section URL (or a bare identifier like 5122-25, 5160-1-05.1, or 5119.36) and asks to extract, convert, pull, dump, or archive the rule text as .md, Markdown, or a document. Works for any chapter or title, not just behavioral health."
license: MIT
compatibility: "Python 3.8+ standard library only (no third-party packages). Requires outbound HTTPS to codes.ohio.gov."
metadata:
  author: chelsea-kohler
  version: '1.2'
---

# Ohio Laws to Markdown

Turns any codes.ohio.gov chapter, rule, or section page into citation-ready Markdown
without hand-copying text out of the browser.

## When to Use This Skill

- The user gives an OAC chapter URL and wants every rule in it as one `.md` file.
- The user gives one or more individual rule or section URLs/identifiers.
- The user wants an ORC chapter or a single ORC section pulled into Markdown.
- The user wants a point-in-time snapshot of rule text for a policy file, wiki page,
  crosswalk, or audit binder.

Do **not** use this for the authenticated PDF versions or for pending/proposed rule
filings on the Register of Ohio — this skill reads the current published HTML only.

## Instructions

1. **Identify the targets.** Accept URLs or bare identifiers; the script normalizes both:

   | Input | Resolves to |
   |---|---|
   | `5122-25` | OAC chapter 5122-25 (all rules) |
   | `5122-25-01`, `5160-1-05.1` | single OAC rule |
   | `chapter-5119` | ORC chapter 5119 (all sections) |
   | `5119.36`, `section-5119.36` | single ORC section |
   | any full `https://codes.ohio.gov/...` URL | that page |

   ORC chapters have no hyphen in the number (`5119`); OAC chapters do (`5122-25`).
   That is how the script picks the right code, so keep the hyphens intact.

2. **Run the script** from `scripts/ohio_laws_to_markdown.py`:

   ```bash
   python3 scripts/ohio_laws_to_markdown.py chapter-5122-25 \
       -o OAC_Chapter_5122-25.md --cache ./.oac_cache
   ```

   Flags:
   - `-o FILE` — one combined Markdown file (default `ohio_laws_extract.md`).
   - `--split DIR` — one `.md` per rule/section instead of (or in addition to) `-o`.
   - `--cache DIR` — save the raw HTML retrieved during this run. Always fetch live pages;
     never reuse older cached responses or stamp them with a new retrieval date.
   - `--delay SEC` — pause between requests (default `0.5`); raise it for large chapters.
   - `--no-supplemental` — drop the Authorized By / Amplifies / Prior Effective Dates block.

   Multiple targets in one run are fine and are de-duplicated in page order:
   `python3 scripts/ohio_laws_to_markdown.py 5122-25 5122-26 -o oac_certification_bundle.md`

3. **Verify the output before delivering.** Always check:
   - The `## ` heading count equals the number of rules/sections on the chapter page.
   - No file ends mid-sentence and no rule body renders as `> No rule text found`
     (that means the page is rescinded/reserved or uses an unexpected template).
   - Deep nesting looks right on at least one spot-check for ORC output (see caveat below).

4. **Report the effective dates.** Tell the user the effective date(s) found in the output,
   and explicitly flag when a chapter carries a recent uniform effective date — that means
   they are looking at newly amended text and any internal policy built on the prior
   effective dates is stale. Include a **⚠️ Risk Flag** when the extract supersedes text
   the user may still be relying on operationally.

5. **Share the file** and state the retrieval date, which the script stamps into the header.

## Output Shape

```markdown
# Chapter 5122-25 | Certification

Source: https://codes.ohio.gov/ohio-administrative-code/chapter-5122-25

Retrieved: August 20, 2026

Documents: 12

---

## Rule 5122-25-01 | Applicability.

URL: https://codes.ohio.gov/ohio-administrative-code/rule-5122-25-01

**Effective:** August 1, 2026
**Promulgated Under:** 119.03

- (A) Statement of applicability

- In general, the rules in this chapter apply to ...

    - (1) In accordance with division (B) of section 5119.35 ...

### Supplemental Information

**Authorized By:** R.C. 5119.36
**Five Year Review Date:** 8/1/2031
**Prior Effective Dates:** 10/1/2003, 2/1/2016, 10/31/2019

---
```

Paragraph depth is expressed as nested Markdown list indentation, so the outline survives
a paste into Word, OneNote, Confluence, or a wiki page.

## How Depth Is Determined

- **OAC rule pages** carry the site's own `level-N` classes on each paragraph. Those are
  authoritative and are used directly.
- **ORC section pages** carry no level classes. Depth is inferred from the
  `(A)` → `(1)` → `(a)` → `(i)` → `(I)` designator ladder, with a special case for `(i)`
  following `(h)` (letter continuation) versus `(i)` opening a roman sub-list.
- **Unnumbered continuation paragraphs** inherit the depth of the paragraph above them,
  which is how the site itself presents them.

⚠️ Risk Flag: depth inference on ORC output is best-effort. If a paragraph citation is
load-bearing for a compliance position, confirm the nesting against the authenticated PDF
linked on the page before relying on it. The paragraph **text** is verbatim either way —
only the visual indentation is inferred.

## Known Limitations

- Hyperlink targets on cross-references are stripped; the visible citation text
  (for example "rule 5122-29-09.1 of the Administrative Code") is preserved but does not
  hyperlink. This is deliberate so the Markdown stays portable.
- Rescinded or reserved rules produce a heading plus a `> No rule text found` note rather
  than failing the run — treat that as a signal to check the page manually.
- Tables inside rule bodies are converted to Markdown tables, but they are rare on this
  site and complex merged-cell layouts may need manual cleanup.
- This is a snapshot, not a subscription. Rules change; re-run and diff rather than
  assuming a saved file is current. Pair with a scheduled re-run when monitoring a chapter.
- The script is polite by default but has no published rate limit to rely on; keep
  `--delay` at or above `0.5` for multi-hundred-section ORC chapters.

## Monitoring Pattern

To watch a chapter for amendments, fetch live content into a stable working file and diff
against the prior output. `--cache` saves live HTML for inspection; it does not skip requests:

```bash
python3 scripts/ohio_laws_to_markdown.py chapter-5122-25 -o current.md
diff previous.md current.md
```

A change in an `**Effective:**` line or a new `Prior Effective Dates` value is the reliable
amendment signal — body text alone can shift from a non-substantive republication.

