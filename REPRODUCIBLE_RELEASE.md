# Reproducible Release

This release candidate is designed to be reproducible from the uploaded DOCX source of truth.

## Inputs

- Source DOCX: `canonical/h-earth-prometheus-white-paper.docx`
- Extraction script: `scripts/extract_wp_markdown_strict.py`
- Normalization policy: UTF-8 without BOM, Unix LF, Markdown tables, normalized headings.

## Rebuild Markdown

```bash
python3 scripts/extract_wp_markdown_strict.py canonical/h-earth-prometheus-white-paper.docx canonical/h-earth-prometheus-white-paper.md
```

## Refresh checksums

```bash
bash scripts/refresh_checksums_no_sign.sh
```

## Verify

```bash
bash scripts/verify_release.sh
```

## Final signing

Only after WP v5 locked checksum-refresh QA has passed:

```bash
bash scripts/sign_release_gpg.sh
bash scripts/verify_signatures.sh
```
