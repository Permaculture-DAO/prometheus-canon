---
source_id: PRM-RISK-RAVEL-OP-002
source_registry_key: PRM-RISK-RAVEL-OP-002@1.1
source_name: PROMETHEUS RAVEL Operational Risk Intelligence Source
release: v1.1
release_date: 2026-10-07
authority_class: CONTROLLED_OPERATIONAL_METHODOLOGY_SOURCE
canonical: false
subordinate_to_canon: true
global_architecture_dependency: PRM-ARCH-DET-002
primary_method_dependency: PRM-RISK-AETERNA-001@1.1
supersedes:
  - PROMETHEUS-SRC-RAVEL-UNDERWRITING-001
default_status: SHADOW_ANALYTICAL_NON_AUTHORITATIVE
---

# PROMETHEUS — RAVEL OPERATIONAL RISK INTELLIGENCE
## Controlled Operational Source v1.1

**Source ID:** `PRM-RISK-RAVEL-OP-002`  
**Global architecture dependency:** `PRM-ARCH-DET-002`  
**Primary methodological dependency:** `PRM-RISK-AETERNA-001@1.1 — AETERNA Risk Synergy`  
**Supersedes:** the prior `PROMETHEUS-SRC-RAVEL-UNDERWRITING-001` as current operational RAVEL source.  
**Predecessor SHA-256:** `47d2352c01fd947b08fe8b9b8c643cc5ae55deb6f09a8d3f8d9914642e381aa6`  
**Status:** `SHADOW / ANALYTICAL / NON-AUTHORITATIVE`.

# 1. Purpose

AETERNA defines the controlled actuarial, insurance, reinsurance, capital-protection and model-risk methodology.

RAVEL operationalises approved methods into versioned Risk Objects, ledgers, stress tests and decision-support outputs.

RAVEL is therefore **not a competing methodology** and not a separate constitutional layer.

# 2. Core operational chain

**Hazard → Trigger → Exposure → Vulnerability → Direct Loss → Secondary Loss → Frequency/Probability → Severity → Dependence → Recovery → Prevention → Mitigation → Diversification → Absorption → Transfer → Retention → Residual Risk → Unmodelled Risk → Ultimate Risk Bearer.**

# 3. Mandatory two-ledger rule

Maintain:

## Loss Generation Ledger
Where and why loss is generated.

## Risk Allocation Ledger
Who absorbs, finances, transfers or externalises that loss.

`LOSS REDUCTION ≠ LOSS ALLOCATION`.

# 4. Risk Object

```text
risk_id
asset_or_project_id
claim_ids[]
evidence_ids[]
risk_category
hazard
trigger
exposure
vulnerability
direct_loss
secondary_loss
frequency_or_probability
severity
dependence
recovery_time
preventive_controls[]
mitigations[]
diversification_treatment
transfer_ids[]
retained_risk
residual_risk
unmodelled_risk
ultimate_risk_bearers[]
evidence_status
confidence
assumptions[]
sensitivities[]
owner
reviewer
review_cadence
decision_gate
model_version
data_hash
method_hash
```

# 5. Compute modes

RAVEL may consume:

- D outputs from deterministic code;
- P outputs from approved probabilistic models;
- H scenario/hypothesis proposals;
- Q optimisation proposals where admitted.

Every P/H/Q input that can affect a material gate must first pass the `PRM-ARCH-DET-002` deterministic verification boundary.

# 6. Evidence discipline

Every material numerical parameter must be classified and sourced.

Where probability/severity cannot be defended:

`NR — NOT RELIABLY RATEABLE`.

Never infer probability from linguistic confidence.

# 7. Operational outputs

Where justified:

- EL / ES / VaR;
- PD / LGD / EAD;
- Cash-Flow-at-Risk;
- liquidity shortfall;
- covenant breach;
- PPCI;
- recovery time;
- reserves;
- stress loss;
- reverse-stress Failure Frontier;
- RRΔ;
- risk-transfer recoverability;
- Ultimate Risk Bearer Map.

# 8. Authority boundary

RAVEL may analyse and recommend.

RAVEL may not:

- certify;
- approve capital;
- bind insurance;
- create legal rights;
- create objective probability from prose;
- amend gates;
- amend Canon;
- convert transferred loss into eliminated loss.

# 9. Lifecycle

Current state: `SHADOW`.

Admission to `VALIDATED_FOR_DEFINED_USE` requires:

- defined use case;
- benchmark;
- independent model review;
- reproducible calculations;
- documented failure modes;
- accepted Claims Register wording;
- governance approval.

# 10. Final invariant

> **AETERNA defines how risk should be analysed. RAVEL makes that analysis operational. Deterministic verification controls whether an output may influence a decision. Human/legal authority controls whether the decision may be acted upon.**

**END — PRM-RISK-RAVEL-OP-002 v1.1**