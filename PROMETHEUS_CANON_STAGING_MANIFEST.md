# Prometheus v1.1 — Canon Staging Manifest

## Status

This repository is being prepared as the clean canonical staging repository for the Prometheus v1.1 Genesis Institutional Canonical Line.

This is not yet the final signed canonical release.

## Repository role

Future GitHub repository:

Permaculture-DAO/prometheus-canon

Role:

Primary canonical source repository for the Prometheus v1.1 Genesis Institutional Canonical Line.

This repository contains the canonical documentation, source-of-truth White Paper, verification procedures, release discipline, governance boundary, and signing workflow for the Prometheus ecosystem.

## Source package

The initial staging material was imported from:

PROMETHEUS_V1_1_CANONICAL_RUNTIME_SYNC_PACK_RC2_STRICT_2026_05_29

The RC2 package passed:

- format checks;
- canonical alignment checks;
- Markdown table completeness checks;
- release verification checks.

The RC2 verification output reported:

- format checks passed;
- canonical alignment checks passed;
- markdown table completeness checks passed: 150/150;
- release verification passed.

## Source of truth

The source of truth for this repository is the updated h•eart•h Prometheus White Paper used for the v1.1 alignment process.

The canonical White Paper files staged here are:

- canonical/h-earth-prometheus-white-paper.docx
- canonical/h-earth-prometheus-white-paper.md
- canonical/h-earth-prometheus-white-paper.source.md

## Imported canonical and governance files

Root-level staged files include:

- README.md
- CONTRIBUTING.md
- RELEASE_NOTES.md
- REPRODUCIBLE_RELEASE.md
- VERIFICATION.md
- DEPRECATION_AND_MIGRATION_POLICY.md
- NO_GPG_SIGNATURES_YET.md

## Imported constitutional files

Constitutional staged files include:

- constitutional/CAL-1.0_Syntropic_rider_license.md
- constitutional/Syntropic_Sovereignty_Header.md
- constitutional/h•eart•h_intelligence_Manifesto.md

## Imported documentation files

Documentation staged files include:

- docs/00_CANONICAL_ALIGNMENT_AUDIT.md
- docs/02_CANONICAL_RELEASE_PLAN.md
- docs/03_DEPLOY_RUNTIME_RUNBOOK.md
- docs/04_GITHUB_PUSH_PLAN.md
- docs/RC2_STRICT_FULL_TEXT_FORMAT_AUDIT.md
- docs/REPOSITORY_MD_SYNC_MATRIX.md
- docs/Runbook.md
- docs/Technical_verification_and_cryptographic_integrity_manual.md

## Imported scripts

Script files staged here include:

- scripts/assert_canonical_alignment.sh
- scripts/extract_wp_markdown_strict.py
- scripts/refresh_checksums_no_sign.sh
- scripts/sign_release_gpg.sh
- scripts/strict_format_audit.py
- scripts/table_completeness_check.py
- scripts/verify_release.sh
- scripts/verify_signatures.sh

## Excluded from import

The following RC2 package files were intentionally not imported into this clean canonical repository at this stage:

- all RC2 `.sha256` files;
- all detached `.asc` signatures, if any;
- runtime artifacts under artifacts/;
- bridge service config under config/;
- repository overlays for runtime repositories not belonging to prometheus-canon.

## Hash and signature boundary

Any hash from the RC2 package is treated as release-candidate package integrity evidence only.

No RC2 `.sha256` file is treated as a final canonical checksum for this Genesis repository.

No GPG signature exists yet for this repository.

Final checksums and detached GPG signatures must be generated only after:

1. final text review;
2. Markdown completeness confirmation;
3. repository-wide Markdown alignment;
4. explicit update or deprecation of stale documents;
5. textual freeze;
6. checksum regeneration;
7. local GPG signing with the authorized release key;
8. release manifest update;
9. GitHub release publication.

## Legacy boundary

Pre-v1.1 repositories, releases, drafts, hashes, signatures, generated packs, and runtime artifacts are legacy development artifacts.

They are not part of this active canonical path unless explicitly reintroduced through the v1.1 signed canonical release process.

## Operational rule

This repository defines canonical meaning.

Runtime repositories implement bounded pilot behavior.

Operational repositories define execution discipline.

Founder mirror repositories publish or mirror canonical content but do not supersede the canonical source repository.

No runtime code, dashboard, README, API response, token interface, or operational script may silently redefine Prometheus constitutional meaning.
