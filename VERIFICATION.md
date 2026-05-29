# Verification

This document defines the RC2 verification workflow for the h•eart•h Prometheus canonical release candidate.

## Verification scope

Verification covers:

- SHA-256 integrity of release files;
- UTF-8 encoding without BOM;
- Unix LF line endings;
- absence of CRLF drift;
- Markdown table extraction completeness;
- canonical ontology alignment checks;
- placeholder classification as pre-signing fields.

## Verify the package

```bash
bash scripts/verify_release.sh
```

Expected result:

```text
SHA256 checks passed
format checks passed
canonical alignment checks passed
markdown table completeness checks passed
release verification passed
```

## Signature verification

Detached OpenPGP signatures are intentionally not authoritative until the final signed release.

After final freeze and GPG signing:

```bash
bash scripts/verify_signatures.sh
```

## Self-hash trap rule

The White Paper must not contain its own final hash inside the hashed body. Final hashes belong in external `.sha256`, `SHA256_SUMS.txt` and `RELEASE_MANIFEST.json` files.
