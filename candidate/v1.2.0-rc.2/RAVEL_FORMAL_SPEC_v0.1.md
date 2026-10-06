# PROMETHEUS RAVEL Formal Specification v0.1

**Status:** candidate methodology / shadow-underwriting only  
**Authority:** subordinate to signed canon and the current successor candidate  
**Runtime rule:** evaluation, not certification

## 1. Scope

The reference implementation SHALL provide deterministic functions for:

1. scenario loss statistics;
2. capital-loss waterfall allocation;
3. contractual risk-transfer application;
4. ultimate-risk-bearer aggregation by economic group;
5. RRΔ comparison against a matched baseline;
6. RTE and URBC diagnostics;
7. brake signal preparation.

It SHALL NOT autonomously approve credit, price insurance, create rights, alter PRU/RAP status or trigger legal consequences.

## 2. Data contracts

### Risk scenario

Required:
- `scenario_id`
- `probability` in [0,1]
- `gross_loss` >= 0
- `mitigated_loss` >= 0
- `horizon`
- `model_version`
- `evidence_refs[]`

The implementation SHALL reject `mitigated_loss > gross_loss` unless an explicit signed adjustment rationale exists in a later admitted schema.

### Capital layer

- `bearer_id`
- `economic_group_id`
- `layer_type`
- `attachment`
- `limit`
- `priority`

### Protection contract

- `provider_bearer_id`
- `receiver_bearer_id`
- `attachment`
- `limit`
- `effectiveness` in [0,1]
- `basis_factor` in [0,1]
- `counterparty_factor` in [0,1]
- `legal_factor` in [0,1]

No face amount is treated as fully effective without the declared factors.

## 3. Statistical functions

For discrete scenarios s:

EL = Σ_s p_s × L_s *(Formula class: diagnostic — subordinate to the single controlling PRU expression in Section T.)*

Quantile/Expected Shortfall SHALL use probability-weighted loss outcomes and declare the confidence level.

PPCI SHALL be defined by an explicit impairment threshold θ, horizon T, initial capital C_0 and recovery/terminal-value convention:

PPCI_{T,θ} = P( PV(Recoveries + TerminalValue) < (1 − θ) × C_0 ) *(Formula class: diagnostic — subordinate to the single controlling PRU expression in Section T.)*

No default value of θ is canonically universal.

## 4. Regenerative Risk Delta

For a metric M:

RRΔ_M = 1 − M(regenerative) / M(baseline) *(Formula class: diagnostic — subordinate to the single controlling PRU expression in Section T.)*

where the baseline is matched and the metric definitions are identical.

Rules:
- undefined if baseline metric <= 0;
- reported with evidence status and uncertainty;
- never converted into VRRC automatically.

## 5. Risk-transfer effectiveness

For a declared retained-risk metric M:

RTE_M = 1 − M(after transfer) / M(before transfer) *(Formula class: diagnostic — subordinate to the single controlling PRU expression in Section T.)*

RTE is receiver/cedent-specific. Aggregate system loss is separately reconciled.

## 6. Ultimate-risk-bearer concentration

Let q_g be the non-negative share of declared tail-risk contribution assigned to economic group g:

URBC = Σ_g q_g² *(Formula class: diagnostic — subordinate to the single controlling PRU expression in Section T.)*

v0.1 MAY use scenario tail-loss shares as a transparent diagnostic proxy. Euler/Shapley allocation is deferred until portfolio methodology is validated.

## 7. Conservation invariant

For each scenario:

| Σ_b L_b − (L_system_mitigated + Friction) | ≤ ε *(Formula class: controlling for model integrity — a conservation test, not a value expression.)*

where ε is a declared numerical tolerance.

Failure is a **model-integrity error**, not a tolerable business variance.

## 8. State vector

R_t = (EL, ES_95, ES_99, PPCI, RecoveryTime, RRΔ, RTE, URBC, Confidence) *(Formula class: diagnostic — subordinate to the single controlling PRU expression in Section T.)*

A scalar index MAY be derived for internal triage only. It SHALL NOT be presented as a regulated rating.

## 9. Missing data and uncertainty

Missing parameters SHALL NOT receive optimistic defaults. The implementation SHALL either:
- reject evaluation; or
- use a conservative declared fallback and surface it in `assumptions[]`.

No missing evidence may silently increase RRΔ, RTE or confidence.

## 10. Holochain boundary

Holochain records:
- model/version identifiers;
- evidence references/hashes;
- risk-assessment summaries;
- ultimate-bearer records;
- brake signals;
- review decisions.

Heavy stochastic computation remains off-chain. Holochain provenance does not certify correctness of the model output.

## 11. API boundary

Public bridge:
- GET only;
- may expose sanitized shadow-assessment summaries;
- never exposes secrets, write/admin functions, autonomous decisions or unadmitted pricing.

## 12. Acceptance tests

Minimum:
- expected-loss arithmetic;
- ES weighting;
- waterfall priority;
- conservation invariant;
- transfer effectiveness bounded [0,1];
- economic-group aggregation;
- RRΔ undefined on invalid baseline;
- VRRC always zero/not-admitted in v0.1;
- brake output labelled review-required, never autonomous.

## 13. Candidate gate, evidence and Risk Record method (2026-10-06)

Status: ordinary methodological PROPOSAL, not Eternity amendment, ratification,
independent assurance or production admission. Prepared by Codex under the
steward's temporary assignment of Claude's lane. Signed v1.1.2-genesis and the
authority hierarchy remain unchanged. Architecture intake is context, not authority.

### Gate vocabulary and decision boundary

UNSPECIFIED: no versioned specification; SPECIFIED: defined use/prerequisites and
acceptance test identified; READY_FOR_TEST: references prepared for evaluation;
PASSED: an explicitly recorded scoped decision asserts the test passed;
FAILED: recorded test failure; SUSPENDED: prior pass withheld for review;
EXPIRED: the stated validity interval has ended. None means financial admission.

Candidate edges: UNSPECIFIED -> SPECIFIED -> READY_FOR_TEST -> PASSED/FAILED;
PASSED -> SUSPENDED/EXPIRED; FAILED/SUSPENDED/EXPIRED -> READY_FOR_TEST for a new
evaluation. Direct reactivation or skipped stages is prohibited. A new decision
supersedes but never deletes history. Identity checks, decision custody and
reviewer qualifications belong to the defined-use policy, not an input boolean.

Evaluate against explicit timezone-aware as_of, specification reference,
decision reference, evidence-content hashes, prerequisite UIDs and expires_at.
as_of >= expires_at means expired; a future-issued decision is unusable.
Every material prerequisite must be passed, in scope and unexpired. Missing,
invalid, suspended or expired upstream references block downstream use; cycles,
duplicate UIDs and unknown dependencies are invalid input. Traffic-light labels
are not equivalent to these states. A deterministic shadow evaluator reports
candidate eligibility only; it does not authenticate a decision, promote a claim,
establish causal truth or issue legal/financial permission.

### Evidence lifecycle

RAW -> IDENTIFIED -> PROVENANCE_BOUND -> QA_QC_CHECKED -> REVIEWABLE ->
VERIFIED_INDICATOR_CANDIDATE -> ADMISSIBLE or REJECTED. Rejection may occur from
any nonterminal stage with a reason. Each advance requires scoped proof
references; ADMISSIBLE additionally requires a decision reference. No skipped
steps or terminal reactivation. Corrected evidence has a new identity with a
supersession reference; originals, adverse findings and dissent remain retained.
Proof references are not proof authentication. PRU/RAVEL/RAP/legal eligibility
are independent defined-use gate evaluations, never inherited evidence states.
UNKNOWN remains distinct from observed zero and from rejection.

### Minimal Risk Record envelope

A synthetic shadow Risk Record identifies risk_uid, subject_uid, hazard,
exposure, vulnerability, financial_state, model_version, evidence_refs,
ultimate_bearers, assumptions and missing_data_statement. It distinguishes
loss generation/reduction from loss allocation and identifies ultimate bearers
without asserting contract enforceability. Quantitative metrics reference the
existing RAVEL model, not a newly invented formula or rating.
Mode remains shadow_underwriting; authority is evaluation_not_certification;
VRRC=0/not_admitted, and underwriting approval/capital admission are false.
Absent source/calibration/decision data are explicit; intake fields cannot
create validity or completeness. No new claim_uid or AAA/BBB rating introduced.

### Implementation, custody and falsification

The first runtime increment is internal, pure and candidate-only; no automatic
production workflow, governance action, source promotion or new authority layer.
Derive machine-readable rules from this proposal, reference its source/commit and
test every permitted and forbidden edge, expiry, hash mutation, unknown/cyclic
dependencies, revoked review references and deterministic reordering.
Independent assurance and the steward's release/signing gates remain open.
