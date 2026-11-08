# PROMETHEUS Claims Register data layer · candidate v0.1

> **Status: CANDIDATE — NOT RATIFIED, NOT SIGNED, NOT FROZEN.**
> This directory is a machine-readable staging layer. It does not amend the signed `v1.1.2-genesis` prose Canon and creates no empirical, legal, market, financial, token or governance authority.

## Authority
- Governing signed prose: `v1.1.2-genesis`.
- Signed runtime pointer: `v1.1.3-runtime-proof`.
- Signed source section: White Paper §W, Claims Register C-001…C-012.
- Source Markdown SHA-256: `f3862005bc4d6e8e4cba0f2a7646e67dff758fcd28c8411046eb5d04875f9540`.
- Source detached signature: verified GOOD with fingerprint `D20DFF6CBE331B3A4109DF848C8CB0D48C7F60DA`.

## Design rule
The signed source claim and later governance decisions are separate layers:
1. **source claim** — immutable release-local text/status;
2. **semantic UID mapping** — identity metadata only when the meaning is unchanged;
3. **governance overlay** — later ratified/interim decisions that constrain interpretation without silently rewriting the signed release;
4. **consumer projection** — runtime/hApp/site/deck may consume an admitted snapshot but never create authority.

Release-local labels such as `C-008` are aliases only. Never join claims across lineages by bare C-number.

## Mapping classification
### Mapping-only candidates
These retain the same signed statement in the successor candidate and may be reviewed as source-identity aliases:
- C-001
- C-003
- C-004
- C-006
- C-007
- C-010
- C-011
- C-012

### HOLD — semantic change or unresolved identity
- **C-002:** candidate adds “auditable” and changes disciplined wording.
- **C-005:** candidate splits H5 into H5a/H5b/H5c; one legacy UID must not be rebound.
- **C-008:** signed utility/access-credit claim is constrained by later ARD-001 + TOD-001; requires source-claim + governance-overlay modelling, not direct aliasing.
- **C-009:** candidate tightens “available via a compliant security” into “requires a separate legal instrument / no offer”; this is not mapping-only.

## Governance chronology relevant to C-008
Commit `ca31942a89ab90ed144ce1e4defca289a2c5de90` in `prometheus-governance` records:
- ARD-001: RATIFIED ordinary decision, A-002 out / A-002R drafting-only.
- TOD-001: INTERIM FAIL-SAFE ADOPTION only; full Eternity ratification + counsel remain open.

Byte-for-byte Git-blob verification confirms both detached signatures are GOOD and their hashes match the ratification checksum set. Windows working-tree CRLF conversion must not be used to verify detached signatures.

## Proposed lifecycle
`candidate/` → steward/reviewer decision → freeze/hash/sign → signed release snapshot → downstream projections.

This candidate does **not** create a new `CURRENT_CLAIMS_REGISTRY` pointer. Adding such a pointer is a separate governance/release decision.

## Files
- `claims-register.schema.json` — candidate authority-aware data contract.
- `claims-register.v0.1-candidate.json` — signed-source records + proposed mappings + governance overlays.
- `ADMISSION_RECORD_DRAFT.md` — non-authoritative mapping-only review record.

No merge should occur until the admission record is resolved and the unresolved HOLD rows remain fail-closed.
