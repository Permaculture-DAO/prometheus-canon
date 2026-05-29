#!/usr/bin/env python3
"""Strict DOCX -> Markdown extractor for Prometheus White Paper.
Preserves paragraphs and tables in document order. Use package version for reproducibility.
"""
import sys, re
from pathlib import Path
from docx import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph

def clean(s):
    return re.sub(r'[ \t]+',' ', (s or '').replace('\u00a0',' ')).strip()

def esc(s):
    return clean(s).replace('|','\\|').replace('\n','<br>')

def iter_blocks(doc):
    for child in doc.element.body.iterchildren():
        if isinstance(child, CT_P): yield Paragraph(child, doc)
        elif isinstance(child, CT_Tbl): yield Table(child, doc)

def table_md(t, i):
    rows=[]; maxc=0
    for r in t.rows:
        cells=[esc(c.text) for c in r.cells]
        rows.append(cells); maxc=max(maxc,len(cells))
    if not rows: return ''
    rows=[r+['']*(maxc-len(r)) for r in rows]
    out=[f'<!-- TABLE {i:03d} START -->','| '+' | '.join(rows[0])+' |','| '+' | '.join(['---']*maxc)+' |']
    out += ['| '+' | '.join(r)+' |' for r in rows[1:]]
    out.append(f'<!-- TABLE {i:03d} END -->')
    return '\n'.join(out)

def main():
    if len(sys.argv)!=3:
        print('usage: extract_wp_markdown_strict.py input.docx output.md', file=sys.stderr); sys.exit(2)
    doc=Document(sys.argv[1])
    out=['---','title: "h•eart•h Prometheus — Regenerative Infrastructure for a Living Economy"','status: "table-complete Markdown derivation"','---','']
    ti=0
    for b in iter_blocks(doc):
        if isinstance(b, Paragraph):
            s=clean(b.text)
            if not s: out.append(''); continue
            if s.startswith('PART '): out.append('\n# '+s)
            elif s.startswith('• '): out.append('- '+s[2:].strip())
            else: out.append(s)
        else:
            ti+=1; out.append('\n'+table_md(b,ti)+'\n')
    Path(sys.argv[2]).write_text('\n'.join(out).rstrip()+'\n', encoding='utf-8', newline='\n')
if __name__=='__main__': main()
