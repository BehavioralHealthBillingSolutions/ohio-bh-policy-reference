#!/usr/bin/env python3
"""Build page-aligned browser views from curated agreement excerpts."""
import hashlib
import json
from pathlib import Path
import re


def main():
    root = Path(__file__).resolve().parents[1]
    excerpts = root / 'Managed Care Agreements/Excerpts'
    records = json.loads((excerpts / 'OMISSIONS.json').read_text())
    manifest_path = root / 'PUBLICATION_MANIFEST.json'
    manifest = json.loads(manifest_path.read_text())
    manifest['preserved_sources'] = [r for r in manifest['preserved_sources'] if '/Parts/' not in r['path']]
    for rec in records:
        text = (root / rec['excerpt_path']).read_text()
        offset = text.index('\n## Original PDF page ')
        header = text[:offset].replace('(OMISSIONS.md)', '(../../OMISSIONS.md)')
        blocks = re.split(r'(?=^## (?:Original PDF page \d+|OMITTED — original PDF pages))', text[offset:], flags=re.M)
        chunks = []
        chunk = ''
        for block in blocks:
            if chunk and len(chunk) + len(block) > 55000:
                chunks.append(chunk)
                chunk = ''
            chunk += block
        if chunk:
            chunks.append(chunk)
        folder = excerpts / 'Parts' / rec['id']
        folder.mkdir(parents=True, exist_ok=True)
        index = [f"# {rec['title']} — browser reading sections", '',
                 '> **INCOMPLETE REFERENCE EXCERPT — NOT THE COMPLETE OFFICIAL DOCUMENT.**', '',
                 f"[Complete official PDF]({rec['url']}) · [Omission register](../../OMISSIONS.md)", '',
                 rec['reason'], '',
                 'These smaller files preserve original PDF page numbers. A listed range may contain an explicit omission notice.', '']
        for n, chunk in enumerate(chunks, 1):
            filename = f'part-{n:02d}.md'
            content = header + '\n\n[Reading index](INDEX.md) · [Omission register](../../OMISSIONS.md)\n\n' + chunk
            (folder / filename).write_text(content)
            pages = re.findall(r'^## Original PDF page (\d+)$', chunk, re.M)
            label = f'Original PDF pages {pages[0]}–{pages[-1]}' if pages else 'Omission notice'
            index.append(f'- [{label}]({filename})')
        index += ['', f"[Single-file retained transcription for download](../../{rec['id']}_EXCERPT.md) — still incomplete; not the official PDF.", '']
        (folder / 'INDEX.md').write_text('\n'.join(index))
        for file in sorted(folder.glob('*.md')):
            manifest['preserved_sources'].append({'path': file.relative_to(root).as_posix(),
                'sha256': hashlib.sha256(file.read_bytes()).hexdigest(), 'source_url': rec['url'],
                'status': 'incomplete agreement browser-reading view; governed by omission register'})
        for path, prefix in [(root / 'Managed Care Agreements/README.md', 'Excerpts/'), (excerpts / 'OMISSIONS.md', '')]:
            old = f"{prefix}{rec['id']}_EXCERPT.md"
            new = f"{prefix}Parts/{rec['id']}/INDEX.md"
            path.write_text(path.read_text().replace(f']({old})', f']({new})'))
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main()
