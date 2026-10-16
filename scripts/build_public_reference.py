#!/usr/bin/env python3
"""Build a curated reference tree without importing private Git history."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
from datetime import datetime, timezone

AGREEMENTS = [
    dict(id='MCO_2026_07', title='ODM Medicaid Managed Care Organization Provider Agreement',
         revision='July 2026', pages=450, omit=[363,404],
         sha256='5911ba372c1f5ae4783b4b649344483f24f9f5c2066b4c2e7b4e2163b9d24428',
         url='https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/Provider%20Agreements/2026_07_MCO_Final_2.pdf'),
    dict(id='MyCare_2026_01', title='ODM Next Generation MyCare Ohio Plan Provider Agreement',
         revision='January 2026', pages=410, omit=[336,369],
         sha256='8095c0e46312ba3bb2a74de9f52bdc80f7fca40f210d8fc3af633a1c19249213',
         url='https://dam.assets.ohio.gov/image/upload/medicaid.ohio.gov/Providers/ProviderTypes/Managed%20Care/MyCareOhio/2026_01_Next_Gen_MyCare_Final_PA.pdf'),
    dict(id='OhioRISE_2026_07', title='ODM OhioRISE Plan Provider Agreement',
         revision='July 2026', pages=375, omit=[],
         sha256='a96beb25bbbd5394323d1afb5219d96113916b7760f15382a93ffc80b415bd86',
         url='https://dam.assets.ohio.gov/image/upload/managedcare.medicaid.ohio.gov/OhioRISE/2026_07_Final_OhioRISE_Provider_Agreement.pdf'),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,required=True,help='Local reviewed source repository')
    parser.add_argument('--agreement-pdfs',type=Path,required=True,help='Directory with version-pinned input PDFs')
    parser.add_argument('--output',type=Path,required=True,help='New, empty output directory')
    args=parser.parse_args()
    import fitz
    if args.output.exists() and any(args.output.iterdir()):
        parser.error('Output must be empty; refusing to merge with an existing tree')
    args.output.mkdir(parents=True,exist_ok=True)
    if args.output.resolve().is_relative_to(args.source_root.resolve()):
        parser.error('Output must be outside the source repository')
    selected=[]
    for directory in ['Ohio Rules','skills']:
        for path in (args.source_root/directory).rglob('*'):
            if path.is_file() and '__pycache__' not in path.parts:
                selected.append(path)
    archive=args.source_root/'Reference MD Files/All Historical and Current'
    for path in archive.rglob('*'):
        if path.is_file() and not path.name.startswith('BH_Manual_') and 'AGREEMENT' not in path.name.upper():
            selected.append(path)
    for name in ['LICENSE','DISCLAIMER.md']:
        selected.append(args.source_root/name)
    for path in selected:
        rel=path.relative_to(args.source_root);dest=args.output/rel
        dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(path,dest)

    records=[]
    for spec in AGREEMENTS:
        data=(args.agreement_pdfs/(spec['id']+'.pdf')).read_bytes()
        if sha(data)!=spec['sha256']:
            raise ValueError('Unreviewed source bytes: '+spec['id'])
        doc=fitz.open(stream=data,filetype='pdf')
        if len(doc)!=spec['pages']:
            raise ValueError('Unexpected PDF page count: '+spec['id'])
        omit=set(range(spec['omit'][0],spec['omit'][1]+1)) if spec['omit'] else set()
        notice=(f"Original PDF pages {spec['omit'][0]}–{spec['omit'][1]} are intentionally omitted: "
                'the Milliman rate-summary report, including its attachments and notices. '
                'Redistribution permission has not been established. The Appendix M divider is retained; '
                'the excerpt resumes at Appendix N.') if omit else (
                'No Milliman report was identified in this July 2026 PDF text. No PDF pages were '
                'intentionally omitted from this transcription. This is not a certification of completeness; '
                'PDF extraction can lose layout, images, tables, or text.')
        lines=[f"# {spec['title']} — reference excerpt",'',
               '> **INCOMPLETE REFERENCE EXCERPT — NOT THE COMPLETE OFFICIAL DOCUMENT.**',
               '> Do not substitute this transcription for the official agreement.', '',
               f"**Source revision:** {spec['revision']}",
               f"**Complete official document:** [Publisher PDF]({spec['url']})",
               f"**Original PDF SHA-256:** `{spec['sha256']}`",
               f"**Original PDF pages:** {spec['pages']}",
               f"**Omission explanation:** {notice}", '',
               'Page labels below use 1-based PDF viewer page numbers, not printed page numbers. '
               'Source text is presented in fenced plain-text blocks to avoid interpreting it as Markdown. '
               'Tables/columns and images must be checked in the original PDF. Contents-page references '
               'to omitted sections remain as original source references; those sections are not included here.',
               '', '[Omission register](OMISSIONS.md)', '']
        included=[]
        for i,page in enumerate(doc,1):
            if i in omit:
                if i==min(omit):
                    lines.extend([f'## OMITTED — original PDF pages {min(omit)}–{max(omit)}','',
                                  notice,'',f"[Read omitted material in the official PDF]({spec['url']}#page={min(omit)})",''])
                continue
            text=page.get_text().rstrip()
            if 'MILLIMAN REPORT' in text or 'Materials may not be reproduced without the express consent of Milliman' in text:
                raise ValueError('Restricted material survived omission: '+spec['id']+' page '+str(i))
            included.append(i)
            fence='`'*max(3,max((len(m.group()) for m in re.finditer(r'`+',text)),default=0)+1)
            lines.extend([f'## Original PDF page {i}','',f"[Open original page]({spec['url']}#page={i})",'',fence+'text',text,fence,''])
        rel=Path('Managed Care Agreements/Excerpts')/(spec['id']+'_EXCERPT.md')
        dest=args.output/rel;dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text('\n'.join(lines),encoding='utf-8')
        records.append({**spec,'excerpt_path':rel.as_posix(),'excerpt_sha256':sha(dest.read_bytes()),
                        'included_pdf_pages':included,'omitted_pdf_pages':sorted(omit),
                        'reason':notice,'completeness_claim':False})
    (args.output/'Managed Care Agreements/Excerpts/OMISSIONS.json').write_text(json.dumps(records,indent=2)+'\n')
    rows=['# Agreement omissions and original-document links','',
          'All files here are reference transcriptions. None is presented as the complete official document.', '',
          'These are ODM-to-plan agreements, not agency-to-payer participation contracts.', '',
          '| Agreement | Original PDF pages | Intentionally omitted | Complete official PDF |',
          '|---|---:|---|---|']
    for x in records:
        omitted=f"{x['omit'][0]}–{x['omit'][1]} (Milliman report)" if x['omit'] else 'None; no Milliman report identified; completeness not certified'
        rows.append(f"| [{x['id']}]({Path(x['excerpt_path']).name}) | {x['pages']} | {omitted} | [Publisher PDF]({x['url']}) |")
    rows.extend(['','Page numbers are PDF viewer positions. Printed pagination restarts within embedded reports.',
                 'The original PDFs are linked, not distributed in this repository. Original complete copies '
                 'must not be committed here, including on branches or in history.', '',
                 'Rights to retained third-party content are not granted by BHBS. Removing a section is '
                 'not a blanket rights clearance for the remaining source text.',''])
    (args.output/'Managed Care Agreements/Excerpts/OMISSIONS.md').write_text('\n'.join(rows))
    print(json.dumps({'copied_files':len(selected),'agreements':len(records),
                      'omitted_pages':{x['id']:len(x['omitted_pdf_pages']) for x in records}}))


if __name__=='__main__':
    main()
