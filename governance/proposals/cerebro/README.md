# PROMETHEUS CEREBRO — deterministic environmental source custody handoff (v0.3 RC1)

**Status: PROPOSED / SHADOW / NON-CANONICAL / NOT ADOPTED.**
**Purpose of this Draft PR:** review the source taxonomy, ownership boundary and admission checklist. This is not source ratification and does not modify signed Canon, the active Source Registry, Source Root, any production runtime, Holochain DNA, Claims Register, or legal/financial rights.

## Controlling authority and dependency
- **Signed governing Canon:** Genesis v1.1.2 (`prometheus-canon` signed Genesis release).
- **Source Root PR #18:** PROPOSED_NOT_ADOPTED. Do not assume proposed v2 Authority Lattice or deterministic architecture has been ratified.
- **Geospatial Intelligence v0.2:** existing [`prometheus-bridge` Draft PR #11](https://github.com/Permaculture-DAO/prometheus-bridge/pull/11), which already owns US land-specific FEMA, USGS, ArcGIS and GEE shadow adapters; this PR must not replicate them.
- **Runtime:** existing S3–S6 admissions and Evidence Spine/MRV retain all gates. Public bridge is read-only, and new live sensor/laboratory/satellite ingest is not authorized by this source proposal.

## Candidate source inventory (separate private release)
The full research handoff **CEREBRO_CONTROLLED_REVIEW_v0_3_RC1_2026-10-18.zip** is provided to the designated source custodian outside this GitHub review proposal. It contains:
- full environmental candidate source specification v0.3, a Geospatial v0.3 ADR, proposed registry delta, schema and tests;
- **115 logical rows:** 56 inherited provider/dataset candidates + 59 normalized external references from 65 occurrences, not 115 independently validated measurements or providers;
- historical PHC 2025 13-variable snapshot (a 2025 report, not substituted for PHC 2026);
- private workstation inventory of 22 filenames with read-only SHA-256 digests and sizes; remote raw bytes were never copied into GitHub;
- reconstructed CSV quoting for two comma-containing filenames, after the earlier v0.2 manifest failed a fresh test; rerun: **26/26 private unit tests and 4/4 public candidate tests PASS** on 2026-10-18. These checks are structural, not empirical data validation.

Sealed private candidate source (SHA-256):
`dafb753a55280f7efc4a67fe3b7d1f1631a3cd90f57f666ae4a9cfff4160c368`

Sealed unified candidate source register (SHA-256):
`b419c76a606bdd29b226bdbe33c3a22d2f6b0a6ba0eca28499de5067659e9239`

**These content hashes identify the privately held files; they do not assert that those files have been uploaded, reviewed, or adopted by this PR.** The complete bytes must be transferred through a controlled custodian process before any proposed source registration or ratification. No public workstation file names, raw GeoJSON or protected-site coordinates are introduced here.

## Scope ownership
| Domain | Responsible component |
|---|---|
| Provider/dataset discovery, licences, product provenance, satellite/PAR/LAI/FAPAR/biodiversity/GHG scientific methods | CEREBRO candidate source-intelligence plane |
| Official parcel/APN, county GIS, rights context, legal cadastral geometry and territorial dossier | Geospatial Intelligence v0.2 / RTC-OS; independently governed legal authority |
| Event transport, normalization and technical admission | Existing runtime S3–S6 |
| Evidence identity, verification and scientific admissibility | Existing Evidence Spine / MRV |
| Planetary Boundaries interpretation, site PHI conclusions | Approved PHI and scientific-method layer, not CEREBRO automatic scoring |
| Capital/underwriting, insurance, ecological credit claims | Existing Aeterna/Ravel and legal/human authority, never an implied consequence of sources |

## Verification and anti-duplication invariants
- A portal or screenshot **is not** a raw measurement; a dataset name **is not** proof of an API being functional.
- Mirrors of the same Sentinel scene (Copernicus, Esri, EOS) map to one upstream product identity.
- iNaturalist occurrence republished by GBIF retains the same provenance and is not two independent records.
- PHC 2025 and 2026 are separately versioned scientific reports; changes in method and thresholds are preserved.
- PAR, FAPAR and LAI remain different variables with different units and methods.
- Historical ESG estimates or NDVI clusters are **not** calibrated carbon stocks, water savings, legal parcels, external financial claims or ecological credits.
- UNKNOWN != ZERO; uncertain licence/rights/source version -> HOLD.
- No agent can turn D/P/H/Q research output into gate transitions without deterministic verification and competent authorization.

## Requested review disposition
**Review-only preclearance:** have source custodian check ownership, provisional `PRM-CEREBRO-SOURCE-001@0.3-rc1` collision, controlling Canon/PR #18 lineage and private source hashes; have EO/MRV, source licence/privacy, security, GIS/land-method and scientific reviewers assess the candidate. **Leave this PR DRAFT.** Separate future action required for any full-byte controlled source submission, registration, Canon change, live adapter admission or deployment.
