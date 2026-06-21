# Decision F8 — Boundary repos: defer with retire/simplify trigger

- **Type:** governance decision under **Architecture Self-Falsifiability** (WP v1.1.2
  §V.x; amendment line). Ordinary (not Eternity) — sociocratic consent + public,
  versioned, dated record. **Status:** RECORDED (proposed, pending steward consent).
- **Date:** 2026-06-20. **Decision owner:** constitutional tier.

## Subject
`prometheus-bridge` and `prometheus-evaluation-stack` are **empty boundary repos**:
- `prometheus-bridge/src/index.mjs` is a 16-line staging placeholder.
- `prometheus-evaluation-stack` is a README-only stub.

The implementing function currently lives in `prometheus-happ`:
- real bridge = `happ/bridge/server.mjs` (Express → Holochain admin/app ports);
- real evaluation = the Benchmark Intelligence Layer in `happ`
  (`schemas/benchmark-intelligence/evaluation_receipt.schema.json`, PRE/PJE/NBE).

## Trigger reading (WP §V.x table)
| Trigger | Holds now? | Note |
|---|---|---|
| T-a Adoption (no external adopter) | n/a | pre-pilot; not yet assessable |
| T-b Capacity (binds nothing in practice) | **yes** | the empty repos bind nothing; happ does the work |
| T-d No-advantage vs lightweight effort | **yes** | happ-internal bridge/eval shows no disadvantage vs separate repos today |
| T-c Crowd-out | no | not observed |

Two triggers hold (T-b, T-d) → the canon would direct **simplify/retire**. Attenuation:
this is a *timing* judgement — distinct facade/QA repos have a legitimate
separation-of-concerns rationale in production, not yet in pre-pilot.

## Decision
**DEFER with an explicit retire-or-populate trigger** (the canon's "provisionally
adopted, with retire/simplify trigger" stance), NOT silent drift and NOT premature
population:
1. Both repos are marked, in-repo, as **boundary placeholders** whose implementation
   currently lives in `prometheus-happ` (done in this change).
2. **Review trigger:** at Genesis Pilot start OR first independent architecture
   review, whichever is first. At that review, if T-b and T-d still hold, **retire**
   (archive like `legacy-*`); if a real cross-repo need has appeared, **populate**
   by extracting the implementation from `happ`.
3. No CI or scaffolding is added to these repos until populated (adding it now would
   be the over-engineering the canon warns against).

## Trigger event — UPDATE 2026-06-21
The **populate** branch of the trigger fired for **`prometheus-bridge`**: a real
cross-repo deployment need appeared — the public API at
**`api.heart-intelligence.earth`**. Per the decision, the bridge has been
**populated** (bounded, read-only HTTP API; displays-never-decides; status +
canon-derived Claims Register with status; bridge policy + audit trail; CI added).
- `prometheus-bridge` → **POPULATED** (no longer a placeholder).
- `prometheus-evaluation-stack` → **still DEFERRED** (no deployment need yet; the
  evaluation layer remains in `happ`). Same trigger stands.

## Net-additions ledger
| Added | Offsetting deletion / justification |
|---|---|
| This decision record + in-repo placeholder markers | Justification: closes audit flag F8; prevents drift; no new capability; smallest action that resolves the trigger reading |
| Bridge populated (API) on trigger | Justification: real deployment need (public API); the canon's "populate" branch, not premature complexity |
