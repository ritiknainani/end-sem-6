# MODULE 4: HASH FUNCTIONS, MESSAGE AUTHENTICATION & DIGITAL SIGNATURES
## CSS — MU Sem 6 Comp Engg

---

## Q1. What characteristics are needed in secure hash function? Explain Secure Hash Algorithm (SHA-512). [10 marks]
**[Asked: Dec 2022, Dec 2024]**

### Properties of Secure Hash Function:
(See Module 1 Q5 for complete list)

1. **Pre-image Resistance (One-way):** Given h, infeasible to find m such that H(m) = h
2. **Second Pre-image Resistance:** Given m₁, infeasible to find m₂ ≠ m₁ with H(m₁) = H(m₂)
3. **Collision Resistance:** Infeasible to find any (m₁, m₂) with m₁ ≠ m₂ and H(m₁) = H(m₂)
4. **Fixed output length** regardless of input
5. **Avalanche effect** — small input change → large output change
6. **Efficient computation**

### SHA-512 Algorithm:

**Overview:**
- Input: message of any length
- Output: 512-bit (64-byte) hash value
- Block size: 1024 bits
- Rounds: 80
- Word size: 64 bits

### SHA-512 Flowchart (DIAGRAM):
```
Message (any length)
        │
        ▼
┌──────────────────────┐
│  1. PADDING          │
│  Append '1' bit      │
│  Append '0' bits     │
│  until length ≡ 896  │
│  mod 1024            │
│  Append 128-bit      │
│  message length      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  2. PARSE            │
│  Divide into N       │
│  blocks of 1024 bits │
│  M₁, M₂, ..., Mₙ    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────────────────────┐
│  3. INITIALIZE HASH VALUES           │
│  H₀⁽⁰⁾ through H₇⁽⁰⁾               │
│  (8 × 64-bit initial values         │
│   derived from square roots          │
│   of first 8 primes)                 │
└──────────┬───────────────────────────┘
           │
    ┌──────┴──────┐
    │ For each    │
    │ block Mᵢ    │
    ├─────────────┤
    │ 4. MESSAGE SCHEDULE              │
    │    W₀..W₁₅ = block words        │
    │    W₁₆..W₇₉ computed using      │
    │    σ₀, σ₁ functions              │
    │                                  │
    │ 5. COMPRESSION (80 rounds)       │
    │    a,b,c,d,e,f,g,h = Hᵢ₋₁       │
    │    For t = 0 to 79:              │
    │      T₁ = h + Σ₁(e) + Ch(e,f,g) │
    │           + Kₜ + Wₜ             │
    │      T₂ = Σ₀(a) + Maj(a,b,c)    │
    │      h=g, g=f, f=e, e=d+T₁      │
    │      d=c, c=b, b=a, a=T₁+T₂     │
    │                                  │
    │ 6. UPDATE HASH                   │
    │    Hᵢ = Hᵢ₋₁ + (a,b,c,d,e,f,g,h)│
    └──────┬──────┘
           │
           ▼
┌──────────────────────┐
│  7. FINAL HASH       │
│  H = H₀ || H₁ ||    │
│  ... || H₇           │
│  = 512-bit digest    │
└──────────────────────┘
```

### Key Functions Used:
- **Ch(e,f,g)** = (e AND f) XOR (NOT e AND g) — Choice function
- **Maj(a,b,c)** = (a AND b) XOR (a AND c) XOR (b AND c) — Majority function
- **Σ₀(a)** = ROTR²⁸(a) XOR ROTR³⁴(a) XOR ROTR³⁹(a)
- **Σ₁(e)** = ROTR¹⁴(e) XOR ROTR¹⁸(e) XOR ROTR⁴¹(e)

---

## Q2. What goals are served using a message digest? Explain using MD5. [10 marks]
**[Asked: May 2023, Dec 2023]**

### Goals of Message Digest:
1. **Data Integrity:** Verify message hasn't been altered during transmission
2. **Authentication:** Verify sender's identity (when combined with secret key)
3. **Non-repudiation:** Sender cannot deny sending (with digital signatures)
4. **Password Storage:** Store hash of password instead of plaintext
5. **Digital Signatures:** Hash message first, then sign the hash (efficient)
6. **Fingerprinting:** Create unique identifier for files/data

### MD5 (Message Digest 5):
- **Output:** 128-bit (16-byte) hash
- **Block size:** 512 bits
- **Rounds:** 4 rounds of 16 operations each = 64 operations total
- **Developed by:** Ron Rivest, 1991

### MD5 Algorithm Diagram:
```
Message → Padding → Append Length → Process 512-bit blocks
                                          │
                    ┌─────────────────────┘
                    │
            ┌───────┴────────┐
            │ Initialize     │
            │ A = 0x67452301 │
            │ B = 0xEFCDAB89 │
            │ C = 0x98BADCFE │
            │ D = 0x10325476 │
            └───────┬────────┘
                    │
    ┌───────────────┴───────────────┐
    │     For each 512-bit block:   │
    │                               │
    │  Round 1 (16 ops): F(B,C,D)   │
    │    F = (B AND C) OR           │
    │        (NOT B AND D)          │
    │                               │
    │  Round 2 (16 ops): G(B,C,D)   │
    │    G = (B AND D) OR           │
    │        (C AND NOT D)          │
    │                               │
    │  Round 3 (16 ops): H(B,C,D)   │
    │    H = B XOR C XOR D          │
    │                               │
    │  Round 4 (16 ops): I(B,C,D)   │
    │    I = C XOR (B OR NOT D)     │
    │                               │
    │  Each operation:              │
    │  a = b + ((a + F/G/H/I(b,c,d) │
    │       + M[k] + T[i]) <<< s)  │
    │  Then rotate: a→d→c→b→a      │
    └───────────────┬───────────────┘
                    │
                    ▼
            128-bit Hash Output
            (concatenation of A,B,C,D)
```

### MD5 Steps:
1. **Padding:** Append '1' bit, then '0' bits until length ≡ 448 mod 512. Append 64-bit original length
2. **Initialize:** Four 32-bit registers (A, B, C, D) with fixed values
3. **Process:** Each 512-bit block through 4 rounds of 16 operations
4. **Output:** Final values of A, B, C, D concatenated = 128-bit hash

---

## Q3. Differentiate between SHA-1 and MD5. [5 marks]
**[Asked: May 2024, May 2025 — Q1]**

| Parameter | MD5 | SHA-1 |
|-----------|-----|-------|
| **Digest Length** | 128 bits | 160 bits |
| **Block Size** | 512 bits | 512 bits |
| **Rounds** | 4 rounds × 16 ops = 64 | 4 rounds × 20 ops = 80 |
| **Speed** | Faster | Slower |
| **Security** | Broken (collision found 2004) | Broken (collision found 2017) |
| **Word Size** | 32 bits | 32 bits |
| **Developer** | Ron Rivest (1991) | NSA (1995) |
| **Collision Resistance** | Weak (2³⁹ operations) | Better than MD5 (2⁶³ ops) |
| **Structure** | Merkle-Damgård | Merkle-Damgård |
| **Registers** | 4 (A,B,C,D) | 5 (A,B,C,D,E) |
| **Current Status** | Deprecated | Deprecated (use SHA-256+) |

---

## Q4. Why are Digital Certificates and Signatures required? Explain any one Digital Signature Algorithm. [10 marks]
**[Asked: Dec 2022, May 2023, Dec 2023, Dec 2024]**

### Why Digital Signatures are Required:
1. **Authentication:** Verifies the identity of the sender
2. **Integrity:** Ensures message hasn't been tampered with
3. **Non-repudiation:** Sender cannot deny sending the message
4. **Legal validity:** Equivalent to handwritten signatures in many jurisdictions

### Why Digital Certificates are Required:
1. **Bind identity to public key** — prevent impersonation
2. **Trust establishment** — issued by trusted Certificate Authority (CA)
3. **Public key verification** — anyone can verify certificate using CA's public key
4. **Prevent man-in-the-middle attacks** on public key distribution

### Role of Digital Signature in Digital Certificates:
- CA **signs** the certificate using its **private key**
- This signature binds the owner's identity to their public key
- Anyone can **verify** the certificate using CA's **public key**
- If verification succeeds → certificate is authentic and untampered

### Digital Signature Process Diagram:
```
SIGNING:
   Message M                    
        │                       
        ▼                       
  ┌──────────┐                  
  │Hash(M)   │→ h (message digest)
  └──────────┘                  
        │                       
        ▼                       
  ┌──────────────────┐          
  │ Encrypt h with   │          
  │ Sender's Private │          
  │ Key (Kpr)        │          
  │ S = E(Kpr, h)    │          
  └────────┬─────────┘          
           │                    
   Send: M + S (message + signature)

VERIFICATION:
  Received: M + S
        │         │
        ▼         ▼
  ┌──────────┐  ┌──────────────────┐
  │Hash(M)   │  │ Decrypt S with   │
  │→ h₁      │  │ Sender's Public  │
  └────┬─────┘  │ Key (Kpub)       │
       │        │ h₂ = D(Kpub, S)  │
       │        └────────┬─────────┘
       │                 │
       └───── Compare ───┘
              h₁ = h₂ ?
         YES → Valid Signature ✓
         NO  → Invalid ✗
```

### RSA Digital Signature Algorithm (most commonly asked):
(See Module 3 Q1 - Numerical 3 for full worked example)

**Signing:** S = M^d mod n (using sender's private key d)
**Verification:** M' = S^e mod n (using sender's public key e)
If M' = M → signature is valid

---

## Q5. What is the need for Message Authentication? List various techniques. [10 marks]
**[Asked: QB Q13]**

### Need for Message Authentication:
1. **Protect against content modification** — attacker changing message content
2. **Protect against sequence modification** — reordering, deleting, or duplicating messages
3. **Protect against timing modification** — delaying or replaying messages
4. **Verify source** — ensure message comes from claimed sender
5. **Protect against masquerade** — attacker pretending to be legitimate user

### Message Authentication Techniques:

**1. Message Encryption (Symmetric):**
- Encrypt entire message with shared secret key
- Only legitimate receiver can decrypt
- Provides confidentiality + authentication (if attacker can't create valid ciphertext)

**2. Message Authentication Code (MAC):**
```
Sender:                          Receiver:
M + K → MAC(M,K) = T            M + K → MAC(M,K) = T'
Send: M || T                     Compare: T = T' ?
```
- Fixed-length value computed from message + secret key
- Appended to message
- Receiver recomputes MAC and compares

**3. Hash Function:**
```
Sender:                          Receiver:
M → H(M) = h                    M → H(M) = h'
Send: M || h                     Compare: h = h' ?
```
- No secret key used (for integrity only)
- For authentication: H(M || K) or encrypt hash

---

## Q6. Differentiate HMAC, CBC-MAC and CMAC. [5 marks]
**[Asked: QB Q24]**

| Parameter | HMAC | CBC-MAC | CMAC |
|-----------|------|---------|------|
| **Full Form** | Hash-based MAC | Cipher Block Chaining MAC | Cipher-based MAC |
| **Based On** | Hash function (MD5/SHA) | Block cipher (DES/AES) | Block cipher (AES) |
| **Formula** | H(K⊕opad ∥ H(K⊕ipad ∥ M)) | Encrypt blocks in CBC mode, last block = MAC | Improved CBC-MAC |
| **Variable-length** | Yes | Only for fixed-length messages | Yes |
| **Security** | Strong | Vulnerable for variable-length | Fixed CBC-MAC issues |
| **Speed** | Fast (hash-based) | Slower (encryption-based) | Moderate |
| **Output** | Truncated hash | Last ciphertext block | Last ciphertext block |
| **Standard** | RFC 2104 | FIPS 113 | NIST SP 800-38B |

### HMAC Diagram:
```
           K (key, padded to block size)
           │
     ┌─────┴─────┐
     ▼           ▼
  K ⊕ ipad    K ⊕ opad
     │           │
     ▼           │
  ┌──────┐       │
  │ M    │       │
  │append│       │
  └──┬───┘       │
     ▼           │
  H(K⊕ipad||M)  │
     │           │
     ▼           ▼
     └──> H(K⊕opad || H(K⊕ipad||M))
                 │
                 ▼
              HMAC output
```

---

## Q7. Discuss various attacks on Digital Signature. [10 marks]
**[Asked: QB Q15]**

### Types of Attacks:

**1. Key-Only Attack:**
- Attacker knows only the signer's public key
- Tries to forge signature without knowing private key
- **Prevention:** Use strong key sizes (2048+ bits for RSA)

**2. Known-Message Attack:**
- Attacker has access to several valid message-signature pairs
- Tries to forge signature on a new message
- **Prevention:** Use strong hash functions

**3. Chosen-Message Attack:**
- Attacker can choose messages and get their signatures from signer
- Uses these to forge signature on different message
- **Prevention:** Use hash-then-sign approach

**4. Existential Forgery:**
- Attacker creates a valid signature for some message (not chosen by attacker)
- The message may be meaningless but the signature is valid
- **Prevention:** Always hash before signing

**5. Selective Forgery:**
- Attacker can forge signature for a specific chosen message
- Most dangerous attack type
- **Prevention:** Use collision-resistant hash functions

### Methods to Overcome:
1. Use hash-then-sign paradigm (hash message first, then sign hash)
2. Use collision-resistant hash functions (SHA-256 or higher)
3. Use sufficiently large key sizes
4. Use standardized signature schemes (RSA-PSS, ECDSA)
5. Add timestamps and sequence numbers to prevent replay
