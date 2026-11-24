# TERRA-US-APP-001 — RC2 integration delta (candidate)
Status: PROPOSED / TEST_ONLY / HOLD_REAL / HOLD_PRODUCTION. Extends RC1 proposal; no change to signed Canon or active registry.

## WP01 authority reconciliation (partial)
Genesis v1.1.2-genesis is the governing signed line per canon README and runtime lineage document. Internal v7.0.x documentary track remains mapped, not merged. Project sources PRM-ARCH-DET-002, PRM-CIV-APP-006, Aeterna/Ravel and RTC-OS remain scoped design inputs pending reconciliation against admitted release hashes. No active source admission claimed. Runtime native G0-G7/P/T gates are unchanged. Full registry and independent review remain open.

## WP02 and WP03 candidate implementation
Runtime PR #40, branch terra-intelligence-rc1-20261124. Code/test commit 8d5f723558055f5af1a199e8ba7c3701a4b5422b; subsequent documentation commit 23767a003c9bc0ba10ff7376cdf6ecf21b29ae04.
- Property-specific fixture schema; exact synthetic APN, jurisdiction, source/field scope and decimal checks.
- Source inventory (candidate only): 3 TEST sources and 10 candidate sources/tools, all live disabled; real permissions, licences, retention, coverage and freshness UNKNOWN.
- Single normalization core in services/api/app/terra_property_core.py, RC1 CLI delegates.
- Native offline adapter in services/api/app/terra_property.py, not registered in production intake.
- Existing S6 builder/hash/verifier reused with namespaced property batch identity. No fake sensor fields and no real Holochain entry.
- P2.2 Evidence Spine write remains closed: registered claims and place/system context required; no invented claim or DB write.

## Observed WSL receipts
On code commit 8d5f723: RC1 regression 15/15; RC2 native tests 10/10; native validate_contracts, S4, S5, S6 guards PASS. These are local synthetic checks, not independent assurance or deployment. Remote RC2 CI requires separate verification. RC1 remote runtime-s0-ci on 967383f87678fe23edaaefffa2f3e89ed37908ab reported success.

## Remaining
WP01 full source registry and competent admission; WP04 source-specific authorized connector design and tests; WP05 workstream reconciliation; WP06 formal Evidence Spine mapping; WP07 GIS (real path remains HOLD); WP08 Ravel shadow; WP09 read-only UI; WP10 review/CI/release controls. No new spend, live acquisition, property contact, legal or capital authority.
