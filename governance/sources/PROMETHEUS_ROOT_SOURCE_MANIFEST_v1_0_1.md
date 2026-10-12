# PROMETHEUS Root Source Manifest v1.0.1 — candidate

Release candidate: PROMETHEUS-SOURCE-ROOT-v2.0.1-candidate (2026-10-08).

This is the selected **design candidate**, not a signed/adopted Source-Root release.
Governing canon: signed v1.1.2-genesis, exact tag object e72c753ba7d916cc406b53d0840ca4c45ca345e4,
commit dcafb0c850029629634ee974b4a8126481a4f9fd, Markdown SHA256
f3862005bc4d6e8e4cba0f2a7646e67dff758fcd28c8411046eb5d04875f9540.
Aggregate DOCX variants are presentation/provenance artifacts, not editable authority.

## Selected design graph

- PRM-ARCH-DET-002@2.0: original restored bytes; global design reference only.
- PRM-RISK-AETERNA-001@1.1.1: metadata candidate patch of 1.1.
- PRM-RISK-RAVEL-OP-002@1.1.1: candidate dependency patch to AETERNA 1.1.1.
- PRM-CIV-APP-006@6.2.1: metadata candidate patch of 6.2.

Machine root: PROMETHEUS_ROOT_SOURCE_MANIFEST_v1_0_1.yaml.
Registry: PROMETHEUS_SOURCE_REGISTRY_v1_0_1.yaml. Every record has a stable ID,
mandatory version, exact ID@version key, hash, scope and pinned dependencies.
ACTIVE means selected design only, except the explicit already-signed Canon record.
SUPERSEDED means superseded **in this candidate graph**, not a governance retirement.
Incomplete old historical inventory remains in the original v1.0 registry and cannot
win default resolution. Unknown source state is rejected.

## Boundaries and original history

Original imported source files, v1.0 manifests/registry/lattice/schemas and v2.0
release checksums remain byte-exact. The restoration commit records the original
import corruption; patches have their own paths, versions, hashes and ledger.
Historical v6.1/v6.2 change-log text stays historical. Inherited references and
application decisions are not newly validated or ratified. META/compiler and typed
lattice precedence remain **PROPOSED_NOT_ADOPTED**, below existing signed rules.
No new scientific, legal, actuarial, token, investment or capital claim is admitted.
No canonical definitions are lifted to canonicals before textual freeze.

ComputeProvenance v1.0.1 rejects material-gate effects for **every** mode. A claimed
D_VERIFIED state requires structural receipt hash/reviewer metadata but does not
authenticate those claims. An authority-bearing effect path is not implemented.
ControlledSourceRelease v1.0.1 is a proposed transport schema only; signer/status
fields do not prove a signature, scientific truth or authority. No hApp/DNA change.

## Verify and hand off

Run from repo root:

    python scripts/validate_source_root.py --gpg "C:/Program Files/GnuPG/bin/gpg.exe"
    python -m unittest discover -s tests -p "test_source_root.py"

Linux CI uses an isolated GPG home, imports only the pinned public key and verifies
the signed historical tag. No secret key, new signature or production credential.
SHA256SUMS covers the candidate release manifest; that manifest deliberately does
not include its own hash or the checksum file hash, preventing circular hashing.
Signing/adoption/publication/deploy require steward actions after fresh review.

## Complexity ledger

Net new files justified: three versioned candidate method/application documents;
three schema patches; registry/lattice/root machine + prose patch; release envelope
and change ledger; one public key; one validator/test suite/CI/dependency list.
Immutable originals cannot be overwritten. No new service, API, database, runtime
write path, framework or duplicate PR. Remove/consolidate candidate machinery if
central source governance replaces it; remove unused candidate versions only by
recorded retention procedure, not automatic cleanup.
