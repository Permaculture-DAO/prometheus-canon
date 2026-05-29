#!/usr/bin/env bash
set -euo pipefail
# SHA checks
sha256sum -c SHA256_SUMS.txt
# format checks
python3 scripts/strict_format_audit.py
# canonical semantic checks
bash scripts/assert_canonical_alignment.sh
# table completeness
python3 scripts/table_completeness_check.py
printf 'release verification passed
'
