# Prometheus v1.1 Genesis Reinstall — Final Clean-Room Status

## Status

Genesis Reinstall Clean-Room Phase completed.

Current phase:

- pre-final-freeze;
- pre-final-canonical-release;
- pre-GPG-signing;
- pre-GitHub-release-publication.

This document records the completion of the repository clean-room reinstall, White Paper source hierarchy clarification, internal White Paper hash/signature audit, legacy quarantine, staging checksum regeneration, local forensic backup, and audit-ready repository topology.

## White Paper source of truth

The active White Paper source hierarchy is:

- `canonical/h-earth-prometheus-white-paper.docx`
- `canonical/h-earth-prometheus-white-paper.md`

The DOCX remains the controlling editorial source until final textual freeze.

The Markdown file is the active generated, reviewable, text-oriented derivation.

No other Markdown copy in the `canonical/` directory is an active White Paper source.

Historical RC2 derivations, source exports, package artifacts, and audit copies belong in `provenance/` or quarantine and do not supersede the active canonical files.

## White Paper internal hash/signature audit

The internal White Paper hash/signature audit confirmed:

- the canonical DOCX and founder mirror DOCX are identical;
- the canonical Markdown and founder mirror Markdown are identical;
- the DOCX does not contain its own SHA-256 hash;
- the DOCX does not contain the Markdown SHA-256 hash;
- the Markdown does not contain the DOCX SHA-256 hash;
- the Markdown does not contain its own SHA-256 hash;
- raw DOCX XML contains no literal SHA-256 values;
- active Markdown contains no literal SHA-256 values.

Hash, checksum, signature, GPG, release manifest, and canonical release references inside the White Paper are methodological, procedural, placeholder, or future-release language.

They are not final embedded release hashes.

## Founder mirror

The founder publication mirror is:

- `Uwohali/hearth-prometheus-whitepaper`

Its active White Paper mirror hierarchy is:

- `canonical/h-earth-prometheus-white-paper.docx`
- `canonical/h-earth-prometheus-white-paper.md`

The controlling canonical source repository remains:

- `Permaculture-DAO/prometheus-canon`

## Active Genesis repositories

The active Genesis repository topology is:

- `Permaculture-DAO/prometheus-canon`
- `Uwohali/hearth-prometheus-whitepaper`
- `Permaculture-DAO/.github`
- `Permaculture-DAO/prometheus-happ`
- `Permaculture-DAO/prometheus-bridge`
- `Permaculture-DAO/prometheus-console`
- `Permaculture-DAO/prometheus-ops-docs`
- `Permaculture-DAO/prometheus-evaluation-stack`
- `Permaculture-DAO/prometheus-pilot-handoff-pack`
- `Permaculture-DAO/prometheus-mock-backend`

## Legacy repositories

Pre-v1.1 repositories were archived as legacy repositories.

Legacy repositories preserve historical development evidence.

Legacy repositories do not govern the Prometheus v1.1 Genesis line.

Legacy material may re-enter an active Genesis repository only through explicit review, documented rationale, stale-term cleanup, semantic conflict resolution, and new commit into the relevant active repository.

## Completed controls

The following controls were completed:

- active White Paper hierarchy clarified;
- duplicate active `source.md` derivations removed from `canonical/`;
- historical derivations moved to `provenance/rc2/`;
- copied checksum reference in the founder mirror marked as not verifiable in-place;
- active Markdown SHA-256 literals removed;
- internal DOCX and Markdown self-hash audit completed;
- raw DOCX XML SHA-256 literal audit completed;
- staging checksum registers regenerated;
- active repositories verified with clean working trees;
- anti-Frankenstein audit completed;
- CRLF audit completed;
- legacy remotes verified;
- legacy local repositories moved into local quarantine;
- local forensic audit scripts and reports moved into local quarantine;
- full local `repos/` backup generated;
- full backup SHA-256 verification completed.

## Backup status

A full local backup was generated under:

`../_BACKUPS_GENESIS_REINSTALL_2026_05_30/`

Backup package:

`GENESIS_REINSTALL_V1_1_REPOS_FULL_BACKUP_2026_05_30.tar.gz`

Backup verification:

`sha256sum -c` returned `OK`.

## Non-final status

This status document does not constitute a final canonical release.

Final canonical release requires:

1. final textual freeze;
2. final semantic QA;
3. final checksum regeneration;
4. final release manifest update;
5. authorized GPG signing;
6. detached signature generation;
7. GitHub release publication;
8. release notes aligned with the final release package.

## Operational rule

Canonical meaning lives in `Permaculture-DAO/prometheus-canon`.

Founder publication lives in `Uwohali/hearth-prometheus-whitepaper`.

Runtime behavior lives in `Permaculture-DAO/prometheus-happ`.

Bridge/API behavior lives in `Permaculture-DAO/prometheus-bridge`.

Frontend behavior lives in `Permaculture-DAO/prometheus-console`.

Operations discipline lives in `Permaculture-DAO/prometheus-ops-docs`.

Evaluation discipline lives in `Permaculture-DAO/prometheus-evaluation-stack`.

Pilot handoff discipline lives in `Permaculture-DAO/prometheus-pilot-handoff-pack`.

Mock behavioral specification lives in `Permaculture-DAO/prometheus-mock-backend`.

Legacy history remains outside the active path unless formally reintroduced.
