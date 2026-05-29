#!/usr/bin/env bash
set -euo pipefail
TARGET="canonical/h-earth-prometheus-white-paper.md"
for term in "One Human Ecosystem" "Prometheus Regenerative Unit" "Regenerative Asset Pool" "verification-first" "HoloFuel" "TRBK" "Valueflows" "agent-centric"; do
  grep -q "$term" "$TARGET" || { echo "missing canonical term: $term"; exit 1; }
done
if grep -RIn "the thirteen foundational articles" . --include="*.md"; then
  echo "stale foundational-articles language found"; exit 1
fi
printf 'canonical alignment checks passed
'
