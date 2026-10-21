---
title: "PROMETHEUS — Deterministic MRF / Zome Validation / Oracle Attestation / Edge-Mesh Source"
source_id: "PRM-SRC-MRF-ZOME-EDGE-001"
version: "0.1.0-candidate"
date: "2026-10-19"
status: "CONTROLLED TECHNICAL & SCIENTIFIC SOURCE CANDIDATE — GOVERNANCE REVIEW REQUIRED"
authority: "Subordinate to signed PROMETHEUS Canon, Eternity-level invariants, ratified governance, and currently admitted architecture sources"
admissibility: "DESIGN_SPECIFICATION / SHADOW_ONLY / SYNTHETIC_ONLY"
canonical_amendment: false
production_authority: false
runtime_write_path_change: false
financial_or_ecological_certification: false
owner_role: "PROMETHEUS Architecture Council / Steward approval pending"
targets:
  - "prometheus-happ"
  - "prometheus-runtime"
  - "prometheus-bridge"
  - "prometheus-ops-docs"
  - "prometheus-console"
---

# PROMETHEUS — Deterministic MRF, Holochain Validation, Oracle Attestation & Ecological Integrity
## Controlled Source Candidate v0.1 — Verification-First / No Silent Canon Amendment

> **Disposition as of 2026-10-19:** GO to bounded *design and synthetic laboratory testing*. NO-GO for REAL persistence, ecological certification, DHT authority expansion, PRU/RAP admission, TRBK issuance, capital action, or production deployment. This file is **not** a signed canonical release.

## 0. Scope, evidence and authority

This source proposes a versioned, frozen **multi-output decision forest** (MRF = Multivariate Random Forest, *not* Markov Random Field) whose numerical inference may be reconstructed in pure Rust and, after compatibility tests, executed in Holochain integrity-zome WASM validation. The same evidence may be used by non-authoritative MRV analysis, oracle-attestation assessment and edge gateways. The deployment must follow the Canon rather than redefine it.

Verified repository observations (2026-10-19):
- \`Permaculture-DAO/prometheus-canon/README.md\`: controlling signed Genesis release is \`v1.1.2-genesis\`; later candidate files do not alter signed Canon.
- \`Permaculture-DAO/prometheus-happ/README.md\`: signed \`v1.1.3-runtime-proof\` is a bounded **synthetic** MQTT-to-Holochain proof only; persistence-gate candidate is not equivalent to that release; conductor sweettests are distinct from CI.
- \`prometheus-happ/zome_integrity/Cargo.toml\` on \`main\`: \`hdk = 0.6.1\`, \`hdi = 0.7.1\`, \`serde = 1.0\` (pins must be reconfirmed at implementation).
- \`prometheus-happ/zome_integrity/src/entry_types.rs\` on \`main\`: integrity \`MrvEvidenceEntry::validate_entry\` returns \`REAL_DATA_PERSISTENCE_GATE_CLOSED\` for \`REAL\` even with a well-formed calibration hash; \`TEST\` evidence must be TEST-namespaced. No synthetic result lifts this gate.
- \`prometheus-canon\` main history (2026-10-12): RAVEL/Aeterna naming update was adopted; source-root v2 was expressly **not** adopted. Do not treat candidate source roots or release terminology as ratified.
- User-provided \`Integrare i Multivariate Random Forest.txt\` is an **architectural hypothesis** and not experimental proof or operative authorization.
- User-provided \`PROMETHEUS_DETERMINISTIC_ARCHITECTURE_v1_0_DEFINITIVE.md\` and \`PROMETHEUS_ARCHITECTURE_META_PROMPT_v1_0.md\` are controlled architecture design sources subordinate to Canon; "definitive" in a filename does not confer signed Canon authority.

Authoritative technical reading (version-sensitive; revalidate when coding):
- Holochain: https://developer.holochain.org/build/validation/ and https://developer.holochain.org/build/validate-callback/ — deterministic validation, resolvable dependencies and \`UnresolvedDependencies\`.
- Holochain: https://developer.holochain.org/build/zomes/ — integrity/coordinator separation and restricted WASM-compatible dependencies.
- Reticulum: https://reticulum.network/manual/ — heterogeneous low-bandwidth transport; no implied Holochain conductor or scientific validation on radio nodes.

### Claim correction register
| ID | Input/source assertion | Disposition | Why |
|---|---|---|---|
| C-MRF-01 | Frozen MRF can be used for identical inferences everywhere | CONDITIONAL | Requires pinned model, ABI, numeric semantics, canonical bytes, runtime and golden tests |
| C-MRF-02 | MRF alone makes single-metric gaming impossible | REJECT AS UNIVERSAL CLAIM | Input manipulation, confounding, missingness, OOD, data selection and model misspecification remain |
| C-MRF-03 | Matching DHT inferences prove ecological truth | REJECT | They can prove conformity to encoded rules only; physical origin and scientific validity require other evidence |
| C-MRF-04 | Distributed peer agreement eliminates oracle dependence | REJECT | Independent physical attestations may remain necessary; DHT validation is not global BFT consensus |
| C-MRF-05 | All edge/LoRa nodes can run WASM/Holochain | REJECT | Sensor, gateway, Holochain host and audit node are materially different hardware classes |
| C-MRF-06 | MRF has negligible resource cost | UNVALIDATED | Footprint depends on trees, nodes, serialization and platform; measure before claims |
| C-MRF-07 | Deterministic agents are equivalent to LLM ensembles | REJECT | Bounded algorithms may be deterministic; LLM proposals remain non-authoritative |

## 1. Canon lock and semantic firewall

Unbreakable spine:
Living System → Intervention → Observation → Evidence → Provenance/Integrity → Verified Indicator → Admissibility → PRU Analytics → Maturity → RAP Aggregation → Compliant Legal Wrapper → Capital.

Cross-cutting: governance, cybersecurity, audit, MRV, AI assistive layer, and RAVEL/Aeterna risk plane. RAVEL is **SHADOW/ANALYTICAL/NON-AUTHORITATIVE** for new underwriting uses until independently admitted. Lowest unresolved material gate controls any downstream claim.

\`UNKNOWN != ZERO\`; \`MODELED != OBSERVED\`; \`SIGNED != PHYSICALLY_TRUE\`; \`QUORUM != SCIENTIFIC_CONSENSUS\`; \`CORRELATION != CAUSATION\`; \`LOSS_REDUCTION != LOSS_ALLOCATION\`; \`RISK_TRANSFER != RISK_ELIMINATION\`.

Forbidden automatic transitions: MRF output → "verified regeneration", MRF output → PRU value, oracle quorum → certification, DHT valid entry → legal right, RAP analysis → investment security, model score → TRBK issuance, AI recommendation → capital deployment. These need independent gates and, where applicable, competent human authority.

## 2. Formal model contract

Let \`X = (x_0,...,x_{p-1})\` be a typed, canonically encoded **input feature vector** and \`Y = f_(theta)(X)\` an \`m\`-dimensional model output. The frozen forest contains \`T\` immutable rooted trees. A split node selects left if \`x[feature] < threshold\`; otherwise right. A leaf contains exactly \`m\` signed-integer outputs in **declared model units**, not automatically physical outcome measurements.

For a baseline equal-weight forest:
\`Y_j = trunc_toward_zero( (sum_{t=0}^{T-1} leaf_(t,j)) / T )\`.
Accumulation uses \`i128\`; values and result must be range-checked before conversion to \`i64\`. No floating-point is required in the initial deterministic validation path. Other aggregation modes require new model/protocol versions and approval.

Determinism means: same canonical bytes, validated \`model_hash\`, numeric version, feature schema, integrity code, and permitted dependencies ⇒ same integer output and same **model-conformity** decision. It does **not** mean climate, ecology or uncertainty are deterministic.

**Candidate bounds, not ratified limits:** \`1<=features<=64\`, \`1<=outputs<=16\`, \`1<=trees<=32\`, \`1<=nodes_per_tree<=1024\`, \`depth<=32\`, fixed maximum input/receipt payloads specified by tests. Admission requires CPU/fuel/RAM benchmarks before selecting actual bounds.

### Frozen representation \`PMRF-BIN-v1\` — design candidate
Canonical byte grammar, big-endian throughout:
- magic bytes: ASCII \`PMRF\` followed by zero byte;
- \`u16 format_version=1\`;
- \`u16 feature_count\`, \`u16 output_count\`, \`u16 tree_count\`;
- per tree: \`u16 node_count\` followed by indexed node records (root index = 0);
- tag \`0\` split: \`u16 feature_index\`, \`i64 threshold\`, \`u16 left_index\`, \`u16 right_index\`;
- tag \`1\` leaf: exactly \`output_count × i64\` leaf values.

Constraints: child indices strictly greater than the current index; tree must be acyclic, entirely reachable from root, have no unused nodes, and be bounded in depth; all features declared; no trailing bytes, duplicates, ambiguous encodings or unknown tags. A frozen artifact hash is \`SHA-256\` over exactly these bytes with a pinned digest/encoding contract; do not accept text-level hash of an unpinned JSON serialization as a substitute.

A trained scientific MRF may require more sophisticated splitting/aggregation than this candidate kernel. In that case preserve the distinction between **scientific model specification** and **the simpler inference interpreter**, or reject parity until proven; never silently change model semantics to fit WASM.

## 3. Typed schema contracts (candidate; version all changes)

\`ModelManifestV1\`: \`model_id, format_version, model_hash, feature_schema_hash, output_schema_hash, training_dataset_hash, training_code_commit, method_version, numeric_contract, tree_count, bounds, validation_report_hash, governance_state, approved_by[], effective_scope, supersedes_hash?\`.

\`ObservationBundleV1\`: \`observation_id, subject_id, site_id, evidence_class(TEST|REAL), captured_at, method_id, method_hash, feature_schema_hash, feature_values_i64[], missingness_bitmap, calibration_hash?, provenance_ids[], raw_evidence_hash, source_identity, source_signature?\`.

\`OracleAttestationV1\`: \`attestation_id, observation_id, raw_evidence_hash, method_hash, signer_agent_id, operator_id, device_id, independence_group_id, calibration_evidence_ref?, signature_scheme, signature_bytes, signed_payload_hash, revocation_epoch, attest_state\`.

\`InferenceReceiptV1\`: \`receipt_id, observation_id, model_hash, feature_schema_hash, canonical_input_hash, output_values_i64[], inference_contract_version, result_hash, producer_id, created_at_source, evidence_class, model_conformity_state\`.

\`EcologicalClaimV1\`: \`claim_id, observation_refs[], inference_receipts[], independent_attestations[], mr_v_review_refs[], confidence_method, limitations[], state, permitted_wording, maturity_gate_refs[]\`.

\`AuditManifestV1\`: \`manifest_version, canon_release_ref, source_hash, code_commit, toolchain_ref, wasm_hash?, model_hash, input_bundle_hashes[], test_report_hash, security_review_hash?, reviewer_ids[], release_state\`.

Rules: stable field order and encoding, unambiguous units/scales, explicit bounded missingness, explicit versioned enum set; no use of floats, timestamps from validator-local clock, or unpinned fetched artifacts in consensus-critical checks. \`REAL\` entries remain rejected under current integrity policy. Generic documentation schemas do not constitute a DNA update.

## 4. Integrity zome / coordinator / off-chain boundary

\`\`\`text
Physical / lab / device observations
   ↓ signed source evidence + quality metadata
Bridge / bounded normalization + TEST namespace
   ↓ canonical ObservationBundle
Holochain coordinator  ──> proposed create entry
   ↓
Integrity-zome validate(op)
   ├─ static type / class / length / signature-scope checks
   ├─ retrieve ONLY deterministic, hash-addressed dependencies with must_get_*
   ├─ resolve frozen model (candidate MVP: baked into approved DNA)
   ├─ pure Rust inference: no network, wall clock, randomness, LLM, mutable registry
   ├─ compare proposed receipt with locally recomputed integer vector
   └─ Valid | Invalid(reason) | UnresolvedDependencies
   ↓
Evidence Spine records DHT conformity (NOT physical truth)
   ↓ separately authorised scientific MRV / oracle review / anti-gaming
   ↓ explicit Claims Register and PRU / RAVEL shadow analysis
\`\`\`

**Recommended minimal viable approach:** one small, explicitly synthetic test forest compiled into the integrity DNA, whose hash is pinned as part of the approved DNA build; validate synthetically namespaced receipt structure and arithmetic only. A model change may alter DNA semantics/hash and requires reviewed migration, not a silent coordinator update.

For external model artifacts or dependencies, prove retrievability/addressability and correct \`UnresolvedDependencies\` semantics; defer design variants that depend on unbounded or mutable network fetching. HDI \`validate\` must never call LLMs, external HTTP, Reticulum peers or dynamic oracles. Coordinator may orchestrate capture and emit proposed records but cannot bypass integrity validation.

**Current blocking implementation fact:** \`REAL_DATA_PERSISTENCE_GATE_CLOSED\` remains in current \`MrvEvidenceEntry\` integrity validation, and cannot be bypassed for MRF integration. Preserve \`TEST-\` evidence subject scoping. Keep all experimental receipt/attestation types separate or gated; no claim that this file has changed a production DNA.

## 5. Oracle attestation ≠ Holochain consensus

Three distinct objects:
1. **DHT rule validation** — deterministic acceptance of specific actions/entries.
2. **Oracle evidence agreement** — optional application-layer threshold/quality policy over signed attestations.
3. **Scientific admissibility** — independent measurements, calibration and study design supporting a stated claim.

Candidate \`OraclePolicyV1\`: \`policy_hash, domain_scope, required_methods, minimum_independent_operator_groups, minimum_independent_device_classes, signer_revocation_policy, time_window_policy, geography_policy, conflict_policy, human_review_gate\`. No universal \`k-of-n\` threshold is adopted; threshold must reflect threats, independence and cost in a scoped ADR.

Threats: collusion, Sybil operators, cloned device identity, reused raw measurements, synchronized spoofing, compromised calibration, replay/stale attestations, sensor-specific bias, malicious missingness, common-mode failures, unavailable dependencies, censorship/partitions. Track \`AGREEMENT\`, \`DISAGREEMENT\`, \`UNDETERMINED\`, \`REQUIRES_INDEPENDENT_REVIEW\` separately from \`DHT_VALID\`. Even perfect agreement proves neither actual restoration nor causal effect.

## 6. Ecological integrity, anti-gaming and causal testing

An MRF cannot make manipulation impossible. Detect candidate co-movements across water, soil, biomass, biodiversity and inputs; retain individual metrics, missingness and negative sentinel outcomes. Reject single-score assertions that hide deteriorating variables.

Adversarial classes: Goodhart/reward hacking, selective sampling, sensor spoofing, unit-switching, missingness masking, out-of-distribution input, temporal selection, label leakage, double counting, OOD extrapolation, model drift and unmeasured ecological spillovers.

**Anti-gaming protocol**: (1) independently calibrated sampling; (2) predeclared indicators and baseline; (3) negative/sentinel indicators; (4) independent review and controls; (5) OOD/drift flags; (6) signed provenance; (7) prohibit downstream promotion where evidence weak; (8) site-out replication. Multi-output statistical covariance is not proof of ecological causal coherence.

**Required distinction:** \`PREDICTION\` vs \`OBSERVATION\` vs \`CAUSALLY_ATTRIBUTED_CHANGE\`. Any purported reduction in RAVEL loss frequency/severity or improved cash-flow requires its own evidence, comparator, risk mechanism, horizon and residual-uncertainty gate. An MRF may be wrong while perfectly deterministic.

## 7. Edge / mesh / Reticulum boundaries

Four resource classes:
- **S1 Sensor/MCU**: capture, timestamp provenance, basic plausibility checks, secure key handling where feasible, buffering. No presumption of Holochain conductor or full WASM.
- **S2 Edge gateway**: ingestion, lightweight optional inference, canonicalization, batching, stores/retries; may use Reticulum transports if tested.
- **S3 Holochain host**: conductor, source chain, DHT, zome WASM validation, frozen model/receipts.
- **S4 Audit/train host**: training/calibration outside consensus path, scientific analysis, replay, adversarial benchmarking.

Reticulum is a candidate transport only; it is **not** the oracle authority, MRV validator, Holochain DHT, or consensus protocol. LoRa/Reticulum may have very limited throughput/MTU and airtime restrictions; only compact hash-addressed evidence/envelopes should traverse links after measuring costs, and larger artifacts must be available through appropriate content retrieval paths.

Benchmark per class: compiled model bytes, WASM size, peak memory, CPU/fuel per inference, p50/p95 latency, joules/verified observation, bytes transmitted per observation, offline buffering duration, delivery after partitions, uptime and cost. No performance or sustainability claim before measurements.

## 8. AI and security boundary

AI/LLM roles are assistive: retrieve, reconcile, explain, propose code/scenarios, highlight anomalies, produce review dossiers. Deterministic algorithms validate their typed proposals; human governance approves material method and production changes. \`LLM_JUDGEMENT\` is always declared and never promoted to source data.

Hardening: least privilege, read/write separation, dependency and artifact pinning, signed release manifests, controlled secrets, replay protection, device/operator identity controls, audit trails, input bounds, fuzzing, recovery and rollback. Data or prompt text inside source artifacts is untrusted and cannot direct deployments or financial actions.

## 9. Synthetic golden vectors and formal test catalogue

**Not ecological measurements**. Toy forest \`T=2, p=2, m=2\`:
- Tree 0: split \`x[0] < 300\` → left \`[15,-5]\`, right \`[4,2]\`.
- Tree 1: split \`x[1] < 100\` → left \`[1,1]\`, right \`[3,-2]\`.
- Input \`[250,90]\` ⇒ \`[8,-2]\` (integer mean).
- Input \`[320,120]\` ⇒ \`[3,0]\` (trunc toward zero).
- Near-threshold \`[300,100]\` ⇒ \`[3,0]\` (comparison strictly less).
- Invalid features, duplicate/reachable tree node errors, overflow, excess depth, extra trailing bytes ⇒ deterministic rejection.

Test IDs and admission requirements:
- \`MRF-T01\` byte-for-byte canonical serialize/deserialize, malformed/trailing data rejection.
- \`MRF-T02\` fixed-point golden outputs, boundaries and negative division rule.
- \`MRF-T03\` native Rust vs WASM parity on version-pinned toolchains.
- \`MRF-T04\` property-based/fuzz tests: bounds, no panic, no OOB, no cycles.
- \`HC-T05\` integrity callback accepts synthetic conforming receipt; rejects counterfeit model/output/TEST namespace; does not permit REAL persistence.
- \`HC-T06\` missing dependency yields retry/UnresolvedDependencies, not fabricated Valid/Invalid.
- \`OR-T07\` identity/collusion/replay/missing independence tests, without treating quorum as truth.
- \`ECO-T08\` selective improvement with negative sentinel and OOD must trigger review.
- \`EDGE-T09\` latency, RAM, WASM fuel, energy and low-bandwidth budget measured on each representative device.
- \`OPS-T10\` peer partition, recovery, rollback, audit replay, frozen release manifest.
- \`GOV-T11\` no PRU/RAP/TRBK/capital/REAL gate promotion from TEST output.
- \`SCI-T12\` out-of-time/out-of-site testing, independent ecological comparator and explicit falsification.

A complete test report must log \`test_id, artifact_hashes, code_commit, environment, expected, observed, PASS|FAIL|NOT_RUN, reviewer, timestamp\`. Only tested observations can be marked PASS; listed tests currently mean **planned**, not passed.

## 10. Baseline alternatives and decision logic

Compare: (A) hand-authored deterministic rules/no model; (B) one small tree; (C) independent single-target trees; (D) joint multi-output forest; (E) off-chain inference plus signed receipt; (F) zome-side inference. Score ecological predictive performance, reproducibility, false-accept/false-reject risk, total verification cost, edge energy, long-term maintenance, data sovereignty and complexity. Holochain must also be compared with signed provenance plus conventional database for the defined use.

**Default decision:** use the smallest fully pinned model and synthetic tests first; upgrade only if benefits exceed baselines under preregistered criteria. Independent statistical validation is required to claim that joint MRF improves cross-variable inference.

## 11. Source roadmap and gates

| Window | Deliverable | Responsible lane | Entry/exit gate |
|---|---|---|---|
| D0 now | source candidate, correction register, Canon lock, ADR and repo inventory | Canon Guardian + Architect | document branch / review only |
| Days 0–30 | freeze MRF binary/numeric schema; no-std or WASM-compatible pure Rust engine; golden/fuzz tests; explicit source/model registries; review existing zome schemas and migration impact | Rust/WASM + Holochain + Security | reproducible native/WASM proof + negative tests; **no REAL** |
| Days 31–90 | shadow synthetic integrity-zome integration; host conductor sweettests; signed oracle receipt sandbox; independence threat tests; site-independent validation design | hApp + MRV + Distributed Systems | DNA migration review, security review, no unauthorized write |
| Months 3–12 | preregistered Site 01 evidence collection *only after REAL gate separately opened*; OOD/anti-gaming eval; edge/Reticulum benchmarks; independent replication plan | Field Science + Edge + Operations | real governance/data permissions + external scientific review |
| Beyond | site-out replication, revised model, portfolio and risk research only if causal evidence permits | Independent Review + RAVEL | domain-specific scientific/legal/market admissions |

### Stop conditions
Fail/retire if model cannot be deterministically reconstructed, cannot fit bounded validator cost, cannot demonstrate calibration/generalization, increases false ecological claims, introduces unrecoverable dependencies or requires Canon violations. A failed test cannot be cured by narrative.

## 12. Decision log / governance work items

- **ADR-MRF-001 (PROPOSED):** compiled frozen synthetic model in DNA for MVP; separately benchmark off-chain signed receipts.
- **ADR-MRF-002 (PROPOSED):** fixed-width signed integer numeric ABI and strict branch comparison; no floating-point in validator v1.
- **ADR-MRF-003 (PROPOSED):** oracle attestation as a separate application-layer review; no global consensus claim.
- **ADR-MRF-004 (PROPOSED):** Reticulum is optional transport on S2/S3; no assumption that sensor S1 runs conductor.
- **ADR-MRF-005 (PROPOSED):** preserve existing REAL persistence gate; any change requires separate steward approval, DNA hash review and conductor tests.
- **ADR-MRF-006 (PROPOSED):** multi-output anti-gaming hypotheses must beat independent sentinel checks and simple baselines.
- **ADR-MRF-007 (PROPOSED):** no value/rights claims; PRU/RAP/RAVEL links remain shadow/non-authoritative.

**Open blockers:** no canonical trained MRF artifact with registered dataset/method; no tested production-class serialization ABI; no MRF WASM parity report; no approved oracle independence policy; no sensor calibration/REAL gate approval for this capability; no edge energy measurements; no scientific out-of-site ecological validation.

## 13. Release / acceptance contract

The source may be stored as a **candidate** in a documentation branch and proposed via draft PR. It becomes a controlled methodology or operative architecture source **only** through the applicable authorized review/ADR procedures. It is never automatically part of signed \`v1.1.2-genesis\` or signed runtime \`v1.1.3-runtime-proof\`.

Acceptance evidence before any functional rollout: frozen source and model hashes; resolved conflict/dissent; formal schemas; peer review; compiled reproducible WASM hash; PASS negative and golden tests; conductor tests on exact DNA artifact; security signoff; rollback; independent verification of intended claim; human authorization for material changes. Keep \`REAL_DATA_PERSISTENCE_GATE_CLOSED\` intact unless separately approved in the integrity DNA.

### Claims register: permitted
- "A deterministic multi-output forest validation method is specified as a source candidate."
- "A synthetic test can verify the arithmetic of a frozen model if its test harness is executed successfully."
- "Reticulum is under evaluation as a low-bandwidth transport, not a validation authority."

### Claims register: prohibited until evidence
- "MRF prevents ecological manipulation."
- "Distributed model agreement proves ecological regeneration."
- "Oracle quorum certifies real sensor data."
- "PROMETHEUS MRF is deployed/production-ready."
- "Verified returns, PRU value or token rights arise from model output."

**Summary gate:** Design-only and synthetic-lab investigation permitted; any broader scientific, financial or runtime-admission claim is explicitly blocked until reviewed evidence exists.


---

## 14. Local Rust/WASM feasibility evidence added 2026-10-19

Companion *draft*, nonproduction hApp proposal: [`prometheus-happ#39`](https://github.com/Permaculture-DAO/prometheus-happ/pull/39). Experimental code path: `experimental/mrf-kernel-lab`. No modification to currently registered hApp workspace, existing integrity zome, REAL gate or signed runtime.

- **VERIFIED IN LOCAL WSL:** pure Rust synthetic kernel: **13/13 unit tests passed**; compiler `rustc 1.96.0 (ac68faa20 2026-05-25)`. Tests cover toy multi-output inference, strict thresholds, signed-integer aggregation, local serializer roundtrip and malformed input rejections.
- **VERIFIED IN LOCAL WSL:** `cargo build --offline --release --target wasm32-unknown-unknown` completed. The local output file measured **28,681 bytes**; local SHA-256 `e206d5c0557ed22d93500a2cd6fc847df0e0c635cd2f0a03c61e98d9e49caf48`. This identifies a local unsigned artifact, not an independent reproducible build or signed Holochain DNA.
- **NOT RUN / NO-GO:** executable WASM parity test in runtime, Holochain integrity callback, DHT dependencies, conductor sweettests, oracle-threshold independence, MRF training and ecological validation, model-signature authority, fuzz testing, real device energy benchmarks.
- **Governance:** both PRs remain drafts; code/runtime release, source admission, Canon change, REAL data and any finance/token action remain unapproved.

These experiments **narrow** the arithmetic/compilation uncertainty only; they do not validate physical observations, scientific claims, production safety, DHT acceptance or the proposed MRF architecture end to end.

**Next technical gate:** independent reproducibility and executed WASM golden-output parity (not merely compilation), then separate HDI-compatible synthetic-only integrity-zome integration with conductor tests on a specific DNA hash.

## 15. Stage Gate 0–30 supplemental technical evidence — 2026-10-19

The design source is accompanied by experimental implementation work in draft [prometheus-happ#39](https://github.com/Permaculture-DAO/prometheus-happ/pull/39), without merging anything into signed Canon or production hApp.

**Verified in actual execution:** Node.js v18.19.1 instantiated a Rust-produced WebAssembly binary; 4,108 input vectors from a native Rust reference executable compared against two WASM output functions, **8,216/8,216 identical i64 results**. This is synthetic *execution parity*, not ecological validation.

**Verified in host unit tests:** Holochain HDK 0.6.1 / HDI 0.7.1 synthetic-only integrity zome: **9/9 host tests passed**, rejecting forged outputs, wrong model hash, REAL evidence, non-TEST namespace, malformed inputs and attempts to elevate authority. These tests do not alone prove conductor acceptance or rejection.

**Verified build and packaging:** standalone experimental integrity-zome and coordinator compiled as WebAssembly with the actual hApp WASM compiler setting getrandom_backend="unsupported" and linker --allow-undefined. Packed an isolated TEST DNA using hc dna pack:
- PMRF synthetic model (115 bytes): SHA-256 e074715a26129c8f00e828774eadc71ef33f94a620c0dcd0e00216b6156bda5f;
- integrity zome WASM SHA-256 46b47071ded9b70ffb3198e50d41242dbd7cffda869e7123ce4ac8074a5363c2;
- coordinator zome WASM SHA-256 dc86b0ab8f48d3c88bd1385a2cc248e46115630999a9614f534bca63dbee12bb;
- experimental packed DNA (1,466,141 bytes): SHA-256 8f60c6b9e9fe9d3722720376a5aa30ca49720268a2a8fdbd036f35f61aba6efc.

**Still a separate gate:** in-process conductor sweettests must be actually run against exactly that TEST DNA and recorded. No REAL persistence, oracle consensus, field data, certified outcomes, signed production artifacts, token rights or capital actions were authorized or tested by the steps above. Reproducible independent builds and fuzz/property benchmarks remain outstanding.


## 16. Independent CI cross-check — technical claim refinement

The Linux GitHub Actions parity run (2026-10-19, [hApp run 39325521772](https://github.com/Permaculture-DAO/prometheus-happ/actions/runs/39325521772)) independently executed **8,216/8,216 matching integer results**, over **4,108 synthetic vectors** in native Rust and WebAssembly. This supports *numeric execution parity* on two separately compiled environments.

The GitHub-runner WASM SHA-256 was ada00809503adfc57dfbed7aa4b930271c2788a90d2fdcd3df0c8e36fcdfb373 (29,244 bytes); the earlier WSL WASM SHA-256 was e206d5c0557ed22d93500a2cd6fc847df0e0c635cd2f0a03c61e98d9e49caf48 (28,681 bytes). **Therefore byte-identical release reproducibility across toolchains is not yet established.** The initially failed CI run exposed a workspace-isolation defect corrected on the test-only branch, providing independent audit evidence of the value of CI. An independent HDI host-unit-test job also passed.

These observations do not alter scientific admissibility, REAL persistence, Canon, insurance/credit authority, token rights or capital gates.


## 17. Milestone audit update — 2026-10-21 (no authority promotion)

On the tested pinned toolchain, independent GitHub Actions run [39326442563](https://github.com/Permaculture-DAO/prometheus-happ/actions/runs/39326442563) built a WASM kernel with SHA-256 e206d5c0557ed22d93500a2cd6fc847df0e0c635cd2f0a03c61e98d9e49caf48 and 28,681 bytes, exactly matching the previously recorded WSL artifact; executable Rust/WASM parity remained 8,216/8,216 scalar checks. This verifies a bounded repeatable binary outcome for this synthetic kernel only; it does **not** establish complete DNA build reproducibility or supply-chain attestation.

On 2026-10-21, eight additional **bounded deterministic adversarial regression tests** passed locally, covering prefix truncation, bitwise mutation, random malformed bytes, canonical re-encoding, repeated signed-input inference, extreme values, structural cycles and arity limits. There are now 21 local kernel unit/integration tests (13 original + 8 additional); this does not replace independent continuous fuzzing or a formal proof.

An isolated in-process Holochain conductor **accepted one valid TEST synthetic MRF receipt** in 93.92 seconds (1 passed, 0 failed; remaining four cases filtered). Acceptance is a real conductor result for that *one case*, and **not proof yet of all malicious-entry rejections**. The five-case combined conductor scenario is under test and must retain its own recorded result. The synthetic packed DNA SHA-256 remains 8f60c6b9e9fe9d3722720376a5aa30ca49720268a2a8fdbd036f35f61aba6efc.

A required design gap remains: currently the zome compares the receipt's declared model hash against a fixed constant but does **not** independently hash the compiled toy model bytes in the callback; as such, source/code governance must bind model bytes to the claimed digest and the DNA artifact. Validation of StoreRecord/RegisterUpdate/RegisterDelete (and possible inter-zome dependencies) remains unproven. No REAL/data/certification/financial/PRU/RAP/TRBK gates are changed.
