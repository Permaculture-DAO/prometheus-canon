# Release Manifest — v1.1.2-genesis

Release identity for signing. SHA256 of the primary artifacts (the full per-file
`SHA256_SUMS.txt` + detached `.asc` are generated at signing time — see
`RELEASE_SIGNING_READINESS.md`). Authorized key: `8C8CB0D48C7F60DA`.

## Canon (this repo)
| File | SHA256 |
|---|---|
| `canonical/h-earth-prometheus-white-paper.docx` (source of truth) | `29f91e6d6a31fb8bd9754a7ef32ea8b7f168bf64fa7097cf9b6ee951ab9fca04` |
| `canonical/h-earth-prometheus-white-paper.md` (pandoc derivation) | `f3862005bc4d6e8e4cba0f2a7646e67dff758fcd28c8411046eb5d04875f9540` |
| `canonical/AMENDMENTS/A-001_HSI_human_state_binding.md` | (signed at signing) |
| `canonical/AMENDMENTS/A-002_consolidated_legal_semantic_firewall.md` | (signed at signing) |

## Holochain runtime bundles (prometheus-happ — distributed, not in this repo)
| Bundle | SHA256 |
|---|---|
| `hearth_prometheus.happ` | `3d331955aba7070063fe3f65220d3b8faec4048439bff38e0518bdb17c85f831` |
| `hearth_prometheus_web.webhapp` | `82a6004db9950090527cd457f21b603728fcf827e222a3ae9e22cc83b0599ae8` |
| `dnas/hearth/hearth.dna` | `3ee84acbf689805bcf6c807568ec934932c9ee4c723155b37c379bb252d5a8f8` |

> Bundle hashes are recorded here for cross-repo provenance. The bundles are built
> artifacts (gitignored in `prometheus-happ`); they are published with their `.asc`
> at release, not committed.

## Scope
v1.1.2-genesis = corpus v1.1.2 + amendments A-001/A-002 (as clauses) + the runtime
bundles above. Custody: substantially single-source, single-authority signature
(see RELEASE_NOTES). Body-incorporation of amendments → v1.1.3.
