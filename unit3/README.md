Great. I will prepare detailed notes for your Bachelor of Information Technology exam under TU on Unit 3: Message Authentication. This will include explanations in paragraph and bullet formats, relevant examples, summaries with mnemonics for memorization, and comparison tables where useful. I’ll let you know as soon as it’s ready.

# Unit 3: Message Authentication (6 Hrs)

## 3.1 Message Authentication

Message authentication ensures that a message is from the claimed sender and has not been altered in transit. In other words, the receiver can verify both the integrity (no tampering) and the origin (authentic sender) of the data. This is usually done by attaching a small authentication tag or code to the message. For example, in a secure communication between Alice and Bob, Alice can compute a **Message Authentication Code (MAC)** on her message using a shared secret key. Bob recomputes the MAC on receipt and checks it against the tag; if they match, Bob knows the message is genuine and unchanged.

- **Key Properties:** Verifies data integrity (no changes) and origin authentication (correct sender).
- **Techniques:** Commonly done with a secret-key _MAC_ or with asymmetric _digital signatures_.
- **MAC (Message Authentication Code):** A short tag computed from the message and a secret key. Both sender and receiver share the key. The receiver recomputes the MAC to check integrity.
- **Example:** Alice sends a file to Bob with a MAC tag. Bob uses the same key to verify the MAC; if an eavesdropper had modified the file, the MAC check would fail.
- **Limitation:** MACs use a shared secret key, so they do not provide non-repudiation (the sender could later claim not to have sent it).

**Mnemonic:** _“MAC = Message Authenticator Code – Makes Authentic Content.”_

## 3.2 Secure Hash Functions

A **secure hash function** takes any input data (of any length) and produces a fixed-size output (the _hash_ or _digest_). The output looks like a random fingerprint of the input. Such functions are _one-way_: it’s computationally infeasible to reverse or find an input from its hash. They also satisfy **collision resistance**: it’s extremely hard to find two different inputs that give the same hash. A key feature is the _avalanche effect_: even a tiny change in input (e.g. flipping 1 bit) causes a completely different hash. This makes it easy to detect any data tampering. For example, a hash of a downloaded file can be compared to the expected hash to check the file wasn’t corrupted or altered.

- **Fixed-size output:** Maps data of any length to a fixed-length digest (e.g. 256 bits).
- **One-way:** Hard to invert; knowing the hash does not reveal the original data.
- **Collision-resistant:** Hard to find two inputs with the same hash.
- **Avalanche effect:** Small input changes produce large, unpredictable hash changes.
- **Uses:** Verifying data integrity (e.g. checksums), password hashing, digital signatures, and building MACs or address identifiers. For example, storing a file’s hash allows later checking that the file wasn’t altered.
- **Note:** A secure hash is not encrypted data; it can be shared openly. Its security lies in its mathematical properties (preimage resistance, collision resistance, etc.).

**Mnemonic:** _“HASH = Hashed Always Secures (and highlights) changes.”_

## 3.3 Message Digests: MD5

**MD5 (Message-Digest Algorithm 5)** is a well-known hash function that produces a 128-bit (16-byte) digest. It was designed by Ronald Rivest in 1991. For each message, MD5 outputs a 128-bit hash; even a slight change in the message yields a very different hash. MD5 was widely used for file checksums and passwords. However, MD5 is now **considered broken**: practical collision attacks exist, meaning two different inputs can be made to produce the same MD5 hash in very little time. In fact, by 2008 researchers declared MD5 “cryptographically broken and unsuitable”. Today MD5 should **not** be used for security purposes like digital signatures; it remains only for legacy or non-security uses (for example, quick file partitioning where collision risk is acceptable).

- **Digest size:** 128 bits (16 bytes).
- **Design:** Created by Rivest (MIT) in 1991 as an improvement over MD4.
- **Speed:** Fast to compute (uses 512-bit blocks internally).
- **Security:** _Insecure._ Collisions can be found quickly. Attacks demonstrated by 2004 show MD5 hashes can be collided in seconds on a normal computer. The Flame malware (2012) even exploited MD5 collisions for a fake security certificate.
- **Use cases (historical):** Common for file integrity checks (e.g. comparing MD5 sums after download). Not safe for any cryptographic integrity/authentication.
- **Summary:** MD5 = legacy hash; small size (128-bit) with **known vulnerabilities**.

| **Feature**          | **MD5**                      | **SHA-1**                   |
| -------------------- | ---------------------------- | --------------------------- |
| Digest length        | 128 bits                     | 160 bits                    |
| Designed by/year     | Rivest, 1991                 | NSA, 1995                   |
| Internal block size  | 512 bits                     | 512 bits                    |
| Security status      | Broken: collisions known     | Broken: collisions found    |
| Typical use (legacy) | Checksums, non-secure hashes | Older SSL/TLS, Git (legacy) |

**Example:** A download site may publish an MD5 checksum so users can verify file integrity. (However, a hostile attacker could spoof both file and MD5 if they wanted to cheat, which is why MD5 is not trusted for security.)

**Mnemonic:** _“MD5 – Many Defects (5 words long!), now Don’t secure.”_

## 3.4 Secure Hash Algorithms: SHA-1, SHA-2

**SHA-1:** The Secure Hash Algorithm 1 produces a 160-bit digest. It was designed by the NSA and published in 1995. SHA-1 improves on MD5 (longer hash, different structure), but it too is now insecure. In 2017 researchers demonstrated a practical collision on SHA-1 (two different files with the same SHA-1). NIST has banned SHA-1 for digital signatures and other security uses. In practice, SHA-1 is _deprecated_: browsers and protocols no longer accept SHA-1 certificates. (Some legacy systems still use it, but migration to SHA-2 is required.)

- **SHA-1 Details:** 160-bit output, uses 512-bit blocks, 80 rounds of mixing.
- **Collision attack:** Yes – broken. First public collision in 2017. Recommended to use SHA-2 or SHA-3 instead.
- **Use cases:** Earlier used in SSL certificates and version control (Git uses SHA-1 hashes for commits). No new applications should use SHA-1.

**SHA-2:** A family of hash functions (SHA-224, SHA-256, SHA-384, SHA-512) developed by NSA and standardized in 2001. The variants differ by output length: SHA-256 produces a 256-bit hash; SHA-512 produces a 512-bit hash; SHA-224 and SHA-384 are truncated versions of SHA-256 and SHA-512, respectively. SHA-2 functions are structurally similar (Merkle–Damgård design) and are currently considered secure (no practical collisions). For example, SHA-256 is widely used in TLS certificates, blockchain (Bitcoin’s addresses use double SHA-256), and file integrity checks.

- **SHA-2 variants:** Output sizes 224, 256, 384, 512 bits. Block sizes: 512 bits (for 224/256) or 1024 bits (for 384/512). Rounds: 64 (for 224/256) or 80 (for 384/512).
- **Security:** No known collisions. Security roughly 128-bit for SHA-256, 256-bit for SHA-512 (due to birthday attack, collision resistance is about half the output length).
- **Adoption:** Widely used in cryptographic protocols and systems. Example: SHA-256 is used in digital certificate signatures and blockchain.

| **SHA-2 Variant** | **Digest (bits)** | **Block (bits)** | **Rounds** | **Collision Security (bits)** |
| ----------------- | ----------------- | ---------------- | ---------- | ----------------------------- |
| SHA-224           | 224               | 512              | 64         | \~112 (no known collision)    |
| SHA-256           | 256               | 512              | 64         | \~128 (no known collision)    |
| SHA-384           | 384               | 1024             | 80         | \~192 (no known collision)    |
| SHA-512           | 512               | 1024             | 80         | \~256 (no known collision)    |

**Comparison (MD5 vs SHA-1 vs SHA-2):**

| **Property**    | **MD5**                  | **SHA-1**                 | **SHA-256 (SHA-2)**             |
| --------------- | ------------------------ | ------------------------- | ------------------------------- |
| Digest size     | 128 bits                 | 160 bits                  | 256 bits                        |
| Security status | Broken (easy collisions) | Broken (collisions found) | Secure (no known collisions)    |
| Use case        | Legacy checksums         | Legacy SSL/Git            | Modern crypto (TLS, blockchain) |
| Recommendation  | _Do not use_             | _Do not use_              | _Use for security_              |

**Example:**

- _SHA-1:_ Never sign important data with SHA-1 today (e.g. Git is replacing SHA-1 hashes in new releases).
- _SHA-2:_ Web browsers and VPNs now require SHA-256 or better in digital certificates.

**Mnemonic:** _“SHA Family: Secure Hash Always – 1 (not strong), 2 (stronger and longer).”_

## 3.5 Digital Signature

A **digital signature** is a cryptographic way to “sign” data so that its authenticity and integrity can be verified by anyone. It relies on asymmetric (public-key) cryptography. The sender uses their private key to sign a message (usually by hashing the message and then encrypting the hash with the private key). The recipient uses the sender’s public key to verify the signature: they decrypt the signature with the public key and compare it to a freshly computed hash of the message. If they match, the recipient is confident the message came from the holder of the private key and was not altered. Digital signatures also provide **non-repudiation**: the signer cannot later deny sending the message, because only their private key could have created that signature.

- **Public-key method:** Uses a private key (to sign) and a public key (to verify). No shared secret is needed between sender and receiver.
- **How it works:** Compute a hash of the message, encrypt the hash with the signer’s private key (that encrypted hash is the signature). Receiver decrypts with public key and checks the hash.
- **Security:** Ensures **authenticity** (verifies sender’s identity) and **integrity** (message unchanged). Also provides non-repudiation.
- **Algorithms:** Common ones include RSA signatures, DSA (Digital Signature Algorithm), and ECDSA (elliptic-curve DSA).
- **Applications:** Signing software or documents, SSL/TLS certificates, blockchain transactions (signing transfers), secure email (PGP/GPG). For instance, when your web browser connects to https\://, the website’s certificate contains a digital signature from a trusted authority.
- **Example:** Alice signs a PDF invoice with her private key. Bob (or anyone) can verify Alice’s signature using her public key, proving it was really from Alice and not altered.

**Mnemonic:** _“SIG = Sender’s Identity Guaranteed – Signature Gives trust.”_

**Sources:** Standard cryptography references and industry glossaries have been used for definitions. Tables summarize common hash algorithms (MD5, SHA-1, SHA-2) and their key properties.
