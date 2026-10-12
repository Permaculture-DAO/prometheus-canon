# CODEX EXECUTION HANDOFF — RTC-OS + Aeterna/Ravel Global Migration

**Source:** User execution request on 2026-10-08.  
**Status:** AUTHORIZED TO IMPLEMENT, PUSH AND MERGE **ONLY AFTER** automated checks, required independent/domain reviews and repository branch protections pass.  
**Tracker:** https://github.com/Permaculture-DAO/prometheus-canon/issues/19  
**Architecture PR:** https://github.com/Permaculture-DAO/prometheus-canon/pull/20  
**Primary application spec:** `governance/applications/CIV-TOPOS-001_TOPOS_Intelligence_Partner_Method_Interoperability_Dossier_v1_0.md` (PR #20 branch).  
**Working branch:** `docs/civ-topos-001-rtc-os-naming`

## 0. Operating contract to Codex (execute, not merely summarize)

You are implementation coordinator for **PROMETHEUS Regenerative Territorial Capital Operating System (RTC-OS)** and the whole-project display-name migration **AETERNA → Aeterna; RAVEL → Ravel**. Treat this as a cross-repo project with separate reviewable PRs, deterministic tests and an auditable deployment ledger. Implement changes where your authenticated repository checkout and available permissions genuinely allow. Do **not** claim access to other repositories, websites, WSL/local archives, Codex cloud agents, secrets, live APIs, insurers, or other operators without verifying access. If no cross-repo tools are available, create a reusable handoff and per-repository checklist, report BLOCKED with exact access requirements, and keep work inside the available checkout.

No destructive rename/rewrite of history. Do not circumvent branch protections, authorship constraints, signatures, legal review, science-review gates, required CI, or CODEOWNERS. User authorizes **eligible routine code merges after every required check passes**; any constitutional/financial/legal release that requires designated human/domain approval is still subject to that approval. No autonomous capital release, insurance binding or token marketing.

## 1. Read controlling sources FIRST

Read current active Root Source Manifest, Source Registry, Authority Lattice, Canon/Full Corpus and existing AGENTS.md and ADRs; follow latest `ACTIVE` references (not merely filenames). Required baselines (version pins must be verified):
- `PRM-ARCH-DET-002@2.0`, PROMETHEUS Deterministic Architecture v2.0;
- `PRM-CIV-APP-006@6.2`, Civilizational Venture Studio;
- Aeterna methodology, **legacy stable machine ID** `PRM-RISK-AETERNA-001@1.1`;
- Ravel operations, **legacy stable machine ID** `PRM-RISK-RAVEL-OP-002@1.1`;
- `PRM-ROOT-SOURCES-001`;
- CIV-TOPOS-001 candidate application document (PR #20).

If a declared file/ref is missing, stale or superseded, record discrepancy before modifications. Use source authority by type: fact, law, constitutional, architecture, method, application, implementation. No new Canon amendment without appropriate constitutional process.

## 2. Target outcome / scope

Build **RTC-OS as application capability of Civilizational Venture Studio**, not a second PROMETHEUS core.

`Territorial Reconnaissance → Site & Rights Profile → Baseline/Counterfactual → Intervention Alternatives → Evidence Spine → MRV/Admissibility → PRU where applicable → Aeterna methods / Ravel loss-generation and risk-allocation ledgers → RAP where applicable → Independent Valuation & Rights → Legal Wrapper → Human Capital Decision → Continuous Stewardship`.

Deliver a minimally working vertical slice using actual deterministic schemas and replayable tests. Respect AI non-authority, `UNKNOWN != ZERO`, `LOSS_REDUCTION != LOSS_ALLOCATION`, `TRANSFERRED_RISK != ELIMINATED_RISK`, immutable provenance, no double counting and multi-jurisdiction legal gates. TOPOS is *only a third-party candidate*, with public descriptions not verified proof or a partnership.

## 3. Repository inventory and owner matrix (Wave 0)

Confirm all accessible active repositories; expected:
- `Permaculture-DAO/prometheus-canon`: registry, ADR, application spec, claims policy;
- `Permaculture-DAO/prometheus-runtime`: schemas, state machines, D/P/H/Q verification, gate engine, two ledgers, auditable replay;
- `Permaculture-DAO/prometheus-happ`: site/evidence provenance and optional hash anchors, no promotion of authority;
- `Permaculture-DAO/prometheus-bridge`: bounded imports/exports and schema translation;
- `Permaculture-DAO/prometheus-console`: territorial views and Aeterna/Ravel display;
- `Permaculture-DAO/prometheus-ops-docs`: deployment, rollback, partner due diligence, DR;
- `Permaculture-DAO/prometheus-governance`: governance approvals and source migration records if applicable;
- `Permaculture-DAO/.github`: CI policies/workflow checks.
Additionally discover any maintained marketing website repository, **actual** deployment repository and local/WSL mirrors. Historical `legacy-*` and all archived signed bundles are provenance, not active edit targets.

For each accessible repo record `remote, default branch, branch protection, HEAD SHA, current CI, source-of-truth status, file count, AETERNA/RAVEL occurrences, human display occurrences, code/API/ID occurrences`. Produce a markdown and JSON inventory and explicit inaccessible list. Do not trust a zero-result remote code-search as proof of zero hits: inspect a full checked-out tree with `rg -n --hidden -S 'AETERNA|RAVEL|Aeterna|Ravel'` or equivalent, excluding only proven vendor/generated dirs.

## 4. Name migration policy (Wave 1)

**Desired public text everywhere ACTIVE:** `Aeterna`, `Ravel`, `Aeterna/Ravel`. Cover UI, manuals, all current readmes, site content, docs, marketing, prompts, copy, operator alerts, titles, search metadata, docs generators and release display names. Scope capitalization exactly, retaining word meaning and grammar.

**Compatibility requirement:** Source IDs `PRM-RISK-AETERNA-001` and `PRM-RISK-RAVEL-OP-002`, filenames/paths referenced by released registries, artifact hashes, case-sensitive imports, Rust symbols, environment keys, CLI flags, endpoints, database discriminators and archival historical documents must not be mechanically renamed. If an active file must be renamed: introduce new versioned file/path and backwards compatible alias, update all references via registry/manifest controlled release, prove lookup compatibility and rollback. Immutable historical proofs must remain byte-identical. In reports, distinguish (a) new canonical display label, (b) stable legacy technical ID, (c) historical immutable spelling.

Create `AETERNA_RAVEL_NAMING_MIGRATION_INVENTORY.json` (historical filename can be legacy identifier only if necessary) or human-readable `Aeterna_Ravel_naming_migration_inventory.json`, path/ref hash snapshots, exclusion register, allowlist for protected all-uppercase references, and a machine test that fails on newly introduced unallowlisted human-facing uppercase names. Acceptance: zero unallowlisted uppercase on active human-facing surfaces, without broken imports/API.

## 5. RTC-OS minimal vertical slice (Wave 2)

Implement domain-focused, versioned and tested objects reusing existing architecture if present:
- `TerritoryProfile`, `SiteProfile`, `StakeholderRightsMap`, `TerritorialReconnaissance`;
- `TerritorialDeterminationDossier` (not a certification), options including no-action, constraints, timestamps, source hashes;
- `EvidenceReference`, `ClaimReference`, `BaselineCounterfactual`, validation-state transitions;
- two distinct `LossGenerationLedger` and `RiskAllocationLedger` records joined by identifiers, preserving `UltimateRiskBearer`;
- `CapitalReadinessGate` with deterministic `HOLD`, `REJECT`, `REVIEW_REQUIRED`, `SHADOW_PASS` outputs; only human/domain authority may perform actual investment approval;
- `ExternalPartnerAssessment` with 40 test IDs from CIV-TOPOS-001 and statuses `OBSERVED | DOCUMENTED | THIRD_PARTY_VERIFIED | ASSUMED | UNKNOWN | INCOMPATIBLE`;
- audit trail with source versions, inputs, hashes, reviewers and replay.

No speculative capitalization of TRBK, ecological premium, carbon credit or unapproved public debt. Treat public retail sovereign/sub-sovereign capital rails as candidate downstream applications with separate legal/issuer gates, not implemented financial products.

Minimum demonstrator: **synthetic fixture** labelled `SYNTHETIC / NON-CAPITAL-FACING` covering valid site decision, missing water rights → HOLD, unsupported ecology outcome → NOT_ADMISSIBLE, unknown insurer recoverability → NR, missing independent review → HOLD. Confirm repeated deterministic replay of identical frozen inputs produces identical result.

## 6. Secure integration and test gates (Wave 3)

- Validate JSON/YAML schema, stable references, no-double-counting, missing-data behavior, PRU/TRBK/legal separation and source authority;
- Typecheck/build Rust, TS, tests in repos as appropriate; lint and docs link check;
- Tests for Unicode/title case vs legacy ID resolution and case-sensitive file systems;
- D/P/H/Q non-authority and deterministic validation; verify any LLM advice cannot create a verified indicator, right, capital approval, coverage or certification;
- Model Ravel shadow state only; assert unknown/NR not silently mapped to zero or safe;
- Reproduce two-ledger identity and Ultimate Risk Bearer under stress and loss transfer;
- Static secret scan, security review, dependency integrity;
- Controlled migration checks for signed source-release SHA256 sidecars (generate a new hash after serialization; NEVER rewrite old release hashes);
- Rollback rehearsal or documented plan for schema/API migrations; staging smoke tests/monitor checks when a staging environment is legitimately available.
CI must pass on the exact commits proposed for merge. If tests or required reviewer approvals are unavailable, report BLOCKED with evidence and leave PR unmerged.

## 7. Multi-repo PRs, pushes and merges (Wave 4)

1. Rebase on verified clean target HEAD or create feature branches under `codex/rtc-os-*` for each repo. Avoid force-pushing protected branches.
2. Commit narrow changes; push each branch; open one PR per repo, linking `prometheus-canon#19`, `prometheus-canon#20`, the baseline and migration inventory.
3. Check GitHub Actions, status checks, branch protection, CODEOWNERS and relevant security/scientific/legal/governance sign-offs.
4. Request appropriate independent review. If Codex review is configured, request `@codex review` in a *separate* review comment after implementation, not in the initial @codex implementation trigger.
5. Fix failures, push and rerun until green. Merge in dependency order: governance/source contracts → runtime schema/tests → hApp/bridge → console → ops/website. Do not release new live capital capabilities.
6. MERGE **only eligible code/document PRs** after all relevant automated and human gates are satisfied and branch protection permits; no admin override. For constitutional authority changes or legal/financial promotions, pause for competent approval and report accurately.
7. Record `repo, branch, PR, commits, checks, reviewers, merge SHA, deployed revision, rollback SHA/path`. Keep a Cross-Repo Completion Matrix updated in issue #19.
8. Verify release and deployment monitoring; reconcile WSL/local PC only when online and authorized. No unverified statement that worldwide mirrors were synchronized.

## 8. Change-budget and partnership constraints

No direct update of immutable Canon or source history. Change documented requirement before implementation; prefer refactoring over duplicate architectures. TOPOS integration cannot assume an agreement, access to proprietary IP, commercial endorsement, accreditation equivalence or independent assurance. The site pilot remains hypothetical absent permissions. Keep a lightweight baseline comparator; simplify/retire expensive functionality if no measurable decision benefit.

## 9. Final Definition of Done

- [ ] Reviewed source authority and complete repo coverage or explicit blocked boundaries;
- [ ] CIV-TOPOS-001 is reviewable with all 40 checks and falsifiability experiment;
- [ ] RTC-OS vertical slice builds, tests, and replays; all HOLD/NR/UNKNOWN conditions tested;
- [ ] Aeterna and Ravel human-facing names present on every active reachable surface, with explicit protected-identifier exception register;
- [ ] No broken API/schema/token/rights mappings, old immutable bundles intact;
- [ ] Each affected repo has branch + commit + pushed PR + successful CI + required approvals;
- [ ] Eligible PRs merged and source manifest/release sidecars reconciled where governance permits;
- [ ] Live deployment only following operational SLO/safety acceptance (never conflate with independent science/capital authority);
- [ ] Final issue #19 comment lists PRs, merge SHAs, no-change repos, blockers, residual risks, and outstanding approvals;
- [ ] No false `DONE` while any material target remains inaccessible/unverified.

## 10. Runbook if cloud agent lacks GitHub API and cross-repo access

Continue local checkout tasks. Use `gh` only if authenticated and permitted; do not solicit secrets in comments. If you can push only via Codex `make_pr`, create the PR for accessible repository and explicitly label other repos as blocked. A GitHub @codex trigger starts a cloud task only when the repository has the connected Codex environment configured. If unavailable, post exact setup requirements. Never fabricate a successful push or merge.

**Execution command:** Implement Wave 0 immediately, then safe Wave 1/2/3, push all eligible branches and merge only after Wave 4 gates. Post each tangible milestone in the tracking PR/issue. Do not stop at planning.
