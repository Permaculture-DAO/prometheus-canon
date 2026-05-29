# No GPG Signatures Yet

This repository is currently in the Prometheus v1.1 Genesis Institutional Canonical Line staging phase.

Any `.sha256` files generated before final textual freeze are release-candidate or local staging integrity hashes only.

They are not final canonical signatures.

Final `SHA256_SUMS.txt`, individual `.sha256` files, detached `.asc` GPG signatures, and GitHub release assets must be regenerated only after:

1. final text review;
2. Markdown completeness confirmation;
3. repository-wide Markdown alignment;
4. explicit update or deprecation of stale documents;
5. textual freeze;
6. checksum regeneration;
7. local GPG signing with the authorized release key;
8. release manifest update;
9. GitHub release publication.

No `.asc` signature should be treated as canonical unless generated after QA approval and signed with the authorized release key.
