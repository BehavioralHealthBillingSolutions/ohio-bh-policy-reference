import fitz,re,json,hashlib,csv,io
from pathlib import Path
import argparse
ap=argparse.ArgumentParser();ap.add_argument('--erf',type=Path,required=True);ap.add_argument('--bia',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
OUT=args.output;OUT.mkdir(parents=True,exist_ok=True)
PACKS={
 'ERF_September':{'file':args.erf,'front':list(range(1,3)),'rescinded':list(range(15,21))+list(range(33,44))+list(range(54,57))+list(range(61,65))+list(range(71,75)),'rates':list(range(29,33)),'rules':{'5160-8-05':(3,11),'5160-27-01':(12,14),'5160-27-02':(21,26),'5160-27-03':(27,28),'5160-27-04':(44,53),'5160-27-06':(57,60),'5160-27-08':(65,70),'5160-27-09':(75,81),'5160-27-10':(82,83),'5160-27-11':(84,85),'5160-27-14':(86,88)}},
 'BIA_October':{'file':args.bia,'front':list(range(1,12)),'rescinded':list(range(29,40)),'rates':[],'rules':{'5160-8-05':(12,20),'5160-27-01':(21,23),'5160-27-02':(24,28),'5160-27-04':(40,44),'5160-27-06':(45,47),'5160-27-08':(48,51),'5160-27-09':(52,57),'5160-27-10':(58,59),'5160-27-14':(60,62)}}}
def compact(x):return re.sub(r'\s+','',x).casefold()
audit={'packets':[],'rules':[]};span_ledger=[]
for name,conf in PACKS.items():
 d=fitz.open(conf['file']);seenpages=set(conf['front']+conf['rescinded']+conf['rates']);ruleout=OUT/name;ruleout.mkdir(exist_ok=True)
 allpieces=[]
 for n,(start,end) in conf['rules'].items():
  seenpages.update(range(start,end+1));paras=[];para='';kept=[];removed=[];anomalies=[]
  for i in range(start-1,end):
   lines=[]
   floor=100
   if i==start-1:
    starts=[l['bbox'][1] for b in d[i].get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] if any(s['text'].strip().startswith('(A)') and s['color'] in [0,255] and s['size']>=10 for s in l['spans'])]
    assert starts,(name,n,'missing first clause')
    floor=min(starts)-0.1
   for b in d[i].get_text('dict')['blocks']:
    if 'lines' not in b:continue
    for line in b['lines']:
     parts=[]
     for s in line['spans']:
      text=s['text'];y=s['bbox'][1];reason='retained'
      if not text.strip():reason='whitespace'
      elif y<floor:reason='running-header-or-rule-title'
      elif y>=730:reason='running-footer'
      elif s['color']==13369344:reason='red-deleted'
      elif s['size']<10:reason='small-markup'
      elif s['color'] not in [0,255]:reason='other-color';anomalies.append({'page':i+1,'text':text,'color':s['color'],'size':s['size']})
      span_ledger.append({'packet':name,'rule':n,'pdf_page':i+1,'bbox':[round(v,2) for v in s['bbox']],'font_size':round(s['size'],2),'color':s['color'],'classification':reason,'text':text})
      if reason=='retained':
       kept.append(text)
       if parts and parts[-1][-1:].isalnum() and text[:1].isalnum():parts.append(' ')
       parts.append(text)
      elif reason=='red-deleted':removed.append(text)
     text=re.sub(r'\s+',' ',''.join(parts).replace('\xa0',' ')).strip()
     if text:lines.append((round(line['bbox'][1],1),line['bbox'][0],text))
   lines.sort(key=lambda x:(x[0],x[1]))
   for y,x,text in lines:
    if re.match(r'^\([A-Za-z0-9]+\)',text):
     if para:paras.append(para)
     para=text
    else:para=(para+' '+text).strip()
  if para:paras.append(para)
  body='\n\n'.join(paras)
  # Verify complete retained-span sequence, including every isolated integer.
  assert compact(''.join(kept))==compact(body),(name,n,'sequence preservation')
  assert body.startswith('(A)'),(name,n,'first clause')
  assert not anomalies,(name,n,anomalies)
  numeric=[x.strip() for x in kept if re.fullmatch(r'\d+(?:\.\d+)?',x.strip())]
  text=f'# {name} Proposed Rule {n}\n\n**Status:** Historical proposed source, not effective law.\n**PDF pages:** {start}–{end}\n**Source PDF SHA-256:** `{hashlib.sha256(conf["file"].read_bytes()).hexdigest()}`\n\n## Rule Text\n\n'+body+'\n'
  (ruleout/(n+'.md')).write_text(text)
  allpieces.append(text)
  audit['rules'].append({'packet':name,'rule':n,'pages':[start,end],'retained_spans':len(kept),'deleted_red_spans':len(removed),'retained_numeric_only':numeric,'rule_body_chars':len(body),'rule_body_sha256':hashlib.sha256(body.encode()).hexdigest(),'sequence_preserved':True,'unclassified_substantive_spans':len(anomalies)})
 assert seenpages==set(range(1,len(d)+1)),(name,'page coverage',seenpages)
 audit['packets'].append({'packet':name,'pages':len(d),'sha256':hashlib.sha256(conf['file'].read_bytes()).hexdigest(),'rule_ids':list(conf['rules']),'frontmatter_pages':conf['front'],'rescinded_predecessor_pages':conf['rescinded'],'rate_appendix_pages':conf['rates'],'every_page_classified':True})
 (OUT/(name+'_Clean_Proposed_Text.md')).write_text('\n\n'.join(allpieces))
 # Front matter: keep all substantive lines; exclude only identified footer bands.
 front=[]
 for page in conf['front']:
  lines=[]
  for b in d[page-1].get_text('dict')['blocks']:
   if 'lines' not in b:continue
   for l in b['lines']:
    txt=''.join(s['text'] for s in l['spans']).strip()
    if not txt:continue
    if name=='BIA_October' and l['bbox'][1]>=700:continue
    lines.append(txt)
  front.append('## PDF Page '+str(page)+'\n\n'+'\n'.join(lines))
 (OUT/(name+'_Front_Matter.md')).write_text('# '+name+' Front Matter\n\n'+'\n\n'.join(front)+'\n')
# Extract fee appendix by actual grid-cell boundaries, preserving blank cells.
d=fitz.open(PACKS['ERF_September']['file']);rows=[];tableaudit=[];rawtables=[]
headers=['HCPCS code','Modifier','Description','Printed effective date','Status code','Current maximum payment','Office maximum payment','Home/community maximum payment','Allowable places of service']
notes=[]
for i in range(28,32):
 p=d[i];tabs=p.find_tables().tables;assert len(tabs)==1,(i,len(tabs))
 t=tabs[0];extracted=t.extract();assert len(extracted[0])==9
 for rownum,row in enumerate(extracted[1:],start=1):
  assert len(row)==9
  assert re.fullmatch(r'[A-Z]?\d{4,5}',row[0] or ''),(i,row)
  rows.append(dict(pdf_page=i+1,pdf_table_row=rownum,**{headers[k]:re.sub(r'\s+',' ',v or '').strip() for k,v in enumerate(row)}))
 # Independently compare each nonmerged cell against a clipped text extraction.
 checked=0;issues=[]
 for ri,r in enumerate(t.rows):
  for ci,cell in enumerate(r.cells):
   if cell is None:continue
   expect=extracted[ri][ci] or ''
   rect=fitz.Rect(cell)
   words=[w for w in p.get_text('words') if rect.x0<=((w[0]+w[2])/2)<=rect.x1 and rect.y0<=((w[1]+w[3])/2)<=rect.y1]
   # get_textbox respects source reading order in this grid.
   clip=' '.join(w[4] for w in words)
   if compact(clip)!=compact(expect):issues.append({'row':ri,'col':ci,'cell':expect,'clip':clip})
   checked+=1
 assert not issues,(i,issues[:3])
 tableaudit.append({'pdf_page':i+1,'rows_excluding_header':len(extracted)-1,'columns':9,'cells_independently_checked':checked,'cell_mismatches':len(issues)})
 rawtables.append({'pdf_page':i+1,'bbox':list(t.bbox),'cells':extracted})
 if i==31:
  text=p.get_textbox(fitz.Rect(0,t.bbox[3],p.rect.width,p.rect.height))
  notes.append(text.strip())
s=io.StringIO();w=csv.DictWriter(s,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(OUT/'ERF_September_Fee_Appendix_A.csv').write_text(s.getvalue())
(OUT/'ERF_September_Fee_Appendix_A.cells.json').write_text(json.dumps(rawtables,indent=2))
(OUT/'ERF_September_Fee_Appendix_A_Notes.md').write_text('# September Proposed Appendix A Notes\n\n**Status:** Historical proposed appendix, not confirmed October rates.\n\n'+'\n\n'.join(notes)+'\n')
audit['fee_tables']=tableaudit;audit['fee_rows']=len(rows)
(OUT/'PDF_Parse_Coverage.json').write_text(json.dumps(audit,indent=2)+'\n')
with (OUT/'PDF_Source_Spans.jsonl').open('w') as f:
 for s in span_ledger:f.write(json.dumps(s)+'\n')
print(json.dumps({'packets':audit['packets'],'rule_versions':len(audit['rules']),'fee_rows':len(rows),'fee_tables':tableaudit},indent=2))
