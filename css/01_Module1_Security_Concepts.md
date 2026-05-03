# MODULE 1: SECURITY CONCEPTS & FUNDAMENTALS
## CSS — MU Sem 6 Comp Engg

---

## Q1. Explain the relationship between Security Services and Mechanisms in detail. [5/10 marks]
**[Asked: May 2023, Dec 2023, Dec 2024 — Q1 short + full question]**

### Security Services (What to protect):
Security services define WHAT kind of protection is needed. As per X.800 / ITU-T:

| # | Security Service | Description |
|---|-----------------|-------------|
| 1 | **Confidentiality** | Protection of data from unauthorized disclosure |
| 2 | **Authentication** | Assurance that communicating entity is the one it claims to be |
| 3 | **Integrity** | Assurance that data has not been altered/tampered |
| 4 | **Non-repudiation** | Protection against denial by one of the parties in communication |
| 5 | **Access Control** | Prevention of unauthorized use of resources |
| 6 | **Availability** | Resources accessible to authorized parties when needed |

### Security Mechanisms (How to protect):
Security mechanisms define HOW protection is implemented.

| # | Mechanism | Description |
|---|-----------|-------------|
| 1 | **Encryption** | Converts plaintext to ciphertext using algorithms |
| 2 | **Digital Signatures** | Data appended to message for authentication & integrity |
| 3 | **Access Control** | Mechanisms that enforce access rights |
| 4 | **Data Integrity** | Mechanisms to verify data hasn't been modified |
| 5 | **Authentication Exchange** | Mechanism to ensure identity via information exchange |
| 6 | **Traffic Padding** | Insertion of dummy data to frustrate traffic analysis |
| 7 | **Routing Control** | Selection of secure routes for data transmission |
| 8 | **Notarization** | Use of trusted third party to assure certain properties |

### Relationship Matrix (DIAGRAM — draw this for max marks):

```
                    SECURITY MECHANISMS
                    ┌──────┬───────┬────────┬──────────┬───────────┬─────────┐
                    │Encry-│Digital│Access  │Data      │Auth       │Traffic  │
                    │ption │Signa- │Control │Integrity │Exchange   │Padding  │
SECURITY            │      │ture   │        │          │           │         │
SERVICES            │      │       │        │          │           │         │
├───────────────────┼──────┼───────┼────────┼──────────┼───────────┼─────────┤
│Confidentiality    │  ✓   │       │        │          │           │   ✓     │
├───────────────────┼──────┼───────┼────────┼──────────┼───────────┼─────────┤
│Authentication     │  ✓   │  ✓    │        │          │    ✓      │         │
├───────────────────┼──────┼───────┼────────┼──────────┼───────────┼─────────┤
│Integrity          │  ✓   │  ✓    │        │    ✓     │           │         │
├───────────────────┼──────┼───────┼────────┼──────────┼───────────┼─────────┤
│Non-repudiation    │      │  ✓    │        │    ✓     │           │         │
├───────────────────┼──────┼───────┼────────┼──────────┼───────────┼─────────┤
│Access Control     │      │       │   ✓    │          │    ✓      │         │
├───────────────────┼──────┼───────┼────────┼──────────┼───────────┼─────────┤
│Availability       │  ✓   │       │   ✓    │          │           │         │
└───────────────────┴──────┴───────┴────────┴──────────┴───────────┴─────────┘
```

**Key Points:**
- One service can use multiple mechanisms (e.g., Authentication uses Encryption + Digital Signature + Auth Exchange)
- One mechanism can serve multiple services (e.g., Encryption supports Confidentiality + Authentication + Integrity)
- No single mechanism can provide all services
- The relationship is many-to-many

---

## Q2. Explain TCP/IP Vulnerabilities Layer Wise. [5/10 marks]
**[Asked: Dec 2022, Dec 2024 — Q1 short]**

### DIAGRAM:
```
┌─────────────────────────────────────────────────────────┐
│                  APPLICATION LAYER                       │
│  Vulnerabilities: Buffer Overflow, SQL Injection,        │
│  XSS, Phishing, Password Cracking, DNS Poisoning        │
├─────────────────────────────────────────────────────────┤
│                  TRANSPORT LAYER                         │
│  Vulnerabilities: SYN Flood Attack, Session Hijacking,   │
│  TCP Sequence Number Attack, Port Scanning               │
├─────────────────────────────────────────────────────────┤
│                  INTERNET/NETWORK LAYER                   │
│  Vulnerabilities: IP Spoofing, ICMP Flood, Smurf         │
│  Attack, Routing Attacks, Fragmentation Attack            │
├─────────────────────────────────────────────────────────┤
│                  NETWORK ACCESS LAYER                     │
│  Vulnerabilities: ARP Spoofing, MAC Flooding,            │
│  Packet Sniffing, VLAN Hopping, Wiretapping              │
└─────────────────────────────────────────────────────────┘
```

### Layer-wise Details:

**1. Application Layer Vulnerabilities:**
- **Buffer Overflow:** Attacker sends more data than buffer can hold, overwriting adjacent memory
- **SQL Injection:** Malicious SQL queries inserted through user input fields
- **Cross-Site Scripting (XSS):** Injecting malicious scripts into web pages
- **Phishing:** Fraudulent attempts to obtain sensitive information
- **DNS Poisoning:** Corrupting DNS cache to redirect users to malicious sites

**2. Transport Layer Vulnerabilities:**
- **SYN Flood Attack:** Sending many SYN requests without completing 3-way handshake, exhausting server resources
- **Session Hijacking:** Attacker takes over an active session between two hosts
- **TCP Sequence Number Attack:** Predicting sequence numbers to inject data into a TCP stream
- **Port Scanning:** Probing ports to find open services for exploitation

**3. Internet/Network Layer Vulnerabilities:**
- **IP Spoofing:** Forging source IP address in packet headers to impersonate another system
- **ICMP Flood (Ping Flood):** Overwhelming target with ICMP echo requests
- **Smurf Attack:** Sending ICMP requests to broadcast address with spoofed source IP
- **Routing Attacks:** Manipulating routing tables to redirect traffic

**4. Network Access/Data Link Layer Vulnerabilities:**
- **ARP Spoofing:** Sending fake ARP messages to link attacker's MAC with legitimate IP
- **MAC Flooding:** Flooding switch with fake MAC addresses to overflow CAM table
- **Packet Sniffing:** Capturing packets traversing the network using tools like Wireshark
- **Wiretapping:** Physical interception of network communication

---

## Q3. Define Non-Repudiation and Authentication. Show with example how it can be achieved. [5 marks]
**[Asked: May 2023, Dec 2023 — Q1]**

### Authentication:
- **Definition:** The process of verifying the identity of a user, device, or system
- It ensures that the communicating entity is actually who it claims to be
- **Types:**
  - **Peer Entity Authentication:** Verifies identity during connection
  - **Data Origin Authentication:** Verifies source of data unit

**Example:** When you log into a website using username + password, the server authenticates your identity. Two-factor authentication (OTP on phone) adds another layer.

### Non-Repudiation:
- **Definition:** Security service that prevents an entity from denying a previous action or commitment
- Neither sender can deny sending the message, nor receiver can deny receiving it
- **Types:**
  - **Non-repudiation of Origin:** Sender cannot deny sending
  - **Non-repudiation of Delivery:** Receiver cannot deny receiving

**Example:** Digital signatures provide non-repudiation. When Alice signs a document with her private key, she cannot later deny signing it because only she possesses that private key.

### How Achieved (DIAGRAM):
```
   Alice                                          Bob
     │                                              │
     │  1. Creates message M                        │
     │  2. Signs with Private Key → Signature S     │
     │                                              │
     │────── M + S (Digitally Signed) ─────────────>│
     │                                              │
     │              3. Bob verifies S using          │
     │                 Alice's Public Key            │
     │              4. If valid → Authenticated      │
     │              5. Alice CANNOT deny sending     │
     │                 (Non-repudiation achieved)    │
```

---

## Q4. Explain Challenge Response-based Authentication Tokens. [5 marks]
**[Asked: May 2023, Dec 2023 — Q1]**

### Concept:
Challenge-response authentication is a protocol where one party (verifier) presents a challenge and the other party (prover) must provide a valid response to authenticate.

### Working Mechanism:
```
   Client (Prover)                    Server (Verifier)
        │                                    │
        │──── 1. Authentication Request ────>│
        │                                    │
        │<─── 2. Challenge (Random Nonce) ───│
        │                                    │
        │     3. Client computes response    │
        │     using shared secret/key        │
        │     Response = f(Challenge, Key)   │
        │                                    │
        │──── 4. Response ──────────────────>│
        │                                    │
        │     5. Server computes expected    │
        │     response independently         │
        │     If Response matches → AUTH OK  │
        │                                    │
        │<─── 6. Success/Failure ───────────│
```

### Key Points:
- **Challenge** is typically a random number (nonce) — different each time → prevents replay attacks
- **Response** is computed using the challenge + a shared secret (password/key)
- The secret is **never transmitted** over the network
- Even if attacker captures the challenge-response pair, they cannot reuse it (nonce changes)
- **Examples:** CHAP protocol, smart card authentication, one-time password tokens

### Types of Tokens:
1. **Synchronous tokens:** Time-based (TOTP) — generates password based on current time
2. **Asynchronous tokens:** Challenge-based — generates response to server-sent challenge
3. **Smart cards:** Contains cryptographic keys, computes response on-chip

---

## Q5. Explain different Hash Algorithm Properties. [5 marks]
**[Asked: Dec 2022, Dec 2024 — Q1]**

### Properties of a Secure Hash Function:

| Property | Description |
|----------|-------------|
| **1. Variable-length input** | Can accept input of any length |
| **2. Fixed-length output** | Produces output of fixed length (e.g., SHA-256 → 256 bits) |
| **3. Efficiency** | H(x) is easy/fast to compute for any given x |
| **4. Pre-image Resistance** | Given hash h, computationally infeasible to find x such that H(x) = h (one-way property) |
| **5. Second Pre-image Resistance** | Given x, infeasible to find y ≠ x such that H(x) = H(y) (weak collision resistance) |
| **6. Collision Resistance** | Infeasible to find any pair (x, y) where x ≠ y and H(x) = H(y) (strong collision resistance) |
| **7. Avalanche Effect** | Small change in input produces drastically different output |
| **8. Deterministic** | Same input always produces same output |

### Diagram — Hash Function Properties:
```
Input (any length)          Hash Function H          Output (fixed length)
──────────────────────>  ┌──────────────────┐  ──────────────────────>
"Hello"                  │                  │    a591a6d40bf420404...
"Hello!"                 │   SHA-256 / MD5  │    334d016f755cd6dc...
(1 char difference)      │   / SHA-1        │    (completely different!)
Large file (GB)          │                  │    Fixed 256/128/160 bits
──────────────────────>  └──────────────────┘  ──────────────────────>

ONE-WAY: Cannot reverse from hash to original message ✗
```

---

## Q6. Explain Algorithmic Modes of Encryption Process of Symmetric Key. [5 marks]
**[Asked: Dec 2022, Dec 2024 — Q1]**

(Covered in detail in Module 2 — Block Cipher Modes: ECB, CBC, CFB, OFB, CTR)

### Quick Summary for Q1 (5 marks):

Symmetric key encryption uses the **same key** for both encryption and decryption. The algorithmic modes define HOW a block cipher processes multiple blocks:

1. **ECB (Electronic Codebook):** Each block encrypted independently — simplest but weakest (identical plaintext blocks → identical ciphertext blocks)
2. **CBC (Cipher Block Chaining):** Each block XORed with previous ciphertext block before encryption — uses IV — most commonly used
3. **CFB (Cipher Feedback):** Converts block cipher to stream cipher — encrypts previous ciphertext and XORs with plaintext
4. **OFB (Output Feedback):** Similar to CFB but encrypts the output of the previous encryption — error doesn't propagate
5. **CTR (Counter):** Uses a counter value encrypted and XORed with plaintext — allows parallel processing

(See Module 2 for diagrams of each mode)
