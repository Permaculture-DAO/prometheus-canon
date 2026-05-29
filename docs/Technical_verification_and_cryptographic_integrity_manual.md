# Technical Verification & Cryptographic Integrity Manual

## Purpose

This manual defines how the h•eart•h Prometheus release artifacts are verified, hashed and signed without confusing document meaning, file integrity and legal/institutional authority.

## Integrity layers

1. Text alignment — documents must reflect the current White Paper ontology.
2. Format normalization — text files must be UTF-8 without BOM and Unix LF.
3. Hashing — SHA-256 confirms byte-level integrity after text freeze.
4. Detached signatures — OpenPGP signatures authenticate released bytes after final review.
5. Manifest — `RELEASE_MANIFEST.json` records files, roles, hashes, signing status and boundaries.

## Pre-signing field policy

Any field that depends on final frozen bytes must be marked as `PRE-SIGNING FIELD` until the final freeze. This includes final release timestamp, final WP hash, manifest hash and detached-signature references.

## Functional separation

Cryptographic integrity proves that files have not changed. It does not prove ecological performance, PRU maturity, financial value, legal rights, investor entitlement or token rights. Those require MRV, governance, methodology, legal structuring and admissibility review.
