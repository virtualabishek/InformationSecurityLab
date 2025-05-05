### Key Points

- Research suggests Unit 2 of the BIT exam at Tribhuvan University covers classical and modern encryption methods, focusing on symmetric encryption algorithms.
- It seems likely that topics include substitution and transposition ciphers, symmetric encryption principles, DES, mathematical foundations (fields, modular arithmetic, Galois fields, polynomial arithmetic), and AES.
- The evidence leans toward these topics being essential for understanding how data is secured, with AES being the modern standard replacing DES.

### Classical Cryptosystems

Classical cryptosystems, like substitution and transposition ciphers, are early encryption methods. Substitution ciphers replace letters with others (e.g., Caesar cipher shifts letters by a fixed number), while transposition ciphers rearrange letters (e.g., Rail Fence cipher). These are simple but weak alone, often combined for better security.

### Symmetric Encryption

Symmetric encryption uses one key for both encryption and decryption, making it fast for large data but requiring secure key sharing. It’s widely used in systems like online banking.

### DES and AES

DES, a 1970s standard, encrypts 64-bit data blocks with a 56-bit key but is now insecure due to short key length. AES, adopted in 2001, uses 128, 192, or 256-bit keys, encrypting 128-bit blocks, and is highly secure for modern applications.

### Mathematical Foundations

Fields, modular arithmetic, Galois fields, and polynomial arithmetic provide the math behind encryption. Modular arithmetic ensures operations stay within a set range, while Galois fields (used in AES) enable secure computations.

For more details, see the comprehensive notes below.

---

# Unit 2: Symmetric and Asymmetric Encryption Algorithms (10 Hrs.)

This document provides detailed notes for Unit 2 of the BIT exam at Tribhuvan University, specifically for the Information Security course (BIT 303, Semester 5). The notes cover classical cryptosystems, symmetric encryption principles, Data Encryption Standard (DES), mathematical foundations (fields, modular arithmetic, Galois fields, polynomial arithmetic), and Advanced Encryption Standard (AES). These notes are designed for exam preparation, offering clear explanations, examples, and key points for memorization.

## Background and Context

The Bachelor of Information Technology (BIT) program at Tribhuvan University is a four-year, eight-semester course that includes Information Security in Semester 5. Unit 2 focuses on encryption algorithms, emphasizing symmetric methods, which are critical for securing data in modern systems. The notes are compiled from standard cryptographic resources and align with the TU syllabus.

## Detailed Notes by Subtopic

### 2.1. Classical Cryptosystems: Substitution and Transposition Ciphers

Classical cryptosystems are early encryption methods that laid the groundwork for modern cryptography. They are categorized into substitution and transposition ciphers, often combined for enhanced security.

#### Substitution Ciphers

1. **Definition**: Each unit of plaintext (e.g., a letter) is replaced by another unit (e.g., a different letter or symbol) to form the ciphertext.
2. **Types**:
   - **Monoalphabetic Substitution**: Uses a single substitution alphabet throughout the message.
     - Example: **Caesar Cipher** shifts each letter by a fixed number (e.g., shift of 3: A → D, B → E). For "WIKIPEDIA", the ciphertext is "ZLNLSHGLD".
     - Example: **Atbash Cipher** reverses the alphabet (A ↔ Z, B ↔ Y).
   - **Polyalphabetic Substitution**: Uses multiple substitution alphabets, switching based on a keyword or pattern.
     - Example: **Vigenère Cipher** uses a keyword to determine shifts for each letter.
3. **Historical Use**: Employed by figures like Mary, Queen of Scots (1578–1584) and in World War I ciphers like ADFGVX.
4. **Security**: Monoalphabetic ciphers are vulnerable to frequency analysis (e.g., E is the most common letter in English). Polyalphabetic ciphers are stronger but still breakable with advanced techniques.

#### Transposition Ciphers

- **Definition**: Rearranges the positions of plaintext units without changing their identities.
- **Types**:
  - **Simple Columnar Transposition**: Plaintext is written into a table row by row and read off column by column, guided by a keyword.
    - Example: For the message "HIDE THE BABOONS" with keyword "GUARD", the plaintext is written in a grid and read by columns.
  - **Double Transposition**: Applies transposition twice for added complexity.
  - **Rail Fence Cipher**: Writes plaintext in a zigzag pattern and reads it row by row.
- **Security**: Weak alone, as attackers can use anagramming to recover the original text. Combining with substitution improves security.

#### Combined Systems

- Many classical ciphers, like the ADFGVX cipher (used by the German Army in WWI), combine substitution (e.g., Polybius square) and transposition (e.g., columnar).
- Modern ciphers like AES and DES use substitution and transposition at the bit level.

#### Example

- **Caesar Cipher**: Encrypt "HELLO" with a shift of 3: H → K, E → I, L → O, L → O, O → R. Ciphertext: "KHOOR".
- **Rail Fence Cipher**: For "ATTACKATDAWN" with 2 rails, write in a zigzag and read rows: Ciphertext: "ATKTDWATACAN".

### 2.2. Symmetric Encryption Principles

Symmetric encryption uses a single key for both encryption and decryption, making it efficient for securing large data volumes.

#### Key Characteristics

- **Single Key**: The same key encrypts and decrypts data, requiring secure key sharing.
- **Speed**: Faster than asymmetric encryption, ideal for bulk encryption.
- **Security**: Depends on the secrecy of the key. If compromised, all encrypted data is at risk.

#### How It Works

- The sender encrypts plaintext using the secret key to produce ciphertext.
- The receiver uses the same key to decrypt the ciphertext back to plaintext.
- Types of symmetric ciphers:
  - **Block Ciphers**: Encrypt fixed-size blocks (e.g., DES, AES).
  - **Stream Ciphers**: Encrypt data bit by bit, faster but less secure against certain attacks.

#### Use Cases

- Encrypting files, databases, and communications (e.g., VPNs, disk encryption).
- Often paired with asymmetric encryption for secure key exchange (e.g., in SSL/TLS).

#### Examples

- DES, AES, Blowfish, Twofish.

#### Advantages

- High speed and efficiency for large data.
- Lower computational requirements compared to asymmetric encryption.

#### Disadvantages

- Key distribution is a challenge; both parties must securely share the key.
- Key compromise risks all encrypted data.

#### Example

- A bank uses symmetric encryption to secure customer data. The same key encrypts data during transmission and decrypts it at the server, ensuring confidentiality.

### 2.3. Data Encryption Standard (DES)

DES is a symmetric-key block cipher that was a cornerstone of encryption in the late 20th century but is now outdated.

#### Overview

- Developed by IBM in the 1970s, adopted by NIST in 1977 as a federal standard.
- Uses a 56-bit key to encrypt 64-bit data blocks.
- Influential in advancing cryptography but replaced due to security weaknesses.

#### How DES Works

- **Block Size**: 64 bits.
- **Key Size**: 64 bits, with every 8th bit for parity, yielding an effective 56-bit key.
- **Encryption Process**:
  - 16 rounds of transformations, each using a 48-bit subkey derived from the main key.
  - Operations include substitution (via S-boxes) and permutation (via P-boxes).
- **Decryption**: Uses the same algorithm, with subkeys applied in reverse order.

#### Security

- Initially secure, but the 56-bit key became vulnerable to brute-force attacks by the 1990s.
- In 1998, the Electronic Frontier Foundation cracked DES in under a day.
- Considered insecure for modern applications.

#### Triple DES (3DES)

- Applies DES three times with different keys, increasing the effective key length to 168 bits (often 112 bits in practice).
- Used in legacy systems but slower and less secure than AES.

#### Replacement

- Withdrawn by NIST in 2005, replaced by AES.

#### Example

- A 1980s bank used DES to encrypt transactions. Today, it would use AES due to DES’s vulnerabilities.

### 2.4. Basic Concepts of Fields, Modular Arithmetic, Galois Fields, Polynomial Arithmetic

These mathematical concepts underpin modern cryptographic algorithms like AES.

#### Fields

- A field is a set with addition and multiplication operations satisfying properties like commutativity, associativity, and the existence of inverses.
- **Finite Fields**: Have a finite number of elements, crucial for cryptography.

#### Modular Arithmetic

- Arithmetic where numbers wrap around after reaching a modulus.
- Example: In modulo 7, 5 + 4 = 2 (since 9 mod 7 = 2).
- Used in cryptography for operations that are computationally easy but hard to reverse without the key.

#### Galois Fields (Finite Fields)

- Denoted GF(p^n), where p is a prime and n is a positive integer, with p^n elements.
- **GF(p)**: Integers modulo p (e.g., GF(7) = {0, 1, 2, 3, 4, 5, 6}).
- **GF(p^n)** for n &gt; 1: Constructed using polynomial arithmetic modulo an irreducible polynomial.
- Properties:
  - Every non-zero element has a multiplicative inverse.
  - Used in AES (e.g., GF(2^8) for byte operations).
- Named after Évariste Galois, who established their theory.

#### Polynomial Arithmetic

1. Performed over finite fields, especially GF(2) for binary operations.
2. Operations: Addition (XOR), multiplication, and division modulo an irreducible polynomial.
3. Example: In GF(2^8), used in AES, arithmetic is modulo x^8 + x^4 + x^3 + x + 1.

#### Role in Cryptography

1. Finite fields ensure operations are closed (results stay within the field).
2. Enable efficient computation of inverses for decryption.
3. Support complex algebraic structures in algorithms like AES.

#### Example

- In AES, bytes are treated as elements in GF(2^8), with operations like multiplication used in the MixColumns step.

### 2.5. Advanced Encryption Standard (AES)

AES is the modern standard for symmetric encryption, widely used for securing sensitive data.

#### Overview

- Adopted by NIST in 2001, replacing DES.
- Developed by Joan Daemen and Vincent Rijmen as Rijndael.
- A block cipher encrypting 128-bit data blocks.

#### Key Sizes

- Supports 128, 192, and 256-bit keys.
- Rounds:
  - 10 for 128-bit keys
  - 12 for 192-bit keys
  - 14 for 256-bit keys

#### How AES Works

- Uses a substitution-permutation network.
- Each round includes:
  1. **SubBytes**: Replaces each byte using an S-box (lookup table).
  2. **ShiftRows**: Cyclically shifts rows of the state.
  3. **MixColumns**: Combines bytes in each column using polynomial arithmetic in GF(2^8).
  4. **AddRoundKey**: XORs the state with a round key.
- The first round has an extra key addition; the last round skips MixColumns.

#### Security

- Highly secure, especially with 256-bit keys, considered unbreakable with current technology.
- Extensively analyzed with no practical attacks when used correctly.

#### Applications

- Secures government data, financial transactions, VPNs, and SSL/TLS.
- Implemented in hardware and software for versatility.

#### Example

- A website uses AES-256 to encrypt user passwords, ensuring they remain confidential even if the database is breached.

## Supporting Resources

- Textbooks like _Cryptography and Network Security_ by William Stallings.
- Online resources like GeeksforGeeks and NIST publications.

## Table: Summary of Unit 2 Subtopics and Key Points

| **Subtopic**                       | **Key Points**                                                                         |
| ---------------------------------- | -------------------------------------------------------------------------------------- |
| Classical Cryptosystems            | Substitution (Caesar, Vigenère) and transposition (Rail Fence); combined for security. |
| Symmetric Encryption Principles    | Single key, fast for bulk data, key distribution challenge; used in DES, AES.          |
| Data Encryption Standard (DES)     | 56-bit key, 64-bit blocks, 16 rounds; now insecure, replaced by AES.                   |
| Fields, Modular Arithmetic         | Finite fields (GF(p^n)), modular arithmetic, polynomial arithmetic; basis for AES.     |
| Advanced Encryption Standard (AES) | 128-bit blocks, 128/192/256-bit keys; SubBytes, ShiftRows, MixColumns; highly secure.  |

## Conclusion

These notes provide a comprehensive overview of Unit 2, covering classical and modern symmetric encryption methods. Focus on understanding the evolution from classical ciphers to AES, the mathematical foundations, and practical applications. Regular revision and practice with examples will enhance your exam performance.
