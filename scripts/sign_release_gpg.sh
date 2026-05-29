#!/usr/bin/env bash
set -euo pipefail
find . -type f ! -name "*.asc" ! -path "*/.git/*" | sort | while read -r f; do
  gpg --armor --detach-sign "$f"
done
