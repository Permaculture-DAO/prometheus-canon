# RTC-OS execution record — 2026-10-08

Status: IMPLEMENTED SYNTHETIC CANDIDATE / GLOBAL HOLD. This is a technical execution record appended to the proposed roadmap, not a Canon amendment or source admission.

## Sources and custody

Issue #19; canon #20 at a9d22fb8da324f371aaa64c795ab3e013d5956b2; source proposal #21 at c5ee7bef26dc0059be99ef3ecbf685ee8abb606c, SHA256 c868662c12b9f0e9c8ee1af938c277042a087adb415f9f70dd6d4480e2c2712f. #21 remains untouched/read-only and PROPOSED. Its upstream pins differ from source-root patch candidates; its access-token proposal conflicts with declined A-002. Neither is imported as authority. Its RTC gate ordinals do not map to the runtime's different G0–G7 meanings.

Signed Canon v1.1.2-genesis verified with public fingerprint D20DFF6CBE331B3A4109DF848C8CB0D48C7F60DA. Good local signature is byte/authentication evidence with configured trust, not independent assurance. No signing, tag replacement, canonical ratification or backup mutation performed.

## Tangible changes and dependency order

| Repository / PR | Candidate work | Dependency / permitted claim |
|---|---|---|
| canon #20 | this ledger, exact exception register, full checkout/worktree inventory | documentary proposed roadmap; not source activation |
| runtime #23 | corrected import at 46c0814; strict RTC typed schema, synthetic TDD, four independent E/P/B/L scales, evidence/claim references, rights map, two Decimal loss ledgers, ultimate bearers, forty UNKNOWN partner checks, qualified gate composition, hashes/replay/golden vectors | stack on runtime #22 controls/PRU, which depends on runtime #21 DDL state fix |
| console #9 | local synthetic dossier viewer, audit SHA validation, Python→JS decimal-string parity, no network/storage/unsafe HTML; display naming | requires reviewed RTC contract, not a new live service |
| bridge #10 | finish workflow/test/comment display naming; unchanged routes/status keys | smoke verified; no public deploy |
| hApp display supplement | display/comment/errors only, no entry/enum/API changes | stack on existing hApp #35; no new conductor or agent identity |
| ops #19 | strict path/hash/count naming gate + hostile tests + scoped allowlists; current runbook labels; SQLite failure-path connection closure and new checksum snapshot | stack on ops #17; old benchmark receipt/old checksum manifest preserved |

Primary checkout branches were preserved (eleven clean at intake). Additional known worktrees were inventoried, including concurrent candidate baselines. Dirty tracked bytecode in ops-systemd-audit was observed and not reset. Old baselines are not silently labelled migrated. See RTC_OS_EXECUTION_INVENTORY_2026-10-08.json.

## Evidence

- Runtime: 316 API tests, all existing source/runtime/contract/S0/S4/S5/S6 guards PASS; bridge Node syntax PASS.
- Console: 15 status-handler tests + 33 other Node tests, release QA and candidate build PASS. Browser exercised local quantified synthetic import; displayed HOLD, NR, all authority flags false. Temporary server closed; no deployment.
- hApp: rustfmt targeted files PASS, 27 integrity tests PASS using existing WSL cache/offline lockfile.
- Bridge: status check and smoke PASS.
- Ops: 7 audit adversarial tests plus 30 resilience tests PASS on WSL/Linux. Storage-only 3 tests PASS on native Windows after closing SQL connections on failure. Full Linux probe uses fcntl and is not advertised as native Windows-compatible.
- Six target trees: zero unallowlisted uppercase display occurrences with explicit, PROPOSED, exact file/path/hash/count exceptions. Legacy registry IDs, immutable sources and dated receipts are not rewritten. Matcher/test literals stay exact; exception JSON Unicode-escapes the legacy literals to prevent self-referential hash exemptions.
- Quantified wire numbers are declared decimal strings, not a scientific calibration or independent pricing result.
- CI and human approvals on final pushed commits are separate evidence; do not infer them from local tests. Later Issue #19 checkpoint records their actual status.

Astra's initial and intermediate internal reviews found real bugs and drove regressions; quota exhausted before final re-review. Sol performs a final internal delta review where available. Neither AI is independent domain assurance or a GitHub required approval.

## Material gates held

1. Competent source owner reconciles PR #21's pins, declined access-token assertion, application sequence and gate taxonomy; no automatic promotion.
2. Governance reviews and admits any new derived source/display version. Existing sealed/historical sources, DOCX corpus, signatures and IDs stay immutable.
3. Exact-head CI/security plus required review/CODEOWNER and repository protections. Protection APIs for private console/ops returned HTTP 403; never interpret that as waived protection. Keep candidates draft when eligibility cannot be established.
4. Real site permissions/baseline/counterfactual, independent science/QA/MRV/review, title/water/legal and lawful capital authority—not synthesized by this code.
5. Operational whole-stack admission, off-host recovery, live monitor's missing HTML security headers, website/WordPress/cloud mirror publication and language coverage. No public service/cache/CRM/payment wording changed.

Source adoption remains unconditional HOLD in this synthetic implementation. E/P/B/L declarations never compensate one another or authorize capital. D/P/H/Q modes never acquire material gate effects here.

## Rollback and change budget

No persisted-schema/API/entry-type migration was introduced. Revert candidate composition/viewer/display commits through normal review; retain old source releases/tags and identifiers. Do not run Phase 8, force-push, admin-bypass, rewrite historical checksums or silently publish.

Use the existing runtime controls/PRU and baseline Ravel arithmetic; no duplicate service. The narrow RTC quantitative request explicitly refuses the broader existing API's unsupported fields. This milestone is sufficient for shadow engineering; it is not a completed territorial capital system.
