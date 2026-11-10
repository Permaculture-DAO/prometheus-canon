---
record_id: PRM-GENESIS-H-W1-PREREG-CANDIDATE-002
protocol_version: 0.2-review-candidate
as_of: 2026-10-24
status: DRAFT_COMPLETE_FOR_DOMAIN_REVIEW_NOT_FROZEN_NOT_REGISTERED
scientific_reviewer_approval: PENDING
site_comparator_eligibility: UNKNOWN
field_baseline: NOT_VERIFIED
ethics_safety_water_access: HOLD
real_data_ingestion: HOLD
modified_existing_H2_protocol: false
---

# GENESIS SICILY — Ecohydrological study H-W1
## Pre-registration candidate / water-cycling mechanism in Mediterranean agroforestry

### 0. Critical scope and predecessor compatibility

A *protocol pre-registration draft* has been prepared but NOT deposited, accepted, signed or frozen. It must be submitted to an agreed independent repository/register **before treatment/randomization/data review**, after source/field/method gates are closed. Existing P1.3D (2026-09-30) named **field infiltration rate as candidate primary endpoint**; H-W1 proposes **root-zone volumetric water content as a separate, complementary candidate primary endpoint for a dedicated H2 sub-study**, without silently changing P1.3D, H1 or canon H1-H5. Competing endpoint selections must be settled by scientific reviewer before freeze. If the H2 programme has no capacity to support two tests, select one confirmatory test and treat the other as exploratory. No retroactive designation once results are seen.

### 1. Study identity and research question

`site_id`: GENESIS-SICILY (specific confidential coordinates pending legal/survey alignment); `target climate`: Mediterranean candidate, local climatic class and years require verified station metadata; `spatial boundary`: surveyed drawing A8D 3,360.87 m² **CANDIDATE ONLY**; `study window`: one full comparable dry-season observation interval **TO FREEZE**; extended baseline and multi-year replicates **PREFERRED**; `experiment sponsor/operator, lawful access and reviewer`: PENDING.

Question: at *comparable metered irrigation and precipitation exposure*, does locally designed multistrata management of a syntropic consortium (`S`) change seasonal root-zone volumetric soil water content of a preselected shared sentinel species versus a simpler agroforestry comparator (`C`)? This is a **package-level contrast**, not proof of fungal communication, local precipitation creation, irrigation-saving or project-wide ecosystem superiority.

### 2. Outcomes/hypothesis/estimand

- **Primary H-W1** (H2 sub-study candidate): `Y_i`, time-weighted seasonal mean VWC (m³/m³) for fixed sentinel-specific root-zone depths `z_1...z_k`, defined by qualified soil scientist and known horizons; avoid averaging unweighted across depths with unlike profile thickness.
- Null `H0`: mean contrast `E[Y_i(S)-Y_i(C)] ≤ 0` when a directional superiority test is justified before freeze; otherwise `H0: difference = 0` (two-sided default). **No selection of sidedness from observed data.**
- Primary estimand: `ITT` treatment assignment effect on water-content season-average for the predefined set of eligible plots at this site and season, adjusted for baseline and prespecified blocking; does not extrapolate to all Mediterranean farms.
- Primary scientific reporting: signed contrast, effect in m³/m³, 95% CI or pre-specified interval, raw series, instrument uncertainty, exact unit n, all deviations. Scientific significance or decision relevance requires an advance-registered minimally meaningful effect (MDE) and variance/precision assumptions not yet available. A positive estimated effect alone does not establish general superiority.
- **Secondary/diagnostic endpoints:** infiltration rate (mm/h, P1.3D owned protocol, if harmonised); gravimetric soil water/quality check; plant growth/survival; area-weighted canopy interception or ground cover; PAR; ET0 and ET estimates with uncertainty; irrigation input (litres or mm/plot); rain (mm); soil temperature and EC; runoff/erosion only where measured; labour and yield at actual harvest. These are **not** confirmatory unless separately designed/powered/frozen.
- Soil salt accumulation and water quality are **non-compensable guardrails**, not simply positive outcome metrics. Increased VWC with poorer root function or harmful salinity is not an unqualified benefit.

### 3. Treatment and comparator definitions

`S`: approved multi-strata syntropic system with declared species guilds, plant spacing/age, pruning, biomass/mulch management, irrigation and site interventions documented per plot/version. `C`: credible simpler agroforestry management with same sentinel species/age class, ethically sufficient soil cover and irrigation, comparable starting soil/topography, distinguished syntropic interventions; no deliberate water deprivation. Treatment separation must be measured in light, root overlap, runoff, irrigation submains and spatial proximity. The historical P1.3D exposure tags apply: `T1` directly treated, `T2` indirect spillover, `C` eligible control. No arbitrary 'untouched' area assumed unaffected.

**Comparator eligibility gate (all required):** (C1) comparable parent material, depth and initial soil state; (C2) similar slope/aspect and baseline water regime; (C3) no hydrological, shade, root, irrigation or mulch contamination that materially changes the estimand; (C4) treatment-free with respect to selected hypothesized pathway, without unsafe or unethical neglect; (C5) long-term lawful access, maintenance and instrument placement. If any C criterion cannot be demonstrated, mark comparator `UNRESOLVED`. An external matched reference permits **association with confounding caveats**, not unqualified randomized causal claim.

### 4. Experimental design decision tree

A. If registered geometry supports multiple **independent** plot-level paired blocks with compatible irrigation, randomize `S/C` within each block by a third party; freeze randomization seed and sequence before implementation. Prevent topological runoff connections and root overlap via scientifically defined buffer. Do not treat 7 irrigation sectors as 7 independent n.

B. If only existing managed plots are available, conduct prospectively monitored matched observational contrasts and use pre/post differences or DiD only if relevant pretrends, common shock, no interference, stable measurement and parallel-trend assumptions are defensible.

C. If comparison/independence is impossible on ~3,360.87 m² boundary, run *single-site ecological process monitoring only* (water-balance, field baseline and instrumentation feasibility), publish observations without treatment efficacy claim. This is the conservative **default until spatial gate closes**.

Replication/power: no exact sample count; estimates from historical note are illustrative only. Field statistician must declare independent plot n, baseline/seasonal variance, within-plot temporal autocorrelation, block dependence, minimally meaningful VWC contrast, expected attrition and precision/power simulation. An exact confirmatory sample target is **HOLD**. Multiple daily sensors do not create biological replication.

### 5. Period and acquisition calendar — prospective only

- **Stage A (before intervention):** verify permissions, GIS registration/units, randomized unit map or observational status, raw soil and water source tests, install calibrated paired sensors and rain/flow meters; freeze methods/SOP and sensor IDs after domain review.
- **Stage B (baseline):** observe pre-intervention period that covers relevant soil dry-down and rain pulses; exact start/date and duration to freeze based on works and seasonal conditions. A purely after-works baseline is labelled `POST_INTERVENTION_REFERENCE` and cannot be called causal pre-treatment baseline.
- **Stage C (dry-season monitoring):** both arms measured on the same clock and sampling frequency, minimum candidate 15–60 minute VWC capture then pre-specified daily summaries; clock timezone (Europe/Rome and UTC), logging of rain and metered irrigation, incident and maintenance register.
- **Stage D (review):** blinded data QA where possible, statistician-specified model, independent review and registration of negative/null/positive results. Do not backdate preregistration or close historical H3/H4/H5 from a 12-month first pilot.

### 6. Ecohydrological mass-balance and site physics

For a clearly bounded plot/time interval, `P + I + Q_in = ET + Q_out + D + ΔS`, where P is rain, I measured irrigation, Q lateral flows, ET evapotranspiration, D drainage below measured root zone and ΔS change in storage. Record all fluxes in common `mm` over plot area. If drainage/groundwater flows are missing, label `PARTIAL_BALANCE` and do not force zero residual. Check sensor depth weighting against actual soil horizons. ET0 (FAO-56) is climate-derived reference; Kc and multi-layer evapotranspiration must be calibrated and cannot be transplanted blindly. No claim that wet soils necessarily mean higher plant-available water (waterlogging, shallow rooting, salinity).

### 7. Data dictionary / provenance minimum

Each stream: `observation_id`, `plot_id`, `treatment_assignment_or_observation_status`, `sensor_id`, `raw_data_ref`, `UTC_timestamp`, `local_time`, `measurement_method/version`, `depth_cm`, `unit`, `raw_value`, `calibration_history`, `water_source_and_EC`, `soil_horizon`, `rainfall_mm`, `irrigation_meter_volume`, `QA_flag`, `missingness_reason`, `intervention_version`, `spatial_coordinate_and_CRS`, `file_hash`, `method_hash`, `reviewer`, `consent/data_rights`. An unavailable sensor/meter ⇒ `UNKNOWN`, not zero. Rights and exact coordinates should be access-controlled.

QA candidate: all material provenance fields required for admissible review (100% for mandatory fields); target ≥90% scheduled daily pairwise observations usable per critical window is **engineering planning criterion** to review against observed weather/field constraints; failures lead to quality downgrades, not selective deletion. Independent calibration before/after study; co-located instrument agreement and gravimetric checks as feasible. Instrument failure logged at point, plot and interval levels.

### 8. Statistical analysis policy (to be frozen prospectively)

- Aggregate to plot × pre-specified daily/weekly window; **plots/blocks, not timestamps, determine sample size**.
- Randomized branch: estimate paired-block ITT difference, baseline-adjusted where appropriate; calculate uncertainty at randomization-unit level with methods feasible for actual block n (randomization/permutation or mixed models if justified), accounting temporal autocorrelation.
- Observational branch: if enough independent units and pretrends, baseline-adjusted contrast or DiD `Y_it = α_i + λ_t + β(S_i × post_t) + γ X_it + ε_it`, with plot effects and acknowledged identification assumptions. No claim from visually rising trends.
- Candidate prespecified covariates: pre-treatment VWC/soil texture/depth, soil EC, irrigation recorded mm, rainfall, pre-treatment slope/aspect/block, canopy/light baseline, known works history. Avoid adjusting away post-treatment mediators when estimating total package effect. Interaction with swale proximity exploratory.
- Primary interval reporting uses an exact pre-specified model chosen *before seeing outcome data*. All models show raw estimates, confidence intervals, sensitivity to missingness, weather and operator changes. Report comparison with noncausal baseline descriptive reference.
- One primary endpoint for H-W1; separate H1 infiltration analysis owns any other confirmatory endpoint; multiplicity across H1–H5 to be settled with scientific reviewer before statistical freeze. Secondary p-values exploratory/descriptive with appropriate interval and correction where repeated testing.
- Missingness: never silently interpolate, carry raw reasons; report complete-case and sensitivity analyses (plausible missing-not-at-random scenarios) selected before outcomes. Attrition and disconnected meters are not reason to censor failing plots from ITT.
- Decisions `SUPPORTED_FOR_DECLARED_CONTEXT`, `INCONCLUSIVE`, `CONTRADICTED`, `NOT_ESTIMABLE`, `SAFETY_HOLD`, decided by qualified reviewer; not automated by a p-value or AI confidence score.

### 9. Safety, ethics, rights and STOP

Stop/HOLD conditions: absent/expired lawful soil/water/sensor access, unsafe hydraulic works, erosion/runoff damage, salinity exceedance for relevant crops as later frozen with qualified agronomist, sensor/data provenance corruption, unacceptable ecological harm or adverse untreated plot conditions. Do not excavate/change swales or withdraw water based on this draft. The field steward/agronomist/hydrologist and competent owner/authority determine restoration/mitigation. A scientific design never creates access, soil disturbance or water rights.

### 10. Pre-registration freeze checklist, permissions and conflicts

| Gate | Current state | Required evidence and custodian |
|---|---|---|
| Field/title/water/operator right | HOLD | signed/current permissions and safety/water-use check by qualified owner/legal/engineer |
| Survey A8D actual georeference | HOLD | georeferenced EPSG/CRS, control points, surveyor signoff |
| Sector 5/7 polygons/swale length/spillover | HOLD | original design vector with closed boundaries, confirmed metres, reconciliation |
| Comparator C1–C5 + true plot units | HOLD | hydrology/soil reviewer validated C candidate, site/field map |
| Confirm H-W1 primary vs historic P1.3D infiltration | HOLD | named scientific reviewer written endpoint decision; preserve historic record |
| Depth/species/measurement SOP/calibration | HOLD | soil profiles, plant identity, devices and qualified field setup |
| Time window, variance, MDE, sample/power | HOLD | actual seasonal pilot variation and pre-data statistical simulation |
| QC, rights, COI, field budget, data governance | HOLD | signed independent review and custodian receipts |
| Named independent scientific reviewer | HOLD | acceptance, credential, COI and accountable decision |
| Prospective registration | NOT DONE | register/datestamp protocol before randomization/intervention/outcome inspection |
| REAL pipeline ingestion and official scientific result | HOLD | separately approved technical/scientific gate, no automatic program changes |

**Current decision:** `DRAFT_READY_FOR_REVIEW`; `REGISTERED=FALSE`, `FROZEN=FALSE`, `SITE_PHYSICALLY_VERIFIED=FALSE`; `CONFIRMATORY_INFERENCE=HOLD`; observation-only preparation within lawful existing authority possible after separate field clearance.

### 11. Historical coexistence / file references

Do not edit existing P1.3D/P1.3E/P1.3F, original H1–H5 endpoint matrix, or Canon. This H-W1 subprotocol references them and adds a candidate H2 question only. The first site paper may still adopt infiltration as the sole H2 primary endpoint if competent reviewers determine hydrology/geometry makes VWC treatment comparisons unreliable. That change must be made *prospectively*, with versioned record.
