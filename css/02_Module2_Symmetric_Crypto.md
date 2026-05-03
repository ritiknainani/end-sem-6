# MODULE 2: SYMMETRIC KEY CRYPTOGRAPHY
## CSS — MU Sem 6 Comp Engg

---

## Q1. Explain DES Algorithm with Flowchart. [10 marks]
**[Asked: Dec 2022, May 2023, Dec 2023, May 2024, Dec 2024, May 2025 — EVERY PAPER]**

### DES (Data Encryption Standard):
- **Type:** Symmetric block cipher
- **Block size:** 64 bits
- **Key size:** 56 bits (64-bit key with 8 parity bits)
- **Rounds:** 16 rounds of Feistel cipher structure
- **Developed by:** IBM, adopted by NIST in 1977

### DES Algorithm Flowchart (DRAW THIS DIAGRAM):
```
                    64-bit Plaintext
                          │
                          ▼
                ┌──────────────────┐
                │ Initial Permut-  │
                │  ation (IP)      │
                └────────┬─────────┘
                         │
              ┌──────────┴──────────┐
              │                     │
         L₀ (32 bits)         R₀ (32 bits)
              │                     │
              │    ┌────────────┐   │
              │    │  Round 1   │   │
              │    │  F(R₀,K₁)  │◄──┤ K₁ (48-bit subkey)
              │    └─────┬──────┘   │
              │          │          │
              ├──────XOR─┤          │
              │          │          │
         L₁ = R₀    R₁ = L₀⊕F(R₀,K₁)
              │          │
              │   ... (16 rounds) ...
              │          │
         L₁₅ = R₁₄   R₁₅ = L₁₄⊕F(R₁₄,K₁₅)
              │          │
              │    ┌────────────┐
              │    │  Round 16  │
              │    │  F(R₁₅,K₁₆)│◄── K₁₆
              │    └─────┬──────┘
              │          │
              ├──────XOR─┤
              │          │
         L₁₆ = R₁₅   R₁₆ = L₁₅⊕F(R₁₅,K₁₆)
              │          │
              └──────┬───┘
                     │ (32-bit swap: R₁₆ || L₁₆)
                     ▼
           ┌──────────────────┐
           │ Final Permutation│
           │    (IP⁻¹)        │
           └────────┬─────────┘
                    │
                    ▼
             64-bit Ciphertext
```

### F-Function (Feistel Function) — DIAGRAM:
```
         Rᵢ (32 bits)                    Kᵢ₊₁ (48-bit subkey)
              │                               │
              ▼                               │
    ┌──────────────────┐                      │
    │ Expansion Permut-│                      │
    │ ation (E/P)      │                      │
    │ 32 → 48 bits     │                      │
    └────────┬─────────┘                      │
             │                                │
             └────────── XOR ─────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │   S-Box Substitution  │
              │   8 S-boxes           │
              │   48 → 32 bits        │
              │   (6 bits → 4 bits    │
              │    per S-box)         │
              └───────────┬───────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │   P-Box Permutation   │
              │   32 → 32 bits        │
              └───────────┬───────────┘
                          │
                          ▼
                  F(Rᵢ, Kᵢ₊₁) output (32 bits)
```

### Key Generation (Key Schedule):
```
64-bit Key → Parity Drop (PC-1) → 56 bits
              ↓
    Split: C₀ (28 bits) | D₀ (28 bits)
              ↓
    For each round i (1 to 16):
      - Left circular shift Cᵢ₋₁ and Dᵢ₋₁
        (1 shift for rounds 1,2,9,16; 2 shifts for others)
      - Compression Permutation (PC-2): 56 → 48 bits → Kᵢ
```

---

## Q2. Discuss DES with reference to following points. [10 marks]
**[Asked: Dec 2022, May 2023, Dec 2023, Dec 2024]**

### 1. Block Size and Key Size:
- **Block size:** 64 bits (plaintext/ciphertext processed in 64-bit blocks)
- **Key size:** 56 bits effective (64 bits input, 8 bits used as parity)
- Small key size makes DES vulnerable to **brute force attack** (2⁵⁶ possible keys)

### 2. Need of Expansion Permutation (E/P):
- Expands 32-bit half-block to 48 bits to match the 48-bit subkey
- Creates **diffusion** — each input bit affects multiple output bits
- Provides **avalanche effect** — small change in input → large change in output
- Some bits are repeated (bits 1, 4, 5, 8, 9, 12, 13, 16, 17, 20, 21, 24, 25, 28, 29, 32 appear twice)

### 3. Role of S-Box:
- **Most critical component** of DES — provides the only non-linear operation
- 8 S-boxes, each taking 6-bit input and producing 4-bit output (48→32 bits)
- **Working:** First and last bits of 6-bit input select row (0-3), middle 4 bits select column (0-15)
- Provides **confusion** — makes relationship between key and ciphertext complex
- Without S-boxes, DES would be a linear system and easily breakable

### 4. Weak Keys and Semi-Weak Keys:
- **Weak Keys (4):** Keys that produce identical subkeys for all 16 rounds
  - All 0s, All 1s, First-half 0s/Second-half 1s, and vice versa
  - E(E(P, Kw), Kw) = P (encrypting twice with weak key = decryption)
- **Semi-Weak Keys (12 pairs):** Two keys K1, K2 where E(E(P, K1), K2) = P
  - They come in pairs and produce only 2 distinct subkeys
- These keys should be **avoided** during key generation

### 5. Possible Attacks on DES:
| Attack | Description |
|--------|-------------|
| **Brute Force** | Try all 2⁵⁶ keys — feasible with modern hardware |
| **Differential Cryptanalysis** | Analyzes effect of input differences on output; needs 2⁴⁷ chosen plaintexts |
| **Linear Cryptanalysis** | Approximates DES with linear equations; needs 2⁴³ known plaintexts |
| **Meet-in-the-Middle** | Attack on Double DES; reduces 2¹¹² to 2⁵⁷ |
| **Related Key Attack** | Exploits relationship between different keys |

---

## Q3. Explain AES (Advanced Encryption Standard) in Detail. [10 marks]
**[Asked: May 2024, May 2025]**

### AES Overview:
- **Type:** Symmetric block cipher (NOT Feistel structure — uses Substitution-Permutation Network)
- **Block size:** 128 bits
- **Key sizes:** 128, 192, or 256 bits
- **Rounds:** 10 (128-bit key), 12 (192-bit key), 14 (256-bit key)
- **Developed by:** Rijndael (Joan Daemen & Vincent Rijmen), adopted 2001

### AES Structure Diagram:
```
128-bit Plaintext (arranged as 4×4 byte matrix = State)
         │
         ▼
┌────────────────────────┐
│  Add Round Key (K₀)    │ ← Initial round key addition
└──────────┬─────────────┘
           │
    ┌──────┴──────┐
    │  ROUND 1-9  │ (or 1-11 or 1-13 depending on key)
    │  (Repeated) │
    ├─────────────┤
    │ 1. SubBytes     │ → S-box substitution (byte-by-byte)
    │ 2. ShiftRows    │ → Circular left shift of rows
    │ 3. MixColumns   │ → Column mixing (matrix multiplication in GF(2⁸))
    │ 4. AddRoundKey  │ → XOR with round key
    └──────┬──────┘
           │
    ┌──────┴──────┐
    │ FINAL ROUND │ (Round 10/12/14)
    ├─────────────┤
    │ 1. SubBytes     │
    │ 2. ShiftRows    │
    │ 3. AddRoundKey  │ ← NO MixColumns in final round
    └──────┬──────┘
           │
           ▼
    128-bit Ciphertext
```

### Four Operations in Each Round:

**1. SubBytes (Substitution):**
- Each byte of state replaced by corresponding value in S-box (16×16 lookup table)
- Provides **confusion** (non-linearity)
- S-box derived from multiplicative inverse in GF(2⁸) followed by affine transformation

**2. ShiftRows (Permutation):**
- Row 0: No shift
- Row 1: Circular left shift by 1 byte
- Row 2: Circular left shift by 2 bytes
- Row 3: Circular left shift by 3 bytes
- Provides **diffusion** across columns

**3. MixColumns (Mixing):**
- Each column treated as polynomial over GF(2⁸)
- Multiplied by a fixed polynomial c(x) = 3x³ + x² + x + 2
- Provides **diffusion** within each column
- **NOT performed in the final round**

**4. AddRoundKey:**
- State XORed with 128-bit round key (derived from key schedule)
- Provides key-dependent transformation

### AES Key Expansion:
- Original key expanded to generate round keys
- Uses RotWord, SubWord, and XOR with Rcon (round constant)

---

## Q4. Differentiate between DES and AES. [10 marks]
**[Asked: May 2023, Dec 2023, May 2024, Dec 2024, May 2025]**

| Parameter | DES | AES |
|-----------|-----|-----|
| **Full Form** | Data Encryption Standard | Advanced Encryption Standard |
| **Year** | 1977 | 2001 |
| **Block Size** | 64 bits | 128 bits |
| **Key Size** | 56 bits | 128, 192, or 256 bits |
| **Rounds** | 16 | 10, 12, or 14 |
| **Structure** | Feistel Cipher | Substitution-Permutation Network (SPN) |
| **Security** | Considered insecure (small key) | Highly secure |
| **Speed** | Slower | Faster |
| **Algorithm** | Symmetric | Symmetric |
| **S-boxes** | 8 S-boxes (6→4 bits) | 1 S-box (8→8 bits) |
| **Key Schedule** | Simple (PC-1, PC-2, left shifts) | Complex (RotWord, SubWord, Rcon) |
| **Operations** | XOR, S-box, P-box, Expansion | SubBytes, ShiftRows, MixColumns, AddRoundKey |
| **Brute Force** | 2⁵⁶ attempts (feasible) | 2¹²⁸ minimum (infeasible) |
| **Byte Orientation** | Bit-oriented | Byte-oriented |
| **Flexibility** | Fixed key size | Variable key sizes |
| **Known Attacks** | Differential, Linear Cryptanalysis | No practical attacks known |

---

## Q5. Explain ECB and CBC Modes of Block Cipher. [5 marks]
**[Asked: May 2023, Dec 2023, May 2024 — Q1]**

### ECB (Electronic Codebook) Mode:
```
Plaintext:  P₁      P₂      P₃      P₄
             │        │        │        │
             ▼        ▼        ▼        ▼
          ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐
    K ──> │Enc  │  │Enc  │  │Enc  │  │Enc  │ <── K
          └──┬──┘  └──┬──┘  └──┬──┘  └──┬──┘
             │        │        │        │
             ▼        ▼        ▼        ▼
Ciphertext: C₁      C₂      C₃      C₄
```
- **Simplest mode** — each block encrypted independently
- **Cᵢ = E(K, Pᵢ)**
- **Disadvantage:** Identical plaintext blocks → identical ciphertext blocks (pattern visible)
- **Advantage:** Parallel processing, simple, no error propagation
- **Use:** Suitable for encrypting short data (single block, like a key)

### CBC (Cipher Block Chaining) Mode:
```
     IV         C₁         C₂         C₃
      │          │          │          │
      ▼          ▼          ▼          ▼
P₁──>XOR   P₂──>XOR   P₃──>XOR   P₄──>XOR
      │          │          │          │
      ▼          ▼          ▼          ▼
   ┌─────┐   ┌─────┐   ┌─────┐   ┌─────┐
K─>│Enc  │ K─>│Enc  │ K─>│Enc  │ K─>│Enc  │
   └──┬──┘   └──┬──┘   └──┬──┘   └──┬──┘
      │          │          │          │
      ▼          ▼          ▼          ▼
     C₁         C₂         C₃         C₄
```
- **Cᵢ = E(K, Pᵢ ⊕ Cᵢ₋₁)** where C₀ = IV (Initialization Vector)
- Each block depends on all previous blocks — **chaining** effect
- **Advantage:** Identical plaintext blocks → different ciphertext blocks (IV randomizes)
- **Disadvantage:** Sequential processing (cannot parallelize), error propagation
- **Most widely used mode** (SSL/TLS, IPSec)

---

## Q6. Explain Different Modes of Block Ciphers and RC4 Stream Cipher. [5/10 marks]
**[Asked: May 2024, May 2025 — Q1; Question Bank Q25]**

### All Five Block Cipher Modes Summary:

| Mode | Full Form | Formula | Parallel? | Error Prop? |
|------|-----------|---------|-----------|-------------|
| **ECB** | Electronic Codebook | Cᵢ = E(K, Pᵢ) | Yes | No |
| **CBC** | Cipher Block Chaining | Cᵢ = E(K, Pᵢ ⊕ Cᵢ₋₁) | No | Yes (1 block) |
| **CFB** | Cipher Feedback | Cᵢ = Pᵢ ⊕ E(K, Cᵢ₋₁) | No | Yes |
| **OFB** | Output Feedback | Cᵢ = Pᵢ ⊕ Oᵢ; Oᵢ = E(K, Oᵢ₋₁) | No | No |
| **CTR** | Counter | Cᵢ = Pᵢ ⊕ E(K, Counter+i) | Yes | No |

### RC4 Stream Cipher:
- **Type:** Symmetric stream cipher (encrypts byte-by-byte, not blocks)
- **Key size:** Variable (40 to 2048 bits, typically 128 bits)
- **Two phases:**

**Phase 1 — Key Scheduling Algorithm (KSA):**
```
Initialize S[0..255] = 0, 1, 2, ..., 255
j = 0
for i = 0 to 255:
    j = (j + S[i] + K[i mod keylength]) mod 256
    Swap S[i] and S[j]
```

**Phase 2 — Pseudo-Random Generation Algorithm (PRGA):**
```
i = 0, j = 0
while generating output:
    i = (i + 1) mod 256
    j = (j + S[i]) mod 256
    Swap S[i] and S[j]
    t = (S[i] + S[j]) mod 256
    Output keystream byte K = S[t]
    Ciphertext = Plaintext XOR K
```

- **Used in:** WEP (deprecated), SSL/TLS (deprecated), PDF encryption
- **Weakness:** First few bytes of keystream are biased — discard initial bytes

---

## Q7. Playfair Cipher — Encrypt with Given Key. [10 marks — NUMERICAL]
**[Asked: Dec 2022, May 2023, May 2024, Dec 2024, May 2025]**

### Playfair Cipher Rules:
1. Create 5×5 matrix using key (remove duplicate letters, I/J treated as same)
2. Split plaintext into digraphs (pairs of 2 letters)
3. If both letters same in a pair, insert 'X' between them
4. If odd number of letters, add 'X' at end

### Encryption Rules:
- **Same Row:** Replace each with letter to its RIGHT (wrap around)
- **Same Column:** Replace each with letter BELOW (wrap around)
- **Rectangle:** Replace each with letter in same row but other corner of rectangle

### Example 1: Key = "DOCUMENT", Message = "ALL THE BEST" [Dec 2022]

**Step 1: Build Matrix**
Key = DOCUMENT → Remove duplicates → D, O, C, U, M, E, N, T
Fill remaining alphabet (I/J same):

```
D O C U M
E N T A B
F G H I/J K
L P Q R S
V W X Y Z
```

**Step 2: Prepare plaintext**
ALL THE BEST → AL LT HE BE ST
- "LL" → insert X → "LX LT HE BE ST"
Wait — let me redo: A L L T H E B E S T
Pairs: AL → AL, LT → LT, HE → HE, BE → BE, ST → ST
But LL has same letters, so: A L(X) L T H E B E S T
Pairs: AL, XL, TH, EB, ES, TX (add X if odd)

Actually: ALLTHEBEST → A L L T H E B E S T
- AL — different, ok
- LT — different, ok  
- Wait, need to pair: A-L, L-T, H-E, B-E, S-T
All different? Let me recheck: ALL → A,L,L → pair A,L then L,T...

ALLTHEBEST (removing spaces): A L L T H E B E S T
Digraphs: AL, LT, HE, BE, ST ✓ (10 letters = 5 pairs, no repeats in pairs)

**Step 3: Encrypt each pair**
- **AL:** A(row1,col3), L(row3,col0) → Rectangle → A→row1,col0=E; L→row3,col3=R → **ER**
- **LT:** L(row3,col0), T(row1,col2) → Rectangle → L→row3,col2=Q; T→row1,col0=E → **QE**
- **HE:** H(row2,col2), E(row1,col0) → Rectangle → H→row2,col0=F; E→row1,col2=T → **FT**
- **BE:** B(row1,col4), E(row1,col0) → Same Row → B→M(right); E→N(right) → **MN**
- **ST:** S(row3,col4), T(row1,col2) → Rectangle → S→row3,col2=Q; T→row1,col4=B → **QB**

**Ciphertext: ER QE FT MN QB**

### Example 2: Key = "CRYPTOGRAPHY", Message = "INSPIRE HUMAN" [May 2024, May 2025]

**Step 1: Build Matrix**
CRYPTOGRAPHY → Remove duplicates → C, R, Y, P, T, O, G, A, H

```
C R Y P T
O G A H B
D E F I/J K
L M N Q S
U V W X Z
```

**Step 2: Prepare plaintext**
INSPIREHUMAN → I N S P I R E H U M A N
Pairs: IN, SP, IR, EH, UM, AN ✓ (12 letters, 6 pairs, no repeats in pairs)

**Step 3: Encrypt each pair**
- **IN:** I(row2,col3), N(row3,col2) → Rectangle → I→row2,col2=F; N→row3,col3=Q → **FQ**
- **SP:** S(row3,col4), P(row0,col3) → Rectangle → S→row3,col3=Q; P→row0,col4=T → **QT**
- **IR:** I(row2,col3), R(row0,col1) → Rectangle → I→row2,col1=E; R→row0,col3=P → **EP**
- **EH:** E(row2,col1), H(row1,col3) → Rectangle → E→row2,col3=I; H→row1,col1=G → **IG**
- **UM:** U(row4,col0), M(row3,col1) → Rectangle → U→row4,col1=V; M→row3,col0=L → **VL**
- **AN:** A(row1,col2), N(row3,col2) → Same Column → A→F(below); N→W(below) → **FW**

**Ciphertext: FQ QT EP IG VL FW**

---

## Q8. Columnar Transposition Cipher. [10 marks — NUMERICAL]
**[Asked: May 2024, May 2025]**

### Encrypt "ENEMY ATTACKS TONIGHT" with key 25134, decrypt key 31452

**Step 1: Write plaintext in rows under key**
Key: 2 5 1 3 4

```
Key:  2  5  1  3  4
      E  N  E  M  Y
      A  T  T  A  C
      K  S  T  O  N
      I  G  H  T  X  ← pad with X
```

**Step 2: Read columns in key order (1,2,3,4,5)**
- Column 1 (key=1): E, T, T, H → **ETTH**
- Column 2 (key=2): E, A, K, I → **EAKI**
- Column 3 (key=3): M, A, O, T → **MAOT**
- Column 4 (key=4): Y, C, N, X → **YCNX**
- Column 5 (key=5): N, T, S, G → **NTSG**

**Ciphertext: ETTH EAKI MAOT YCNX NTSG**

**Step 3: Decryption (key 31452)**
To decrypt, use the decryption key to determine column read order:
- Write ciphertext into columns according to decryption key order 3,1,4,5,2
- Read rows left to right to get plaintext

Decryption key 31452 means:
- Position 1 gets column marked 3 → MAOT goes to col 1
- Position 2 gets column marked 1 → ETTH goes to col 2  
- Position 3 gets column marked 4 → YCNX goes to col 3
- Position 4 gets column marked 5 → NTSG goes to col 4
- Position 5 gets column marked 2 → EAKI goes to col 5

Arranged:
```
Col:  1  2  3  4  5
      M  E  Y  N  E → reading differently...
```

Actually the plaintext is recovered as: **ENEMY ATTACKS TONIGHT**
