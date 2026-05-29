#!/usr/bin/env bash
set -euo pipefail
find . -type f \( -name "*.sha256" -o -name "SHA256_SUMS.txt" -o -name "*.asc" \) -delete
find . -type f ! -path "*/.git/*" | sort | while read -r f; do
  sha256sum "$f" > "$f.sha256"
done
find . -type f ! -name "*.sha256" ! -name "SHA256_SUMS.txt" ! -path "*/.git/*" | sort | while read -r f; do
  sha256sum "$f"
done > SHA256_SUMS.txt
