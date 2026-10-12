# Supersession note — v1.1.2-genesis Full Corpus → canon v1.2.0

| Field | Value |
|---|---|
| Status | **DRAFT for the v1.2.0 release notes.** Not effective until v1.2.0 is ratified, signed and tagged. |
| Subject | Signed `canonical/h-earth-prometheus-white-paper.md`, v1.1.2-genesis, sha256 `f3862005bc4d6e8e4cba0f2a7646e67dff758fcd28c8411046eb5d04875f9540` (`prometheus-canonicals/releases/2026-06-21/`). Line numbers below refer to that exact file. |
| Prepared | 2026-10-01, Claude Code (internal; not independent review) |

## 1. What happens to the Full Corpus

1. **Bytes stay immutable.** The signed file, its `.docx` and its signatures are never edited. At release the
   file moves (unchanged) to `provenance/v1.1.2/` in `prometheus-canon`; the signed archive copy in
   `prometheus-canonicals/releases/2026-06-21/` stays where it is.
2. **Role changes.** From v1.2.0 the Full Corpus is the **subordinate knowledge and provenance corpus** (source
   hierarchy rank 3). It can inform interpretation but **cannot override** the canon.
3. **Precedence rule.** Where a corpus passage conflicts with v1.2.0, v1.2.0 governs. Corpus passages that do not
   conflict remain valid reference material.
4. **Completeness.** The table below lists the conflicts identified so far. It is **not exhaustive**: the
   independent documentary review (see `prometheus-governance/audit/DOCUMENTARY_REVIEW_PACKAGE.md`) must complete it
   before the release is frozen.

## 2. Passages superseded or corrected

| Lines | Topic | Corpus wording (short) | Disposition | Governing text in v1.2.0 |
|---|---|---|---|---|
| 131, 135 | Token architecture | "three layers… the access token is engineered as consumptive utility" + Figure 6 | **SUPERSEDED** (A-002 declined, ARD-001) | §T "Token and instrument boundary"; X.1 |
| 174 | Claim C-008 | "The access token provides consumptive utility… redeemable access credit" | **SUPERSEDED**; `prometheus.token.access_utility_candidate` deprecated | W, C-008 = `prometheus.trbk.external_interface_no_prometheus_rights` |
| 182–205 | X.1–X.3 | Three-layer table; Howey and EU utility-token analyses | **SUPERSEDED / withdrawn to provenance** | X.1 (separation + P0–P4); X.2 (classification reserved to counsel) |
| 211, 330 | Red-team / review lenses | "three-layer separation" | **SUPERSEDED** | X.4, X.11 as amended |
| 342 | Glossary "Access token" | "A consumptive utility and access credit" | **SUPERSEDED** | X.12 "TRBK" entry |
| 1190, 14539, 19375, 26501 | TRBK definition | "TRBK represents a governance, coordination, access, or participation layer" | **SUPERSEDED** (TOD-001 interim; full ratification pending) | T; X.1; W C-008: TRBK is external to the canon; no Prometheus rights |
| 19379, 19405 | TRBK role | "part of the coordination architecture… TRBK supports coordination" | **SUPERSEDED** | same as above |
| 17942, 18148 | TRBK ≠ ownership | negative boundaries ("not automatic fractional ownership", "not land ownership") | **RETAINED** (consistent, stricter in v1.2.0) | X.1 |
| 165–178 | Claims Register | C-001…C-012 as global IDs | **SUPERSEDED as keys**; labels kept as release-local aliases | W: `claim_uid` + lineage |
| 168, 14281, 19076 | OHE definition | "the biophysical unit…" | **SUPERSEDED** | H; X.12: bounded, place-contextualised social-ecological unit, human participation endogenous |
| 24931–24939 | Genesis protocol (XI.2) | "Three OHE-compatible units (~1,000 m² each)…; final dataset at 48 months" | **SUPERSEDED** | R: G-MEP (~12 months) / G-VP (up to 48 months); claim ceiling by timepoint; surveyed experimental boundary |
| 22973 | "Three layers" (asset intelligence / portfolio-readiness / regulated asset management) | a separation of activities, not of tokens | **RETAINED** (compatible) | consistent with A, P, T |
| 47290 | Token interoperability | "Prometheus may interact with… access tokens… TRBK…; interoperability must remain strictly bounded" | **QUALIFIED**: any TRBK interaction only via the TOD-001 pathway policy (P0 default; P1 design only; P2 NO-GO; P3 RED; P4 prohibited) | X.1 pathway policy; TCD-001 (draft) |
| 59128 | Repository link | stray "(github.com in Bing)" search link | **ERRATUM** (conversion artefact; no meaning) | not reproduced |

## 3. Carried forward unchanged (for the reviewer's invariant check)

The v1.2.0 text carries these from v1.1.2 and they are **not** superseded:
- the non-bypassable sequence (text unchanged; "living system" now defined in the glossary);
- PRU/RAP firewall;
- human-state and biometric weight 0 (A-001);
- the pre-pilot rule `U_max_capital = 0` (corpus around lines 49835–49857);
- the Jacobi et al. 2025 temperate caveat;
- the civic, political-neutrality and child-safeguarding provisions;
- HoloFuel operational only;
- canon custody and the three Eternity disciplines.

## 4. To verify before freeze

- A full-text pass of the ~265,000-word corpus for any further "access token", "utility", "consumptive", "redeem"
  and TRBK-role wording (lines 22973 and 47290 were checked on 2026-10-01 and are classified above).
