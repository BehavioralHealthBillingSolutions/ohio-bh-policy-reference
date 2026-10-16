# ERF 236150 clean-text correction and validation record

**Priority:** P0  
**Status:** Corrected candidate for repository review  
**Validated:** 2026-09-12  
**Policy status:** Proposed; not effective  

## Record corrected

`Reference MD Files/All Historical and Current/ERF236150_Proposed_BH_Rules_2026-09-11.md`

The prior export removed every isolated integer as though it were a PDF page number. That deleted valid rule content, including numeric CPT/HCPCS rows and numeric amendment text. The corrected export removes numeric-only text only when its PDF position is within the running header or footer.

## Source and output identity

| Artifact | SHA-256 |
|---|---|
| Original ERF 236150 PDF | `a5340983d9de47e687f885e332c1d6d5c7c3177ba25842ad68355dddfec4755d` |
| Corrected clean Markdown | `9340574a054766af38a83018a52a1badd804085f98397c918b1e7acb732c734b` |

## Inclusion and exclusion rules

The corrected record:

- includes all 11 proposed rules in the packet;
- retains proposed blue additions and unchanged black rule text;
- retains isolated numeric rule and fee-schedule content, including CPT/HCPCS values;
- excludes red deleted text and the five predecessor copies marked for rescission;
- excludes running headers, footers, page numbers, redline labels, and authoring artifacts;
- repairs PDF line-wrap splits where a decimal value was divided across lines, including `10.5`.

## Validation evidence

- Corrected file length: 1,805 lines.
- Rule-heading count: 11.
- All 633 reviewed blue-added spans were present in the corrected export.
- All 1,855 reviewed black-retained spans were present in the corrected export.
- Fifty-two numeric-only CPT/HCPCS or other substantive numeric lines were retained.
- Six page-boundary word and rule-number splits were rejoined, and two isolated numeric insertions were normalized into their surrounding citations.
- Dense fee tables remain sequential text and still require the original PDF for row-layout interpretation.

## Use limitation

This is a working clean-text transcription for comparison and analysis. It is not the official filing, a certified legal transcript, or evidence that the proposal is effective. The original ERF 236150 PDF controls when wording, color, pagination, or table layout matters.
