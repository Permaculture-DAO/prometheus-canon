# Repository topology decision candidate — Sprint 0

Status: candidate; requires authorized review.

## Proposed consolidated implementation topology

- `prometheus-canon`: canonical documentation and controlling definitions;
- `prometheus-canonical-releases`: immutable release registry and verification;
- `prometheus-happ`: Holochain DNA, zomes and hApp package;
- `prometheus-runtime`: ingestion, normalization, QA and evidence batch packaging;
- `prometheus-ui`: bounded operator UI and web-hApp frontend;
- `prometheus-ops`: deployment, observability, backup, restore, incident and release operations;
- `.github`: organization-wide governance and workflow templates.

## Collision rule

Before adopting this topology, the organization must determine whether private repositories named `prometheus-console`, `prometheus-ops-docs`, `prometheus-bridge`, `prometheus-evaluation-stack`, `prometheus-pilot-handoff-pack`, or `prometheus-mock-backend` contain active Genesis work.

No repository may be silently replaced, abandoned or promoted. Migration requires a recorded source/destination map, owner, tests, archive status and deprecation notice.
