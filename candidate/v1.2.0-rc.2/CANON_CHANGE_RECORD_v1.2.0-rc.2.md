# Canon Change Record — v1.2.0-rc.2

| Field | Value |
|---|---|
| Record | CCR-v1.2.0-rc.2 |
| Date | 2026-10-01 |
| Decision class | Ordinary (successor-line selection, ontology clarification without altering sequence text). Items marked ⚠️ remain Eternity-level and are **not** closed by this record. |
| Signed authority in force | `v1.1.2-genesis` (unchanged by this record) |
| Candidate | `PROMETHEUS_Canonical_White_Paper_v1.2.0-rc.2.md` (this folder) |
| Status | **CANDIDATE — not ratified, not signed, not frozen** |
| Provenance | AI-authored (Claude Code), building on AI-authored inputs (ChatGPT workstream, July and September 2026) plus founder material. Internal review only. Disclosed per canon custody: the canon remains substantially single-source. |

## 1. Lineage resolved

| Line | Disposition |
|---|---|
| `v1.1.2-genesis` (signed) | Remains controlling until a successor is ratified and signed. |
| `v1.2.0-convergence-rc.1` (Jul 2026) | **Absorbed.** Its release identity, validation matrix, TRBK boundary and pathway policy, source-control and release procedure, assurance boundary and source-class rule are carried into this candidate. Kept as provenance; not developed further. |
| White Paper editorial 8.0 RC (27 Sep 2026; staged in canon PR #14) | **Body of this candidate.** Converted from DOCX (sha256 `fef40a96d3dcce2a2c5658bce7289f6c65fc74731995d7b97471486d151edf42`) to Markdown with pandoc 3.10 and patched as below. |
| White Paper editorial 7.1 RLS draft (26 Sep 2026) | **Absorbed.** Its relational substance enters through Option A (§3). Its change to the first term of the sequence is **not** adopted. Kept as provenance. |
| Corpus 7.x, runtime S0–S6, hApp 1.1.3 runtime proof | Unchanged; subordinate lineages. |

Numbering: canon release `v1.2.0-rc.2` (continuity with the signed line and with CCD-001/ARD-001/TOD-001); editorial revision 8.1. Version axes are independent (X.15).

## 2. Signed decisions honoured

- **CCD-001 (ratified):** Markdown is the source. Two clean pandoc 3.10 builds with `SOURCE_DATE_EPOCH=1759276800` produced byte-identical DOCX (sha256 prefix `0d87a454e1de9221`). The DOCX→text roundtrip matches the Markdown source with 0 differences, ignoring whitespace and table markup. **Independent review of parity is still required.**
- **ARD-001 (ratified):** A-001 carried (human-state weight zero). **A-002 declined.** The 8.0 RC text re-introduced the A-002 classification (C-008 "access token… redeemable access credit"; X.1 layer 1; X.2–X.3 utility-token analyses; glossary). **All removed.**
- **TOD-001 (interim only):** the interim fail-safe TRBK boundary and the P0–P4 pathway policy are carried in T, W (C-008), X.1 and the glossary, explicitly labelled interim. ⚠️ Full Eternity ratification and the counsel opinion remain open; A-002R is not disposed.

## 3. Clause changes (against editorial 8.0 RC)

Status codes follow `CANON_CLAUSE_RECONCILIATION_v0.1`.

| Section | Action | Change |
|---|---|---|
| Front matter | ADD | Release identity, absorbed lines, validation-status matrix |
| A | AMEND | Relational and place-based participation creates no rights |
| B | AMEND | Principles apply to place-contextualised systems with human participation endogenous; no gate loosened |
| C | AMEND | Abstract: place-contextualised living systems |
| G | ADD | Relational living-system frame; place and relational context precondition. **Sequence text unchanged** (Option A) |
| H | AMEND | OHE: bounded, place-contextualised social-ecological unit; versioned boundary; not an isolated parcel |
| I | ADD | Embedded observation rule; relational evidence firewall |
| M | ADD | Role separation and scope-specific conflict of interest |
| N | ADD | Versioned evidence record types; append-and-supersede; `claim_uid` |
| O | AMEND | AI cannot promote inferred relations; model/version provenance |
| P | AMEND | TRBK confers no Prometheus right; participation creates no entitlement |
| Q | CLARIFY | Context, public-value, resilience-attribute and human-state variables at default weight zero; controlling expression unchanged |
| Q (restore) | RESTORE | Pre-pilot rule `U_max_capital = 0` (signed v1.1.2, lines ~49855–49857; also in v1.2.0-convergence). WP 8.0 RC had dropped it; found in Claude's invariant self-check on 2026-10-01 |
| R | ADD | G-MEP / G-VP tiers; claim ceiling by timepoint; H3/H4/H5a–H5c duration rules; surveyed experimental boundary |
| R (2026-10-02) | AMEND | Imported the internal v7.0.3 H5 non-substitution discipline as a candidate amendment: H5a ecological complementarity, H5b full-cost economic surplus and H5c organisational/cooperative advantage remain separately specified and evidenced. Not a restoration from signed v1.1.2. |
| S | AMEND | Proof of physical origin = adversarial assurance, not unforgeability |
| T | REPLACE ⚠️ | Token architecture → TRBK external boundary (interim TOD-001) |
| U | ADD | Semantic drift, claim-ID collision, boundary drift, relational overreach, reviewer conflict, model-completeness illusion, staleness |
| V | AMEND | Phase 1 = G-MEP design with context record and versioned boundary |
| W | AMEND | `claim_uid` column; C-013–C-018 added; `prometheus.token.access_utility_candidate` **deprecated** |
| X.1–X.3 | REPLACE ⚠️ | Token/instrument separation + pathway policy; utility-token Howey/MiCA analyses withdrawn to provenance; X.3 reserved |
| X.4, X.11 | AMEND | References updated to TRBK boundary |
| X.10 | ADD | Checklist items: `claim_uid`, relational firewall, TRBK, downstream staleness |
| X.12 | AMEND | Glossary: living system, OHE, context, `claim_uid`, G-MEP/G-VP, TRBK (replaces "access token"); HoloFuel named as the operational layer (8.0 RC omitted it; restored from v1.2.0 §5.6) |
| X.14 | AMEND | Status as of 1 Oct 2026, including Evidence Spine gaps |
| X.15–X.17 | ADD (from v1.2.0) | Source control and release procedure; independent assurance boundary; source-class rule |
| Firewall | AMEND | "three-layer token architecture" → "any separate legal instrument" |
| media | DELETE | `image7.png` (figure of the declined three-layer token design) |

Net size: about 6,300 → 8,400 words. Justification for the complexity budget: the additions replace three parallel candidates (v1.2.0, 7.1, 8.0 = about 17,100 words) with one line. Those candidates are retired to provenance.

## 4. Downstream propagation (must not state more than this candidate)

| Artefact | Required action |
|---|---|
| canon PR #14 (8.0 RC staging) | Superseded by this candidate; close or rebase onto it. Do not merge as is. |
| Claim UID registry v0.2 (P0_2 package) and runtime PR #18, hApp PR #31 | Replace `prometheus.token.access_utility_candidate` with `prometheus.trbk.external_interface_no_prometheus_rights`; add `prometheus.hypothesis.r1_risk_compression` and `prometheus.hypothesis.t1_time_positive_value` |
| bridge/runtime artefacts carrying `prometheus.hypothesis.h5_cooperative_syntropic_surplus` | **STALE** until reviewed; do not rebind this deprecated UID to H5a, H5b or H5c. Map only where a downstream artefact explicitly supports the narrower hypothesis identity. |
| bridge PRs #4/#5, console PRs #6/#7, public console (merged) | Display claim status by `claim_uid`; no token or value wording beyond W |
| `.github` org profile, website, investor deck (Jun 2026), Manifesto (Mar 2026) | **STALE** until reviewed against this candidate; public TRBK wording unchanged until TOD-001 + A-002R close ⚠️ |
| `prometheus-canonicals` | Machine-readable claims and schema bundle to be derived from W after textual freeze |

## 5. Still open before ratification

1. ⚠️ TOD-001 full Eternity ratification + counsel opinion (brief #5); A-002R disposition.
2. Independent documentary review of the compression from about 275,000 words (v1.1.2) to about 8,400 words.
3. Independent review of CCD-001 build parity; pinned build environment recorded in CI.
4. Clause-level import check that no v1.1.2 invariant was lost (civic, safeguarding, HSI, Jacobi anchor and firewall are present; full audit pending).
   - 2026-10-02 reconciliation remediation: imported the internal v7.0.3 H5 non-substitution discipline as a candidate amendment. H5a ecological complementarity, H5b full-cost economic surplus and H5c organisational/cooperative advantage must remain separately specified and evidenced. Independent review required.
5. Textual freeze → manifest → SHA-256 → steward GPG signature → tag → release (steward actions).

## 6. RAVEL v2 candidate amendment — 2026-10-05

This branch adds a **candidate ordinary methodological amendment** that evolves the existing Ravel risk-signalling discipline into PROMETHEUS RAVEL (Risk Allocation, Vulnerability, Exposure & Loss).

Files:
- `RAVEL_ARCHITECTURE_AMENDMENT_v0.1.md`
- `RAVEL_FORMAL_SPEC_v0.1.md`

White Paper sections T, U, V, W, X.10 and X.12 are amended to:
- distinguish loss generation/reduction from loss allocation/transfer;
- add the no-risk-disappears-through-representation invariant;
- define shadow-underwriting metrics EL, ES, PPCI, RRΔ, RTE, URBR/URBC;
- preserve the Regenerative Brake as a review trigger, not autonomous enforcement;
- hold VRRC at zero/not-admitted for capital-facing purposes until causal evidence, independent review, legal admission and external insurer/underwriter acceptance close;
- add claim UIDs C-019–C-026.

**Authority boundary:** this amendment does not modify the signed `v1.1.2-genesis` release, does not close R1/T1, does not create an insurance-recognition pathway and does not admit any capital-facing risk discount. Independent actuarial/scientific/legal review remains open.


### 6.1 Review corrections — Claude canon-lane review, 2026-10-05

- **Brake semantics change, recorded explicitly.** The superseded sentence was: tail-risk model plus systemic-coherence index, with "an automatic regenerative brake" that throttles issuance when coherence degrades. The candidate replaces it with a review trigger: RAVEL signals, governance decides; no autonomous financial enforcement (C-024). This narrows authority and is therefore a tightening, not a relaxation, but it is a semantic change and is recorded as one.
- **Roadmap rows 4 and 6 amended** to add RAVEL shadow-underwriting dry-run and RAP portfolio stress/concentration review, each with VRRC = 0 and no pricing, underwriting-approval, insurance-recognition or risk-discount claim.
- **Formula notation.** LaTeX bracket blocks (which did not render in the markdown → docx pipeline) were converted to the White Paper's plain-text formula convention. Every RAVEL formula is labelled *diagnostic and subordinate to the single controlling PRU expression in Section T*; the conservation test is labelled controlling for model integrity only (not a value expression); VRRC = 0 is labelled a policy-imposed boundary value.
- **Invariant tier.** "Constitutional risk invariants" in the architecture amendment were renamed *candidate methodological risk invariants*. They are not Eternity-level and amend no Eternity invariant.
- **Claim-status vocabulary.** C-019–C-026 statuses normalised to the existing register vocabulary (Candidate methodological amendment; Research-only; Hypothesis; pilot-required; Boundary; not admitted; Methodological). No claim was strengthened.
- **Complexity-budget justification.** Net addition: two candidate documents (architecture amendment, formal spec) plus eight claim rows. Justification: RAVEL makes explicit a risk-allocation discipline (loss generation vs loss allocation, ultimate risk bearer) that the canon previously implied only through a single "adaptive risk control" sentence; the brake sentence it replaces is removed, not kept alongside. The formal spec is a candidate for folding into `prometheus-canonicals` once schemas are lifted after textual freeze, at which point the duplicate prose should be retired.
- **Context source.** The "PROMETHEUS Master Prompt — Finanza Biomimetica / RAVEL / LLM v1.0" is recorded as context input only (layer 7), filed under `_CONTEXT_INBOX/2026-10-05_ravel_b/`. Where it conflicts with signed decisions (notably any description of TRBK as an access/utility instrument, against ARD-001/TOD-001), the signed decisions govern; nothing from it is canonical by virtue of this amendment.
