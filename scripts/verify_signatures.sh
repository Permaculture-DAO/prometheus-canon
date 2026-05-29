#!/usr/bin/env bash
set -euo pipefail
find . -name "*.asc" | sort | while read -r sig; do
  file="${sig%.asc}"
  gpg --verify "$sig" "$file"
done
