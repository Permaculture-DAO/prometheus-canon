# P2.2 Claims Register semantic UID admission record · DRAFT

> **STATUS: DRAFT — NO AUTHORITY / NO SIGNATURE / NOT RATIFIED.**

## Proposed decision class
**Ordinary metadata / source-identity mapping only.**

Rationale: the proposed admitted subset does not change signed claim text, evidence status, investor-facing boundary or disciplined wording. It assigns stable semantic identifiers only where the successor candidate carries the **same statement**.

This record does **not** admit any semantic successor, token/legal change, H5 split, empirical claim, value, market status or runtime authority.

## Signed authority in force
- Current signed Canon: `v1.1.2-genesis`.
- Source Markdown SHA-256: `f3862005bc4d6e8e4cba0f2a7646e67dff758fcd28c8411046eb5d04875f9540`.
- Detached signature: GOOD, authorized fingerprint `D20DFF6CBE331B3A4109DF848C8CB0D48C7F60DA`.

## Proposed mapping-only admission set
- C-001 → `prometheus.architecture.candidate_regenerative_infrastructure`
- C-003 → `prometheus.pru.analytical_interface_no_rights`
- C-004 → `prometheus.rap.portfolio_readability_not_market_admission`
- C-006 → `prometheus.hypothesis.r1_risk_compression`
- C-007 → `prometheus.hypothesis.t1_time_positive_value`
- C-010 → `prometheus.ai.assistive_non_authoritative`
- C-011 → `prometheus.digital_provenance.traceability_not_truth`
- C-012 → `prometheus.frontier_research.zero_weight_until_admitted`

## Explicit HOLD set
- C-002 — successor wording expands “deployable” → “deployable and auditable”.
- C-005 — successor splits H5 into H5a/H5b/H5c; no aggregate UID rebinding.
- C-008 — signed claim + ratified ARD-001 + interim TOD-001 require source-claim/governance-overlay treatment.
- C-009 — successor changes from “available via compliant security” to separate legal instrument/no-offer framing.

## Proposed topology
1. Candidate work lives under `prometheus-canon/candidate/claims-register-v0.1/`.
2. If admitted, the source/mapping registry remains owned by `prometheus-canon`.
3. A frozen signed snapshot is distributed through `prometheus-canonical-releases`.
4. Runtime/hApp/site/deck consume versioned projections and cannot modify authority.
5. Any future `CURRENT_CLAIMS_REGISTRY` pointer requires a separate explicit governance/release decision.

## Decision
- [ ] **ADMIT THE 8 SOURCE-IDENTITY MAPPINGS ONLY**
- [ ] RETURN FOR REVISION
- [ ] REJECT

## Conditions if admitted
- C-002/C-005/C-008/C-009 remain HOLD.
- No signed v1.1.2 wording is changed.
- No new public claim is created.
- No legal, empirical, market or financial status is implied.
- Candidate files are frozen, hashed and signed before any signed-registry distribution.
- Downstream consumers pin the admitted registry version/hash.
- Rollback = revert consumer pointer to prior admitted snapshot; signed historical source is never rewritten.

## Freeze fields
Populate only after the human decision:
- Decision date/time:
- Authorized role / authority basis:
- Candidate commit SHA:
- Registry SHA-256:
- Schema SHA-256:
- Reviewer:
- Conditions:
- Detached signature:
- Effective state:

The AI may prepare and test this record but cannot tick the decision, sign it, or create authority.
