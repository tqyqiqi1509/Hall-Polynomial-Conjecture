# v2 OpenTimestamps receipts

The exact PDF and complete paper-folder ZIP are included here alongside their `.ots` files. The ZIP contains all twelve files of the original paper folder, including its SHA-256 manifest; it excludes timestamp receipts to avoid a circular commitment.

The requests were accepted by OpenTimestamps calendars on 19 October 2026. `status.json` records the request/upgrade-check time, SHA-256 digests and proof status. At publication both proofs are **pending Bitcoin confirmation**. The recorded request time is a local observation, not a completed blockchain timestamp.

## Upgrade and verify

Keep the original files and `.ots` receipts. Once calendars have anchored the commitment, use the official OpenTimestamps client:

```
ots upgrade Hall-Polynomial-Conjecture-v2.pdf.ots
ots upgrade Hall-Polynomial-Conjecture-v2-complete.zip.ots
ots verify Hall-Polynomial-Conjecture-v2.pdf.ots
ots verify Hall-Polynomial-Conjecture-v2-complete.zip.ots
```

The included `timestamp.py` uses the installed `python-opentimestamps` library to request or upgrade receipts and compare the original-file digests. An attestation in that script's output still requires verification against the Bitcoin chain. Official client documentation: https://github.com/opentimestamps/opentimestamps-client . The browser verifier is https://opentimestamps.org/ .

An anchored proof supports existence of the exact committed bytes before the relevant block. It does not by itself establish authorship, originality, mathematical correctness, an exact creation time or a legal ruling on priority. Independent scholarly publication records can complement this evidence.

The published release assets are frozen. Upgrade a downloaded copy and preserve the original receipt; a later completed proof can be published as a separate supplementary record without changing the paper or frozen assets.
