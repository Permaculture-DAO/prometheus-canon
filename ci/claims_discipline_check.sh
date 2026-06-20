#!/usr/bin/env bash
# claims_discipline_check.sh — anti-overclaiming linter (Phase 6 CI gate, draft).
#
# Canon rule (master prompt STYLE + Claims Register): capital/market-facing copy
# must use diligence language, not sales language. This scans markdown / html / js
# for high-precision forbidden phrases that should never appear unqualified, and
# warns on softer terms that require a claim-status nearby.
#
# Usage: claims_discipline_check.sh <path> [<path> ...]
# Exit:  1 if any FAIL-tier phrase is found; 0 otherwise (WARN tier never fails).
#
# A line is exempt from a FAIL if it also contains an explicit negation/firewall
# marker (the canon legitimately *prohibits* these terms in its firewall lists).
set -uo pipefail

# FAIL: phrases that are overclaiming in essentially any context.
FAIL_TERMS=(
  "risk-free" "risk free" "no risk" "100% safe" "fully safe"
  "guaranteed return" "guaranteed returns" "guaranteed profit" "guaranteed yield"
  "passive income" "get rich" "price will rise" "price is guaranteed"
  "will appreciate" "guaranteed appreciation" "investable asset class"
)
# Exemption markers: if present on the same line, the term is in a disciplinary /
# negation / firewall context (the canon legitimately *prohibits* these phrases).
# Heuristic: the canon's own uses are always paired with negation/qualification.
EXEMPT_RE='prohibit|forbid|never|\bnot\b|\bno\b|cannot|must not|may not|shall not|disallow|candidate|claim.?status|register status|conditional|impl(y|ies|ied)|without|rather than|instead|false|myth|misconception|disclaim|not yet|→|->'

# WARN: legitimate sometimes (e.g. the Jacobi use-rule), but flagged for review.
WARN_TERMS=( "revolutionary" "proven" "guaranteed" "validated" "best-in-class" )

paths=("$@"); [ ${#paths[@]} -eq 0 ] && { echo "usage: $0 <path>..."; exit 2; }

fail=0; warn=0
scan() {
  local term="$1" tier="$2"
  # case-insensitive, line-numbered, only md/html/js
  while IFS= read -r hit; do
    if [ "$tier" = FAIL ]; then
      # skip exempt lines (firewall/prohibition context)
      echo "$hit" | grep -qiE "$EXEMPT_RE" && continue
      echo "FAIL  $term :: $hit"; fail=$((fail+1))
    else
      echo "WARN  $term :: $hit"; warn=$((warn+1))
    fi
  done < <(grep -rinE --include='*.md' --include='*.html' --include='*.js' --exclude-dir='_superseded_rc2_strict' --exclude-dir='node_modules' -- "$term" "${paths[@]}" 2>/dev/null)
}

echo "=== claims-discipline check ==="
for t in "${FAIL_TERMS[@]}"; do scan "$t" FAIL; done
for t in "${WARN_TERMS[@]}"; do scan "$t" WARN; done

echo "--- summary: $fail FAIL, $warn WARN ---"
[ "$fail" -gt 0 ] && { echo "CLAIMS_DISCIPLINE=FAILED"; exit 1; }
echo "CLAIMS_DISCIPLINE=OK"; exit 0
