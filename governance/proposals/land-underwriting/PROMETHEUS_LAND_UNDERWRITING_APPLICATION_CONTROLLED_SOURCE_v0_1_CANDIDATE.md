# PROMETHEUS — Land Readiness & Deterministic Underwriting Boundary
## Controlled application source — v0.1, **PROPOSED / NOT ADOPTED**

**Provisional Source ID:** `PRM-LAND-APP-001@0.1` — *provisional only; not allocated in a ratified registry.*  
**Candidate date:** 2026-10-17  
**Authority class proposed:** `CONTROLLED_APPLICATION_SPECIFICATION`  
**Adoption state:** `PROPOSED_NOT_ADOPTED`  
**Deployment state:** `SHADOW_ENGINEERING_CANDIDATE`  
**Capital authority:** **NONE**  
**Scope:** Deterministic readiness triage and evidence-integrity preflight for land dossiers. **Not land valuation, underwriting approval, investment advice, legal due diligence, insurance underwriting, certification, or release of capital.**

### 1. Status and constitutional boundary

This proposal is subordinate to the signed Canon `PRM-CANON-SIGNED@v1.1.2-genesis`. The architecture and domain-source dependency graph are **subject to source-custodian ratification**. In particular, Source-Root v2 candidate PR #18 is **PROPOSED_NOT_ADOPTED**; its `ACTIVE` status values select candidate design records and do not confer governance authority. An `engineering PASS` is not a scientific, legal, valuation or source-governance PASS.

This source does **not** amend Canon, replace `PRM-ARCH-DET-002`, Aeterna, Ravel, the Civilizational Venture Studio or proposed RTC-OS. Implementation documents and WSL test receipts are evidence of software behavior, not controlling methodology.

### 2. Normative invariants

1. `UNKNOWN != ZERO`; missing, stale, invalid, contradictory and unauthenticated inputs must remain distinguishable.
2. `LOSS_REDUCTION != LOSS_ALLOCATION`; `TRANSFERRED_RISK != ELIMINATED_RISK`. Those analyses remain under Aeterna/Ravel.
3. AI and caller-supplied catalogs are non-authoritative. Hash agreement establishes *consistency* against an input snapshot, not real-world truth, reviewer qualification or signature authentication.
4. `P/H/Q` outputs do not determine state or permissions; all such outputs must traverse a deterministic `D` gate and qualified independent review.
5. Legal title, land-use permissions, water rights, environmental compliance and financial obligations require competent evidence and governing legal instruments. Software cannot grant them.
6. Holochain entry persistence and hashes cannot create factual validity, professional certification, property rights, PRU/RAP admission, TRBK utility, investor rights or capital authority.
7. No hypothetical ecological premium, regenerative uplift, carbon/biodiversity credit revenue, zoning windfall or token appreciation may be silently entered into a financial base case.
8. No automatic land valuation (`land_value=null`) and no derived residual valuation in this candidate. A separate reviewed methodology is required for any valuation work.

### 3. Domain contract

The proposed function `land_readiness_shadow` accepts an explicit site and dossier identifier, an explicit as-of snapshot, bounded exact-schema declarations of gate records and evidence/decision catalogs, and optionally a **development input completeness** declaration. It produces a deterministic, replayable *review-readiness* record. Required domain gates are `rights`, `land_use`, `environment`, `water` and `data`; additional declared gate prerequisites are subject to the same integrity checks.

The scoped identity is `LAND:<site_id>:<dossier_id>`. The proposed data-integrity contract must call the existing `controls.GateRecord` / `controls.evaluate_gates`, not introduce a second authority engine. Validation concerns specification references, decision-snapshot digests, evidence content hashes and typed states, date bounds, revocations, graph prerequisites, and identifier/shape limits. Caller-supplied reference catalogs are never treated as verified solely because they are internally consistent.

The candidate shall disclose `as_of` as caller-declared and `freshness_verified=false`; the 366-day maximum decision interval is a *candidate safety rule*, not proof of freshness. A historical snapshot can be internally eligible for external review without proving current suitability.

### 4. Allowed output states

- **`HOLD`:** any ineligible, missing, rejected, expired, mismatched, unverified-at-the-declared-snapshot or otherwise blocking gate; also an internally declared `FAILED` gate without independently established adverse-decision authority.
- **`GO_FOR_EXTERNAL_REVIEW`:** only all required declared controls are internally consistent. This means *ready for independent review*, **not** approved, rated, investable or certified.

The output MUST always mark `authoritative=false`, `underwriting_approval=false`, `capital_admission=false`, `certification=false`, `creates_rights=false`, `references_status=caller_declared_not_authenticated`, `independent_reviewer_authority_required=true`, and `land_value=null` with `valuation_status=valuation_not_admitted`. It SHALL NOT emit authoritative `NO_GO`, PRU value, RAP liquidity, a credit rating, insurance price, legal status, or a TRBK entitlement.

### 5. Architecture integration: retain existing owners

| Existing system | Owner / role | Boundary for this proposal |
| --- | --- | --- |
| Signed Canon | Constitutional authority | Must not be changed by this application |
| `PRM-ARCH-DET-002` | Global architecture candidate | Architectural dependency; no silent activation |
| Existing `controls` | Deterministic gating | Reuse existing gate evaluator; no parallel gate taxonomy |
| Aeterna | Risk generation vs allocation methodology | Future review dependency; never duplicated here |
| Ravel | Scenario risk/loss analytics | Separate optional downstream analysis; not invoked by adapter |
| PRU/RAP | Analysis/aggregation definitions | No admission or rights may be inferred |
| `prometheus-runtime` | Bounded evaluation candidate | Pure local function, no new public API or persistence |
| `prometheus-happ` PR #31/#33 | Proposed Holochain semantic/control plane | Read-only compatibility review only; REAL path CLOSED |
| RTC-OS candidate | Territorial application coordination | Proposed interface and policy alignment, not adopted authority |

### 6. Determinism and test contract

Fixed exact input bytes and method version must produce reproducible canonical output and input SHA-256, including when the order of logically unordered references changes. Reject ambiguous Unicode/control identifiers and invalid timestamps; fail closed on missing/revoked/mismatched evidence, duplicate IDs, forbidden edges, invalid scopes or expired decisions. Require regression tests for one-site-to-another replay, contradictory gate precedence, orphan evidence, numeric input types, output no-authority flags and non-development behavior.

An internal PASS never authenticates title, water access, market comparables, ecological causal impact or a valuation method. Independent site evidence and qualified review remain prerequisites for decisions affecting external parties.

### 7. Product hypothesis, not financial claim

`Land Readiness & Risk Dossier` is an **asset-light service candidate**: source-indexed readiness, evidence gaps, site constraints, risk-owner questions and an external-review checklist. Paid demand, unit economics, buyer willingness-to-pay and professional service/licensing boundaries are unverified. Evidence Node recurring monitoring or B2B2B infrastructure are optional subsequent hypotheses; land SPV acquisition and investment activity remain separate and on HOLD.

### 8. Required gates before adoption

1. **G1 engineering custody:** exact reviewed files; SHA-256 manifest; fully passing rerun; authorized signed commit; isolated remote branch; draft PR; exact-HEAD CI; maintained review trail.
2. **G2 source custody:** reserve `source_id@version` without collision; verify source predecessor/dependency hashes; resolve PR #18 candidate-vs-adopted precedence; competent source-steward review; proposed registry record; documented dissent and explicit ratification. No `ACTIVE` classification before that act.
3. **G3 Holochain compatibility:** pin exact PR #31/#33 heads; TEST-only conductor reconstruction; verify identity/provenance read interfaces; REAL persistence must remain disabled absent separate admission.
4. **G4 domain evidence:** site title/zoning/water/environment data verified by qualified humans; separate independent valuer and risk methodology where relevant; scientific causal attribution tested and falsifiable.
5. **G5 production/capital:** distinct legal, security, certification, risk-transfer, capital and operational approvals. No promotion by implication from G1–G4.

### 9. Release and supersession discipline

This is an *entirely new provisional application source*, not a replacement version of Aeterna/Ravel or of `PRM-CIV-APP-006`. Its proposed source text must be preserved byte-exact once reviewed; changes create a new version with predecessor hash and supersession note. Never silently rewrite an upstream controlled file or source registry. Any future `ControlledSourceRelease` signer, timestamp or authority status must come from an actual authorized action, not fabricated placeholders.

### 10. Implementation receipt (non-normative evidence)

See `PROMETHEUS_LAND_UW_EXECUTION_HANDOFF_RC2_20261017.md`. Candidate runtime upstream base: `6c74fb75e99da31f9bb6c76574a9ce131cfc608f`. Three engineering files: `land_underwriting.py` (SHA-256 `753c03a7f1435eba247bf696dff5463b78761301c3c2d40210c30d038d59977e`); `test_land_underwriting.py` (`4f28bbb808bd81916e0be73efe30fd0850c1a1ea1312197634d882ed097ce54c`); integration document (`d2897309914b477c1f4efa792147c2e64c22a34147900513473a4699e483e71a`). Full observed test receipt: **281 passed, 160 subtests passed**, one dependency warning, exit 0. The code release remains **UNSIGNED / UNPUBLISHED** as of the handoff. Test counts and file digests are evidence, not a certification or active source authorization.

**END — PROPOSED SOURCE / NO AUTOMATIC ADOPTION**
