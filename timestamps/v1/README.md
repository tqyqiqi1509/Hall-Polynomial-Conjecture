# OpenTimestamps proofs for Hall Polynomial Conjecture v1

These proofs concern the exact PDF and source ZIP attached to:
https://github.com/tqyqiqi1509/Hall-Polynomial-Conjecture/releases/tag/v1

The files were not recompiled or edited for timestamping.

## Status

Both proofs have been upgraded with Bitcoin block attestations. The original digests and proof paths match the Merkle root of Bitcoin block 972025. Its header timestamp is 2026-10-19 00:39:43 +08:00 (Asia/Shanghai).
Verification used Blockstream public block-header data, not a local full Bitcoin node. See verification.json for details.

Keep each original file together with its corresponding .ots proof.
The SHA-256 file digests were checked against the frozen v1 release.

## Complete the proofs

Once calendars have anchored the commitments, use the official client:

    ots upgrade Hall-Polynomial-Conjecture-v1.pdf.ots
    ots upgrade Hall-Polynomial-Conjecture-v1-source.zip.ots

The included timestamp.py can also retrieve and merge calendar updates using the official Python OpenTimestamps library:

    python timestamp.py

It records whether a Bitcoin block-header attestation is present. It does not independently validate Bitcoin consensus or verify block inclusion against a Bitcoin node.

## Verify

    ots verify Hall-Polynomial-Conjecture-v1.pdf.ots
    ots verify Hall-Polynomial-Conjecture-v1-source.zip.ots

The official Python client requires access to Bitcoin Core for independent verification.
The OpenTimestamps website also provides a browser verification interface:
https://opentimestamps.org/

A Bitcoin timestamp supports existence of these exact bytes before the anchoring block.
It does not certify mathematical correctness, authorship, or academic priority.
