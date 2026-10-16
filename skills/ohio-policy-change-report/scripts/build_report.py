#!/usr/bin/env python3
"""Render linked policy reports from reviewed comparison specs and exact source bodies."""
import argparse, difflib, hashlib, json, re
from pathlib import Path
from urllib.parse import quote, unquote

def body(text):
    marker = '\n## Rule Text\n'
    if marker not in text:
        raise ValueError('Source must contain ## Rule Text')
    result = text.split(marker, 1)[1].strip()
    if not result or 'No rule text found' in result:
        raise ValueError('Missing source body')
    return result

def norm(text):
    return [' '.join(re.sub(r'^\s*[-*] ', '', p).split())
            for p in re.split(r'\n\s*\n', text) if p.strip()]

def slug(value):
    return 'policy-' + re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-')

def link(path, output):
    import os
    return quote(os.path.relpath(path, output.parent).replace('\\', '/'), safe='/')

def embed(text, source_path, output):
    # Rebase navigational metadata when embedding a document in another folder.
    prefix, marker, rule_text = text.partition('\n## Rule Text\n')
    def replace_link(match):
        target = match[1]
        if target.startswith(('https:', 'http:', 'mailto:')):
            return match[0]
        path, separator, fragment = target.partition('#')
        resolved = (source_path.parent / unquote(path)).resolve() if path else source_path
        return '](' + link(resolved, output) + (separator + fragment if separator else '') + ')'
    prefix = re.sub(r'\]\(([^)]+)\)', replace_link, prefix)
    text = prefix + marker + rule_text
    # Downgrade document headings without editing the rule body.
    return re.sub(r'^(#{1,3}) ', lambda m: '#' * (len(m[1]) + 3) + ' ', text, flags=re.M)

def build(spec_path, output):
    spec_path = spec_path.resolve(); output = output.resolve()
    spec = json.loads(spec_path.read_text(encoding='utf-8'))
    required = ['title', 'mode', 'as_of', 'baseline_label', 'target_label', 'overview', 'entries']
    for key in required:
        if key not in spec: raise ValueError('Missing field: ' + key)
    if spec['mode'] not in ['refresh', 'current-versus-proposed', 'draft-revision']:
        raise ValueError('Unknown comparison mode')
    if not spec['entries']: raise ValueError('No entries')
    output.parent.mkdir(parents=True, exist_ok=True)
    diff_path = output.with_suffix('.diff.md')
    hash_path = output.with_suffix('.sources.json')
    text_path = output.with_suffix('.text.md')
    table = ['| Identifier | Classification | Report entry |', '|---|---|---|']
    full_text = ['# Full Baseline and Target Source Text', f'[Return to summary]({quote(output.name)})']
    head = [f"# {spec['title']}", f"**As of:** {spec['as_of']}  \n**Mode:** {spec['mode']}  \n**Baseline:** {spec['baseline_label']}  \n**Target:** {spec['target_label']}",
            '## Executive Summary', spec['overview'], '## Source Links']
    head += [f"- [{x['label']}]({x['href']})" for x in spec.get('context_links', [])]
    head += [f'- [Reproducible text diffs]({quote(diff_path.name)})',
             f'- [Source hashes and coverage]({quote(hash_path.name)})',
             '## Comparison Coverage', spec.get('coverage_notes', 'See the entry inventory below.'),
             f'[Full source text appendix]({quote(text_path.name)})']
    seen = set(); blocks = []; diffs = ['# Policy Source Text Diffs']; hashes = []
    for entry in spec['entries']:
        for key in ['id', 'title', 'classification', 'current_path', 'target_path', 'summary', 'impact', 'action']:
            if not entry.get(key): raise ValueError('Missing entry field: ' + key)
        if entry['id'] in seen: raise ValueError('Duplicate identifier')
        seen.add(entry['id']); anchor = slug(entry['id'])
        cell = lambda value: str(value).replace('|', '\\|').replace('\n', ' ')
        table.append(f"| {cell(entry['id'])} | {cell(entry['classification'])} | [Open](#{anchor}) |")
        source_data = []
        for side, field in [('current', 'current_path'), ('target', 'target_path')]:
            path = (spec_path.parent / entry[field]).resolve()
            text = path.read_text(encoding='utf-8'); rule_body = body(text)
            source_data.append((path, text, rule_body))
            hashes.append({'id': entry['id'], 'side': side, 'path': link(path, output),
                           'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                           'rule_body_sha256': hashlib.sha256(rule_body.encode()).hexdigest()})
        current, target = source_data
        equal = norm(current[2]) == norm(target[2])
        if equal and entry['classification'].lower().startswith('substantive'):
            raise ValueError('Substantive classification with equal text: ' + entry['id'])
        blocks += [f'<a id="{anchor}"></a>', f"### {entry['id']} — {entry['title']}",
                   f"**Classification:** {entry['classification']}", entry['summary'],
                   '**Likely impact:** ' + entry['impact'], '**Next action:** ' + entry['action']]
        if entry.get('risk'): blocks.append('⚠️ Risk Flag. ' + entry['risk'])
        blocks += [f'[Baseline source]({link(current[0], output)}) · [Target source]({link(target[0], output)}) · [Text diff]({quote(diff_path.name)}#{anchor})',
                   f'[Full baseline and target text]({quote(text_path.name)}#{anchor})', '[Return to coverage](#comparison-coverage)']
        full_text += [f'<a id="{anchor}"></a>', f"## {entry['id']} — {entry['title']}",
                      '### Full Baseline Text', embed(current[1].strip(), current[0], text_path),
                      '### Full Target Text', embed(target[1].strip(), target[0], text_path),
                      f'[Return to rule summary]({quote(output.name)}#{anchor})']
        unified = '\n'.join(difflib.unified_diff(norm(current[2]), norm(target[2]),
                            fromfile=entry['current_path'], tofile=entry['target_path'], lineterm=''))
        diffs += [f'<a id="{anchor}"></a>', f"## {entry['id']} — {entry['title']}",
                  '```diff\n' + (unified or 'No normalized body-text change.') + '\n```',
                  f'[Return to report]({quote(output.name)}#{anchor})']
    report_text = '\n\n'.join(head + ['\n'.join(table)] + ['## Changes and Likely Impacts'] + blocks +
                             ['## Operational Actions and Validation', spec.get('afterword', '')]) + '\n'
    appendix_text = '\n\n'.join(full_text) + '\n'
    # Confirm both exact rule bodies remain embedded in the appendix.
    for entry in spec['entries']:
        for field in ['current_path', 'target_path']:
            raw = (spec_path.parent / entry[field]).read_text(encoding='utf-8')
            if body(raw) not in appendix_text: raise ValueError('Source preservation failed')
    output.write_text(report_text, encoding='utf-8')
    text_path.write_text(appendix_text, encoding='utf-8')
    diff_path.write_text('\n\n'.join(diffs) + '\n', encoding='utf-8')
    hash_path.write_text(json.dumps({'mode': spec['mode'], 'as_of': spec['as_of'],
                         'entry_count': len(seen), 'sources': hashes}, indent=2) + '\n', encoding='utf-8')
    return {'report': str(output), 'text': str(text_path), 'diff': str(diff_path), 'hashes': str(hash_path), 'entries': len(seen)}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('spec', type=Path, help='Reviewed JSON specification; source paths relative to this file')
    parser.add_argument('--output', required=True, type=Path, help='Output Markdown report path')
    args = parser.parse_args()
    print(json.dumps(build(args.spec, args.output)))
