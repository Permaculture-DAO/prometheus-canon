# PROMETHEUS — TERRA Intelligence | US Real Estate Evidence Adapter
Candidate application profile v0.1.0-rc.1 · 2026-11-24

Status: PROPOSED / SYNTHETIC_ONLY / NON-CANONICAL / NON-OFFERING
Candidate ID: TERRA-US-APP-001 (not registered)
Governing canon: signed Genesis v1.1.2-genesis; runtime internal v7.0.x mapped, not merged.
No change to signed releases, active Source Registry, Claims Register, production gates or canonical definitions.

## ADR: Extend, do not replace
TERRA is a scoped property-data adapter and review dossier capability, not a new global architecture, land registry, broker, legal adviser, title certifier or investment engine.
The project-attached PRM-ARCH-DET-002@2.0, PRM-CIV-APP-006@6.2, Aeterna/Ravel 1.1, RTC-OS and FLGA RC1/RC2 are design inputs subject to source-admission and lineage reconciliation. Their attachment does not establish active signed authority. The legacy root manifest path was not accessible on main at the inspected path; resolve authoritative versions and hashes before promotion.

Reuse the runtime S3 contract -> S4 gated adapter -> S5 normalization/QA -> S6 evidence-reference batch. Keep Holochain provenance only and the bridge read-only. No real GIS M7.3 path, production intake, independent-assurance or capital gate is opened by this candidate.

## RC1 implemented target
A dependency-free offline synthetic record normalizer and conflict-preserving report; strict TEST-only scope; exact jurisdiction/APN matching; decimal units; separate asking and recorded sale observations; source evidence hashes; deterministic replay. No network, DB, scheduler, credentials or real property collection.
Output states are TEST / HOLD only; all rights, title, legal, environmental, data-use and production admission remain UNKNOWN. A hash identifies canonical JSON bytes, not factual truth.
All source identifiers and jurisdiction codes in fixtures are synthetic or labels for testing; no real parcel or person is represented.

## Target integration (not yet implemented)
- Source registry: per dataset/field jurisdiction, authority, licence, acquisition/retention rights, cost, quota, freshness, adapter version, upstream hash.
- Acquisition: official assessor/recorder/permit/GIS datasets, FEMA, USGS, USDA, USFWS; PRYCD/TERRA AI, Firecrawl, MCP, authorised APIs/exports only after permission and source-specific tests.
- Normalisation: APN as string, local APN rules, county/state code consistency, listing vs sale vs assessed value, parcel splits/merges, bitemporal observations, conflicts preserved. Fuzzy matches are review candidates.
- Geospatial: geometry/CRS/version/accuracy, spatial joins only as screening, no survey/title or wetland determination.
- Legal/administrative: applicable effective law and competent office; issue records, reviewer and missing evidence. No autonomous legal conclusion.
- Aeterna/Ravel: use the existing risk objects and separate loss-generation/allocation ledgers in SHADOW; unknown is not zero; no valuation/underwriting claim.
- Canonical gates: keep runtime G0–G7, P1–P4 and T1 definitions unchanged; map local evidence checks via a reviewed ADR, never use a score to bypass hard gates.
- Existing workstreams BIGFOOT, FLOIE and FL-LAND: reconcile authorized evidence with stable identities and preserve historical HOLD; no real-data ingestion in RC1.
- Privacy: no skip tracing, personal-contact harvesting, targeting by protected traits, private-owner profiling or unrestricted social scraping. No personal information in distributed immutable storage.
- Authority: source-specific licence, read-only permissions, zero incremental spend, competent human review, no property offers, purchases, external contacts, financing or contracts.
- Security: untrusted source text, no instruction execution, least privilege, no secrets in reports, bounded retries and kill switch.

## Acceptance and release
RC1: deterministic synthetic fixture replay; reject REAL mode, invalid APN/units/missing provenance; preserve conflicts; no claim upgrade.
RC2: independently review source registry, compare against simpler manual workflow, align contracts with existing S3/S4/S5/S6 interfaces, test compatibility and negative cases.
Staging: separate authorization, approved data rights and isolation; review schema, lineage, risk and CI; no production changes by default.
Production: competent governance decision, pinned release, independent security/QA, rollback, source admission, documented deploy receipt. No live ingestion before all applicable gates pass.

State: DESIGN_GO / SYNTHETIC_BUILD / HOLD_REAL / HOLD_PRODUCTION / NO_CAPITAL_AUTHORITY.
