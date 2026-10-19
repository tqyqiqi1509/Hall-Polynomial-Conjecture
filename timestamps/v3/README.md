# v3 OpenTimestamps proofs

These proofs commit to the exact v3 PDF and complete manuscript ZIP distributed as release assets. See `status.json` for the recorded state and SHA-256 hashes. The initial state is **pending Bitcoin confirmation**.

Download the two original release files into this directory before running `timestamp.py`; retain the exact original bytes. With the Python `opentimestamps` library installed, the script upgrades the saved proofs by querying their calendars. An attestation being present does not itself establish independent Bitcoin verification. Use the official OpenTimestamps client to upgrade and verify against Bitcoin, or the OpenTimestamps verification service at https://opentimestamps.org/.

The timestamp concerns the existence of these exact file bytes; it does not certify authorship, originality or mathematical correctness. Earlier versions remain separate.
