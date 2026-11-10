# REI application controlled-source proposal — review and adoption gates
Date: 2026-10-17

This custody receipt is **not a ratification, signature, timestamp attestation, or certificate**.

## Candidate contents

- `PROMETHEUS_REI_CONTROLLED_APPLICATION_SOURCE_v0_1_CANDIDATE.md`: proposed application source `PRM-REI-APP-001@0.1`.
- `PRM_REI_SOURCE_REGISTRY_DELTA_v0_1_PROPOSED.yaml`: source hash and upstream candidate pinning.
- This review checklist.

SHA-256 for immutable source content: `d1f2fa0a4773c6c48bfdfa9329216ac2b42ace50210f7b196185d14bcad50d8d` (computed by independent checkout read after first source commit, not a proof of legal identity).

## Required independent source-custodian review

- [ ] Confirm competent steward identity and legal authority for source adoption.
- [ ] Check provisional `PRM-REI-APP-001@0.1` for collision in **actual adopted registry**, not only the draft design graph.
- [ ] Recompute source SHA from remote exact HEAD and verify copy and scope.
- [ ] Verify signed Canon identity, SHA and Source Root candidate dependency status without assuming PR #18 is ratified.
- [ ] Confirm Aeterna/Ravel/Civilizational hashes and declared authority precedence, identify any upstream discrepancies.
- [ ] Review source for conflict with land source PR #25 and RTC-OS PROPOSED/SHADOW boundaries.
- [ ] Independently review technical SHADOW PR #32, #31 and #26 before promotion.
- [ ] Seek competent legal, ecological MRV, property, professional risk method, and impacted-party review for real deployments.
- [ ] Record dissent, conflict of interest, rejection criteria, adoption decision, signer's provenance and qualified scope.
- [ ] Only after adoption: create a separately versioned source registry and immutable signed release; no modification to the historical proposed text.

## Decision fields for an authorised future act

`source_id_reserved`: PENDING  
`source_status`: PROPOSED_NOT_ADOPTED  
`steward_decision`: PENDING  
`reviewer_signatures`: NONE_OBSERVED  
`applicable_effective_date`: UNASSIGNED  
`production_readiness`: HOLD  
`capital/advice/insurance/tokens`: HOLD

## Rollback / non-invasive handling

Closing the Draft PR and deleting its isolated branch (after preserving an audit record) removes this proposal without affecting `main`, the signed Canon, old application sources, RAVEL/Aeterna, Holochain DNA or production data. No source supersession is claimed.
