# REI P1/P2 — Separate Claude Code read-only adversarial review receipt
**Date:** 2026-10-17  
**Review class:** AI cross-review for defect discovery; **NOT** independent qualified actuarial, scientific or source governance approval.

A separate Claude Code CLI session read and analyzed the runtime branch at
`6c409ecf615b3a10799af3d6d359cc7f82cb301a`, with tool access limited
to Read/Grep/Glob. Claude explicitly refused to call this an independent
professional signoff, disclosed that it had not executed tests, and asked
for real reviewers. Technical test results were obtained separately in WSL
and GitHub CI, not inferred from the Claude session.

### Findings and dispositions

1. **Outdated ASOP 47 citation (DOCUMENTATION P1):** source documentation cited the repealed U.S. standard without identifying successor ASOP 58, effective May 1, 2025. Corrected on runtime red-team branch in an explicit subsequent commit; initial author documents remain preserved on original PR #33.
2. **Risk bearer input ambiguity (METHOD P0 for real-world adoption):** lower/uppercase UNKNOWN aliases were patched and tested. NFKC/fullwidth lookalikes, mixed scripts, 'N/A', 'TBD', UNKNOWN_BEARER, aliases for economic groups and fictitious counterparty IDs are still NOT authenticated. No technique that merely matches string aliases can independently certify identity. Future reviewed schema should use source-authenticated opaque IDs and legal/economic group mapping; remains HOLD.
3. **Transfer provenance and semantics (METHOD P1):** matched round trips or zero nominal transfers can mathematically balance; that is not evidence of a legal transfer, its economic effect, or payment. No actual treaty/policy, counterparty solvency, probability or basis risk calibration is run. Preserve declared-only GO_FOR_EXTERNAL_REVIEW and external approval HOLD.
4. **Caller time basis (METHOD P1):** assessment `as_of` may be historic/future if internally valid; no real-time clock or third-party timestamp attestation. P1 output does not grant `freshness_verified`; future authenticated admission needs external valid-time evidence and expiry checks. Historical forensic review can intentionally use historical as_of.
5. **Reproducibility (ENGINEERING):** `"75"` and `"75.000000"` compare numerically but hash differently as declared byte strings; this is expected exact-declaration hashing, not semantic numeric equivalence. Scope must be documented.
6. **Regression discovery (ENGINEERING P2):** P1 old command selected only `test_rei_ravel_ledger_shadow.py`, not `test_rei_ravel_adversarial_review.py`. Review branch docs corrected discovery to `test_rei_ravel_*.py`, without editing original draft commit.
7. **MRV scientific design (METHOD P1):** equivalent soil mass was not explicitly required for comparable soil carbon stocks, though concentration and bulk density/depth were listed. Review branch added equivalent soil mass and source links to IPCC 2019; source is a design protocol only, not field data.
8. **MRV standards mapping (METHOD P1):** review branch now links ISO 14064-2:2019 and GHG Protocol Land Sector and Removals Standard; GHG Protocol lists effective date January 1, 2027. Their applicability remains claim-specific, independent of the existence of this prototype.
9. **Missing independent credentials/signatures (GOVERNANCE P0):** zero formal GitHub reviews on the relevant source and P1/P2 PRs when inspected; no actual independent professional signoff, source-steward signature or adopted lattice update was established.

### Governance consequence

A completed AI cross-review and passing CI are distinct from independent qualified actuarial, ecological/MRV, land/title, technical-security and source custodian reviews. No source adoption, legal advice, insured risk claim, carbon claim, valuation, capital release or production admission can follow automatically.

**Decision: HOLD RATIFICATION / GO FOR QUALIFIED REVIEW RECRUITMENT.**
