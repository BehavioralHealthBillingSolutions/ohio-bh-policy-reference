# ERF 236150 Source Validation and Provenance

**Review date:** October 7, 2026 America/New_York  
**Source status:** October 5 BIA/CSI draft attachment, not effective  
**Current sources:** Live Ohio Laws extraction retrieved October 7, 2026  
**Prior draft:** September 11 repository working transcription, with its September 12 validation record

The stable BIA URL returned a 62-page PDF with submission date October 5, 2026 and comment deadline October 12, 2026. Pages 1–11 are the BIA narrative. The attachment contains nine unique proposed rules plus a separately marked ACT predecessor on pages 29–39. The predecessor is excluded from the clean proposed rule text. Red deleted spans are excluded, black retained and blue added spans are included, and gray/invisible markup labels and running headers/footers are excluded. Numeric-only rule text is not discarded by value.

Current coverage is 12 rules in Chapter 5160-27 plus rule 5160-8-05. Nine current counterparts and nine proposed counterparts are preserved in the linked full-text companion. Effective rules 5160-27-03, -11, -12 and -13 are outside this October proposed packet, not classified as repealed. September proposed -03 and -11 remain in the earlier immutable package.

## Extraction Inventory

| Rule | PDF pages | Retained body spans | Excluded red spans | Proposed body characters |
|---|---|---:|---:|---:|
| 5160-8-05 | 12–20 | 355 | 89 | 14788 |
| 5160-27-01 | 21–23 | 81 | 5 | 4046 |
| 5160-27-02 | 24–28 | 157 | 0 | 10624 |
| 5160-27-04 | 40–44 | 143 | 0 | 9504 |
| 5160-27-06 | 45–47 | 78 | 0 | 4997 |
| 5160-27-08 | 48–51 | 116 | 0 | 7347 |
| 5160-27-09 | 52–57 | 189 | 0 | 12270 |
| 5160-27-10 | 58–59 | 54 | 9 | 3172 |
| 5160-27-14 | 60–62 | 112 | 24 | 4589 |

## Source Hashes

| Source | SHA-256 |
|---|---|
| Official BIA PDF returned by source URL | `2bf304ea740a8206cefd3045c9619d7ef9f53c04423263b19b22576fcb2d156a` |
| [ERF236150_BIA_2026-10-05_Narrative.md](../Reference%20MD%20Files/All%20Historical%20and%20Current/ERF236150_BIA_2026-10-05_Narrative.md) | `c5f44e14b6c3fe45cb99fee24a9238fc4793d65fc116d9c48a5d85c3a4d21a7e` |
| [ERF236150_BIA_2026-10-05_Proposed_Clean_Text.md](../Reference%20MD%20Files/All%20Historical%20and%20Current/ERF236150_BIA_2026-10-05_Proposed_Clean_Text.md) | `2b777dac9e191bcc14d9fcf175b8dc3baec96335a97b96a4fa14cc8f894a291d` |
| [OAC_Chapter_5160-27.md](../Reference%20MD%20Files/All%20Historical%20and%20Current/OAC/2026-10-07/OAC_Chapter_5160-27.md) | `00ae87094f6108cb6f9bb5bf948b42d0d937bb70154f1a21c9d596d763b3de20` |
| [OAC_Rule_5160-8-05.md](../Reference%20MD%20Files/All%20Historical%20and%20Current/OAC/2026-10-07/OAC_Rule_5160-8-05.md) | `6079064bdd6681a7d571afe628f260f84532af7867a715fa0d090e1f88b7a0b7` |

## Verification

- Full current chapter/rule extraction has expected heading counts of 12 and 1, effective metadata for each rule, and no missing-text placeholders.
- Proposed rule coverage matches the BIA's nine unique identifiers. All nine begin at paragraph (A), and rule boundaries are preserved. An inventory of the retained and excluded colored spans is recorded above.
- Representative PDF pages were visually inspected for markup interpretation and material service/limitation clauses. Full/half MH attendance thresholds, TBS qualification text, PSR/residential exclusion, ASAM documentation and referenced errors were checked against extracted rule text.
- The renderer preserves each rule body exactly in the full-text companion and creates current-versus-proposed diffs and source/body hashes. The renderer was also exercised on a separate single-rule invocation with exact-body and link checks.
- Local relative filenames and fragments are checked before publication. Source-hash metadata is generated after navigational links are added; immutable source copies are hashed separately.

## Limitations

These are working Markdown transcriptions, not authenticated legal copies. Whitespace and paragraph indentation are normalized; substantive wording and source typos are retained. Deleted markup and proposed text must be distinguished using the source PDF. No whole-packet dollar rates or replacement authorization thresholds can be validated from this package because those appendices are absent. Unresolved draft inconsistencies are identified under the affected report entries. Do not infer adoption, a general effective date, or a payer rollout date from the printed comment deadline or July 2027 milestones.

## October 8 Thorough Parse Recheck

[Complete BIA/ERF parse audit](Parse_Audit_2026-10-08/README.md) classifies all 150 pages in the September and October PDFs, extracts 20 proposed rule versions, and reconstructs all 145 September fee-table data rows by source grid cells. The nine October body transcripts agree with the prior export after word normalization. Summary reports now link to exact full-text companions; the Markdown table generator uses contiguous rows.

