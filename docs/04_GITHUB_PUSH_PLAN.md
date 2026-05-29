# GitHub Push Plan — RC2 Strict

## Preparation

```bash
cd /path/to/hearth-prometheus-whitepaper
git checkout main
git pull --ff-only
git checkout -b release/v1.1.0-rc.2-strict
```

## Apply overlay

```bash
PACK=/path/to/PROMETHEUS_V1_1_CANONICAL_RUNTIME_SYNC_PACK_RC2_STRICT_2026_05_29
cp -R "$PACK/repo_overlays/hearth-prometheus-whitepaper/"* .
cp "$PACK/RELEASE_MANIFEST.json" ./RELEASE_MANIFEST.json
cp "$PACK/SHA256_SUMS.txt" ./SHA256_SUMS.txt
cp -R "$PACK/scripts" ./scripts
```

## Verify

```bash
bash scripts/verify_release.sh
```

## Commit

```bash
git add .
git commit -m "docs: align Prometheus v1.1 RC2 strict canonical release"
git push -u origin release/v1.1.0-rc.2-strict
```
