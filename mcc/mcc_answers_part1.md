# 📝 MCC Complete Answer Guide — Part 1 (TIER 1 & 2)

---

## 1. 📌 IP PACKET DELIVERY TO/FROM MOBILE NODE [10 Marks] — 🔴 6/6

### Answer:

**Mobile IP** allows a mobile node (MN) to move between networks while maintaining its IP address and active connections.

### Key Entities:
| Entity | Role |
|--------|------|
| **Mobile Node (MN)** | Device that moves between networks |
| **Home Agent (HA)** | Router on MN's home network; intercepts packets for MN |
| **Foreign Agent (FA)** | Router on visited network; delivers packets to MN |
| **Home Address** | Permanent IP address of MN |
| **Care-of Address (CoA)** | Temporary address on foreign network |
| **Correspondent Node (CN)** | Any node communicating with MN |

### Packet Delivery Mechanism:

```
┌──────────┐                              ┌──────────┐
│Correspond.│──── Packet to MN's ────────►│  Home    │
│  Node    │     Home Address             │  Agent   │
└──────────┘                              └────┬─────┘
                                               │
                          Intercepts packet,   │
                          Tunnels to CoA       │
                          (IP-in-IP)           │
                                               ▼
                                          ┌──────────┐
                                          │ Foreign  │
                                          │  Agent   │
                                          └────┬─────┘
                                               │
                                          Decapsulates,│
                                          Delivers     │
                                               ▼
                                          ┌──────────┐
                                          │  Mobile  │
                                          │  Node    │
                                          └──────────┘
```

### Step-by-Step:

**Delivery TO Mobile Node (Incoming):**
1. CN sends packet to MN's **home address**
2. **HA intercepts** packet (proxy ARP)
3. HA looks up MN's current **Care-of Address** in binding table
4. HA **tunnels** (encapsulates) packet → sends to CoA
5. **FA receives** tunneled packet, **decapsulates** it
6. FA delivers original packet to MN

**Delivery FROM Mobile Node (Outgoing):**
1. MN sends packet **directly to CN** (standard IP routing)
2. Source address = MN's **home address**
3. Packet routed normally through foreign network
4. **No tunneling needed** for outgoing packets

### Triangle Routing Problem:
```
    CN ───────────────► HA (home)
                         │ tunnel
                         ▼
                        FA ──► MN

Inefficient! Even if CN is near MN,
packets go via HA first.
```

**Solution: Route Optimization** — CN caches MN's CoA and sends directly.

---

## 2. 📌 SNOOPING TCP & MOBILE TCP [10 Marks] — 🔴 6/6

### Snooping TCP:

A **transparent** protocol enhancement at the **base station (BS)** that improves TCP performance over wireless links without modifying end hosts.

**How it works:**
1. BS **buffers** TCP segments sent from CN to MN
2. BS monitors **ACKs** from MN
3. If ACK not received (wireless loss), BS **locally retransmits** from buffer
4. **Hides wireless losses** from the sender (CN)
5. CN's TCP assumes smooth delivery → doesn't reduce congestion window

```
CN ──────────► Base Station ──────────► MN
               (Snooping Agent)
               ┌─────────────┐
               │ Buffers data │
               │ Monitors ACKs│
               │ Local retrans│
               └─────────────┘
```

**Advantages:**
- Transparent to end hosts (no modification needed)
- Prevents unnecessary congestion window reduction
- Fast local retransmission
- Maintains end-to-end TCP semantics

**Disadvantages:**
- Cannot handle **long disconnections** well
- Violates **end-to-end principle** (intermediate node interferes)
- **Encryption** prevents snooping (can't inspect TCP headers)
- Overhead of buffering at BS

### Mobile TCP (M-TCP):

**Splits** the TCP connection into **two segments** at a Supervisory Host (SH):
1. **Wired segment**: CN ↔ SH (standard TCP)
2. **Wireless segment**: SH ↔ MN (optimized TCP)

```
CN ◄──── TCP (wired) ────► SH ◄──── TCP (wireless) ────► MN
                        (Supervisory
                          Host)
```

**Advantages:**
- Handles **frequent disconnections** well
- SH freezes sender's TCP during disconnection (sets window = 0)
- Better for **high error-rate** wireless links
- No unnecessary retransmission by CN

**Disadvantages:**
- **Breaks end-to-end semantics** (two separate connections)
- Requires **SH infrastructure** (not transparent)
- ACK to CN doesn't guarantee MN received data
- Added latency due to split

### Comparison:

| Feature | Snooping TCP | Mobile TCP |
|---------|-------------|------------|
| Approach | Snoop + local retransmit | Split connection |
| Transparency | ✅ Transparent | ❌ Not transparent |
| End-to-end semantics | ✅ Preserved | ❌ Broken |
| Disconnection handling | Poor | ✅ Good |
| Encryption compatible | ❌ No | ✅ Yes |
| Modification needed | Only at BS | SH + protocol stack |

---

## 3. 📌 GSM SYSTEM ARCHITECTURE [10 Marks] — 🔴 5/6

### Answer:

**GSM** (Global System for Mobile Communications) is a **2G** digital cellular standard.

### Architecture Block Diagram:

```
┌─────────────────────────────────────────────────────────┐
│                    GSM ARCHITECTURE                      │
│                                                          │
│  ┌──────────┐    ┌─────────────────┐    ┌────────────┐  │
│  │   MS     │◄──►│      BSS        │◄──►│    NSS     │  │
│  │(Mobile   │    │(Base Station    │    │(Network    │  │
│  │ Station) │    │ Subsystem)      │    │ Switching  │  │
│  └──────────┘    └─────────────────┘    │ Subsystem) │  │
│                                         └────────────┘  │
│       Um              Abis         A                     │
│   (Air Interface)  (BSC-BTS)   (BSC-MSC)                │
└─────────────────────────────────────────────────────────┘
```

### 1. Mobile Station (MS):
- **ME (Mobile Equipment)**: Physical phone/device with IMEI number
- **SIM (Subscriber Identity Module)**: Contains IMSI, authentication key (Ki), A3/A8 algorithms

### 2. Base Station Subsystem (BSS):
| Component | Function |
|-----------|----------|
| **BTS** (Base Transceiver Station) | Radio equipment (antenna, transceiver). Handles radio interface with MS |
| **BSC** (Base Station Controller) | Controls multiple BTSs. Manages handover, frequency allocation, power control |

### 3. Network Switching Subsystem (NSS):
| Component | Function |
|-----------|----------|
| **MSC** (Mobile Switching Center) | Core switch for call routing, handover between BSCs, connects to PSTN |
| **HLR** (Home Location Register) | Permanent database: subscriber info, IMSI, services, current VLR location |
| **VLR** (Visitor Location Register) | Temporary database: info of subscribers currently in MSC area |
| **AuC** (Authentication Center) | Generates security parameters (RAND, SRES, Kc) using Ki |
| **EIR** (Equipment Identity Register) | Database of valid/stolen/faulty mobile equipment (IMEI check) |

### Interfaces:

| Interface | Between | Purpose |
|-----------|---------|---------|
| **Um** | MS ↔ BTS | Air/Radio interface |
| **Abis** | BTS ↔ BSC | BTS control |
| **A** | BSC ↔ MSC | Signaling & traffic |
| **B** | MSC ↔ VLR | Subscriber data queries |
| **C** | MSC ↔ HLR | Routing info for calls |
| **D** | HLR ↔ VLR | Location updates |
| **E** | MSC ↔ MSC | Handover between MSCs |
| **F** | MSC ↔ EIR | Equipment validation |

---

## 4. 📌 GSM SECURITY ALGORITHMS (A3, A5, A8) [10 Marks] — 🔴 5/6

### Answer:

GSM uses **three algorithms** for authentication and encryption:

### A3 — Authentication Algorithm
- Used to **authenticate** the subscriber
- Located in **SIM card** and **AuC**
- Input: **RAND** (128-bit random number) + **Ki** (subscriber's secret key)
- Output: **SRES** (32-bit Signed Response)

### A8 — Key Generation Algorithm
- Generates the **session encryption key (Kc)**
- Input: **RAND** + **Ki**
- Output: **Kc** (64-bit cipher key)

### A5 — Encryption Algorithm
- **Stream cipher** for encrypting voice/data over air interface
- Located in **MS** and **BTS**
- Input: **Kc** + frame number
- Output: Encrypted bitstream
- Versions: A5/1 (strong), A5/2 (weak), A5/3 (KASUMI)

### Authentication Process:

```
    AuC/HLR                    MSC/VLR                    MS (SIM)
       │                         │                          │
       │──── (RAND, SRES, Kc) ──►│                          │
       │     (pre-computed        │                          │
       │      triplets)           │                          │
       │                         │──── RAND ──────────────►│
       │                         │                          │
       │                         │                    ┌─────┴─────┐
       │                         │                    │ A3(RAND,Ki)│
       │                         │                    │ → SRES'    │
       │                         │                    │ A8(RAND,Ki)│
       │                         │                    │ → Kc       │
       │                         │                    └─────┬─────┘
       │                         │                          │
       │                         │◄──── SRES' ─────────────│
       │                         │                          │
       │                    ┌────┴────┐                     │
       │                    │Compare  │                     │
       │                    │SRES=SRES'│                    │
       │                    │YES→Auth │                     │
       │                    │NO→Reject│                     │
       │                    └─────────┘                     │
```

### After Authentication:
- Both sides have **Kc**
- **A5** encrypts all communication using Kc
- Kc changes with each new authentication

---

## 5. 📌 HIDDEN & EXPOSED STATION PROBLEM [10 Marks] — 🟠 4/6

### Hidden Station Problem:

```
     A ←──range──→ B ←──range──→ C
     │              │              │
     └── can't ─────┘── can't ────┘
         hear C          hear A
```

- **A** and **C** are both in range of **B** but NOT in range of each other
- A starts transmitting to B
- C cannot detect A's transmission (carrier sense says "free")
- C starts transmitting to B → **COLLISION at B**
- Neither A nor C knows about the collision

### Exposed Station Problem:

```
     A ←──range──→ B ←──range──→ C ←──range──→ D
```

- **B** is transmitting to **A**
- **C** hears B's transmission (carrier sense says "busy")
- C wants to transmit to **D** (which is away from B)
- C **unnecessarily waits** even though its transmission to D wouldn't interfere
- **Reduced throughput** due to unnecessary deferral

### Solution: RTS/CTS (MACA Protocol)

```
  A                    B                    C
  │                    │                    │
  │──── RTS ─────────►│                    │
  │    (Request       │                    │
  │     to Send)      │                    │
  │                   │──── CTS ──────────►│
  │◄──── CTS ─────────│   (Clear          │
  │    (Clear         │    to Send)       │
  │     to Send)      │                   │
  │                   │                   │
  │═══ DATA ════════►│   C hears CTS,    │
  │                   │   DEFERS sending  │
  │◄──── ACK ─────────│                   │
  │                   │                   │
```

- **RTS**: Sender announces intent to transmit
- **CTS**: Receiver grants permission (also warns hidden nodes)
- **NAV** (Network Allocation Vector): Duration field in RTS/CTS tells others how long to wait
- Solves hidden station: C hears CTS → knows to wait
- Partially solves exposed station: C only defers if it hears CTS for B

---

## 6. 📌 GPRS ARCHITECTURE [10 Marks] — 🟠 4/6

### Answer:

**GPRS** (General Packet Radio Service) is a **2.5G** packet-switched extension to GSM for data services.

### New Components Added to GSM:

| Component | Function |
|-----------|----------|
| **SGSN** (Serving GPRS Support Node) | Tracks MN location, performs authentication, handles packet routing within its area. Similar to MSC for packet data |
| **GGSN** (Gateway GPRS Support Node) | Gateway between GPRS network and external packet data networks (Internet). Similar to GMSC |
| **PCU** (Packet Control Unit) | Added to BSC for packet data handling, manages radio resources for data |
| **GR** (GPRS Register) | Stores GPRS subscriber data (added to HLR) |

### Architecture Diagram:

```
                    ┌──────────────────────────────────┐
                    │       External PDN (Internet)    │
                    └──────────────┬───────────────────┘
                                   │ Gi interface
                              ┌────▼────┐
                              │  GGSN   │ (Gateway)
                              └────┬────┘
                                   │ Gn interface
                              ┌────▼────┐
            ┌─────────────────│  SGSN   │──────────┐
            │                 └────┬────┘          │
            │ Gs                   │ Gb            │ Gr
            │                     │                │
       ┌────▼────┐          ┌─────▼────┐     ┌────▼────┐
       │  MSC/   │          │BSC + PCU │     │  HLR/   │
       │  VLR    │          └────┬─────┘     │  GR     │
       └─────────┘               │            └─────────┘
                            ┌────▼────┐
                            │   BTS   │
                            └────┬────┘
                                 │ Um
                            ┌────▼────┐
                            │   MS    │
                            └─────────┘
```

### Interfaces:

| Interface | Between | Purpose |
|-----------|---------|---------|
| Gb | SGSN ↔ BSS | Packet data transfer |
| Gn | SGSN ↔ GGSN | GPRS backbone (GTP tunnel) |
| Gi | GGSN ↔ External PDN | Connection to Internet |
| Gr | SGSN ↔ HLR | Subscriber data |
| Gs | SGSN ↔ MSC/VLR | Coordination with circuit-switched |

### Key Differences from GSM:
- GSM = **circuit-switched** (voice), GPRS = **packet-switched** (data)
- GPRS adds SGSN, GGSN, PCU
- Supports speeds up to **171.2 kbps** (theoretical)
- Uses time slots dynamically (multiple slots per user)
- Always-on connectivity (no dial-up needed)

---

## 7. 📌 WIRELESS LAN THREATS & SECURITY [10 Marks] — 🟠 4/6

### Wireless LAN Threats:

| Threat | Description |
|--------|-------------|
| **Eavesdropping** | Intercepting wireless signals to read data (passive attack) |
| **Unauthorized Access** | Connecting to network without permission (war driving) |
| **Man-in-the-Middle (MITM)** | Attacker positions between two parties, intercepts/alters data |
| **Denial of Service (DoS)** | Jamming radio signals or flooding with deauth frames |
| **Rogue Access Point** | Fake AP set up by attacker to lure connections |
| **MAC Spoofing** | Attacker clones legitimate device's MAC address |
| **Evil Twin Attack** | AP with same SSID as legitimate AP to capture traffic |
| **Replay Attack** | Capturing and retransmitting valid data to gain access |

### Wi-Fi Security Protocols:

| Protocol | Encryption | Key Length | Security Level |
|----------|-----------|-----------|---------------|
| **WEP** | RC4 stream cipher | 40/104 bit | ❌ Weak (cracked) |
| **WPA** | TKIP (Temporal Key Integrity Protocol) | 128 bit | ⚠️ Moderate |
| **WPA2** | AES-CCMP | 128 bit | ✅ Strong |
| **WPA3** | SAE (Simultaneous Authentication of Equals) | 192/256 bit | ✅✅ Strongest |

---

## 8. 📌 AGENT REGISTRATION & DISCOVERY [10 Marks] — 🟠 4/6

### Agent Discovery:

Process by which MN discovers whether it's on home or foreign network.

**Two Methods:**
1. **Agent Advertisement**: HA/FA periodically broadcasts ICMP messages with CoA info
2. **Agent Solicitation**: MN actively sends solicitation message to discover agents

### Registration Process:

```
    MN                    FA                    HA
    │                     │                     │
    │── Reg Request ────►│                     │
    │   (Home addr,      │── Reg Request ────►│
    │    CoA, lifetime)  │   (relayed)        │
    │                    │                     │
    │                    │                ┌────┴────┐
    │                    │                │Validates │
    │                    │                │Creates   │
    │                    │                │Binding   │
    │                    │                │(HA↔CoA)  │
    │                    │                └────┬────┘
    │                    │                     │
    │                    │◄── Reg Reply ───────│
    │◄── Reg Reply ──────│   (accepted/       │
    │   (status)         │    denied)          │
    │                    │                     │
```

**Registration Request contains:**
- MN's home address, HA address, CoA
- Requested lifetime, identification (for replay protection)
- Extensions for authentication

**Registration Reply contains:**
- Status code (accepted/denied + reason)
- Granted lifetime
- HA address

### Deregistration:
When MN returns to home network → sends registration with **lifetime = 0** → HA removes binding.
