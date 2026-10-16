# BIA/ERF Thorough Parse and Markdown Review

**Review date:** October 8, 2026. Both packets are historical proposed sources, not effective rules.

[Return to change report](../ERF236150_Current_vs_Proposed_Change_Report_2026-10-07.md)

## Packet Coverage

| Packet | PDF pages | Proposed rules | Front matter | Rescinded predecessors | Fee appendix |
|---|---:|---:|---|---|---|
| September ERF | 88 | 11 | 1–2 | 15–20, 33–43, 54–56, 61–64, 71–74 | 29–32 |
| October BIA/CSI | 62 | 9 | 1–11 | 29–39 | None |



Every one of the **150 pages** is classified. The clean exports contain **20 rule versions**. Rule 5160-27-03 and -11 appear in September but are not attached in October; omission is not classified as repeal. The October BIA identifies a submission date of October 5 and comment deadline of October 12, 2026.

## Clean Rule Text

| Rule | September ERF | October BIA |
|---|---|---|
| 5160-8-05 | [Text](ERF_September/5160-8-05.md) | [Text](BIA_October/5160-8-05.md) |
| 5160-27-01 | [Text](ERF_September/5160-27-01.md) | [Text](BIA_October/5160-27-01.md) |
| 5160-27-02 | [Text](ERF_September/5160-27-02.md) | [Text](BIA_October/5160-27-02.md) |
| 5160-27-03 | [Text](ERF_September/5160-27-03.md) | Not attached |
| 5160-27-04 | [Text](ERF_September/5160-27-04.md) | [Text](BIA_October/5160-27-04.md) |
| 5160-27-06 | [Text](ERF_September/5160-27-06.md) | [Text](BIA_October/5160-27-06.md) |
| 5160-27-08 | [Text](ERF_September/5160-27-08.md) | [Text](BIA_October/5160-27-08.md) |
| 5160-27-09 | [Text](ERF_September/5160-27-09.md) | [Text](BIA_October/5160-27-09.md) |
| 5160-27-10 | [Text](ERF_September/5160-27-10.md) | [Text](BIA_October/5160-27-10.md) |
| 5160-27-11 | [Text](ERF_September/5160-27-11.md) | Not attached |
| 5160-27-14 | [Text](ERF_September/5160-27-14.md) | [Text](BIA_October/5160-27-14.md) |



## Fee Appendix

The September appendix has **145 data rows, nine source columns, and 1,341 cells including headers**. Each cell was checked independently using word-center containment within its grid boundaries: zero mismatches. Empty cells remain empty, with no rate carry-forward or inferred provider tier. Dates, modifiers, status codes and allowable places of service remain in their printed columns.

- [Fee table CSV](ERF_September_Fee_Appendix_A.csv)
- [Raw grid cells and page boundaries](ERF_September_Fee_Appendix_A.cells.json)
- [Printed footnotes](ERF_September_Fee_Appendix_A_Notes.md)

These are September proposed rates. **October includes no fee appendix**, so this audit does not confirm them for the October proposal. Printed footnote 4 cites 5101-27-01; the source citation is retained rather than silently corrected.

## Extraction Checks

All retained black/blue rule-body spans preserve their complete normalized sequence, including isolated numbers. Red deleted spans are excluded from clean proposal bodies; titles, headers, small markup and footers are classified separately. No unclassified substantive-color spans were found. First-page title boundaries are detected from the first (A) clause to handle wrapped titles.

All eleven September rule bodies also match the corrected historical export under the same normalization, with the fee appendix checked separately by cell. [September results](September_Transcript_Recheck.json).

All nine October rule bodies match the previously published transcripts after removing punctuation, whitespace and Markdown bullets; this recheck found no changed words under that normalization. [Results](October_Transcript_Recheck.json). This is a transcript agreement check, not a legal equivalence claim.

## Full Evidence and Reproduction

- [Page/span coverage and hashes](PDF_Parse_Coverage.json)
- [Proposed source-span ledger](PDF_Source_Spans.jsonl.gz)
- [September complete page transcripts, including rescinded predecessors](ERF_September_All_Pages.md)
- [October complete page transcripts, including BIA and rescinded ACT](BIA_October_All_Pages.md)
- [September front matter](ERF_September_Front_Matter.md)
- [October BIA front matter](BIA_October_Front_Matter.md)
- [Reproducible extractor](reparse_packets.py)

Run with PyMuPDF: `python reparse_packets.py --erf ERF236150.pdf --bia BIAERF236150.pdf --output audit-output`. Use PDFs with the hashes in the coverage manifest. Raw page transcripts retain drafting markup and must not be used directly as operative text.

## Markdown Review

Summary tables use contiguous GFM rows, consistent column counts, and escaped cell pipes. The ORC and current-versus-proposed reports retain summaries and likely impacts while moving full source text into exact linked companions. Existing rule entry anchors remain available for links from other documents. Full source-body preservation and relative link/anchor checks are recorded in [Markdown validation](Markdown_Validation.json).
