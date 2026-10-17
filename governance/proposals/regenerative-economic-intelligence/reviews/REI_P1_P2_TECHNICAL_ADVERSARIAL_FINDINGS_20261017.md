# REI P1/P2 — Adversarial readiness review (non-credentialed technical assessment)
**As-of:** 2026-10-17  
**Result:** ENGINEERING REVIEW PERFORMED / QUALIFIED EXTERNAL REVIEW STILL PENDING / SOURCE RATIFICATION HOLD

## Evidence observed

- Canon REI source PR #26, head `b360cd74b9e003b8f043bba30a737f1f72eec05a`, remained OPEN/DRAFT, with no GitHub reviews at inspection. Commit verification `unsigned`.
- Runtime P1/P2 PR #33, head `c3ec5148c171443d9a25726a515521682f4ea893`, remained OPEN/DRAFT, with no GitHub reviews at inspection. Commit verification `unsigned`.
- Source Root candidate PR #18 and land source proposal PR #25 remained OPEN/DRAFT.
- Local isolated engineering replay from past work: P1 nine synthetic unit tests PASS on original PR #33. The independent negative-case suite on review branch includes five additional tests and a narrow input-hardening patch; tests PASS.
- Human actuarial/MRV/legal/source-custodian signatures: **NOT OBSERVED**. This technical red-team is NOT those independent approvals.

## P0 governance observations

**P0-GOV-01 — Unratified dependencies.** A registry in PR #18 describes ACTIVE within a CANDIDATE_DESIGN_ONLY scope. It is not actual source admission. Maintain the signed Canon's precedence. The REI source ID remains provisional; verify collision against the actual adopted registry and secure a separate signed release. *Disposition: HOLD ratification*.

**P0-GOV-02 — Unsigned PR head.** Exact GitHub head commits for source PR #26 and runtime PR #33 were reported `verified=false, reason=unsigned`. A success CI does not sign or authenticate. Do not modify/rewrite historical commits; create any future signed source/adoption release as a separate authorised act. *Disposition: HOLD ratification/merge*.

**P0-GOV-03 — No formal independent review.** GitHub review lists on REI source PR #26 and P1/P2 runtime PR #33 were empty. Credentialed reviewer competence and conflicts not recorded. *Disposition: HOLD signoff*.

## P1 red-team findings

**P1-RISK-01 — Case-variant missing bearer identifier, mitigated in review PR.** The original prototype's reserved-bearer rejection compared only uppercase `UNKNOWN`, `UNALLOCATED`, `UNALLOCATED_RESIDUAL`. A lowercased equivalent could have passed the placeholder test when the ledger arithmetic balances. Review branch changes sentinel matching to case-insensitive and adds tests, without claiming true bearer identity.

**P1-RISK-02 — Claimant-provided imaginary bearer still passes syntax.** A synthetic bearer name `fictional-company` can yield `GO_FOR_EXTERNAL_REVIEW` if internally balanced. This is not an approval bug in the bounded contract because outputs explicitly mark `ultimate_bearers_legally_verified=false` and `evidence_authenticity=NOT_ESTABLISHED`; nevertheless it is a blocking gap for any real-risk, professional or source-method ratification. Requires authenticated bearer directory, enforceable contract, group linkage and provenance.

**P1-RISK-03 — Not a RAVEL-authorised object.** This adapter does not bind its declared loss generation and allocation to an authenticated REI `risk_ledger_links` or versioned RAVEL risk object and method. No counterparty solvency, policy performance, basis risk, correlated tails or actuarial calibration. Equations are illustrative arithmetic, not loss-reduction proof. No API/REAL integration authorised.

**P1-RISK-04 — Standards reference stale.** Runtime P1 proposal cited ASOP 47 without stating it was superseded/repealed. Effective May 1, 2025, ASOP 58 Enterprise Risk Management replaced ASOP 46/47 (U.S. ASB). Add an append-only erratum; do not misstate it as globally applicable law. See:
https://www.actuarialstandardsboard.org/asops/enterprise-risk-management-58/
https://www.actuarialstandardsboard.org/asops/asop-nos-46-47-risk-evaluation-risk-treatment-repealed/

## P2 independent-method check

**P2-MRV-01 — Scientific protocol drafted, empirical audit not performed.** Proposed source contains useful field-level sampling, calibration, uncertainty, baseline/counterfactual, missingness, leakage, privacy and potential replication. It is currently prose; no authenticated sensor records, lab methods, pre-registered study, control parcel, audit of compliance or reproducible causal result.

**P2-MRV-02 — Sector precision.** Soil-carbon stock analysis needs soil depth, bulk density, coarse fragment content, and comparable soil mass; a change in concentration alone does not prove a change in stocks. The IPCC 2019 Refinement Volume 4 chapter 2 gives relevant inventory-method considerations. A site pilot needs a qualified agronomy method fit for local use; inventory guidelines do not automatically validate a project credit claim.
https://www.ipcc-nggip.iges.or.jp/public/2019rf/vol4.html

**P2-MRV-03 — Correct method scope and effective date.** ISO 14064-2:2019 remains current for GHG project quantification, monitoring and reporting. GHG Protocol Land Sector and Removals Standard v1.1 lists effective date January 1, 2027. Select the applicable method by date and claim; do not assert compliance based on a reference link or protocol draft.
https://www.iso.org/standard/66454.html
https://ghgprotocol.org/land-sector-and-removals-standard

**P2-MRV-04 — Pre-registration / independent replicability.** Require signed pre-intervention preregistration, explicit effect estimand, comparison design, sample-size feasibility, geospatial/privacy policy, adverse outcomes, archival raw-data custodian, domain reviewer acceptance and independent replication plan. Do not report the pilot as verified causal regeneration without them.

## Decisions and evidence requirements

- GO: standalone synthetic engineering R&D and reviewer solicitation, under D/P/H/Q non-authoritative SHADOW.
- HOLD: source ratification, production, qualified risk methods, verified risk transfer, ecological causal statements, capital/insurance/token permissions.
- Required independent signoffs: competent Canon source steward, qualified P1 actuarial/risk methodology professional, qualified P2 ecological/MRV/causal methods professional, and legal/privacy/tenancy reviewers where real sites are affected.
- Signing, credentials, conflicts and exact reviewed commits must be recorded in a separate governed decision record. This document must not be represented as an independently signed actuarial or scientific report.

**No signed adoption decision or effective date is generated by this file.**
