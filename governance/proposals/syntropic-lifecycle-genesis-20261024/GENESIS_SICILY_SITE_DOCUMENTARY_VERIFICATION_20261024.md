---
record_id: PRM-GENESIS-SITEQA-20261024
status: VERIFIED_DOCUMENTARY_INPUTS_WITH_FIELD_VERIFICATION_PENDING
as_of: 2026-10-24
site: Genesis Sicily / Marina di Ragusa (RG)
field_visit_conducted: false
canonical_site_boundary_frozen: false
study_ready_to_activate: false
---

# Genesis Sicily — current documentary site check (not an in-situ survey)

## 1. Sources actually inspected

- Genesis technical `GUIDA_CAMPO_PILOTA_SICILIA.docx` (2026-06-21; older feasibility/management planning, not signed site-right proof).
- `P1_3D_GENESIS_SPATIAL_EXPERIMENTAL_DESIGN_NOTE_v0.1.md` (2026-09-30; draft experimental treatment/control classes and candidate primary infiltration endpoint).
- `P1_3E_GENESIS_SPATIAL_EVIDENCE_PACKAGE_CANDIDATE.md` (2026-09-30; surveyed A8D boundary hashed, project raster, geometry uncertainty).
- `P1_3F_DXF_PROBE_PROGETTO_IRRIGUO.md` (2026-10-01; read-only vector irrigation DXF probe, unregistered coordinate frames and unconfirmed units).
- `P1_GATE_DECISION.md`, `PREREGISTRATION_ACCEPTANCE_CHECKLIST.md`, `STATISTICAL_ANALYSIS_PLAN_DRAFT_v0.1.md`, `SAMPLING_AND_POWER_PLANNING_NOTE_v0.1.md`, `HYPOTHESIS_ENDPOINT_GATE_MATRIX.csv` (2026-09-29 scientific freeze package).
- Verified current remote directory listing of three original design DXFs on federica: `progetto irriguo.dxf` (378,144,975 B, source file modification 2026-09-30), `RILIEVO TERRENO.dxf` (606,473 B, modified 2026-09-30), `RILIEVO TERRENO BELLASSAI.dxf` (682,588 B, source modification 2024-08-20). Presence/metadata alone does not verify surveyed correctness or georeferencing.

## 2. Evidence matrix

| Fact or claim | Documentary state | Consequence |
|---|---|---|
| Survey A8D experimental drawing boundary `3,360.87 m²` | P1.3D and P1.3E report a hashed 13-vertex shape, coordinates in unresolved drawing CRS | candidate boundary only; no geodetic/polygon freeze or extrapolation to legal cadastral extent |
| Guide identifies ~`3,594 m²` land/cadastral area | earlier June 2026 guide, different perimeter and basis | do not equate 3,594 and 3,360.87; obtain competent reconciliation |
| Guide estimates low infiltration (`~10^-6 m/s`) and clay/stone soil | planning assumption, not a fresh independently documented field test | do not treat rate/texture as measured scientific baseline |
| Post-operam permeable area `3,002.6 m²` vs `2,993.3 m²` unaffected agriculture | technical relation extract in P1.3D | area classification difference ≠ untreated control |
| Seven irrigation sectors | operational layout in source, **not** independent statistical units | no pseudoreplicate n=7 |
| Sector 5 detailed `356.57/356.6 m²` versus aggregate `406 m²` | unresolved internal numeric conflict | HOLD irrigated area and matching geometry |
| Swale ~`80 m` descriptive / `65.8 m` geometric / `94.5 m` filtration path; candidate pair of open polylines `66.48 drawing units` | distinct geometric concepts, source drawings not registered | no canonical length or hydraulic influence polygon |
| Swale influence ~`228.8 m²` | planning estimate | not measured spillover buffer or independent comparator |
| Irrigation project vector DXF exists | P1.3F confirms PVC/drip and swale labels | vector file ≠ registered geospatial layer; designer to confirm units and ≥3 shared ground-control points |
| Three survey DXFs present | current device directory and file metadata read | none provides field sensor readings, titles, consent or regulator approval |
| Actual soil moisture, precipitation, EC, field infiltration, metered irrigation, calibration and stress | no new site-specific measurements supplied or verified in this review | **UNKNOWN**, baseline not ready |
| Signed land access, water extraction, operator safety/works authorization | mentioned as proposed arrangement in older field guide, not an executed current agreement examined here | **UNVERIFIED**; no intervention authorization |

## 3. Required qualified field + GIS verification before any experimental freeze

1. Land steward/owner and qualified surveyor confirm lawful parcel boundary, actual intervention footprint, easements, water-use rights and current works restrictions. Do not disclose private parcel coordinates publicly.
2. Civil/hydraulic designer delivers survey-frame registered vector DXF and source-hashed polygon set for 7 sectors, swale banks/centerline, water network, buildings, exclusions, treatments and potential spillovers; resolves unit metadata and Sector 5 calculation.
3. Qualified soil/hydrology field team verifies soil horizons and texture, bulk density and infiltration at documented points, salinity/EC, slope/aspect, hydrological connectivity, irrigation lines/meters, sensor install rights, secure site access and safety; preserves raw evidence/uncertainty.
4. Field steward dates intervention history, water-source volume/salinity, species/plant age, soil import, mulching, swales, greenhouse construction, and any preceding works; distinguish baseline before intervention from baseline after works.
5. Scientific reviewer determines independent units and comparator; assesses internal control C1–C5 vs external matched reference. If spillover/control geometry cannot be defended, remain observational/exploratory.
6. Instrument/data reviewer confirms LoRaWAN or other sensors actually installed and calibrated, event time synchronization, field QA, independent review and data rights; design sketches do not prove sensor deployment.

**Observed remote-device presence ≠ current ground truth.** No physical visit, live sensor stream, signed executed property/water permission, independent survey or recent laboratory result was available in this audit. The right status is `SITE_DOCUMENTARY_QA: PARTIAL_PASS`, `SPATIAL_FREEZE: HOLD`, `FIELD_BASELINE: HOLD`, `INTERVENTION/REAL_WRITE: HOLD`.
