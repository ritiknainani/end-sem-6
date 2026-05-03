# MODULE 5: NETWORK & EMAIL SECURITY
## CSS — MU Sem 6 Comp Engg

---

## Q1. How does PGP achieve Confidentiality and Authentication in Emails? [10 marks]
**[Asked: Dec 2022, May 2023, Dec 2023, Dec 2024 — VERY HIGH FREQUENCY]**

### PGP (Pretty Good Privacy):
- Email security application providing: Confidentiality, Authentication, Integrity, Non-repudiation
- Combines symmetric + asymmetric encryption + digital signatures + compression

### PGP — Authentication Only:
```
Sender (Alice)                              Receiver (Bob)
                                            
Message M                                   
    │                                       
    ▼                                       
┌──────────┐                                
│ SHA-256   │ → H (hash of message)         
└────┬─────┘                                
     ▼                                      
┌──────────────┐                            
│ Encrypt H    │                            
│ with Alice's │                            
│ Private Key  │ → Digital Signature (DS)   
│ (KRa)        │                            
└──────┬───────┘                            
       │                                    
  M || DS ─────────────────────────────>  ┌──────────────┐
                                          │ Separate M   │
                                          │ and DS       │
                                          ├──────────────┤
                                          │ Decrypt DS   │
                                          │ with Alice's │
                                          │ Public Key   │
                                          │ (KUa) → H'  │
                                          ├──────────────┤
                                          │ Hash M → H  │
                                          │ Compare H=H'│
                                          │ If yes →     │
                                          │ Authenticated│
                                          └──────────────┘
```

### PGP — Confidentiality Only:
```
Sender (Alice)                              Receiver (Bob)
                                            
Message M                                   
    │                                       
    ▼                                       
┌────────────────┐                          
│ Generate random│                          
│ session key Ks │                          
└───┬────────────┘                          
    │                                       
    ├──────────────────────┐                
    ▼                      ▼                
┌──────────┐      ┌──────────────┐          
│Encrypt M │      │Encrypt Ks   │          
│with Ks   │      │with Bob's   │          
│(symmetric│      │Public Key   │          
│e.g. AES) │      │(KUb)        │          
└────┬─────┘      └──────┬──────┘          
     │                   │                  
     └─── E(Ks,M) || E(KUb,Ks) ──────>  ┌──────────────┐
                                          │ Decrypt Ks   │
                                          │ with Bob's   │
                                          │ Private Key  │
                                          │ (KRb)        │
                                          ├──────────────┤
                                          │ Decrypt M    │
                                          │ with Ks      │
                                          │ → Plaintext  │
                                          └──────────────┘
```

### PGP — Both Authentication + Confidentiality (MOST ASKED):
```
Sender (Alice)                              Receiver (Bob)

Message M
    │
    ├──── Hash (SHA) ──→ H
    │                     │
    │              Encrypt H with KRa ──→ DS
    │                     │
    └── M || DS ──────────┘
              │
              ▼
         ┌─────────┐
         │Compress  │ → ZIP
         └────┬────┘
              │
    Generate random session key Ks
              │
    ┌─────────┼─────────────┐
    ▼         │             ▼
Encrypt       │         Encrypt Ks
compressed    │         with KUb
data with Ks  │         (RSA)
(AES/3DES)    │
    │         │             │
    └─────────┼─────────────┘
              │
         E(Ks, Compressed(M||DS)) || E(KUb, Ks)
              │
              ▼
         Base64 Encoding (Radix-64)
              │
              ▼
         Sent via Email
              │
    ──────────┼─────────────────────────>
              │
         RECEIVER:
         1. Base64 Decode
         2. Decrypt Ks using KRb (private key)
         3. Decrypt message using Ks
         4. Decompress
         5. Separate M and DS
         6. Verify DS using KUa (Alice's public key)
         7. Hash M and compare with decrypted DS
         → If match: Authenticated + Confidential ✓
```

### PGP Services Summary:
| Service | How Achieved |
|---------|-------------|
| **Confidentiality** | Symmetric encryption (AES) + session key encrypted with receiver's public key |
| **Authentication** | Digital signature using sender's private key |
| **Integrity** | Hash function (SHA) |
| **Compression** | ZIP compression (before encryption) |
| **Compatibility** | Base64/Radix-64 encoding for email systems |
| **Segmentation** | Large messages split into max size segments |

---

## Q2. Explain IPSec Protocol. Explain Transport and Tunnel Modes, AH and ESP. [10 marks]
**[Asked: Dec 2023, May 2025]**

### IPSec (Internet Protocol Security):
- Network layer security protocol suite
- Provides: Authentication, Integrity, Confidentiality, Anti-replay protection
- Operates at IP layer — transparent to applications
- Used in VPNs (Virtual Private Networks)

### Two Protocols in IPSec:

**1. AH (Authentication Header):**
- Provides: Authentication + Integrity + Anti-replay
- Does NOT provide confidentiality (no encryption)
- Covers entire IP packet including header (in transport mode)
- Protocol number: 51

**AH Header Format:**
```
┌──────────────┬──────────────┬──────────────┐
│ Next Header  │ Payload Len  │ Reserved     │
├──────────────┴──────────────┴──────────────┤
│        Security Parameter Index (SPI)       │
├─────────────────────────────────────────────┤
│           Sequence Number                   │
├─────────────────────────────────────────────┤
│     Authentication Data (ICV - HMAC)        │
└─────────────────────────────────────────────┘
```

**2. ESP (Encapsulating Security Payload):**
- Provides: Confidentiality + Authentication + Integrity + Anti-replay
- Encrypts the payload
- Protocol number: 50

**ESP Header Format:**
```
┌─────────────────────────────────────────────┐
│        Security Parameter Index (SPI)       │
├─────────────────────────────────────────────┤
│           Sequence Number                   │
├─────────────────────────────────────────────┤
│     ┌─────────────────────────────┐         │
│     │    Payload Data (encrypted) │         │
│     │                             │         │
│     │    Padding                  │         │
│     │    Pad Length | Next Header │         │
│     └─────────────────────────────┘         │
├─────────────────────────────────────────────┤
│     Authentication Data (optional ICV)      │
└─────────────────────────────────────────────┘
```

### Two Modes of Operation:

**Transport Mode:**
```
┌────────────┬──────────┬──────────────────┐
│ Original   │ IPSec    │ Original         │
│ IP Header  │ Header   │ Payload          │
│            │ (AH/ESP) │ (TCP/UDP + Data) │
└────────────┴──────────┴──────────────────┘
                          ▲
                   Protected area (AH: authenticated; ESP: encrypted)

- Protects payload only, original IP header stays
- Used for end-to-end communication (host-to-host)
- Less overhead
```

**Tunnel Mode:**
```
┌────────────┬──────────┬────────────────────────────┐
│ New IP     │ IPSec    │ Original IP Header +        │
│ Header     │ Header   │ Original Payload            │
│            │ (AH/ESP) │ (entire original packet)    │
└────────────┴──────────┴────────────────────────────┘
                          ▲
                   Protected area (entire original packet)

- Protects entire original IP packet
- New IP header added
- Used for gateway-to-gateway (VPN tunnels)
- More overhead but better security
```

### Comparison Diagram:
```
TRANSPORT MODE:
┌──────┐                              ┌──────┐
│Host A│ ◄──── IPSec (Transport) ────►│Host B│
└──────┘      Payload protected       └──────┘

TUNNEL MODE:
┌──────┐    ┌─────────┐     ┌─────────┐    ┌──────┐
│Host A│────│Gateway 1│◄═══►│Gateway 2│────│Host B│
└──────┘    └─────────┘     └─────────┘    └──────┘
              IPSec Tunnel
         Entire packet protected
```

### AH vs ESP:
| Parameter | AH | ESP |
|-----------|-----|-----|
| Authentication | ✓ | ✓ (optional) |
| Integrity | ✓ | ✓ |
| Confidentiality | ✗ | ✓ |
| Anti-replay | ✓ | ✓ |
| IP header protection | ✓ (immutable fields) | ✗ |
| Protocol number | 51 | 50 |
| NAT friendly | ✗ | ✓ |

---

## Q3. What are different types of Firewalls? How is Firewall different from IDS? [10 marks]
**[Asked: Dec 2022, May 2023, May 2024, Dec 2024, May 2025]**

### What is a Firewall?
- Network security device that monitors and controls incoming/outgoing network traffic
- Acts as a barrier between trusted internal network and untrusted external network
- Based on predetermined security rules

### Firewall Diagram:
```
                    ┌──────────────┐
  INTERNET         │              │        INTERNAL
  (Untrusted) ◄───►│   FIREWALL   │◄──────► NETWORK
                    │              │        (Trusted)
                    └──────────────┘
                     Rules:
                     ✓ Allow HTTP (80)
                     ✓ Allow HTTPS (443)
                     ✗ Block Telnet (23)
                     ✗ Block unknown
```

### Types of Firewalls:

**1. Packet Filtering Firewall:**
- Operates at Network Layer (Layer 3)
- Examines: Source/Destination IP, Port numbers, Protocol type
- Makes allow/deny decisions based on header information
- **Fast but limited** — cannot inspect packet content
- Example: Router ACLs

**2. Stateful Inspection Firewall:**
- Operates at Network + Transport Layer (Layer 3-4)
- Maintains **state table** of active connections
- Tracks the state of network connections (TCP handshake, etc.)
- More secure than packet filtering — understands connection context
- Example: iptables, Windows Firewall

**3. Application-Level Gateway (Proxy Firewall):**
- Operates at Application Layer (Layer 7)
- Acts as **proxy** between client and server
- Inspects packet CONTENT (not just headers)
- Can filter based on application data (URL, file type, content)
- **Most secure** but slowest
- Example: Squid proxy

**4. Circuit-Level Gateway:**
- Operates at Session Layer (Layer 5)
- Monitors TCP handshake to determine if session is legitimate
- Does not inspect packet content
- Creates a circuit between internal and external systems
- Example: SOCKS proxy

**5. Next-Generation Firewall (NGFW):**
- Combines traditional firewall + IDS/IPS + application awareness
- Deep packet inspection, SSL inspection, user identity tracking
- Example: Palo Alto, Fortinet

### Comparison Table:
| Type | Layer | Inspects | Speed | Security |
|------|-------|----------|-------|----------|
| Packet Filter | 3 | Headers only | Fastest | Low |
| Stateful | 3-4 | Headers + State | Fast | Medium |
| Application Proxy | 7 | Full content | Slowest | Highest |
| Circuit Level | 5 | TCP handshake | Moderate | Medium |
| NGFW | 3-7 | Everything | Moderate | Very High |

### Firewall vs IDS:

| Parameter | Firewall | IDS |
|-----------|----------|-----|
| **Function** | Prevents unauthorized access | Detects intrusions/attacks |
| **Action** | Blocks/allows traffic | Alerts/logs (passive) |
| **Placement** | At network perimeter | Inside network |
| **Type** | Prevention tool | Detection tool |
| **Response** | Active (blocks traffic) | Passive (sends alerts) |
| **Focus** | External threats | Internal + External threats |
| **Rules** | Allow/Deny based on rules | Signature/Anomaly-based |
| **Performance** | Inline (all traffic passes through) | Can be out-of-band |

---

## Q4. Draw and Describe X.509 Digital Certificate Format. [10 marks]
**[Asked: May 2023, Dec 2023, May 2024, May 2025]**

### What is X.509 Certificate?
- Standard format for public key certificates
- Issued by Certificate Authority (CA)
- Binds an identity to a public key
- Used in SSL/TLS, HTTPS, email encryption

### X.509 Certificate Format Diagram:
```
┌─────────────────────────────────────────────┐
│              X.509 CERTIFICATE              │
├─────────────────────────────────────────────┤
│  Version (V1, V2, or V3)                   │
├─────────────────────────────────────────────┤
│  Serial Number (unique per CA)              │
├─────────────────────────────────────────────┤
│  Signature Algorithm Identifier             │
│  (e.g., SHA256withRSA)                      │
├─────────────────────────────────────────────┤
│  Issuer Name                                │
│  (CA's Distinguished Name)                  │
│  e.g., CN=VeriSign CA, O=VeriSign Inc.      │
├─────────────────────────────────────────────┤
│  Validity Period                            │
│  ├── Not Before (start date)                │
│  └── Not After (expiry date)                │
├─────────────────────────────────────────────┤
│  Subject Name                               │
│  (Certificate owner's Distinguished Name)   │
│  e.g., CN=www.example.com, O=Example Inc.   │
├─────────────────────────────────────────────┤
│  Subject's Public Key Information           │
│  ├── Algorithm (e.g., RSA)                  │
│  └── Public Key (e, n)                      │
├─────────────────────────────────────────────┤
│  Issuer Unique ID (V2, V3 only)             │
├─────────────────────────────────────────────┤
│  Subject Unique ID (V2, V3 only)            │
├─────────────────────────────────────────────┤
│  Extensions (V3 only)                       │
│  ├── Key Usage                              │
│  ├── Subject Alt Name                       │
│  ├── Basic Constraints                      │
│  └── CRL Distribution Points               │
├─────────────────────────────────────────────┤
│  Certificate Signature Algorithm            │
├─────────────────────────────────────────────┤
│  Certificate Signature Value                │
│  (CA's digital signature over all above)    │
└─────────────────────────────────────────────┘
```

### Field Descriptions:

| Field | Description |
|-------|-------------|
| **Version** | V1 (basic), V2 (unique IDs), V3 (extensions) |
| **Serial Number** | Unique integer assigned by CA to each certificate |
| **Signature Algorithm** | Algorithm used by CA to sign (e.g., RSA-SHA256) |
| **Issuer** | CA that issued and signed the certificate |
| **Validity** | Time period during which certificate is valid |
| **Subject** | Entity the certificate identifies |
| **Public Key** | Subject's public key + algorithm identifier |
| **Extensions** | Additional info — key usage, constraints, CRL |
| **Signature** | CA's digital signature — ensures authenticity |

### Certificate Verification Process:
```
1. Extract CA's public key from CA's certificate
2. Decrypt the signature on the certificate using CA's public key
3. Hash the certificate contents (excluding signature)
4. Compare decrypted signature with computed hash
5. If match → Certificate is authentic ✓
6. Check validity period, revocation status (CRL/OCSP)
```

---

## Q5. What are the different components of IDS? Explain different approaches. [10 marks]
**[Asked: Dec 2022, QB Q11]**

### IDS (Intrusion Detection System):
- Software/hardware that monitors network traffic for suspicious activity
- Generates alerts when potential threats are detected
- **Passive** — detects and reports but doesn't block

### IDS Components:
```
┌─────────────────────────────────────────────────┐
│                    IDS SYSTEM                    │
│                                                  │
│  ┌──────────┐    ┌──────────────┐   ┌─────────┐│
│  │ Sensor/  │───>│  Analysis    │──>│Response │ │
│  │ Agent    │    │  Engine      │   │Manager  │ │
│  │(captures │    │(analyzes     │   │(alerts, │ │
│  │ traffic) │    │ patterns)    │   │ logs)   │ │
│  └──────────┘    └──────────────┘   └─────────┘│
│       │                │                  │     │
│       ▼                ▼                  ▼     │
│  ┌──────────┐    ┌──────────────┐   ┌─────────┐│
│  │  Data    │    │  Knowledge  │   │Dashboard│ │
│  │Collection│    │  Base/Rules │   │& Console│ │
│  └──────────┘    └──────────────┘   └─────────┘│
└─────────────────────────────────────────────────┘
```

**1. Sensors/Agents:** Collect data from network/host
**2. Analysis Engine:** Core component — analyzes collected data
**3. Knowledge Base:** Contains rules, signatures, baseline profiles
**4. Response Manager:** Generates alerts, logs events, notifies admin
**5. Console/Dashboard:** User interface for management and monitoring

### IDS Approaches:

**1. Signature-Based Detection (Misuse Detection):**
- Compares observed activity against **known attack patterns** (signatures)
- Like antivirus — maintains database of attack signatures
- **Advantage:** High accuracy for known attacks, low false positives
- **Disadvantage:** Cannot detect **zero-day/unknown attacks**

**2. Anomaly-Based Detection:**
- Builds baseline of **normal behavior** profile
- Flags deviations from normal as suspicious
- Uses statistical analysis, machine learning, neural networks
- **Advantage:** Can detect **new/unknown attacks**
- **Disadvantage:** High **false positive** rate, needs training period

**3. Stateful Protocol Analysis:**
- Compares observed events with **predetermined profiles of normal protocol behavior**
- Vendor-defined protocol models
- **Advantage:** Can detect protocol violations
- **Disadvantage:** Resource-intensive, protocol-specific

### Types of IDS:
| Type | NIDS (Network) | HIDS (Host) |
|------|----------------|-------------|
| **Monitors** | Network traffic | Host system activity |
| **Placement** | Network segments | Individual hosts |
| **Detects** | Network attacks | File modifications, logins |
| **Example** | Snort, Suricata | OSSEC, Tripwire |
