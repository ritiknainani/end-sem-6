# MODULE 3: ASYMMETRIC KEY CRYPTOGRAPHY & NUMBER THEORY
## CSS — MU Sem 6 Comp Engg

---

## Q1. RSA Algorithm — Key Generation, Encryption, Decryption. [10 marks — NUMERICAL]
**[Asked in EVERY paper — Dec 2022 through May 2025]**

### RSA Algorithm Steps:

**Key Generation:**
1. Choose two large prime numbers **p** and **q**
2. Compute **n = p × q**
3. Compute **φ(n) = (p-1)(q-1)** (Euler's Totient)
4. Choose **e** such that: 1 < e < φ(n) and **gcd(e, φ(n)) = 1**
5. Compute **d** such that: **e × d ≡ 1 (mod φ(n))** i.e., d = e⁻¹ mod φ(n)
6. **Public Key = (e, n)** | **Private Key = (d, n)**

**Encryption:** C = Mᵉ mod n
**Decryption:** M = Cᵈ mod n

### RSA Diagram:
```
   Sender (Alice)                              Receiver (Bob)
                                               
   Key Generation:                             
   p, q (primes) → n = p×q                    
   φ(n) = (p-1)(q-1)                          
   Choose e: gcd(e,φ(n))=1                    
   Find d: e×d ≡ 1 mod φ(n)                   
                                               
   Public Key (e,n) ─── Published ───────────> Known to all
   Private Key (d,n) ── Kept Secret            
                                               
   Encryption:                    Decryption:  
   C = Mᵉ mod n ──────────────> M = Cᵈ mod n 
```

---

### NUMERICAL 1: Public Key (17,321), (5,321), encrypt m=7 [Dec 2022]

**User A:** Public key = (e₁, n) = (17, 321)
**User B:** Public key = (e₂, n) = (5, 321)

**Find private keys:**
n = 321 = 3 × 107 → p = 3, q = 107
φ(n) = (3-1)(107-1) = 2 × 106 = **212**

**For User A:** e₁ = 17, find d₁
17 × d₁ ≡ 1 mod 212
Using Extended Euclidean Algorithm:
212 = 12 × 17 + 8
17 = 2 × 8 + 1
Back-substituting: 1 = 17 - 2(8) = 17 - 2(212 - 12×17) = 25×17 - 2×212
So d₁ = 25
**Verify:** 17 × 25 = 425 = 2×212 + 1 ✓

**For User B:** e₂ = 5, find d₂
5 × d₂ ≡ 1 mod 212
212 = 42 × 5 + 2
5 = 2 × 2 + 1
Back: 1 = 5 - 2(2) = 5 - 2(212 - 42×5) = 85×5 - 2×212
So d₂ = 85
**Verify:** 5 × 85 = 425 = 2×212 + 1 ✓

**Encrypt m=7 by B's public key:**
C = mᵉ² mod n = 7⁵ mod 321
7⁵ = 16807
16807 mod 321 = 16807 - 52×321 = 16807 - 16692 = **115**
**C = 115**

**Decrypt by B:**
M = Cᵈ² mod n = 115⁸⁵ mod 321
(Using modular exponentiation, this gives back M = 7) ✓

---

### NUMERICAL 2: Public Key (7,187), find φ(N), private key D, cipher for M=10 [May 2023]

**Given:** Public key (E, N) = (7, 187)

**Step 1:** Find p and q
N = 187 = 11 × 17 → p = 11, q = 17

**Step 2:** Calculate φ(N)
**φ(187) = (11-1)(17-1) = 10 × 16 = 160**

**Step 3:** Find private key D
E × D ≡ 1 mod φ(N)
7 × D ≡ 1 mod 160

Using Extended Euclidean:
160 = 22 × 7 + 6
7 = 1 × 6 + 1
Back: 1 = 7 - 1(6) = 7 - 1(160 - 22×7) = 23×7 - 1×160
**D = 23**
**Verify:** 7 × 23 = 161 = 1×160 + 1 ✓

**Step 4:** Encrypt M = 10
C = Mᴱ mod N = 10⁷ mod 187
10¹ = 10
10² = 100
10⁴ = 100² = 10000 mod 187 = 10000 - 53×187 = 10000 - 9911 = 89
10⁷ = 10⁴ × 10² × 10¹ = 89 × 100 × 10 = 89000 mod 187
89000 ÷ 187 = 475 remainder 175
**C = 175**

**Step 5:** Decrypt to verify
M = Cᴰ mod N = 175²³ mod 187 = 10 ✓

---

### NUMERICAL 3: Public Key (7,33) — RSA Digital Signature [May 2024, May 2025]

**Given:** Public key (E, N) = (7, 33)

**Step 1:** Find p and q
N = 33 = 3 × 11 → p = 3, q = 11

**Step 2:** φ(33) = (3-1)(11-1) = 2 × 10 = **20**

**Step 3:** Find private key D
7 × D ≡ 1 mod 20
Try: 7 × 3 = 21 = 1×20 + 1 ✓
**D = 3**

**Step 4: Digital Signature — Sign message M = 'C' (value = 3)**

**Signing (by User A using Private Key D=3):**
Signature S = Mᴰ mod N = 3³ mod 33 = 27 mod 33 = **27**

**Verification (by User B using Public Key E=7):**
M' = Sᴱ mod N = 27⁷ mod 33
27¹ = 27
27² = 729 mod 33 = 729 - 22×33 = 729 - 726 = 3
27⁴ = 3² = 9
27⁷ = 27⁴ × 27² × 27¹ = 9 × 3 × 27 = 729 mod 33 = 3
**M' = 3 = M ✓ → Signature is VALID**

### RSA Digital Signature Diagram:
```
   Sender (Alice)                           Receiver (Bob)
   Message M = 3                            
        │                                   
        ▼                                   
  ┌──────────────┐                          
  │ Sign with    │                          
  │ Private Key  │                          
  │ S = M^D mod N│                          
  │ = 3³ mod 33  │                          
  │ = 27         │                          
  └──────┬───────┘                          
         │                                  
    M=3, S=27 ─────────────────────────>  ┌──────────────┐
                                          │ Verify with  │
                                          │ Public Key   │
                                          │ M' = S^E mod N│
                                          │ = 27⁷ mod 33 │
                                          │ = 3          │
                                          └──────┬───────┘
                                                 │
                                          M' = M = 3 ?
                                          YES → Valid ✓
```

---

## Q2. Diffie-Hellman Key Exchange Algorithm. [10 marks — NUMERICAL]
**[Asked: Dec 2022, May 2023, May 2024, Dec 2024, May 2025]**

### Algorithm:
1. Two users agree on public values: **prime p** and **generator g**
2. Each user selects a **private key** (secret number)
3. Each computes a **public value** and sends to other
4. Each computes the **shared secret key** using received value

### Diagram:
```
                    Public: p (prime), g (generator)
                    
   Alice                                         Bob
   Private: a                                    Private: b
   
   Compute:                                      Compute:
   A = gᵃ mod p ─────── Send A ──────────────>  
                <─────── Send B ──────────────   B = gᵇ mod p
   
   Compute Shared Key:                           Compute Shared Key:
   K = Bᵃ mod p                                  K = Aᵇ mod p
   = (gᵇ)ᵃ mod p                                = (gᵃ)ᵇ mod p
   = gᵃᵇ mod p                                  = gᵃᵇ mod p
   
               K(Alice) = K(Bob) = gᵃᵇ mod p ✓
```

---

### NUMERICAL 1: n=11, g=7, x=3, y=6 [Dec 2022]

**Given:** p = 11, g = 7, private keys: x = 3 (User P), y = 6 (User Q)

**User P computes public value:**
A = gˣ mod p = 7³ mod 11 = 343 mod 11
343 ÷ 11 = 31 remainder 2
**A = 2**

**User Q computes public value:**
B = gʸ mod p = 7⁶ mod 11
7² = 49 mod 11 = 5
7⁴ = 5² = 25 mod 11 = 3
7⁶ = 7⁴ × 7² = 3 × 5 = 15 mod 11 = 4
**B = 4**

**Shared Secret Key:**
User P: K = Bˣ mod p = 4³ mod 11 = 64 mod 11 = 64 - 5×11 = 9 → **K = 9**
User Q: K = Aʸ mod p = 2⁶ mod 11 = 64 mod 11 = 9 → **K = 9** ✓

**Shared Secret Key = 9**

---

### NUMERICAL 2: p=23, g=5, secret keys 6 and 15 [May 2024, May 2025]

**Given:** p = 23, g = 5, a = 6 (Alice), b = 15 (Bob)

**Alice computes:**
A = 5⁶ mod 23
5¹ = 5
5² = 25 mod 23 = 2
5⁴ = 2² = 4
5⁶ = 5⁴ × 5² = 4 × 2 = 8
**A = 8**

**Bob computes:**
B = 5¹⁵ mod 23
5¹ = 5
5² = 2
5⁴ = 4
5⁸ = 4² = 16
5¹⁵ = 5⁸ × 5⁴ × 5² × 5¹ = 16 × 4 × 2 × 5 = 640 mod 23
640 ÷ 23 = 27 remainder 19
**B = 19**

**Shared Secret Key:**
Alice: K = B^a mod p = 19⁶ mod 23
19¹ = 19
19² = 361 mod 23 = 361 - 15×23 = 361 - 345 = 16
19⁴ = 16² = 256 mod 23 = 256 - 11×23 = 256 - 253 = 3
19⁶ = 19⁴ × 19² = 3 × 16 = 48 mod 23 = 2
**K = 2**

Bob: K = A^b mod p = 8¹⁵ mod 23
8¹ = 8
8² = 64 mod 23 = 64 - 2×23 = 18
8⁴ = 18² = 324 mod 23 = 324 - 14×23 = 324 - 322 = 2
8⁸ = 2² = 4
8¹⁵ = 8⁸ × 8⁴ × 8² × 8¹ = 4 × 2 × 18 × 8 = 1152 mod 23
1152 ÷ 23 = 50 remainder 2
**K = 2** ✓

**Shared Secret Key = 2**

---

### Attacks on Diffie-Hellman:
1. **Man-in-the-Middle Attack:** Attacker intercepts and replaces public values
```
Alice ──A──> Mallory ──A'──> Bob
Alice <──B'── Mallory <──B── Bob
```
Mallory establishes separate keys with both Alice and Bob

2. **Discrete Logarithm Attack:** If attacker can solve gˣ mod p = A for x → breaks DH
3. **Small Subgroup Attack:** Using small order elements to reduce key space

**Prevention:** Use digital certificates, authenticated DH, or Station-to-Station (STS) protocol

---

## Q3. Euler's Phi (Totient) Function — Rules & Numerical. [10 marks]
**[Asked: May 2023, Dec 2023]**

### Definition:
**φ(n)** = count of integers from 1 to n that are relatively prime to n (i.e., gcd(k,n) = 1)

### Rules for Finding φ(n):

| Rule | Condition | Formula | Example |
|------|-----------|---------|---------|
| **Rule 1** | n is prime | φ(n) = n - 1 | φ(7) = 6 |
| **Rule 2** | n = pᵏ (prime power) | φ(n) = pᵏ - pᵏ⁻¹ = pᵏ⁻¹(p-1) | φ(8) = φ(2³) = 2²(2-1) = 4 |
| **Rule 3** | n = p × q (two primes) | φ(n) = (p-1)(q-1) | φ(15) = (3-1)(5-1) = 8 |
| **Rule 4** | n = p₁ᵃ¹ × p₂ᵃ² × ... | φ(n) = n × ∏(1 - 1/pᵢ) | See below |
| **Rule 5** | φ(1) = 1 | By definition | |
| **Rule 6** | gcd(a,b) = 1 | φ(a×b) = φ(a) × φ(b) | Multiplicative property |

### Numerical: Calculate φ(11), φ(49), φ(240) [May 2023]

**φ(11):**
11 is prime → φ(11) = 11 - 1 = **10** (Rule 1)

**φ(49):**
49 = 7² → φ(49) = 7² - 7¹ = 49 - 7 = **42** (Rule 2)
Or: φ(7²) = 7¹(7-1) = 7 × 6 = **42**

**φ(240):**
240 = 2⁴ × 3 × 5
φ(240) = 240 × (1 - 1/2) × (1 - 1/3) × (1 - 1/5)
= 240 × 1/2 × 2/3 × 4/5
= 240 × 8/30
= **64** (Rule 4)

Or using multiplicative property:
φ(240) = φ(2⁴) × φ(3) × φ(5) = 8 × 2 × 4 = **64**

---

## Q4. Explain Euclidean Algorithm. [5 marks]
**[Asked: May 2024, May 2025 — Q1]**

### Purpose: 
Find GCD (Greatest Common Divisor) of two numbers.

### Algorithm:
```
GCD(a, b):
  while b ≠ 0:
      temp = b
      b = a mod b
      a = temp
  return a
```

### Example: GCD(252, 198)
```
252 = 1 × 198 + 54    → GCD(198, 54)
198 = 3 × 54 + 36     → GCD(54, 36)
54  = 1 × 36 + 18     → GCD(36, 18)
36  = 2 × 18 + 0      → GCD(18, 0)
```
**GCD(252, 198) = 18**

### Extended Euclidean Algorithm:
Finds x, y such that: **ax + by = GCD(a, b)**
Used in RSA to find modular inverse (private key d)

### Example: Find inverse of 7 mod 160 (for RSA)
```
160 = 22 × 7 + 6
7   = 1 × 6 + 1
6   = 6 × 1 + 0

Back-substitute:
1 = 7 - 1 × 6
1 = 7 - 1 × (160 - 22 × 7)
1 = 23 × 7 - 1 × 160

So 7⁻¹ mod 160 = 23
```

---

## Q5. Explain Public Key Distribution in Detail. [10 marks]
**[Asked: QB Q20]**

### Problem:
How to securely distribute public keys so that users can trust the key belongs to the claimed owner?

### Methods:

**1. Public Announcement:**
- Users broadcast their public keys (e.g., append to email, post on website)
- **Problem:** Anyone can forge a key and claim to be someone else

**2. Publicly Available Directory:**
- Trusted entity maintains a directory {name, public key}
- Users register their keys with the directory
- **Problem:** Directory can be tampered with; single point of failure

**3. Public-Key Authority:**
- Central authority stores all public keys
- Users request other's public key from authority in real-time
- Authority signs responses with its private key
- **Problem:** Authority is bottleneck; must be online always

**4. Public-Key Certificates (Best Method):**
- Certificate Authority (CA) issues digital certificates
- Certificate binds identity to public key, signed by CA's private key
- Users verify certificate using CA's public key
- **No need for CA to be online** — certificates can be verified independently

### Certificate-based Distribution Diagram:
```
     ┌──────────────────────┐
     │  Certificate Authority│
     │  (CA)                 │
     └──────┬───────────────┘
            │ Issues certificates
     ┌──────┴──────┐
     │             │
     ▼             ▼
  ┌──────┐      ┌──────┐
  │Alice │      │ Bob  │
  │Cert: │      │Cert: │
  │{Alice,│     │{Bob, │
  │ PubA, │     │ PubB,│
  │ SigCA}│     │SigCA}│
  └──────┘      └──────┘
  
  Alice sends her certificate to Bob
  Bob verifies CA's signature using CA's public key
  If valid → trusts Alice's public key
```
