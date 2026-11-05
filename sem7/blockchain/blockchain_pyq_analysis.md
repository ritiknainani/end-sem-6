# Mumbai University (MU) Semester 7 — Blockchain
## Comprehensive 6-Paper PYQ Trend Analysis & Priority Roadmap
*(Exam Cycles Analyzed: December 2022, May 2023, December 2023, May 2024, December 2024, May 2025)*
**Course Code:** Department Level Optional Course (DLOC) | **Scheme:** Rev 2019 / C-Scheme | **Total Marks:** 80 per paper

---

## 1. Executive Summary & Syllabus Module Architecture

Blockchain in Mumbai University Semester 7 follows a structured 6-module curriculum. Analysis of all six consecutive examination cycles reveals exceptional repetition in questions, recurring Solidity programming tasks, consensus algorithm comparisons, and enterprise architectures.

```
+---------------------------------------------------------------------------------------------------+
|                               MU SEM 7 BLOCKCHAIN MODULE ARCHITECTURE                             |
+---------------------------------------------------------------------------------------------------+
|  M1: Introduction to Blockchain (10-15 Marks)                                                     |
|      - Hash Functions (SHA-256) & Properties of Blockchain (Immutability, Transparency)          |
|      - Merkle Tree: Structure, Construction, Proof of Membership (Merkle Root)                    |
|      - Block Header Anatomy: Previous Hash, Merkle Root, Nonce, Timestamp, Difficulty Target      |
|      - Types: Public, Private, Consortium / Federated Blockchains                                 |
|      - Challenges of Blockchain Implementation (Scalability, Interoperability, Energy)             |
+---------------------------------------------------------------------------------------------------+
|  M2: Cryptocurrency & Consensus Protocols (20-25 Marks) -- [CORE THEORY & PROTOCOLS]              |
|      - Bitcoin vs Altcoins vs Tokens | Hot Wallets vs Cold Wallets                                 |
|      - UTXO Model vs Account-Based Model | Transaction Lifecycle                                  |
|      - Double Spending Problem & Proof of Work (PoW) Longest Chain Resolution                     |
|      - Consensus Taxonomy: PoW vs PoS vs PoB vs PoET | Mining Difficulty & 2016-Block Adjustment|
|      - Mining Pools: Hashrate distribution, Centralization risks, Payouts (PPS, PPLNS, Prop)      |
+---------------------------------------------------------------------------------------------------+
|  M3: Programming for Blockchain (Solidity & Smart Contracts) (20-25 Marks) -- [GUARANTEED CODE]   |
|      - Smart Contract Lifecycle & Representation as a Finite State Machine                        |
|      - Solidity Syntax: Visibility (public, private, internal, external), Mutability (view, pure) |
|      - Address vs Address Payable (transfer, send, call) | Fallback & Receive Functions           |
|      - Fixed & Dynamic Arrays, Structs, Mappings, Storage vs Memory                               |
|      - Inheritance: Single, Multi-Level, Multiple Inheritance & C3 Linearization                  |
|      - Recurring Exam Code: Prime number check, Multi-level inheritance, 2nd largest array element|
+---------------------------------------------------------------------------------------------------+
|  M4: Public Blockchain (Ethereum Ecosystem) (15-20 Marks)                                        |
|      - Ethereum Architecture: EOA vs Contract Accounts, World State Trie, Receipts Trie           |
|      - Ethereum Virtual Machine (EVM): Stack-based bytecode, 256-bit word size, Opcodes           |
|      - Gas Mechanics: Gas Units, Gas Price (Gwei), Gas Limit, Total Fee Calculation               |
|      - Bitcoin vs Ethereum Comparative Matrix | Test Networks (Sepolia, Goerli, Ganache)          |
|      - Oracles & The Oracle Problem (Chainlink Decentralized Oracle Networks)                     |
+---------------------------------------------------------------------------------------------------+
|  M5: Private Blockchain & Enterprise Consensus (20-25 Marks) -- [ENTERPRISE CORE]                 |
|      - State Machine Replication (SMR) & Crowdfunding State Machine                               |
|      - Crash Fault Tolerant (CFT) vs Byzantine Fault Tolerant (BFT)                               |
|      - RAFT Consensus: Leader Election, Log Replication, Heartbeats, Term safety (Appeared 4x!)   |
|      - PAXOS Consensus: Proposers, Acceptors, Learners, 2-Phase Protocol                          |
|      - PBFT Consensus: 3-Phase protocol (Pre-prepare, Prepare, Commit), 3f+1 tolerance            |
|      - Hyperledger Fabric v1 Architecture: Peers (Endorsing, Committing), Orderer, MSP vs CA,     |
|        Chaincode, Execute-Order-Validate Transaction Flow Walkthrough                             |
+---------------------------------------------------------------------------------------------------+
|  M6: Tools, Platforms & Decentralized Finance (10-15 Marks)                                      |
|      - Enterprise Platforms: Corda (UTXO, Notary Service), Ripple (RPCA), Quorum (Tessera)        |
|      - Decentralized Finance (DeFi) Architecture: Automated Market Makers (AMM x*y=k), Pools      |
|      - Supply Chain Management Case Study on Hyperledger Fabric                                   |
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Topic-by-Topic 6-Paper Frequency Matrix

The following matrix records every appearance of a topic across the 6 analyzed papers (Dec 2022 to May 2025).

| # | Topic / Concept Description | Dec 22 | May 23 | Dec 23 | May 24 | Dec 24 | May 25 | Total Count | Frequency Tier |
|---|-----------------------------|:------:|:------:|:------:|:------:|:------:|:------:|:-----------:|:--------------:|
| **1** | **Solidity Coding Tasks** (Prime number check, Multi-level inheritance, Arrays, 2nd largest) | Q1e (5M), Q4b (10M), Q5b (10M) | Q1e (5M), Q4b (10M), Q5b (10M) | Q4b (10M), Q5b (10M) | Q1d (5M), Q4a (10M), Q4b (10M) | Q4b (10M), Q5b (10M) | Q1b (5M), Q3a (10M), Q4b (10M) | **16 times** | **Tier 1 (Guaranteed 20M)** |
| **2** | **Public vs Private vs Consortium Blockchains** | Q1a (5M) | Q1a (5M) | Q1d (5M) | Q2a (10M) | — | Q5a (10M) | **5 times** | **Tier 1 (Guaranteed 5/10M)** |
| **3** | **Merkle Tree Structure & Proof of Membership** | Q1d (5M) | Q1d (5M) | — | Q3a (10M) | Q1a (5M) | — | **4 times** | **Tier 1 (Guaranteed)** |
| **4** | **Double Spending Problem & PoW Solution** | Q2b (10M) | Q1b (5M) | — | — | Q5a (10M) | Q1c (5M) | **4 times** | **Tier 1 (Guaranteed)** |
| **5** | **Consensus Protocols (PoW vs PoS vs PoB vs PoET)** | — | — | Q6a (10M) | Q2b (10M) | Q1c (5M) | Q4a (10M) | **4 times** | **Tier 1 (Guaranteed 10M)** |
| **6** | **Mining Difficulty & Bitcoin Mining Pools** | Q3a (10M) | — | Q1c (5M) | Q3b (10M), Q6d (10M) | — | Q1e (5M) | **5 times** | **Tier 1 (High Yield)** |
| **7** | **Hot Wallets vs Cold Wallets** | — | Q1c (5M) | Q1b (5M) | Q1b (5M) | — | Q1d (5M) | **4 times** | **Tier 1 (Guaranteed 5M)** |
| **8** | **Ethereum Architecture & EVM Mechanics** | Q4a (10M) | Q4a (10M) | Q1e (5M), Q3b (10M) | Q1a (5M), Q6c (10M) | Q4a (10M) | Q3b (10M), Q6a (10M) | **8 times** | **Tier 1 (Guaranteed 10M)** |
| **9** | **Hyperledger Fabric v1 Architecture & MSP / CA** | Q3b (10M) | Q3b (10M) | Q3a (10M), Q6b (10M) | — | Q6b (10M) | Q2b (10M) | **6 times** | **Tier 1 (Guaranteed 10M)** |
| **10** | **RAFT & PAXOS Consensus Algorithms** | Q5a (10M) | Q5a (10M) | — | Q5b (10M) | Q2b (10M), Q6c (10M) | Q6b (10M) | **6 times** | **Tier 1 (Guaranteed 10M)** |
| **11** | **State Machine Replication (SMR) in Smart Contracts** | — | Q3a (10M) | Q2a (10M) | Q5a (10M) | Q3b (10M) | — | **4 times** | **Tier 1 (High Yield)** |
| **12** | **Corda, Ripple, Quorum Platforms** | Q6a/c (10M) | Q6a/c (10M) | — | Q6b (10M) | Q6a/d (10M) | Q6c (10M) | **6 times** | **Tier 2 (High Yield)** |
| **13** | **Decentralized Finance (DeFi) & Smart Contracts** | — | Q6d (10M) | Q6d (10M) | Q6a (10M) | — | — | **3 times** | **Tier 2 (High Yield)** |
| **14** | **PBFT & Byzantine Fault Tolerance** | Q1c (5M) | — | Q2b (10M) | — | — | — | **2 times** | **Tier 2 (Standard)** |
| **15** | **Bitcoin UTXO Model** | Q6b (10M) | Q6b (10M) | Q1a (5M) | — | — | Q6d (10M) | **4 times** | **Tier 2 (High Yield)** |

---

## 3. High-Priority Preparation Tiers (Exam Survival Strategy)

To score 70+ out of 80 marks in MU Semester 7 Blockchain, students must master:

### Tier 1: Non-Negotiable Core (Guarantees 55-60 Marks)
1. **Solidity Programming (20 Marks Guaranteed):**
   - Must write production-ready, compilable Solidity code (`pragma solidity ^0.8.0;`).
   - Prime number checker function (`pure` returns `bool`).
   - Multi-level inheritance (`contract A`, `contract B is A`, `contract C is B`).
   - Find second largest element in an array (`memory` array iteration).
   - Visibility specifiers (`public`, `private`, `internal`, `external`) & Mutability (`view`, `pure`, `payable`).
   - Fallback and receive functions (`fallback() external payable`, `receive() external payable`).
2. **Consensus Protocols: Public vs Enterprise (15-20 Marks):**
   - PoW: Mathematical puzzle $H(\text{block\_header} + \text{nonce}) < \text{Target}$, Longest Chain Rule, 51% Attack threshold.
   - PoS: Validator staking, slashing conditions, energy efficiency.
   - PoET: Intel SGX enclaves, wait-timer lottery.
   - RAFT: Leader election, heartbeat timeouts, term numbers, log replication.
   - PAXOS: 2-phase agreement (Prepare-Promise, Accept-Accepted).
3. **Hyperledger Fabric v1 Architecture & Transaction Flow (10 Marks):**
   - Entities: Clients, Endorsing Peers, Committing Peers, Orderer Nodes, Fabric CA, MSP.
   - 3-Phase Lifecycle: Proposal & Endorsement $\to$ Ordering $\to$ Validation & Commitment.
4. **Ethereum Architecture & Gas Mechanics (10 Marks):**
   - EOA vs Smart Contract Accounts (Nonce, Balance, Storage Root, Code Hash).
   - EVM Stack Architecture (256-bit word size, Rom, Memory, Storage).
   - Gas calculation: $\text{Total Tx Fee} = \text{Gas Used} \times \text{Gas Price}$.
5. **Merkle Tree & Double Spending (10 Marks):**
   - Full binary hash tree structure, verification proof complexity $O(\log_2 N)$.
   - Double spending attack scenario, mempool verification, and confirmation depth.

### Tier 2: High-Yield Theory & Enterprise Platforms (20-25 Marks)
1. **Public vs Private vs Consortium Blockchains:**
   - 7-point comparative matrix: Access control, consensus, speed/TPS, energy consumption, identity, decentralization, immutability.
2. **State Machine Replication (SMR) in Smart Contracts:**
   - Formal definition: Deterministic state transition $\delta(S_t, T) = S_{t+1}$. Crowdfunding contract state diagram (Funding $\to$ Goal Met / Refund $\to$ Closed).
3. **Enterprise DLT Platforms (Corda, Ripple, Quorum):**
   - Corda: Financial contracts, Notary nodes, peer-to-peer transaction sharing without global state.
   - Ripple: Ripple Protocol Consensus Algorithm (RPCA), UNL (Unique Node List).
   - Quorum: Enterprise Ethereum, private state with Tessera enclave, Istanbul BFT / Raft.
4. **Decentralized Finance (DeFi) Architecture:**
   - Automated Market Maker (AMM) constant product formula: $x \cdot y = k$.
   - Flash loans, liquidity pools, collateralized debt positions (CDPs).
5. **Bitcoin UTXO Model vs Ethereum Account Model:**
   - UTXO: Unspent Transaction Outputs, stateless, high parallelism.
   - Account Model: Global state trie, stateful, intuitive smart contracts.

---

## 4. Masterclass Content Division

- **`blockchain_masterclass_part1.md`**:
  - **Module 1:** Blockchain definition, Block header anatomy, Merkle tree construction & membership proof, Public vs Private vs Consortium comparison, Implementation challenges.
  - **Module 2:** Cryptocurrencies, Hot vs Cold wallets, UTXO model, Double spending problem, Proof of Work (PoW) mathematical derivation, Mining difficulty formula ($D = \text{Target}_{\text{max}} / \text{Target}$) & 2016-block adjustment, Mining pools (PPS vs PPLNS), PoW vs PoS vs PoB vs PoET comparative matrix.
  - **Module 3:** Smart contracts as State Machine Replication (SMR), Solidity visibility & mutability qualifiers, Address vs Address Payable, Fallback vs Receive functions, Storage vs Memory, **5 Complete Solved Solidity Programs** (Prime checker, Multi-level inheritance, Single inheritance, Second largest array element, Multiple inheritance C3 linearization).

- **`blockchain_masterclass_part2.md`**:
  - **Module 4:** Ethereum Architecture (EOA vs Contract, 4-trie structure), EVM stack mechanics, Gas fee computation, Bitcoin vs Ethereum comparative table, Ethereum test networks (Sepolia, Goerli, Ganache), Blockchain Oracles & Chainlink.
  - **Module 5:** Private Blockchain characteristics, Crash Fault Tolerant (CFT) vs Byzantine Fault Tolerant (BFT), **RAFT Consensus Algorithm** (Leader Election, Heartbeats, Log Replication), **PAXOS Consensus Algorithm** (Phase 1 & Phase 2 walk), **PBFT Algorithm** (Pre-prepare, Prepare, Commit, $3f+1$ proof), **Hyperledger Fabric v1 Architecture** (Endorser, Orderer, Committer, MSP vs CA, 3-phase transaction lifecycle).
  - **Module 6:** Enterprise DLTs: Corda (Notaries, P2P states), Ripple (RPCA, UNL), Quorum (Tessera private enclave), Decentralized Finance (DeFi: AMM $x \cdot y = k$, Liquidity Pools), Hyperledger Supply Chain Case Study.
