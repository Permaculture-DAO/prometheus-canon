# TERRA-US-APP-001 — RC3 connector/reconciliation delta
Status: PROPOSED / TEST_ONLY / HOLD_REAL / HOLD_PRODUCTION.
Extends RC1/RC2 proposals; no signed Canon or active registry modification.

## ADR — reuse land underwriting shadow
Inspected existing runtime branch feat/land-underwriting-reconciled-20261017, app/land_underwriting.py blob 097dda6f39431a6f32df22a11625963db184584d and docs/LAND_UNDERWRITING_SHADOW_INTEGRATION.md blob 785c5be95e9052d5b35167bd0a3ac5ef978aa39c. The candidate land-underwriting-shadow/v2 evaluates caller-declared gate integrity for rights, land_use, environment, water and data; it cannot authenticate evidence, reviewers or source facts, and land_value is always null. Candidate branch presence does not establish active admission.
TERRA owns source acquisition contracts and evidence reconciliation; existing shadow engine owns bounded gate diagnostics. No merge or duplication of underwriting engine. No automatic TERRA-to-admissible evidence conversion.

## RC3 implemented candidate
Runtime PR #40 head d8ac6ef5630dfb823462bf4d44e842adb831b5b6: terra_connector.py, test_terra_connector.py, terra.connector.envelope.schema.json, TERRA_RC3_CONNECTOR_RECONCILIATION.md.
Offline fixture-only connector, same-source/scope snapshot deltas, exact hash dedup across three workstream labels, conflict and caller-declared freshness flags. No disappearance-to-sale inference. All outputs HOLD/non-authoritative. No external connection, real archive import, paid request or scheduled job. Tests authored; execution receipts separate.

## Remaining
WP01 full authority/source admission; WP04 provider-specific permissions, costs, coverage and connector clients; WP05 actual archive reconciliation; WP06 claim/context mapping; WP07 GIS real path HOLD; WP08 reviewed shadow interoperability; WP09 read-only interface; WP10 independent review and release. Desktop Commander quota previously reported 97%; prefer GitHub checks, no incremental spend.
