#!/usr/bin/env python3
from pathlib import Path
import re, sys
md=Path('canonical/h-earth-prometheus-white-paper.md').read_text(encoding='utf-8')
count=len(re.findall(r'<!-- TABLE \d+ START -->', md))
expected=150
if count != expected:
    print(f'table completeness failed: {count}/{expected}'); sys.exit(1)
print(f'markdown table completeness checks passed: {count}/{expected}')
