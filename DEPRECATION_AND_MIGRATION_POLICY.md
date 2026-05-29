# Deprecation and Migration Policy

## Purpose

This policy prevents stale Prometheus documents from silently competing with the v1.1 White Paper source of truth.

## Source of truth

For this release line, the uploaded `h•eart•h_Prometheus_White_Paper.docx` is the source of truth. The package contains a copy at:

```text
canonical/h-earth-prometheus-white-paper.docx
```

The Markdown derivative is:

```text
canonical/h-earth-prometheus-white-paper.md
```

## Current repository root `.md` files covered by RC2

- `CAL-1.0_Syntropic_rider_license.md` — updated / retained.
- `CONTRIBUTING.md` — updated.
- `README.md` — updated.
- `RELEASE_NOTES.md` — updated.
- `REPRODUCIBLE_RELEASE.md` — updated.
- `Runbook.md` — updated.
- `Syntropic_Sovereignty_Header.md` — updated / retained.
- `Technical_verification_&_cryptographic_integrity_manual.md` — updated.
- `VERIFICATION.md` — updated.
- `h•eart•h_Prometheus_White_Paper.md` — replaced by table-complete Markdown derivative.
- `h•eart•h_intelligence_Manifesto.md` — updated / retained.

## Deprecated legacy materials

The following legacy materials may be preserved only as historical references unless fully migrated:

- `CANONICAL_DOCUMENTS.md`
- `PROMETHEUS_CANON_12_PAGES.md`
- `Prometheus — Executive Summary & Investment Thesis.md`
- `HAPP_INTEGRATION_NOTES.md`
- `Root_Of_Trust.md`
- old `.asc` signatures generated before the final RC2 freeze
- old `.sha256` files generated from pre-RC2 content

## Rule

Any file not updated, explicitly retained or explicitly deprecated must not be treated as release-critical.
