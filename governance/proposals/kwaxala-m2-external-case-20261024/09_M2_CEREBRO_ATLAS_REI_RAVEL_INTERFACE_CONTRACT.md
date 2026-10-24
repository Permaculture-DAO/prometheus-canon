---
project: PROMETHEUS
record_scope: EXTERNAL_CASE_RESEARCH_CANDIDATE
case_id: PRM-EXT-CASE-KWAXALA-001@0.2-CANDIDATE
supersedes_candidate: PRM-EXT-CASE-KWAXALA-001@0.1
created: 2026-10-24
status: M2_RESEARCH_PRECLEARANCE_NOT_ADOPTED
canonical_authority: NONE
scientific_certification: NONE
financial_authority: NONE
real_runtime_write: PROHIBITED
---
# M2 — Nonduplicative integration contract / data exchange design v0.2

This is a **SHADOW, read-only, design-only** contract; it does not create a real API endpoint or protected Canon. It can be referenced from CEREBRO PR #28, REI PR #26/#27, Geospatial Bridge PR #11, Placenta–Climax PR #30 **only after owners separately approve**.

## Minimal typed context
- `case_id`: fixed provisional ID `PRM-EXT-CASE-KWAXALA-001@0.2-CANDIDATE`;
- `claim_id`: stable per-source claim, not proof of truth;
- `source_uri` / `retrieved_at` / `source_original_sha256` optional `null` where original bytes not held;
- `authority_class`: OFFICIAL / STAKEHOLDER_ASSERTED / PUBLISHER_CASE / PROMETHEUS_DRAFT / UNKNOWN;
- `evidence_status`: OBSERVED_OFFICIAL / ASSERTED_ONLY / UNVERIFIED / NOT_APPLICABLE;
- `site_id` and `polygon_revision` only from competent Atlas geo-workflow; no coordinates guessed;
- `legal_right_id`: linked legal document with jurisdiction and scope; never derived from carbon record;
- `carbon_project_registry_id` and `credit_serial_range` only from actual registry; unknown => null;
- `observation_id`: MRV Evidence Spine from original verified method/instrument, not language-model reconstruction;
- `cashflow_id`: REI from independently received cleared bank records and executed contractual priority; unknown => null;
- `risk_case_id` and `ultimate_bearer_id`: Aeterna/Ravel separate loss-generation vs bearer, explicit unknown;
- `consent_receipt_id`: confidential community authority and data licence; absence blocks disclosure.

## Ownership / event chain
`CEREBRO.(case_source+claim)` --reference--> `Atlas.(polygon+rights_overlay)` --reference--> `EvidenceSpine.(measurement/protocol/registry)` --reference--> `REI.(contract+cash)` --reference--> `Ravel.(scenario+bearer)`.

CEREBRO may cite references but **cannot allocate legal rights**. Atlas cannot turn maps into deeds. Evidence Spine cannot mint an offset by containing a tree measurement. REI cannot book an unrealized ecological gain as cash. Ravel cannot guarantee or transfer risk via model score. None can promote a source to Canon, activate REAL writes or mint tokens.

## Nonoverlap acceptance tests
1. Same case/source ID resolves one original factual record, not 5 duplicated owners.
2. Site polygon metadata can distinguish 7,865ha protected area vs larger expansion vision.
3. Rights lookups return `UNKNOWN`, not `NONE`/`OWNED`, when ABA/title not provided.
4. Carbon issuance returns `UNKNOWN`/null when serial absent; it does not calculate synthetic units from hectares.
5. Finance reflects paid bank receipts, not `return_target=5%` as actual history.
6. Risk output always includes correlated loss, contractual bearer and `UNKNOWN` fallback.
7. Deny public exposure of sensitive Indigenous/data-rights information without competent consent.
8. Signing or authorizing a real API remains a distinct future governance action.
