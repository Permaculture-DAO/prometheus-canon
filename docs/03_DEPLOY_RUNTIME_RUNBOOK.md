# Deploy Runtime Runbook — RC2 Strict

The RC2 canonical package is not a runtime deploy by itself. It is the canonical documentation source that runtime repositories must obey.

## Runtime repos

- `prometheus-happ`
- `prometheus-bridge`
- `prometheus-console`
- `prometheus-ops-docs`
- `prometheus-evaluation-stack`
- `prometheus-pilot-handoff-pack`
- `prometheus-canonicals`
- `prometheus-mock-backend`

## Order

1. Merge canonical repository RC2.
2. Apply each repo overlay.
3. Run repo-specific tests.
4. Verify that no runtime repo redefines PRU, TRBK, HoloFuel, OHE or RAP.
5. Deploy only bounded pilot runtime.
