# Mumbai University (MU) Semester 7 — Blockchain
## Masterclass Part 2: Modules 4, 5 & 6 (Ethereum, Enterprise Consensus, Hyperledger & DeFi)
**Course Code:** Department Level Optional Course (DLOC) | **Scheme:** Rev 2019 / C-Scheme | **Applicable Cycles:** Dec 2022 – May 2025

---

# MODULE 4: PUBLIC BLOCKCHAIN (ETHEREUM ECOSYSTEM)

---

## 4.1 Ethereum Architecture: Accounts, Tries & World State
*(Appeared in: Dec 2022 Q4a [10M], May 2023 Q4a [10M], Dec 2023 Q1e/Q3b [10M], May 2024 Q6c [10M], Dec 2024 Q4a [10M], May 2025 Q3b [10M])*

While Bitcoin operates as a decentralized calculator maintaining a UTXO ledger, Ethereum (Vitalik Buterin, 2014) operates as a **Decentralized World Computer** executing a Turing-complete state transition system.

```
+---------------------------------------------------------------------------------------------------+
|                                     ETHEREUM GLOBAL ARCHITECTURE                                  |
+---------------------------------------------------------------------------------------------------+
|  [ETHEREUM BLOCK HEADER]                                                                          |
|  - Previous Hash, Nonce, Timestamp, Difficulty, Block Number                                      |
|  - State Root Hash -------------------+                                                           |
|  - Transactions Root Hash             |                                                           |
|  - Receipts Root Hash                 |                                                           |
+---------------------------------------|-----------------------------------------------------------+
                                        v
| WORLD STATE TRIE (Modified Merkle Patricia Trie):                                                 |
| Maps 160-bit Account Addresses to Account State Tuples:                                           |
|                                                                                                   |
|    Address 0x1a8... ---> [ Nonce | Balance | Storage Root | Code Hash ]                           |
|    Address 0x7c4... ---> [ Nonce | Balance | Storage Root | Code Hash ]                           |
|                                                     |             |                               |
|                                                     v             v                               |
|                                            [Storage Trie]   [EVM Bytecode]                        |
|                                           (Contract Memory) (Static Code)                         |
+---------------------------------------------------------------------------------------------------+
```

### The Two Types of Accounts in Ethereum:
1. **Externally Owned Accounts (EOAs):**
   - Controlled entirely by human users via **private keys**.
   - Contains: Nonce (transaction counter) and Balance (Ether in Wei).
   - Can initiate transactions (send Ether or trigger smart contracts). Has **no code**.
2. **Contract Accounts (Smart Contracts):**
   - Controlled by its **immutable compiled EVM code**, not a private key.
   - Contains: Nonce (number of contracts created), Balance, Storage Root (Merkle Patricia root of persistent variable storage), and Code Hash (hash of EVM bytecode).
   - Executes only when triggered by a transaction from an EOA or an internal call from another contract.

---

### 🌟 Deep-Dive: Complete Workflow of Ethereum [10 Marks] — Nov'25 (Q4a)
> **MU Official Exam Question (Paper Code 42177, Q4a):**
> *"Explain Workflow of Ethereum."*

The operational lifecycle of Ethereum can be formalized as a deterministic state machine transition:
$$\mathbf{\Upsilon(S, T) = S'}$$
Where $S$ is the current World State, $T$ is a transaction, $\Upsilon$ is the Ethereum State Transition Function, and $S'$ is the new resultant World State.

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                          COMPLETE ETHEREUM TRANSACTION WORKFLOW                  │
│                                                                                  │
│  [STEP 1: CREATION & SIGNING]                                                    │
│  EOA User creates raw transaction: [Nonce, GasPrice, GasLimit, To, Value, Data]  │
│  Signs with ECDSA Private Key (secp256k1) yielding signature (v, r, s)           │
│                           │                                                      │
│                           ▼                                                      │
│  [STEP 2: MEMPOOL BROADCAST]                                                     │
│  Transaction propagated over P2P Gossip protocol to validator/miner mempools     │
│                           │                                                      │
│                           ▼                                                      │
│  [STEP 3: PRE-EXECUTION VALIDATION]                                              │
│  • Signature valid? • Nonce == current account nonce?                            │
│  • Sender balance >= (GasLimit * GasPrice + Value)?                              │
│  • Upfront fee deducted: Sender Balance -= (GasLimit * GasPrice)                 │
│  • Sender Nonce incremented by 1                                                 │
│                           │                                                      │
│                           ▼                                                      │
│  [STEP 4: EVM BYTECODE EXECUTION]                                                │
│  • If 'To' is EOA: Transfer value directly.                                      │
│  • If 'To' is Contract (or empty to create contract):                            │
│    Instantiate EVM stack, load contract bytecode into ROM.                       │
│    Execute opcodes (PUSH, ADD, MSTORE, SSTORE); deduct gas per opcode.           │
│                           │                                                      │
│                           ▼                                                      │
│  [STEP 5: STATE FINALIZATION & GAS REFUND]                                       │
│  • Calculate remaining unused gas: GasRemaining = GasLimit - GasUsed             │
│  • Refund remaining gas: Sender Balance += (GasRemaining * GasPrice)             │
│  • Transfer fee to block builder/validator: Miner Fee = GasUsed * GasPrice       │
│  • Update World State Trie root hash, Transaction Root, and Receipts Root        │
│                           │                                                      │
│                           ▼                                                      │
│  [STEP 6: BLOCK PACKAGING & CONSENSUS]                                           │
│  Block proposed by validator; attested by committee via PoS (Casper FFG/LMD GHOST)│
│  Block finalized and appended permanently to blockchain ledger.                  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

1. **Step 1: Transaction Creation & Cryptographic Signing:**
   - The user constructs a payload containing: Nonce (prevents replay attacks), Gas Price, Gas Limit, Recipient Address (`To`), Ether Amount (`Value`), and optional Bytecode / Call Data (`Data`).
   - The user signs the SHA3/Keccak-256 transaction hash with their private key using the **ECDSA secp256k1** elliptic curve algorithm, generating signature components $(v, r, s)$.
2. **Step 2: P2P Network Propagation & Mempool Buffering:**
   - The signed transaction is serialized and broadcast across the Ethereum devp2p network. Nodes verify cryptographic validity and place it into their local **Memory Pool (Mempool)**.
3. **Step 3: Pre-Execution Validation:**
   - Before executing code, the validating node verifies:
     - The signature correctly recovers the sender's public key (EOA address).
     - The transaction nonce matches the sender's account nonce exactly.
     - The sender has sufficient Ether balance to pay the **maximum upfront cost**:
       $$\text{Max Cost} = (\text{Gas Limit} \times \text{Gas Price}) + \text{Value}$$
     - The upfront gas fee is immediately deducted, and the sender's nonce increments by 1.
4. **Step 4: EVM Execution:**
   - If `To` is empty, the EVM runs the initialization bytecode to deploy a **new smart contract**, returning the runtime bytecode stored in state.
   - If `To` is a smart contract address, the EVM invokes the contract's code, feeding `Data` as input. Opcodes consume gas according to the EVM gas schedule.
5. **Step 5: Post-Execution Gas Settlement:**
   - Unused gas is refunded to the sender. If an `Out of Gas` error occurs, state changes roll back, but spent gas is forfeited to the miner.
6. **Step 6: World State Update & Block Finalization:**
   - Modified accounts generate a new **Merkle Patricia State Root Hash**. The transaction receipt (gas used, logs, event topics) is added to the Receipts Trie. The proposed block is validated by consensus and committed to the canonical chain.

---

## 4.2 The Ethereum Virtual Machine (EVM) & Gas Mechanics
*(Appeared in: Dec 2023 Q3b [10M], May 2024 Q1a [5M], Dec 2024 Q4a [10M], May 2025 Q6a [10M])*

### EVM Architecture
The EVM is a sandboxed, quasi-Turing-complete virtual machine that executes bytecode instructions deterministically across every node in the Ethereum network.

```
+---------------------------------------------------------------------------------------------------+
|                                      EVM EXECUTION ARCHITECTURE                                   |
+---------------------------------------------------------------------------------------------------+
|  [ TRANSIENT / EXECUTION CONTEXT ]                   [ PERSISTENT ON-CHAIN STORAGE ]              |
|                                                                                                   |
|  +--------------------------------------------+      +------------------------------------------+ |
|  | EVM STACK:                                 |      | STORAGE (Contract State):                | |
|  | - Stack-based engine (max depth 1024).     |      | - Key-value store (2^256 slots).         | |
|  | - Word size: 256 bits (32 bytes).          |      | - Persistent across transactions.        | |
|  | - Opcodes: PUSH, POP, DUP, SWAP, ADD, MSTORE|     | - Opcodes: SLOAD (100-2100 gas),         | |
|  +--------------------------------------------+      |            SSTORE (up to 20,000 gas!).   | |
|                        |                             +------------------------------------------+ |
|                        v                                                                          |
|  +--------------------------------------------+      +------------------------------------------+ |
|  | MEMORY (Volatile Scratchpad):              |      | ROM / CODE:                              | |
|  | - Byte-addressable linear array.           |      | - Immutable compiled smart contract      | |
|  | - Cleared between transaction calls.       |      |   bytecode deployed on-chain.            | |
|  | - Expands dynamically (Gas scales quad.). |      +------------------------------------------+ |
|  +--------------------------------------------+                                                   |
+---------------------------------------------------------------------------------------------------+
```

### Gas Mechanics & Halting Problem Resolution
Because Ethereum executes Turing-complete code containing arbitrary `while` loops, it is vulnerable to the **Halting Problem** (infinite loops that could freeze the entire global network).
Ethereum solves this by requiring every computational opcode to consume a specified fee denominated in **Gas**.

#### Gas Formula:
$$\mathbf{\text{Total Transaction Fee (Ether)} = \text{Gas Used} \times \text{Gas Price}}$$
- **Gas Units (Work Measure):** Fixed measure of computational difficulty (e.g., `ADD` = 3 gas, `SHA3` = 30 gas, `SSTORE` = 20,000 gas to write to new storage).
- **Gas Price (Gwei):** The amount of Ether the user offers to pay per unit of gas ($1 \text{ Gwei} = 10^{-9} \text{ ETH} = 10^9 \text{ Wei}$).
- **Gas Limit:** The maximum amount of gas the user permits the transaction to consume.
  - Standard ETH transfer: Exactly $21,000$ Gas.

#### Out of Gas vs Revert Scenarios:
- **Out of Gas Exception:** If execution exceeds the user-specified Gas Limit, state changes revert immediately, but **the miner retains 100% of the gas fee** as compensation for spent compute.
- **Controlled Revert (`require()` / `revert()`):** State changes revert, but **unconsumed remaining gas is refunded** to the sender.

---

## 4.3 Bitcoin vs Ethereum: Architectural Comparison
*(Appeared in: Dec 2022 Q3a [10M], Dec 2024 Q1b [5M], May 2024 Q1e [5M])*

| Parameter | Bitcoin (BTC) | Ethereum (ETH) |
|:---|:---|:---|
| **Primary Design Philosophy** | Digital gold / Peer-to-peer electronic cash. | Decentralized programmable world computer. |
| **State Model** | **UTXO (Unspent Transaction Output)**. | **Account-Based Model (State Trie)**. |
| **Smart Contract Capability** | Non-Turing-complete Script (no loops). | **Turing-complete Solidity / EVM bytecode**. |
| **Average Block Time** | **10 Minutes**. | **12 Seconds** (Post-Merge Proof of Stake). |
| **Consensus Mechanism** | Proof of Work (SHA-256). | Proof of Stake (Casper / LMD-GHOST). |
| **Block Size / Throughput** | 1–4 MB Block Weight ($\approx 7$ TPS). | Dynamic gas limit ($\approx 15–30$ TPS on L1). |
| **Denomination Hierarchy** | 1 BTC = $10^8$ Satoshis. | 1 ETH = $10^9$ Gwei = $10^{18}$ Wei. |

---

## 4.4 Ethereum Test Networks & Local Development
*(Appeared in: Dec 2023 Q4a [10M], May 2025 Q5b [10M])*

Deploying and testing smart contracts on the Ethereum Mainnet requires real Ether. Developers use **Testnets** that mirror mainnet EVM rules using free, valueless test Ether:

1. **Sepolia Testnet:** Primary recommended PoS testnet for application developers. Features a closed, reliable validator set ensuring network stability.
2. **Holesky Testnet:** Infrastructure and staking testnet designed to test validator scalability.
3. **Goerli / Ropsten / Rinkeby / Kovan (Historical / Deprecated):** Early testnets used across prior years (Ropsten used PoW; Kovan/Rinkeby used PoA).
4. **Local Development Blockchains:**
   - **Ganache / Hardhat Network / Anvil (Foundry):** In-memory local simulated blockchains running on `localhost:8545` providing instantaneous transaction mining and automated test accounts.

---

## 4.5 Blockchain Oracles & The Oracle Problem
*(Appeared in: Syllabus Module 4.2)*

### The Oracle Problem
Blockchains are self-contained, deterministic state machines. A smart contract **cannot natively make external HTTP/API requests** to the outside world (e.g., cannot call `http://api.weather.com` or fetch stock prices).
- *Reason:* If 10,000 validating nodes execute a smart contract that queries an external API, the API might return different values at different milliseconds, destroying consensus.

### Blockchain Oracles
An **Oracle** is a trusted middleware service that fetches external real-world data, signs it with a cryptographic key, and posts it onto the blockchain via an on-chain transaction.

```
+---------------------------------------------------------------------------------------------------+
|                              DECENTRALIZED ORACLE NETWORK (CHAINLINK)                             |
+---------------------------------------------------------------------------------------------------+
|  REAL-WORLD DATA SOURCES                                                                          |
|  [ NASDAQ API ]       [ Binance API ]       [ CoinMarketCap ]       [ Kraken Exchange ]           |
+---------------------------------------------------------------------------------------------------+
          \                   |                     |                    /                          |
           \                  |                     |                   /                           |
            v                 v                     v                  v                            |
| INDEPENDENT CHAINLINK NODE OPERATORS (Off-Chain Reporting - OCR):                                 |
|  - Each node fetches data independently, validates, and signs with private key.                   |
|  - Aggregation: Computes Median Price off-chain to eliminate outliers/bribes.                      |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v (Single aggregated transaction)
| ON-CHAIN SMART CONTRACT (Price Feed Consumer):                                                    |
|  - Verifies multi-signatures of oracle nodes.                                                     |
|  - Supplies tamper-proof price data to DeFi contracts (Aave, Uniswap, Synthetix).                |
+---------------------------------------------------------------------------------------------------+
```

---

## MU Keyword Checklist: Module 4
- [ ] *Externally Owned Accounts (EOA) vs Contract Accounts (Nonce, Balance, Storage Root, Code Hash)*
- [ ] *World State Trie, Modified Merkle Patricia Trie, Account State Tuples*
- [ ] *EVM Architecture: 256-bit Word Size, 1024 Stack Depth, Volatile Memory, Persistent Storage (SLOAD/SSTORE)*
- [ ] *Gas Mechanics: Gas Limit, Gas Price (Gwei), Total Fee = Gas Used $\times$ Gas Price*
- [ ] *Out of Gas (Retains fee) vs Controlled Revert (Refunds unused gas)*
- [ ] *Bitcoin (UTXO, 10 min) vs Ethereum (Account-based, 12 sec, Turing-complete)*
- [ ] *Testnets: Sepolia, Holesky, Ganache Local Environment*
- [ ] *The Oracle Problem: Deterministic Consensus Constraint, Chainlink Decentralized Oracle Networks (DON)*

---
---

# MODULE 5: PRIVATE BLOCKCHAIN & ENTERPRISE CONSENSUS

---

## 5.1 Private Blockchains & State Machine Replication (SMR)
*(Appeared in: May 2023 Q3a [10M], Dec 2023 Q2a [10M], May 2024 Q5a [10M], Dec 2024 Q3b [10M])*

### Enterprise Drivers for Private Blockchains
Enterprises (banks, healthcare, supply chains) require blockchain features without public exposure:
1. **Identified Participants:** Known, KYC-vetted entities; zero anonymous bad actors.
2. **Data Confidentiality:** Commercial pricing and patient records must not broadcast globally.
3. **High Throughput & Low Latency:** Millisecond transaction settlement (>3,000 TPS).
4. **Predictable Cost:** Zero gas transaction fees.

### State Machine Replication (SMR)
State Machine Replication is the foundational paradigm of distributed fault-tolerant computing (Lamport, 1984).
- A distributed service is modeled as an identical deterministic state machine replicated across $N$ servers.
- A **Consensus Protocol** ensures that all replicas receive and process an identical sequence of state-transition inputs from an ordered log:
  $$\delta(S_t, T_k) = S_{t+1}$$

---

## 5.2 Fault Tolerance Models: CFT vs BFT
*(Appeared in: Dec 2022 Q1c [5M], Dec 2023 Q2b [10M])*

```
+---------------------------------------------------------------------------------------------------+
|                                       CFT VS BFT COMPARISON                                       |
+---------------------------------------------------------------------------------------------------+
| Parameter          | Crash Fault Tolerance (CFT)           | Byzantine Fault Tolerance (BFT)      |
+--------------------+---------------------------------------+--------------------------------------+
| Adversarial Model  | Fail-Stop: Nodes may crash, stop, or  | Arbitrary / Malicious: Nodes may lie,|
|                    | experience network latency, but NEVER | collude, forge messages, or exhibit  |
|                    | send corrupted or malicious messages. | two-faced (Byzantine) behavior.      |
+--------------------+---------------------------------------+--------------------------------------+
| Node Requirement   | N >= 2f + 1 (Tolerates f crashes)     | N >= 3f + 1 (Tolerates f traitors)   |
+--------------------+---------------------------------------+--------------------------------------+
| Message Complexity | O(N) linear message exchanges.        | O(N^2) quadratic message rounds.     |
+--------------------+---------------------------------------+--------------------------------------+
| Environmental Fit  | Trusted private enterprise networks   | Semi-trusted consortiums or public   |
|                    | with unified administrative domains.  | cross-organizational networks.       |
+--------------------+---------------------------------------+--------------------------------------+
| Representative     | **RAFT**, **PAXOS**                   | **PBFT**, **IBFT**, **Tendermint**   |
+--------------------+---------------------------------------+--------------------------------------+
```

### Mathematical Derivation of $N \ge 3f + 1$ for BFT:
Let $N$ be the total nodes, and $f$ be the number of Byzantine (malicious) nodes.
1. The system must remain available if $f$ nodes crash (fail to reply) $\implies$ The system must reach agreement using at most $N - f$ responses.
2. Among the $N - f$ responses received, up to $f$ could be from malicious Byzantine nodes giving false information.
3. To ensure that honest nodes constitute a strict majority of the remaining responders:
   $$(N - f) - f > f \implies N - 2f > f \implies \mathbf{N > 3f \implies N_{\text{min}} = 3f + 1}$$

---

## 5.3 The RAFT Consensus Algorithm (Detailed Walkthrough)
*(Appeared in: May 2023 Q5a [10M], May 2024 Q5b [10M], Dec 2024 Q2b [10M], May 2025 Q6b [10M])*

RAFT (Ongaro & Ousterhout, Stanford 2014) is designed for understandability, decomposing consensus into two independent sub-problems: **Leader Election** and **Log Replication**.

```
+---------------------------------------------------------------------------------------------------+
|                                    RAFT STATE TRANSITIONS & ROLES                                 |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|                       +----------------------------------------------------+                      |
|                       |            Times out, starts election              |                      |
|                       v                                                    |                      |
|               +---------------+   Votes from majority of servers    +---------------+             |
|               |   CANDIDATE   | ----------------------------------> |    LEADER     |             |
|               +---------------+                                     +---------------+             |
|                       |                                                    |                      |
|                       | Discovers current leader                           | Discovers server with|
|                       | or higher term                                     | higher term          |
|                       v                                                    v                      |
|               +---------------------------------------------------------------------+             |
|               |                              FOLLOWER                               |             |
|               +---------------------------------------------------------------------+             |
|                       ^                                                    ^                      |
|                       +------------------ Starts Up -----------------------+                      |
+---------------------------------------------------------------------------------------------------+
```

### The Three Phases of RAFT:

1. **Leader Election:**
   - Time is divided into arbitrary numbered **Terms** ($1, 2, 3 \ldots$).
   - Nodes begin as **Followers**. If a follower hears no heartbeat from a leader within a randomized **Election Timeout** ($150\text{ms} - 300\text{ms}$), it increments its term, transitions to **Candidate**, votes for itself, and broadcasts `RequestVote` RPCs.
   - If the candidate receives votes from a **strict majority** ($\lfloor N/2 \rfloor + 1$) of nodes, it becomes the **Leader**.
   - *Split Vote Resolution:* Randomized timeouts ensure that split votes (where two candidates tie) are rapidly resolved as one candidate times out and initiates a new term first.

2. **Log Replication:**
   - The Leader receives client command proposals.
   - The Leader appends the command to its local log as an uncommitted entry, then broadcasts `AppendEntries` RPCs to all followers.
   - When a majority of followers acknowledge writing the entry to their logs, the Leader commits the entry, applies it to its local state machine, and returns the result to the client.
   - The Leader notifies followers of the commit in subsequent heartbeats, prompting followers to apply the entry to their state machines.

3. **Safety Invariants:**
   - **Election Safety:** At most one leader can be elected per term.
   - **Leader Completeness:** If a log entry is committed in a given term, that entry will be present in the logs of the leaders for all higher-numbered terms (a candidate must prove its log is at least as up-to-date as the voter's log to receive a vote).

---

## 5.4 The PAXOS Consensus Protocol
*(Appeared in: Dec 2022 Q5a [10M], Dec 2024 Q6c [10M])*

Leslie Lamport's PAXOS protocol achieves consensus in asynchronous networks with crash failures across three logical roles: **Proposers**, **Acceptors**, and **Learners**.

```
+---------------------------------------------------------------------------------------------------+
|                                    PAXOS 2-PHASE PROTOCOL FLOW                                    |
+---------------------------------------------------------------------------------------------------+
|   PROPOSER                                              ACCEPTORS (Quorum)                        |
|                                                                                                   |
|   [ PHASE 1: PREPARE ]                                                                            |
|   Prepare(n) -----------------------------------------> Receive Prepare(n)                       |
|                                                         If n > highest seen:                      |
|   Promise(n, max_accepted_val) <----------------------- Promise not to accept proposals < n       |
|                                                         Send highest accepted (n_v, v)            |
|                                                                                                   |
|   [ PHASE 2: ACCEPT ]                                                                             |
|   Select v (value of highest n_v from                                                             |
|   promises, or own value if none)                                                                 |
|   Accept(n, v) ---------------------------------------> Receive Accept(n, v)                     |
|                                                         If n >= highest promised:                 |
|   Accepted(n, v) <------------------------------------- Accept proposal; broadcast to Learners   |
+---------------------------------------------------------------------------------------------------+
```

---

## 5.5 Hyperledger Fabric v1 Architecture & Transaction Flow
*(Appeared in: Dec 2022 Q3b [10M], May 2023 Q3b [10M], Dec 2023 Q3a/Q6b [10M], Dec 2024 Q6b [10M], May 2025 Q2b [10M])*

Hyperledger Fabric (Linux Foundation) is an enterprise-grade, permissioned distributed ledger platform featuring a modular **Execute-Order-Validate** architecture (diverging fundamentally from traditional Order-Execute blockchains).

```
+---------------------------------------------------------------------------------------------------+
|                              HYPERLEDGER FABRIC TRANSACTION WORKFLOW                              |
+---------------------------------------------------------------------------------------------------+
|  [ CLIENT APP ]                                                                                   |
|        |                                                                                          |
|        | 1. Submit Proposal (Tx)                                                                  |
|        v                                                                                          |
|  +-------------------------------------------------------+                                        |
|  | ENDORSING PEERS (Peer_1, Peer_2):                     |                                        |
|  | - Verify client signature via MSP.                    |                                        |
|  | - Simulate Chaincode in Docker sandbox (NO LEDGER WRITES).                                     |
|  | - Generate Read/Write Sets + Cryptographic Endorsement.|                                        |
|  +-------------------------------------------------------+                                        |
|        |                                                                                          |
|        | 2. Endorsement Responses (RW Sets + Signatures)                                          |
|        v                                                                                          |
|  [ CLIENT APP verifies endorsements match Endorsement Policy ]                                    |
|        |                                                                                          |
|        | 3. Broadcast Transaction (RW Sets + Signatures)                                         |
|        v                                                                                          |
|  +-------------------------------------------------------+                                        |
|  | ORDERING SERVICE (Raft / Kafka Orderer Nodes):        |                                        |
|  | - Sequences transactions chronologically into blocks. |                                        |
|  | - DOES NOT execute chaincode or inspect RW sets.      |                                        |
|  +-------------------------------------------------------+                                        |
|        |                                                                                          |
|        | 4. Deliver Blocks across Channels                                                        |
|        v                                                                                          |
|  +-------------------------------------------------------+                                        |
|  | COMMITTING PEERS (All Network Peers):                 |                                        |
|  | - Validation Step: Check Endorsement Policy is met.   |                                        |
|  | - Concurrency Check: MVCC read-set version validation. |                                        |
|  | - Commit Step: Append valid block to ledger & update  |                                        |
|  |   World State (LevelDB / CouchDB).                    |                                        |
|  +-------------------------------------------------------+                                        |
+---------------------------------------------------------------------------------------------------+
```

### Core Components of Hyperledger Fabric:
1. **Peers:**
   - **Endorsing Peers:** Execute chaincode simulations and produce signed read/write sets according to endorsement policies.
   - **Committing Peers:** Maintain ledger copies and World State; validate transactions against MVCC conflicts.
   - **Anchor Peers:** Discovered via gossip protocol to bridge cross-organization communication.
2. **Ordering Service (Orderer):** Establishes total global transaction ordering; builds blocks.
3. **Membership Service Provider (MSP) vs Fabric CA:**
   - **Fabric CA (Certificate Authority):** Generates and issues digital X.509 PKI identity certificates.
   - **MSP:** The abstract rules engine that *interprets* certificates, defines organizational roles (Admins, Endorsers, Clients), and enforces access control on channels.
4. **Chaincode:** Smart contracts written in Go, Java, or Node.js executing inside isolated Docker containers.

---

## MU Keyword Checklist: Module 5
- [ ] *State Machine Replication (SMR): Deterministic transitions $\delta(S_t, T) = S_{t+1}$*
- [ ] *Crash Fault Tolerant (CFT, $N \ge 2f+1$) vs Byzantine Fault Tolerant (BFT, $N \ge 3f+1$)*
- [ ] *RAFT: Leader Election, Heartbeats, Randomized Timeouts, Term Numbers, Log Replication*
- [ ] *PAXOS: Proposers, Acceptors, Learners, Phase 1 (Prepare/Promise), Phase 2 (Accept/Accepted)*
- [ ] *PBFT: 3-Phase Protocol (Pre-prepare, Prepare, Commit), $3f+1$ tolerance*
- [ ] *Hyperledger Fabric: Execute-Order-Validate Architecture, Endorsing vs Committing Peers*
- [ ] *Ordering Service (Raft), Read/Write Sets, MVCC (Multi-Version Concurrency Control)*
- [ ] *Fabric CA (Issues X.509 certs) vs MSP (Evaluates certificates and organizational access)*

---
---

# MODULE 6: TOOLS, APPLICATIONS & DECENTRALIZED FINANCE (DEFI)

---

## 6.1 Enterprise DLT Platforms: Corda, Ripple & Quorum
*(Appeared in: Dec 2022 Q6a/c [10M], May 2023 Q6a/c [10M], May 2024 Q6b [10M], Dec 2024 Q6a/d [10M], May 2025 Q6c [10M])*

```
+---------------------------------------------------------------------------------------------------+
|                                 ENTERPRISE DLT PLATFORM COMPARISON                                |
+---------------------------------------------------------------------------------------------------+
| Parameter          | R3 Corda                     | Ripple (XRP Ledger)         | ConsenSys Quorum        |
+--------------------+-----------------------------+-----------------------------+-------------------------+
| Target Domain      | Financial Institutions,     | Cross-border interbank      | Enterprise Ethereum     |
|                    | Legal contracts, Banking.   | payments and remittances.   | (Finance, Supply Chain).|
+--------------------+-----------------------------+-----------------------------+-------------------------+
| Ledger Structure   | **NOT a Blockchain**. P2P   | Distributed Ledger          | Block-based Blockchain  |
|                    | State DAG (need-to-know).   | with continuous consensus.  | (Geth fork).            |
+--------------------+-----------------------------+-----------------------------+-------------------------+
| Consensus Model    | **Notary Services**         | **RPCA** (Ripple Protocol   | **Istanbul BFT (IBFT)** |
|                    | (Uniqueness verification).  | Consensus Algorithm), UNL.  | or **Raft**.            |
+--------------------+-----------------------------+-----------------------------+-------------------------+
| Smart Contracts    | CorDapps (Java / Kotlin).   | Smart contracts limited;    | Solidity smart          |
|                    | Ricardian Contracts.        | focuses on payment rails.   | contracts running on EVM|
+--------------------+-----------------------------+-----------------------------+-------------------------+
| Data Privacy       | Point-to-point state sharing| Public ledger with          | **Tessera / Constellation|
|                    | (Zero global broadcast).    | pseudonymous accounts.      | Private Enclave**.      |
+--------------------+-----------------------------+-----------------------------+-------------------------+
```

### Detailed Breakdown:
1. **R3 Corda:**
   - Rejects the global broadcast paradigm: Data is shared strictly between transaction participants on a *need-to-know basis*.
   - Uses **Ricardian Contracts** (pairing legal prose templates with executable digital code).
   - Double spending is prevented by **Notaries** (nodes certifying that inputs haven't been previously consumed).
2. **Ripple (XRP Ledger):**
   - Engineered for sub-second, negligible-cost fiat currency exchange and cross-border settlement.
   - Replaces mining with the **Ripple Protocol Consensus Algorithm (RPCA)** utilizing **Unique Node Lists (UNL)** (trusted validator sets).
3. **Quorum:**
   - Developed by J.P. Morgan, Quorum adds enterprise privacy to Ethereum.
   - Dual-state architecture: Separates transactions into **Public State** (visible to all network nodes) and **Private State** (encrypted payloads decrypted only by intended counterparty nodes using the **Tessera private enclave**).

---

## 6.2 Decentralized Finance (DeFi) Architecture
*(Appeared in: May 2023 Q6d [10M], Dec 2023 Q6d [10M], May 2024 Q6a [10M])*

Decentralized Finance (DeFi) replaces traditional centralized financial intermediaries (banks, brokerages, clearinghouses) with autonomous smart contracts on public blockchains.

```
+---------------------------------------------------------------------------------------------------+
|                                 DEFI ARCHITECTURAL CORE COMPONENTS                                |
+---------------------------------------------------------------------------------------------------+
| 1. AUTOMATED MARKET MAKERS (AMM) & DECENTRALIZED EXCHANGES (DEX):                                 |
|    - Replaces order books with algorithmic liquidity pools.                                       |
|    - Constant Product Market Maker Formula (Uniswap):                                             |
|                             x * y = k                                                             |
|      where x = reserve of Token A, y = reserve of Token B, k = invariant constant.                 |
|    - Swap Pricing: If a trader buys Delta_x of Token A, they must deposit Delta_y such that:       |
|                             (x - Delta_x) * (y + Delta_y) = k                                     |
+---------------------------------------------------------------------------------------------------+
| 2. LENDING & BORROWING PROTOCOLS (Aave, Compound):                                                |
|    - Over-collateralized loans (e.g., deposit $150 of ETH to borrow $100 of USDC).                 |
|    - Liquidation Mechanisms: If collateral value drops below liquidation threshold, liquidators   |
|      auction off collateral to maintain solvency.                                                 |
+---------------------------------------------------------------------------------------------------+
| 3. FLASH LOANS:                                                                                   |
|    - Uncollateralized loans borrowed and repaid within the EXACT SAME Ethereum transaction!       |
|    - Atomic Execution: If the borrower does not repay principal + fee by the end of execution,    |
|      the entire transaction reverts automatically as if it never happened.                       |
+---------------------------------------------------------------------------------------------------+
| 4. STABLECOINS:                                                                                   |
|    - Fiat-backed (USDT, USDC): 1:1 reserves held in traditional commercial banks.                 |
|    - Crypto-collateralized (DAI): Backed by smart-contract locked cryptocurrency vaults.          |
+---------------------------------------------------------------------------------------------------+
```

---

## 6.3 Case Study: Supply Chain Management Using Hyperledger Fabric
*(Appeared in: Syllabus Module 5.3 & 6.2)*

### Real-World Architecture: Pharmaceutical Cold-Chain Tracking
- **Business Problem:** Counterfeit medications, temperature breaches in refrigerated vaccine transit, lack of provenance tracking across multi-party carrier networks.
- **Hyperledger Fabric Implementation:**
  1. **Consortium Participants:** Pharmaceutical Manufacturer, Logistics Carriers, Customs Regulators, Hospitals/Pharmacies.
  2. **Private Channels:**
     - Channel 1 (`All-Parties Channel`): Records batch tracking, temperature compliance proofs, and ownership transfers.
     - Channel 2 (`Commercial Channel`): Connects Manufacturer and Hospital for confidential commercial procurement pricing.
  3. **Endorsement Policy:** Requires dual endorsement: $\text{OutOf}(2, \text{Carrier\_MSP}, \text{Manufacturer\_MSP})$.
  4. **IoT Sensor Integration:** IoT GPS/temperature trackers broadcast temperature pings directly into chaincode; any reading exceeding $+8^\circ\text{C}$ triggers automated insurance claims and halts shipment clearance.

---

## MU Keyword Checklist: Module 6
- [ ] *Corda: Not a Blockchain, Need-to-know State DAG, Notary Service, Ricardian Contracts*
- [ ] *Ripple: RPCA Consensus, Unique Node List (UNL), Gateways, Cross-Border Payments*
- [ ] *Quorum: Enterprise Ethereum, Tessera Private Transaction Enclave, IBFT Consensus*
- [ ] *DeFi: Automated Market Maker (AMM) $x \cdot y = k$, Liquidity Pools, Liquidity Providers*
- [ ] *Flash Loans: Uncollateralized, Single Transaction Atomicity, Revert on non-repayment*
- [ ] *Hyperledger Supply Chain: Private Channels, Endorsement Policies, IoT Integration*
