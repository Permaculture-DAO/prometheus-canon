# ADR-CEREBRO-GEO-003 — environmental sources vs. territorial geospatial interpretation
**Date:** 2026-10-18
**Status:** PROPOSED / NON-ADOPTED / SHADOW

## Verified overlap
GitHub [prometheus-bridge Draft PR #11](https://github.com/Permaculture-DAO/prometheus-bridge/pull/11) includes `docs/US_LAND_INTELLIGENCE_GEO_INTEGRATION_v0_2.md`, `src/land_arcgis_shadow.mjs`, `src/land_intelligence_shadow.mjs`, and synthetic tests. This is the existing experimental **US Land Intelligence / Geospatial Intelligence Integration v0.2** lane: FEMA NFHL point screening, USGS EPQS elevation, public ArcGIS discovery/point query construction, GEE declarative manifest. Its adapters are not live production routes, and GEE manifest does not mean GEE analysis was run.

## Ownership boundary
1. **CEREBRO** owns the scientific source catalog, source-of-record product metadata, acquisition receipts for future licensed read-only EO/environmental jobs, unit/QA and scientific provenance annotations. Source discovery does not confer authority.
2. **Geospatial Intelligence v0.2 / RTC-OS** owns authoritative parcel identity, APN, county geofence/title/rights separation, overlays and territory-level determination. Official cadastral/recorded source supersedes commercial map pictures for parcel/rights claims.
3. **The existing runtime pipeline** owns real device/telemetry event contracts, gated technical ingestion and evidence batch packaging; new CEREBRO external adapters must not bypass S3–S6.
4. **Evidence Spine/MRV** owns scientific and governance evidence states, independent QA/admissibility review, provenance and controlled Claims Register downstream gates. CEREBRO never validates its own outputs as a sovereign scientific authority.
5. **Planetary Health/PHI and risk/finance** remain downstream approved methods and competent human authorities; report-level global boundary values are not local parcel-level measurements.

## Joining without double counting
- Define canonical product keys based on provider + dataset/product ID + source scene/observation ID + processing version + UTC temporal range + CRS/geometry reference.
- Record different viewer URLs (Copernicus Browser, EOS LandViewer, Esri) as presentations of the upstream asset, not three independent observations.
- For iNaturalist -> GBIF mirror events preserve the original occurrence ID, recorded taxonomic status and positional uncertainty, with appropriate sensitive-species protections.
- Reject silent transformations across PAR/FAPAR/LAI; source units, radiation definitions, footprint, uncertainty and model class are material.
- For parcels: `jurisdiction + county + official parcel/APN + recorded geometry source + effective date`; never infer title from satellite clusters or programmatic point overlays.
- All material derived indicators keep `input_hashes[], method_hash, calibration_state, reviewer, missingness_state, source_version`.

## Scientific and legal negative tests
Missing licence; obsolete endpoint; two browsers wrapping one Sentinel scene; mismatched coordinate order/CRS; APN parcel overlay mismatch; unknown satellite cloud mask; sampling bias; historical PHC control variables inserted as new year measurements; protected species/archaeology disclosure; fake calibrated sensor; ESG calculation conflict; unwanted agent-generated write requests. All must yield REVIEW/HOLD or typed failure and not auto-admission.

## Adoption
This decision is a **candidate ADR**, not a Canon amendment or data-engineering deployment. The signed Genesis v1.1.2 remains the governing source. Source Root PR #18, RTC-OS, CEREBRO and land source proposals remain separate reviewed artifacts. No merges or production write permissions are granted by this ADR.
