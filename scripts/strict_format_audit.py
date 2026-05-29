#!/usr/bin/env python3
from pathlib import Path
import sys
exts={'.md','.txt','.json','.sh','.py','.conf','.service','.example'}
errors=[]
for p in Path('.').rglob('*'):
    if p.is_file() and p.suffix in exts and '.git' not in p.parts:
        b=p.read_bytes()
        if b.startswith(b'\xef\xbb\xbf'): errors.append(f'BOM: {p}')
        if b'\r\n' in b or b'\r' in b: errors.append(f'CRLF/CR: {p}')
        try: b.decode('utf-8')
        except UnicodeDecodeError: errors.append(f'not UTF-8: {p}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('format checks passed')
