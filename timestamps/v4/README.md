# v4 confirmed Bitcoin timestamps

Both release artifacts (PDF and source/complete-folder ZIP) have confirmed Bitcoin attestations in block **972137**, whose header records **2026-10-19T19:17:20+08:00**.

The `.ots` files in this directory are the completed proofs. `verification.json` records each original-file SHA-256 and the verified proof/header information. `status.json` replaces the earlier pending status. The immutable release may still contain its original pending proof bytes; use the completed copies here. The paper assets themselves are unchanged.

Original files: https://github.com/tqyqiqi1509/Hall-Polynomial-Conjecture/releases/tag/v4

To verify, download the matching original artifact and its `.ots` file. Use the official OpenTimestamps client or https://opentimestamps.org/. Our check validated the file digests and OTS operation paths, matched the Merkle roots, checked header hashes and proof of work, and compared headers from Blockstream and mempool.space; it did not use a local Bitcoin full node.

These proofs support existence of the exact committed bytes before the corresponding Bitcoin block. Block-header time is not an exact trusted wall-clock creation time. The proofs alone do not establish authorship, originality, mathematical correctness or a ruling on academic priority.
