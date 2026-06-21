# Changelog — prometheus-canon

All notable changes to the canonical White Paper. Versioned and hashed
(canon-amendment & custody discipline). GPG signing deferred until text freeze +
QA (`NO_GPG_SIGNATURES_YET`).

## [v1.1.2-genesis] — FREEZE-PREP COMPLETE, PENDING SIGNATURE (2026-06-21)
Freeze-prep for the first signed Genesis release. Internally reconciled and ready
for the maintainer to sign (key `8C8CB0D48C7F60DA`).
- RELEASE_NOTES reconciled to v1.1.2 Full Corpus (was rc.2-strict).
- `NO_GPG_SIGNATURES_YET.md` removed → `RELEASE_SIGNING_READINESS.md`.
- `RELEASE_MANIFEST.md` added (artifact SHA256: WP docx `29f91e6d…ca04`, WP md
  `f3862005…f9540`; bundles happ `3d331955…f831`, webhapp `82a6004d…9ae8`,
  dna `3ee84acb…a8f8`).
- Amendments A-001/A-002 included as versioned clauses; body-incorporation → v1.1.3.
- Disclosure: substantially single-source, single-authority signature.
- Not yet signed; signing is the maintainer's action.

## [amendment A-002] — UNRELEASED (2026-06-20, pending ratification)
- `canonical/AMENDMENTS/A-002_consolidated_legal_semantic_firewall.md` — consolidates
  the 15 master-prompt firewall terms (PRU, RAP, TRBK, HoloFuel, token, governance
  right, investor exposure, land/cash-flow right, ecological claim, verified
  indicator, admissible value, research-only, financial instrument, compliant
  wrapper) into one `term → definition → forbidden interpretation` table. Consolidates
  existing WP v1.1.2 content (X.1/X.2/X.3, §13.16.2); introduces no new meaning.
  Incorporate into the source DOCX at next freeze, then re-derive.

## [v1.1.2-corpus-import] — UNRELEASED (staged 2026-06-20, pending Gate 2 + freeze)

**Change:** the canonical White Paper of record was replaced by the v3.1-complete
**Full Corpus** (v1.1.2). The previous `v1.1.0-rc.2-strict` lineage (pre-disciplines)
was preserved, not deleted.

**Source of record (DOCX):** `PROMETHEUS_Canonical_White_Paper_Full_Corpus.docx`
- SHA256 `29f91e6d6a31fb8bd9754a7ef32ea8b7f168bf64fa7097cf9b6ee951ab9fca04`

**New canonical files:**
- `canonical/h-earth-prometheus-white-paper.docx` — SHA256 `29f91e6d6a31fb8bd9754a7ef32ea8b7f168bf64fa7097cf9b6ee951ab9fca04` (byte-identical to source corpus) — **source of truth**
- `canonical/h-earth-prometheus-white-paper.md` — SHA256 `9d5ebd7ad7aaff39d5b8a800e9d45dc98ddce63d9f92b9b658d2cbdadf3f2da9` (59,343 lines; readable derivation via pandoc 3.10 `docx → gfm --wrap=none`)
- `canonical/corpus_media/` — media extracted from the corpus

**Reproducible provenance derivation (parity with prior releases):**
- `provenance/v1.1.2/h-earth-prometheus-white-paper.strict.md` — SHA256 `aa153e1e8eb8ba4b645fc010872ffaf0cc1cba4b587c371f7d21483f03588da5` (35,015 lines, 598 tables; derived from the canonical DOCX via `scripts/extract_wp_markdown_strict.py`, python-docx 1.2.0, table-complete)

**Canon amendments (proposed, pending ratification):**
- `canonical/AMENDMENTS/A-001_HSI_human_state_binding.md` — binds the happ Human State Interface (HSI) under the existing human-state weight=0 invariant (closes audit flag F9).

**Superseded (preserved under `canonical/_superseded_rc2_strict/`):**
- `h-earth-prometheus-white-paper.rc2-strict.md` — SHA256 `00d9bc173bad2f9008b6b030ab244361b7d4bcd8a3ee700f81e626c04f50a472`
- `h-earth-prometheus-white-paper.rc2-strict.docx`

**Why:** the rc.2-strict WP contained none of the v3.1 apparatus (Canon Amendment &
Custody, Architecture Self-Falsifiability, Anti-Overproduction, Howey,
lowest-gate). The Full Corpus already contains all of it plus MiCA, human-state
weight=0, Legal Semantic Firewall, three-layer token architecture, Red-Team /
Capital-Readiness / Scientific-Falsifiability matrices, Hypothesis–Evidence
mapping, Jacobi/Lancet anchor, Audit Readiness Note. See
`../PHASE2_GAPAUDIT_REPORT.md`.

**Open before freeze:**
- ~~Name the HSI explicitly under human-state weight=0~~ → done: amendment A-001 (pending ratification).
- ~~Reproducibility parity strict re-derive~~ → done: `provenance/v1.1.2/…strict.md`.
- Incorporate amendment A-001 into the source DOCX at freeze, then re-derive.
- Reconcile signing state with `prometheus-canonicals` April freezes (superseded).
- GPG signing remains the maintainer's action, after QA.
