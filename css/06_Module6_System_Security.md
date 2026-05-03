# MODULE 6: SYSTEM SECURITY & ATTACKS
## CSS — MU Sem 6 Comp Engg

---

## Q1. What is DDoS Attack and how is it launched? [10 marks]
**[Asked: Dec 2022, May 2023, Dec 2023, May 2025 — VERY HIGH FREQUENCY]**

### DDoS (Distributed Denial of Service) Attack:
- An attack that aims to make a service/server **unavailable** to legitimate users
- Floods the target with overwhelming traffic from **multiple sources**
- "Distributed" because attack comes from many compromised systems simultaneously

### How DDoS is Launched — Step by Step:

**Phase 1: Building the Botnet (Preparation)**
1. Attacker scans internet for **vulnerable systems** (weak passwords, unpatched software)
2. Infects them with **malware/trojan** → turns them into **zombies/bots**
3. Thousands of compromised systems form a **botnet**
4. Attacker controls botnet through **Command & Control (C&C) servers**

**Phase 2: Launching the Attack**
5. Attacker sends **attack command** to C&C server
6. C&C server relays command to all bots
7. All bots simultaneously send massive traffic to target
8. Target server becomes **overwhelmed** and cannot serve legitimate users

### DDoS Attack Diagram:
```
                        ┌──────────┐
                        │ ATTACKER │
                        └────┬─────┘
                             │ Commands
                             ▼
                    ┌─────────────────┐
                    │  C&C Server(s)  │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │  Bot/    │  │  Bot/    │  │  Bot/    │
        │  Zombie 1│  │  Zombie 2│  │  Zombie 3│  ... (thousands)
        └────┬─────┘  └────┬─────┘  └────┬─────┘
             │              │              │
             └──────────────┼──────────────┘
                            │
                    ████████████████
                    █  FLOOD OF   █
                    █  TRAFFIC    █
                    ████████████████
                            │
                            ▼
                    ┌──────────────┐
                    │   TARGET     │
                    │   SERVER     │
                    │  (CRASHED/   │
                    │  OVERLOADED) │
                    └──────────────┘
                            ✗
                  Legitimate users DENIED
```

### Types of DDoS Attacks:

| Type | Layer | Method |
|------|-------|--------|
| **Volumetric** | Network (L3) | UDP Flood, ICMP Flood, DNS Amplification |
| **Protocol** | Transport (L4) | SYN Flood, Ping of Death, Smurf Attack |
| **Application** | Application (L7) | HTTP Flood, Slowloris, DNS Query Flood |

### Specific DDoS Attack Types:
1. **SYN Flood:** Send thousands of SYN packets without completing TCP handshake → exhausts server connection table
2. **UDP Flood:** Send large volume of UDP packets to random ports → server responds with ICMP unreachable → overwhelmed
3. **HTTP Flood:** Send legitimate-looking HTTP requests at massive scale
4. **DNS Amplification:** Send small DNS queries with spoofed source IP → DNS server sends large responses to target
5. **Ping of Death:** Send oversized ICMP packets (>65,535 bytes) → buffer overflow

### Prevention/Mitigation:
1. **Traffic filtering** — block known bad IPs, rate limiting
2. **Content Delivery Networks (CDN)** — distribute traffic across servers
3. **DDoS mitigation services** — Cloudflare, Akamai
4. **Blackhole routing** — redirect attack traffic to null route
5. **Firewall and IDS/IPS** — detect and block attack patterns
6. **Anycast network diffusion** — spread traffic across multiple data centers

---

## Q2. What is ICMP Flood Attack? Explain in Detail. [10 marks]
**[Asked: May 2024]**

### ICMP Flood (Ping Flood):
- Type of DoS attack that floods target with ICMP Echo Request (ping) packets
- Goal: Consume target's bandwidth and processing resources

### How it Works:
1. Attacker sends massive number of **ICMP Echo Request** packets to target
2. Target must process each request and send **ICMP Echo Reply**
3. Both incoming and outgoing bandwidth consumed
4. Eventually target becomes unreachable to legitimate traffic

### ICMP Flood Diagram:
```
   Attacker                              Target Server
      │                                       │
      │──── ICMP Echo Request ───────────────>│
      │──── ICMP Echo Request ───────────────>│
      │──── ICMP Echo Request ───────────────>│ Processing
      │──── ICMP Echo Request ───────────────>│ overload...
      │──── ICMP Echo Request ───────────────>│
      │  ... (thousands per second) ...       │
      │                                       │
      │<──── ICMP Echo Reply ─────────────────│
      │<──── ICMP Echo Reply ─────────────────│ Bandwidth
      │<──── ICMP Echo Reply ─────────────────│ exhausted
      │                                       │
                                              ✗ Server DOWN
```

### Variants:
1. **Ping Flood:** Direct flooding with ping requests
2. **Smurf Attack:** Send ICMP requests to broadcast address with **spoofed source IP** (target's IP) → all hosts on network reply to target
3. **Ping of Death:** Send malformed/oversized ping packets

### Smurf Attack Diagram:
```
   Attacker                  Network (Broadcast)        Target
      │                           │                       │
      │── ICMP Request ──────>   │                       │
      │  (Src: Target's IP)      │                       │
      │  (Dst: Broadcast)        │                       │
      │                     ┌────┴────┐                  │
      │                     │All hosts │                  │
      │                     │respond   │                  │
      │                     └────┬────┘                  │
      │                          │                       │
      │               Host1 ──── ICMP Reply ───────────>│
      │               Host2 ──── ICMP Reply ───────────>│ FLOODED!
      │               Host3 ──── ICMP Reply ───────────>│
      │               ...        ICMP Reply ───────────>│
```

### Prevention:
1. Configure routers to **not forward broadcast-directed ICMP**
2. Configure hosts to **not respond to ICMP broadcast**
3. **Rate limit** ICMP traffic
4. Use **firewall rules** to filter excessive ICMP
5. Enable **ICMP flood detection** on IDS/IPS

---

## Q3. Explain Buffer Overflow Attack. [5 marks]
**[Asked: May 2023, Dec 2023 — Q1]**

### Definition:
A buffer overflow occurs when a program writes more data to a buffer than it can hold, causing data to **overflow into adjacent memory locations**.

### How it Works:
```
Normal Buffer:
┌────────────────────────┐
│  Buffer (allocated)    │ Other memory │
│  "Hello"               │ (safe)       │
└────────────────────────┘

Buffer Overflow:
┌────────────────────────┐
│  Buffer (allocated)    │█████████████│
│  "HelloWorldOverfl"    │ OVERWRITTEN!│
│                        │(return addr)│
└────────────────────────┘
                           ▲
                    Attacker overwrites
                    return address with
                    address of malicious code
```

### Stack-based Buffer Overflow:
```
High Address
┌─────────────────────┐
│    Return Address    │ ← Overwritten with address of shellcode
├─────────────────────┤
│    Saved EBP        │ ← Overwritten
├─────────────────────┤
│    Buffer[12]       │ ← Normal buffer space
│    ████████████████ │ ← Overflow data goes beyond buffer
├─────────────────────┤
│    Local Variables   │
└─────────────────────┘
Low Address
```

### Impact:
1. **Crash the program** — overwritten data corrupts execution
2. **Execute arbitrary code** — attacker injects shellcode
3. **Privilege escalation** — gain root/admin access
4. **System compromise** — full control of target system

### Prevention:
1. **Input validation** — check buffer boundaries
2. **Stack canaries** — random values placed before return address
3. **ASLR** (Address Space Layout Randomization) — randomize memory layout
4. **DEP/NX bit** (Data Execution Prevention) — mark stack as non-executable
5. **Safe functions** — use strncpy() instead of strcpy(), fgets() instead of gets()

---

## Q4. Give Examples of Replay Attacks. List Three General Approaches for Dealing with Replay Attack. [5/10 marks]
**[Asked: Dec 2022, Dec 2024 — Q1]**

### Replay Attack:
An attacker **captures** a valid data transmission and **retransmits** it later to trick the receiver into accepting it as legitimate.

### Diagram:
```
   Alice                    Attacker                    Bob
     │                         │                         │
     │──── Message M ──────────┼──────────────────────>│
     │     (legitimate)        │  ◄── Captures M        │
     │                         │                         │
     │                         │     (Later...)          │
     │                         │                         │
     │                         │──── Message M ────────>│
     │                         │  (Replayed!)            │
     │                         │                 Bob thinks│
     │                         │                 it's from │
     │                         │                 Alice!    │
```

### Examples:
1. **Authentication replay:** Attacker captures login credentials and replays them to gain access
2. **Transaction replay:** Attacker captures a bank transfer request and replays it to repeat the transfer
3. **Kerberos ticket replay:** Attacker captures authentication ticket and uses it to impersonate user

### Three Approaches to Deal with Replay Attacks:

**1. Sequence Numbers:**
- Attach unique incrementing sequence number to each message
- Receiver tracks last sequence number received
- Reject any message with sequence number ≤ last received
- **Problem:** Requires maintaining state for each communicating pair

**2. Timestamps:**
- Include current timestamp in each message
- Receiver checks if timestamp is within acceptable time window (e.g., ±5 minutes)
- Reject messages outside the window
- **Problem:** Requires synchronized clocks between parties

**3. Nonce (Number used Once):**
- Challenge-response mechanism
- Receiver sends random nonce to sender
- Sender includes nonce in response (often signed/encrypted)
- Each session uses different nonce → replay of old response fails
- **Most secure approach** — no need for synchronized clocks or sequence tracking

---

## Q5. Explain Worms and Viruses. [5 marks]
**[Asked: May 2024, May 2025 — Q1]**

### Computer Virus:
- **Malicious program** that attaches itself to legitimate programs/files
- **Requires host** — cannot exist independently
- **Requires human action** to spread (opening file, running program)
- **Self-replicating** — copies itself to other files/programs

**Types of Viruses:**
| Type | Description |
|------|-------------|
| Boot Sector | Infects master boot record |
| File Infector | Attaches to executable files (.exe, .com) |
| Macro Virus | Infects documents (Word, Excel macros) |
| Polymorphic | Changes its code with each infection |
| Metamorphic | Rewrites itself completely |
| Stealth | Hides from antivirus detection |

### Computer Worm:
- **Standalone malicious program** — does NOT need a host
- **Self-replicating** — spreads automatically through networks
- **No human action needed** — exploits vulnerabilities to spread
- Consumes network bandwidth and system resources

**Famous Worms:** Morris Worm (1988), ILOVEYOU (2000), Code Red (2001), Slammer (2003), WannaCry (2017)

### Virus vs Worm:

| Parameter | Virus | Worm |
|-----------|-------|------|
| **Host needed** | Yes (attaches to files) | No (standalone) |
| **Human action** | Required (open file) | Not required |
| **Spread method** | Via infected files | Via network vulnerabilities |
| **Speed of spread** | Slower | Much faster |
| **Network impact** | Minimal | Consumes bandwidth |
| **Replication** | Within system (files) | Across network |
| **Detection** | Antivirus signatures | Network monitoring + AV |
| **Example** | Melissa, CIH | Morris, WannaCry |

---

## Q6. Write Short Notes on Packet Sniffing Attack. [5 marks]
**[Asked: QB Q25]**

### Packet Sniffing:
- **Passive attack** — attacker captures (sniffs) network packets
- Uses special software/hardware to intercept data in transit
- Can capture: usernames, passwords, emails, files, credit card numbers

### How it Works:
```
   Sender                                    Receiver
     │                                          │
     │────── Data Packets ─────────────────────>│
     │     (traveling on network)               │
     │              │                           │
     │              ▼                           │
     │        ┌──────────┐                      │
     │        │ SNIFFER  │                      │
     │        │(captures │                      │
     │        │ packets) │                      │
     │        └──────────┘                      │
     │        Attacker sees                     │
     │        all unencrypted                   │
     │        data!                             │
```

### Tools: Wireshark, tcpdump, Ettercap, Cain & Abel

### Prevention:
1. **Encryption** (HTTPS, SSL/TLS, VPN)
2. **SSH** instead of Telnet
3. **Switched networks** instead of hubs
4. **Network monitoring** for promiscuous mode NICs
5. **WPA3** for WiFi networks

---

## Q7. Write Short Note on ARP Spoofing. [5 marks]
**[Asked: QB Q25]**

### ARP Spoofing (ARP Poisoning):
- Attacker sends **fake ARP (Address Resolution Protocol) messages** on local network
- Links attacker's MAC address with IP address of legitimate host (e.g., default gateway)
- All traffic intended for that IP is redirected to attacker

### Diagram:
```
BEFORE ATTACK:
   Host A                Gateway                Host B
   IP: 10.0.0.5         IP: 10.0.0.1           IP: 10.0.0.10
   MAC: AA:AA            MAC: GG:GG             MAC: BB:BB
   
   ARP Table:            ARP Table:
   10.0.0.1→GG:GG       10.0.0.5→AA:AA

AFTER ARP SPOOFING:
   Host A                Attacker               Gateway
   IP: 10.0.0.5         IP: 10.0.0.99          IP: 10.0.0.1
   MAC: AA:AA            MAC: XX:XX             MAC: GG:GG
   
   ARP Table:                                   ARP Table:
   10.0.0.1→XX:XX  ← POISONED!                10.0.0.5→XX:XX ← POISONED!
   (thinks attacker                            (thinks attacker
    is gateway)                                 is Host A)

   Traffic Flow:
   Host A ───────> Attacker ───────> Gateway
                  (reads/modifies
                   traffic = MITM)
```

### Uses by Attacker:
1. **Man-in-the-Middle:** Intercept and read all traffic
2. **Session Hijacking:** Take over active sessions
3. **DoS:** Drop packets instead of forwarding

### Prevention:
1. **Static ARP entries** for critical servers
2. **Dynamic ARP Inspection (DAI)** on switches
3. **VPN/Encryption** — even if sniffed, data unreadable
4. **ARP monitoring tools** — ARPwatch, XArp
5. **802.1X port-based authentication**
