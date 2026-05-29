# Contributing to h•eart•h Prometheus

This repository is a canonical documentation and release-integrity repository. Contributions must preserve the v1.1 ontology and the verification-first discipline defined by the current White Paper.

## Contribution boundary

Contributors may propose improvements to documentation, methodology notes, scripts, reproducibility workflows, formatting, spelling, clarity, repository alignment and runtime handoff documents.

Contributors may not redefine the core ontology without canonical review:

- OHE is the minimum deployable regenerative infrastructure unit.
- MRV and provenance generate reviewable evidence.
- PRU is the value-analysis interface, not land ownership and not token ownership.
- RAP is the portfolio aggregation layer.
- TRBK is governance, coordination, access or participation, subject to legal boundaries.
- HoloFuel is an operational infrastructure layer.
- Future securities, notes, fund interests, revenue rights or tokenized instruments require legal structuring.

## Evidence discipline

All claims about regenerative performance must identify their status as claim, observation, verified indicator or admissible value. Aspirational language must not be promoted into financial or institutional language without evidence, confidence scoring and review.

## File-format discipline

- UTF-8 without BOM.
- Unix LF line endings.
- Markdown headings normalized with `#`, `##`, `###`.
- No CRLF drift.
- No stale signatures after text changes.
- No final `.asc` signatures until text freeze is complete.

## Pull-request rule

A pull request touching canonical files should include:

1. reason for change;
2. affected files;
3. confirmation that no PRU/TRBK/HoloFuel/legal-rights boundary was altered accidentally;
4. `bash scripts/verify_release.sh` output after checksum regeneration, where applicable.
