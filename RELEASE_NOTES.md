# Release Notes — v1.1.0-rc.2-strict

## Status

`v1.1.0-rc.2-strict` is a text-complete and table-complete canonical/runtime synchronization candidate generated from the uploaded White Paper DOCX.

This candidate is not the final signed public release. It is the strict QA candidate preceding final GPG signing.

## Major changes from RC1

- Added table-complete Markdown extraction from the DOCX source of truth.
- Preserved all DOCX tables as Markdown tables with table boundary comments.
- Normalized Markdown heading structure.
- Added repository-wide Markdown synchronization coverage for all current root `.md` files identified in the public repository and legacy canonical materials.
- Added explicit deprecation and migration policy for stale or superseded documents.
- Reclassified unresolved hash/signature/timestamp values as `PRE-SIGNING FIELD` values.
- Regenerated SHA-256 checksums after text freeze candidate generation.
- Deferred real GPG `.asc` signatures until final authorized signing after the WP v5 locked checksum-refresh gate.

## Notable ontology alignment

This release aligns repository documentation to the institutional White Paper architecture:

OHE → MRV → verified indicators → PRU → PRU maturity classification → RAP → legal/institutional wrapper → capital allocation → reinvestment → expanded regeneration.

## Signing boundary

Final signatures must be generated only from the release maintainer environment after review.
