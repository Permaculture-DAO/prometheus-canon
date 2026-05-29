# Runbook — Prometheus v1.1 RC2 Strict

## Objective

Move from verified text-complete release candidate to final canonical release without semantic drift, stale hashes or invalid signatures.

## Stage 1 — Validate source of truth

Confirm that the packaged DOCX is the uploaded White Paper source of truth and that the Markdown derivative includes all text and all DOCX tables.

```bash
bash scripts/verify_release.sh
```

## Stage 2 — Review Markdown

Review:

- `canonical/h-earth-prometheus-white-paper.md`
- `docs/RC2_STRICT_FULL_TEXT_FORMAT_AUDIT.md`
- `docs/REPOSITORY_MD_SYNC_MATRIX.md`
- `repo_overlays/hearth-prometheus-whitepaper/DEPRECATION_AND_MIGRATION_POLICY.md`

## Stage 3 — Apply overlay to repository

```bash
git checkout main
git pull --ff-only
git checkout -b release/v1.1.0-rc.2-strict
cp -R repo_overlays/hearth-prometheus-whitepaper/* /path/to/hearth-prometheus-whitepaper/
```

## Stage 4 — Refresh and verify in repository

```bash
bash scripts/refresh_checksums_no_sign.sh
bash scripts/verify_release.sh
```

## Stage 5 — Final freeze and sign

Only after human review:

```bash
bash scripts/sign_release_gpg.sh
bash scripts/verify_signatures.sh
git add .
git commit -m "docs: publish Prometheus v1.1 RC2 strict canonical alignment"
git tag -s v1.1.0-rc.2 -m "h•eart•h Prometheus v1.1.0-rc.2 strict canonical release candidate"
```
