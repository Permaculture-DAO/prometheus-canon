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

For discrete scenarios (s):

[
EL=\sum_s p_sL_s
]

Quantile/Expected Shortfall SHALL use probability-weighted loss outcomes and declare the confidence level.

PPCI SHALL be defined by an explicit impairment threshold (\theta), horizon (T), initial capital (C_0) and recovery/terminal-value convention:

[
PPCI_{T,\theta}=P(PV(Recoveries+TerminalValue)<(1-\theta)C_0)
]

No default value of (\theta) is canonically universal.

## 4. Regenerative Risk Delta

For a metric (M):

[
RR\Delta_M=1-\frac{M(regenerative)}{M(baseline)}
]

where the baseline is matched and the metric definitions are identical.

Rules:
- undefined if baseline metric <= 0;
- reported with evidence status and uncertainty;
- never converted into VRRC automatically.

## 5. Risk-transfer effectiveness

For a declared retained-risk metric (M):

[
RTE_M=1-\frac{M(after\ transfer)}{M(before\ transfer)}
]

RTE is receiver/cedent-specific. Aggregate system loss is separately reconciled.

## 6. Ultimate-risk-bearer concentration

Let (q_g) be the non-negative share of declared tail-risk contribution assigned to economic group (g):

[
URBC=\sum_g q_g^2
]

v0.1 MAY use scenario tail-loss shares as a transparent diagnostic proxy. Euler/Shapley allocation is deferred until portfolio methodology is validated.

## 7. Conservation invariant

For each scenario:

[
|\sum_b L_b-(L_{system}^{mitigated}+Friction)| \le \epsilon
]

where (epsilon) is a declared numerical tolerance.

Failure is a **model-integrity error**, not a tolerable business variance.

## 8. State vector

[
R_t=(EL,ES_{95},ES_{99},PPCI,RecoveryTime,RR\Delta,RTE,URBC,Confidence)
]

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
