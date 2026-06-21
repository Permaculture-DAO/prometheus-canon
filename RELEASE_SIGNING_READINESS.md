# Release Signing Readiness — v1.1.2-genesis

Supersedes `NO_GPG_SIGNATURES_YET.md`. The freeze-prep is complete; the release is
**ready to sign**. Signing is the **maintainer's action** (authorized key
`8C8CB0D48C7F60DA`); the agent prepares and verifies but never signs.

## Freeze-prep done
- [x] White Paper of record reconciled to v1.1.2 Full Corpus (RELEASE_NOTES).
- [x] rc.2-strict lineage preserved + migration note.
- [x] Amendments A-001/A-002 present as versioned clauses; disclosure recorded.
- [x] Custody disclosure (substantially single-source) recorded.
- [x] CHANGELOG release entry + RELEASE_MANIFEST with hashes.
- [x] gap-audit passed (master-prompt v3.1).

## Signing procedure (maintainer, PowerShell — Windows + Gpg4win)
1. Add the public key to GitHub once (Settings → SSH and GPG keys):
   `& 'C:\Program Files\GnuPG\bin\gpg.exe' --armor --export 8C8CB0D48C7F60DA | Set-Clipboard`
2. Configure git signing:
   `git config --global gpg.program 'C:\Program Files\GnuPG\bin\gpg.exe'`
   `git config --global user.signingkey 8C8CB0D48C7F60DA`
   `git config --global tag.gpgsign true`
3. Sign every canon file (detached `.asc`), from the canon repo root:
   ```powershell
   $gpg='C:\Program Files\GnuPG\bin\gpg.exe'; $k='8C8CB0D48C7F60DA'
   Get-ChildItem -Recurse -File | ? { $_.Extension -ne '.asc' -and $_.FullName -notmatch '\\\.git\\' } |
     % { & $gpg --armor --detach-sign --local-user $k $_.FullName }
   ```
4. Tag the signed release: `git tag -s v1.1.2-genesis -m "h-eart-h Prometheus — Genesis v1.1.2 (signed)"; git push origin v1.1.2-genesis`
5. Freeze the signed set into `prometheus-canonicals/releases/<YYYY-MM-DD>/`.

## Holochain bundles (signed for distribution, not committed)
From `prometheus-happ`:
```powershell
& $gpg --armor --detach-sign --local-user $k hearth_prometheus.happ
& $gpg --armor --detach-sign --local-user $k hearth_prometheus_web.webhapp
& $gpg --armor --detach-sign --local-user $k dnas\hearth\hearth.dna
```
Publish bundle + `.asc` + SHA256 (see RELEASE_MANIFEST). Verify:
`& $gpg --verify hearth_prometheus.happ.asc hearth_prometheus.happ`.

> No `.asc` is canonical unless generated after this QA/freeze and signed with the
> authorized key. Past git commits are not retroactively signed (no history rewrite).
