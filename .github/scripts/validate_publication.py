#!/usr/bin/env python3
"""Validate curated publication sources and omission disclosures from Git objects."""
import argparse
import hashlib
import json
from pathlib import PurePosixPath
import re
import subprocess


def git(*args):
    return subprocess.check_output(['git',*args])


def tree(ref):
    out={}
    for rec in git('ls-tree','-rz','--full-tree',ref).split(b'\0'):
        if rec:
            info,path=rec.split(b'\t',1);out[path.decode()]=tuple(info.decode().split())
    return out


def read(ref,path):
    return git('show',ref+':'+path)


def protected(path):
    return (path.startswith(('Reference MD Files/All Historical and Current/','Ohio Rules/Comparisons/'))
            or (path.startswith('Managed Care Agreements/Excerpts/') and (path.endswith('_EXCERPT.md') or '/Parts/' in path)))


def check_omissions(records,read_file):
    errors=[]
    for rec in records:
        name=rec['id'];included=rec['included_pdf_pages'];omitted=rec['omitted_pdf_pages']
        if (set(included)&set(omitted) or sorted(included+omitted)!=list(range(1,rec['pages']+1))):
            errors.append(name+': page inventory has overlap, duplicates, or gaps')
        expected=list(range(rec['omit'][0],rec['omit'][1]+1)) if rec['omit'] else []
        if omitted!=expected:
            errors.append(name+': omitted pages differ from declared ranges')
        data=read_file(rec['excerpt_path']);text=data.decode()
        if hashlib.sha256(data).hexdigest()!=rec['excerpt_sha256']:
            errors.append(name+': excerpt hash mismatch')
        headers=[int(x) for x in re.findall(r'^## Original PDF page (\d+)$',text,re.M)]
        if headers!=included:
            errors.append(name+': page headings do not match retained inventory')
        if ('INCOMPLETE REFERENCE EXCERPT' not in text or rec['url'] not in text
                or rec.get('completeness_claim') is not False):
            errors.append(name+': required incompleteness/source disclosure missing')
        if omitted and f'## OMITTED — original PDF pages {min(omitted)}–{max(omitted)}' not in text:
            errors.append(name+': omission marker missing')
    return errors


def validate(base,head):
    before,after=tree(base),tree(head);errors=[]
    for path in before:
        if protected(path) and before[path]!=after.get(path):
            errors.append('Preserved source cannot be changed/deleted/renamed: '+path)
    manifest=json.loads(read(head,'PUBLICATION_MANIFEST.json'))
    exclusions=json.loads(read(head,'EXCLUDED_CONTENT_SHA256.json'))
    excluded=set(exclusions['sha256'])
    sources={r['path']:r for r in manifest['preserved_sources']}
    for path,entry in after.items():
        blob=read(head,path);digest=hashlib.sha256(blob).hexdigest()
        if digest in excluded:
            errors.append('Excluded complete source content detected: '+path)
        if PurePosixPath(path).name.startswith('BH_Manual_'):
            errors.append('Full manual snapshots must remain link-only: '+path)
        if path.startswith('Managed Care Agreements/') and path.lower().endswith('.pdf'):
            errors.append('Complete agreement PDFs must remain link-only: '+path)
        if path.endswith('.json'):
            try:json.loads(blob)
            except (ValueError,UnicodeDecodeError):errors.append('Invalid JSON: '+path)
        if protected(path):
            if entry[0]!='100644':errors.append('Preserved source must be regular/non-executable: '+path)
            source=sources.get(path,{})
            if source.get('sha256')!=digest:errors.append('Missing/incorrect source hash: '+path)
            if not source.get('source_url','').startswith('https://') or not source.get('status'):
                errors.append('Missing source attribution/status: '+path)
    for path in sources:
        if path not in after:errors.append('Manifest source missing: '+path)
    records=json.loads(read(head,'Managed Care Agreements/Excerpts/OMISSIONS.json'))
    errors.extend(check_omissions(records,lambda path:read(head,path)))
    return errors


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--base',required=True);ap.add_argument('--head',default='HEAD');args=ap.parse_args()
    errors=validate(args.base,args.head)
    for e in errors:print('ERROR: '+e)
    if errors:raise SystemExit(1)
    print('PASS: immutable sources, exact hashes, exclusions, and omission disclosures verified.')


if __name__=='__main__':main()
