# Founder Mirror Sync Note (DRAFT, Phase 7) — document, do NOT execute

> How `Uwohali/hearth-prometheus-whitepaper` (founder publication mirror) is synced
> from the canon — and why it must NOT be synced before a signed freeze. The mirror
> never supersedes `prometheus-canon` unless explicitly synced via the signed
> canonical release process (WORKSPACE_MANIFEST).

## Current state (do not sync yet)
- Canon is at WP **v1.1.2 corpus**, `NO_GPG_SIGNATURES_YET` (staging).
- The mirror still references **WP v1.0.2** (also referenced staleley in
  `happ/CONTRIBUTING.md`, flag F10).
- The `prometheus-canonicals` April freezes are **superseded** by v1.1.2.

## Why not before freeze
Publishing the mirror now would propagate an unsigned, pre-freeze canon as if
public/authoritative, and would bypass custody (no signed release, amendments
A-001/A-002 not yet incorporated). The mirror is a publication of a signed state,
not a working copy.

## Sync procedure (only after a signed canonical release)
1. Text freeze of `prometheus-canon`; incorporate amendments A-001 + A-002 into the
   source DOCX; re-derive md (pandoc) + strict provenance md; recompute hashes.
2. QA + canonical boundary review; reconcile against superseded April canonicals.
3. **Maintainer** generates SHA256 + GPG signatures (the human's action) and a
   signed GitHub release; record version/date/hash + migration note in CHANGELOG.
4. Freeze that exact signed set into `prometheus-canonicals/releases/<date>/`.
5. Sync the mirror FROM the signed release only (matching hashes); update the
   mirror's WP version reference (retire v1.0.2); fix `happ/CONTRIBUTING.md` (F10).
6. Verify mirror artifacts hash-match the signed canon; no independent edits.

## Invariant
The mirror is downstream of a signed canon, never a source. No sync without a
signature; no signature without QA + freeze; signing is the maintainer's action.
