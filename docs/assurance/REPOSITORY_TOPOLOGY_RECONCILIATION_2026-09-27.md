# PROMETHEUS Repository Topology Reconciliation Gate

Status: assurance candidate; non-canonical until reviewed and adopted.
Date: 2026-09-27

## Decision purpose

Prevent repository consolidation, renaming, archival, or responsibility migration from silently changing the Genesis implementation boundary or losing active work.

## Current finding

Collision discovery is POSITIVE. Active Genesis responsibilities exist outside the proposed `prometheus-ui` / `prometheus-ops` consolidation, including at minimum:

- `prometheus-console`
- `prometheus-ops-docs`
- `prometheus-bridge`
- `prometheus-evaluation-stack`
- `prometheus-pilot-handoff-pack`
- `prometheus-mock-backend`
- `prometheus-happ`
- `prometheus-runtime`
- `prometheus-canon`

Therefore `prometheus-ui` and `prometheus-ops` remain candidate target names only. They MUST NOT be treated as authoritative topology until a migration/retention decision is approved.

## Required source-to-destination matrix

For every active repository record:

1. current repository and owner;
2. current authoritative responsibilities;
3. runtime/API/data interfaces;
4. active tests and workflows;
5. canonical or claim-boundary dependencies;
6. proposed destination, or explicit RETAIN decision;
7. migration method and rollback path;
8. no-loss verification evidence;
9. archive/deprecation status, if applicable;
10. approval record.

## No-loss gate

A repository MAY NOT be archived, renamed, replaced, or have its authoritative responsibility moved unless all of the following are true:

- every active responsibility has an explicit destination or RETAIN decision;
- tests and CI responsibilities are preserved;
- runtime routes/interfaces are mapped;
- operational runbooks are preserved;
- canonical and scientific claim boundaries are unchanged or separately change-controlled;
- rollback is documented;
- the destination passes equivalent or stronger verification;
- the Release/Gate review records approval.

## Current bounded architecture

Until reconciliation is complete, existing repositories remain authoritative for the responsibilities they currently implement. No document may infer implementation merely from the candidate topology.

## Holochain compatibility dependency

Topology reconciliation MUST NOT be coupled silently to a Holochain major/minor-line migration. The current Genesis deployment line remains pinned to Holochain/hc 0.6.1 until a separate compatibility decision authorizes otherwise.

## Claim boundary

Repository consolidation is engineering governance. It does not establish production readiness, scientific validation, field validation, certification, ecological outcome, legal admission, token rights, market rights, or financial value.
