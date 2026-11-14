# Mumbai University (MU) Semester 7 — Blockchain
## Masterclass Part 1: Modules 1, 2 & 3 (Foundations, Cryptocurrencies, Consensus & Solidity)
**Course Code:** Department Level Optional Course (DLOC) | **Scheme:** Rev 2019 / C-Scheme | **Applicable Cycles:** Dec 2022 – May 2025

---

# MODULE 1: INTRODUCTION TO BLOCKCHAIN

---

## 1.1 Blockchain Definition & Cryptographic Fundamentals
*(Appeared in: Dec 2022 Q1a [5M], Dec 2024 Q2a [10M])*

### Formal Definition
A **Blockchain** is a distributed, decentralized, append-only immutable ledger that records transactions across a peer-to-peer (P2P) network using cryptographic hashing, digital signatures, and consensus protocols without relying on a central intermediary.

```
+---------------------------------------------------------------------------------------------------+
|                                 THE CRYPTOGRAPHIC BLOCKCHAIN LEDGER                               |
+---------------------------------------------------------------------------------------------------+
|  [BLOCK N-1]                      [BLOCK N]                       [BLOCK N+1]                     |
|  +-------------------------+      +-------------------------+      +-------------------------+    |
|  | Block Hash: 0000a89...  |      | Block Hash: 00005f2...  |      | Block Hash: 00001c4...  |    |
|  | Prev Hash:  000041b...  |      | Prev Hash:  0000a89...  |----->| Prev Hash:  00005f2...  |    |
|  | Merkle Root: e2f39...   |      | Merkle Root: 7d14b...   |      | Merkle Root: 99a12...   |    |
|  | Nonce: 849204           |      | Nonce: 1048576          |      | Nonce: 394182           |    |
|  +-------------------------+      +-------------------------+      +-------------------------+    |
|  | Transactions:           |      | Transactions:           |      | Transactions:           |    |
|  | Tx 1, Tx 2, ...         |      | Tx 1, Tx 2, ...         |      | Tx 1, Tx 2, ...         |    |
|  +-------------------------+      +-------------------------+      +-------------------------+    |
+---------------------------------------------------------------------------------------------------+
```

### Cryptographic Hash Functions (SHA-256)
A cryptographic hash function $H: \{0, 1\}^* \to \{0, 1\}^{256}$ maps arbitrary-length input data into a deterministic, fixed-size 256-bit string.

#### Four Mandatory Cryptographic Properties:
1. **Pre-image Resistance (One-Way Property):** Given a hash output $y$, it is computationally infeasible to find input $x$ such that $H(x) = y$.
2. **Second Pre-image Resistance (Weak Collision Resistance):** Given input $x_1$, it is computationally infeasible to find a distinct input $x_2 \ne x_1$ such that $H(x_1) = H(x_2)$.
3. **Collision Resistance (Strong Collision Resistance):** It is computationally infeasible to find *any* pair of distinct inputs $(x_1, x_2)$ such that $H(x_1) = H(x_2)$. (Requires $O(2^{128})$ operations by the Birthday Paradox for 256-bit hashes).
4. **Avalanche Effect:** A modification of even a single bit in the input produces an unpredictable, drastic change in more than $50\%$ of the output hash bits.

---

## 1.2 Structure of a Block: Header Anatomy & Payload
*(Appeared in: May 2023 Q2a [10M], Dec 2024 Q2a [10M])*

A block consists of two distinct components: the **Block Header** (80 bytes in Bitcoin) and the **Block Body** (containing the serialized transaction list).

```
+---------------------------------------------------------------------------------------------------+
|                                  ANATOMY OF A BLOCK IN BLOCKCHAIN                                 |
+---------------------------------------------------------------------------------------------------+
|  BLOCK HEADER (80 Bytes total):                                                                   |
|  +-------------------+------------+-------------------------------------------------------------+ |
|  | Field Name        | Size       | Description / Function                                      | |
|  +-------------------+------------+-------------------------------------------------------------+ |
|  | Version           | 4 Bytes    | Block version number tracking protocol upgrade rules.       | |
|  | Previous Hash     | 32 Bytes   | 256-bit SHA-256 hash of previous block header (Chain link). | |
|  | Merkle Root Hash  | 32 Bytes   | Root hash summarizing all transactions in this block.       | |
|  | Timestamp         | 4 Bytes    | Unix epoch time indicating block generation moment.         | |
|  | Bits (Target)     | 4 Bytes    | Encoded difficulty threshold target for Proof of Work.      | |
|  | Nonce             | 4 Bytes    | 32-bit counter incremented by miners to solve the puzzle.   | |
|  +-------------------+------------+-------------------------------------------------------------+ |
+---------------------------------------------------------------------------------------------------+
|  BLOCK BODY:                                                                                      |
|  - Transaction Counter: VarInt encoding total transactions included (e.g., 2,500 transactions).   |
|  - Coinbase Transaction: First transaction generating new cryptocurrency reward + fees to miner.   |
|  - Raw Transaction List: Serialized transaction payloads [Tx_1, Tx_2, ..., Tx_N].                 |
+---------------------------------------------------------------------------------------------------+
```

---

## 1.3 The Merkle Tree: Structure, Construction & Membership Proof
*(Appeared in: Dec 2022 Q1d [5M], May 2023 Q1d [5M], May 2024 Q3a [10M], Dec 2024 Q1a [5M])*

A **Merkle Tree** (Ralph Merkle, 1979) is a binary hash tree where every leaf node is labeled with the cryptographic hash of a data transaction, and every non-leaf node is labeled with the cryptographic hash of the concatenated labels of its children.

```
+---------------------------------------------------------------------------------------------------+
|                                      MERKLE TREE ARCHITECTURE                                     |
+---------------------------------------------------------------------------------------------------+
|                                        [ MERKLE ROOT ]                                            |
|                                        H_1234 = H(H_12 || H_34)                                   |
|                                            /             \                                        |
|                                           /               \                                       |
|                                  [ H_12 ]                   [ H_34 ]                              |
|                            H(H_1 || H_2)                     H(H_3 || H_4)                        |
|                               /        \                     /         \                          |
|                              /          \                   /           \                         |
|                         [ H_1 ]        [ H_2 ]         [ H_3 ]         [ H_4 ]                    |
|                         H(Tx 1)        H(Tx 2)         H(Tx 3)         H(Tx 4)                    |
|                            |              |               |               |                       |
|                          Tx 1           Tx 2            Tx 3            Tx 4                      |
+---------------------------------------------------------------------------------------------------+
```

### Merkle Tree Mathematical Construction
For $N = 4$ transactions:
1. **Leaf Hashes:**
   $$H_1 = \text{SHA256}(\text{Tx}_1), \quad H_2 = \text{SHA256}(\text{Tx}_2), \quad H_3 = \text{SHA256}(\text{Tx}_3), \quad H_4 = \text{SHA256}(\text{Tx}_4)$$
2. **Intermediate Nodes:**
   $$H_{12} = \text{SHA256}(H_1 \mathbin{\Vert} H_2), \quad H_{34} = \text{SHA256}(H_3 \mathbin{\Vert} H_4)$$
   *(Note: $\Vert$ represents byte concatenation).*
3. **Merkle Root:**
   $$\text{Merkle Root} = H_{1234} = \text{SHA256}(H_{12} \mathbin{\Vert} H_{34})$$
*(Note: If a block contains an odd number of transactions, the final transaction hash is duplicated to form a balanced pair).*

### Merkle Proof (Simplified Payment Verification - SPV)
To verify that transaction $\text{Tx}_3$ belongs to the block without downloading the entire blockchain:
- An SPV light node downloads only the **80-byte Block Header** (which contains the Merkle Root $H_{1234}$).
- The full node provides the **Audit Path (Merkle Path)**: $\{H_4, H_{12}\}$.
- The SPV client computes:
  1. $H_3 = \text{SHA256}(\text{Tx}_3)$
  2. $H_{34} = \text{SHA256}(H_3 \mathbin{\Vert} H_4)$
  3. $H_{\text{computed}} = \text{SHA256}(H_{12} \mathbin{\Vert} H_{34})$
- **Verification:** If $H_{\text{computed}} == H_{1234}$, the transaction is mathematically guaranteed to be included in the block.
- **Time Complexity:** Verification requires only $\mathbf{O(\log_2 N)}$ hashes instead of scanning $O(N)$ transactions linearly.

---

## 1.4 Public vs Private vs Consortium Blockchains
*(Appeared in: Dec 2022 Q1a [5M], May 2023 Q1a [5M], Dec 2023 Q1d [5M], May 2024 Q2a [10M], May 2025 Q5a [10M])*

```
+---------------------------------------------------------------------------------------------------+
|                                  BLOCKCHAIN TAXONOMY COMPARISON                                   |
+---------------------------------------------------------------------------------------------------+
| Parameter          | Public (Permissionless)     | Private (Permissioned)    | Consortium / Federated     |
+--------------------+-----------------------------+---------------------------+----------------------------+
| Access / Read      | Open to anyone worldwide    | Restricted to single org  | Restricted to member orgs  |
| Permission         | (Anonymous / Pseudonymous)  | (Identified employees)    | (Pre-selected council)     |
+--------------------+-----------------------------+---------------------------+----------------------------+
| Write / Validator  | Anyone running node         | Single central entity     | Authorized consortium nodes|
| Permission         | (Miners / Stakers)          | (Admin control)           | (Multi-org quorum)         |
+--------------------+-----------------------------+---------------------------+----------------------------+
| Consensus Protocol | Proof of Work, Proof of     | Crash Fault Tolerant:     | PBFT, Raft, Istanbul BFT   |
|                    | Stake (PoW, PoS)            | RAFT, PAXOS               | (IBFT), Quorum             |
+--------------------+-----------------------------+---------------------------+----------------------------+
| Throughput (TPS)   | Very Low (7 - 30 TPS)       | Extremely High (>10,000)  | High (1,000 - 5,000 TPS)   |
+--------------------+-----------------------------+---------------------------+----------------------------+
| Energy Consumption | High (if PoW)               | Negligible                | Negligible                 |
+--------------------+-----------------------------+---------------------------+----------------------------+
| Immutability       | Near impossible to tamper   | Could be modified by root | Could be modified if       |
|                    | (Requires 51% attack)       | admin consensus           | majority members collude   |
+--------------------+-----------------------------+---------------------------+----------------------------+
| Primary Examples   | Bitcoin, Ethereum, Solana   | Multichain, Monax         | Hyperledger Fabric, Corda, |
|                    |                             |                           | Quorum, R3 Banking Network |
+--------------------+-----------------------------+---------------------------+----------------------------+
```

---

## 1.5 Challenges of Blockchain Implementation
*(Appeared in: Dec 2022 Q2a [10M], Dec 2024 Q1e [5M])*

1. **The Blockchain Scalability Trilemma (Vitalik Buterin):** A blockchain system can achieve at most two of three properties simultaneously: **Decentralization**, **Security**, and **Scalability**. (e.g., Bitcoin prioritizes Decentralization and Security at the cost of $7$ TPS throughput).
2. **High Energy Consumption:** Proof of Work networks consume gigawatts of electricity executing repetitive hashing operations.
3. **Interoperability Deficits:** Independent blockchains (e.g., Bitcoin, Ethereum, Polkadot) operate in isolated cryptographic silos without native communication protocols.
4. **Storage Bloat:** Full nodes must store the entire historical ledger state (Bitcoin $>500$ GB, Ethereum $>1$ TB), creating centralizing barriers to entry.
5. **Smart Contract Vulnerability & Immutability Paradox:** Once deployed, code cannot be patched. Software flaws (e.g., The DAO reentrancy attack) lead to permanent financial loss without recourse.

---

## MU Keyword Checklist: Module 1
- [ ] *SHA-256, Pre-image resistance, Collision resistance, Avalanche effect*
- [ ] *Block Header: 80 Bytes, Version, Previous Hash, Merkle Root, Timestamp, Bits, Nonce*
- [ ] *Merkle Tree, Leaf Hashes, Merkle Root, Audit Path, $O(\log_2 N)$ verification complexity*
- [ ] *Public vs Private vs Consortium 7-point comparative matrix*
- [ ] *Scalability Trilemma (Decentralization, Security, Scalability), 51% Attack threshold*

---
---

# MODULE 2: CRYPTOCURRENCY & CONSENSUS PROTOCOLS

---

## 2.1 Cryptocurrencies & Storage: Hot vs Cold Wallets
*(Appeared in: May 2023 Q1c/Q2b [10M], Dec 2023 Q1b [5M], May 2024 Q1b [5M], Dec 2024 Q3a [10M], May 2025 Q1d/Q2a [10M])*

### Cryptocurrency Taxonomy:
1. **Bitcoin (BTC):** First-generation peer-to-peer decentralized electronic currency focused on native value transfer and censorship-resistant digital store of value.
2. **Altcoins:** Any alternative cryptocurrency launched after Bitcoin possessing its own native independent blockchain (e.g., Ethereum [ETH], Litecoin [LTC], Ripple [XRP], Solana [SOL]).
3. **Tokens:** Digital assets built on top of an existing host blockchain via smart contract standards (e.g., ERC-20 fungible tokens like USDT/UNI, ERC-721 non-fungible tokens [NFTs]).

### Hot Wallets vs Cold Wallets

```
+---------------------------------------------------------------------------------------------------+
|                                    HOT WALLETS VS COLD WALLETS                                    |
+---------------------------------------------------------------------------------------------------+
| Parameter          | Hot Wallet (Online / Connected)       | Cold Wallet (Offline / Air-Gapped)   |
+--------------------+---------------------------------------+--------------------------------------+
| Internet Link      | Continuously connected to internet.   | Completely offline; air-gapped from  |
|                    |                                       | network connections.                 |
+--------------------+---------------------------------------+--------------------------------------+
| Private Key Locus  | Stored on web server, mobile app, or  | Stored securely inside tamper-proof  |
|                    | browser extension memory.             | hardware chip or physical paper.     |
+--------------------+---------------------------------------+--------------------------------------+
| Security Level     | Low to Moderate (Vulnerable to malware| Extreme (Immune to remote online     |
|                    | keyloggers, phishing, server hacks).  | exploits, trojans, network attacks). |
+--------------------+---------------------------------------+--------------------------------------+
| Transaction Speed  | Instantaneous (1-click signing).      | Slower (Requires physical button     |
|                    |                                       | confirmation, USB/QR air-gap sync).  |
+--------------------+---------------------------------------+--------------------------------------+
| Primary Use Case   | Daily trading, micro-transactions,    | Long-term institutional holding      |
|                    | interacting with DeFi DApps.          | ("HODLing"), custody storage.        |
+--------------------+---------------------------------------+--------------------------------------+
| Archetypes         | MetaMask, Trust Wallet, Coinbase App. | Ledger Nano X, Trezor, Paper Wallet. |
+--------------------+---------------------------------------+--------------------------------------+
```

---

## 2.2 Transactions & The Bitcoin UTXO Model
*(Appeared in: Dec 2022 Q6b [10M], May 2023 Q6b [10M], Dec 2023 Q1a/Q5a [10M], May 2025 Q6d [10M])*

Bitcoin does not track account balances (e.g., "Alice has 5 BTC"). Instead, it tracks **Unspent Transaction Outputs (UTXOs)**.
A user's total wallet balance is dynamically calculated by summing all unspent outputs locked to their public keys.

```
+---------------------------------------------------------------------------------------------------+
|                                 BITCOIN UTXO TRANSACTION LIFECYCLE                                |
+---------------------------------------------------------------------------------------------------+
|  TRANSACTION 1:                                                                                   |
|  [Inputs]                              [Outputs]                                                  |
|  - Coinbase (Mining) ----------------> Output 0: 50 BTC (Locked to Alice's Public Key)            |
+---------------------------------------------------------------------------------------------------+
                                            |
                                            v (Alice spends 20 BTC to Bob)
|  TRANSACTION 2:                                                                                   |
|  [Inputs]                              [Outputs]                                                  |
|  - Prev Tx: Tx 1, Out: 0               - Output 0: 20 BTC (Locked to Bob's Key)                   |
|    ScriptSig: [Alice's Signature] ----> - Output 1: 29.99 BTC (Change locked to Alice's Key)       |
|                                        (Implicit 0.01 BTC = Transaction Fee to Miner)             |
+---------------------------------------------------------------------------------------------------+
```

### Key Principles of the UTXO Model:
1. **All-or-Nothing Spending:** A UTXO cannot be partially spent. If Alice owns a $50$ BTC UTXO and wants to pay Bob $20$ BTC, she must consume the entire $50$ BTC UTXO, generating $20$ BTC to Bob and $29.99$ BTC back to herself as a change output.
2. **Transaction Fee Equation:**
   $$\text{Transaction Fee} = \sum \text{Input Values} - \sum \text{Output Values}$$
3. **UTXO vs Account-Based Model (Ethereum):**
   - *UTXO Model:* Stateless, high privacy, parallel transaction validation across independent UTXOs.
   - *Account Model:* Stateful, simpler mental model, enables complex smart contract logic, but requires sequential nonce management to prevent replay attacks.

---

## 2.3 The Double Spending Problem & Proof of Work Solution
*(Appeared in: Dec 2022 Q2b [10M], May 2023 Q1b [5M], Dec 2024 Q5a [10M], May 2025 Q1c [5M])*

### The Problem
In digital systems, electronic information is trivially replicable at zero cost. **Double Spending** occurs when an attacker attempts to spend the exact same cryptocurrency token in two separate transactions simultaneously (e.g., paying Merchant Bob for goods, while concurrently broadcasting a transaction routing those same funds back to the attacker's wallet).

```
+---------------------------------------------------------------------------------------------------+
|                                  DOUBLE SPENDING ATTACK SCENARIO                                  |
+---------------------------------------------------------------------------------------------------+
|  Attacker owns UTXO_A (10 BTC)                                                                    |
|                                                                                                   |
|          +--- Tx 1: UTXO_A sent to Merchant Bob ---> [ Included in Public Block 101 ]             |
|          |    (Merchant Bob ships goods after 1 confirmation)                                     |
|          |                                                                                        |
|  UTXO_A -+                                                                                        |
|          |                                                                                        |
|          +--- Tx 2: UTXO_A sent to Attacker Wallet -> [ Mined in Secret Private Chain ]           |
|               (Attacker mines blocks secretly faster than the public network)                     |
+---------------------------------------------------------------------------------------------------+
```

### How Proof of Work Solves Double Spending
1. **Distributed Timestamping & Mempool Verification:** When a transaction is broadcast, every node verifies that the referenced UTXO is currently unspent. Once a transaction is included in a block, the UTXO is consumed.
2. **Proof of Work Computational Cost:** Adding a block requires expending massive computational energy finding a valid nonce.
3. **The Longest Chain Rule (Nakamoto Consensus):** Nodes always accept and propagate the chain with the largest amount of accumulated Proof of Work (**the longest chain**).
4. **Reorganization Resistance via Block Confirmations:** If an attacker attempts to overwrite Block 101, they must re-mine Block 101 and all subsequent blocks faster than the entire combined honest network.
   - The probability $P$ of an attacker with hashrate fraction $q < 0.5$ catching up after $z$ honest confirmations decays exponentially:
     $$P \approx \left(\frac{q}{p}\right)^z \quad (\text{where } p = 1 - q)$$
   - At $z = 6$ confirmations ($\approx 1$ hour), the double spending probability drops to less than $0.1\%$, providing mathematical finality.

---

## 2.4 Mining Difficulty & Proof of Work Formulation
*(Appeared in: Dec 2022 Q3a [10M], May 2024 Q3b [10M], May 2025 Q1e [5M])*

### Mathematical Proof of Work Puzzle
A miner must find an integer **Nonce** such that the double SHA-256 hash of the block header is strictly less than a dynamic 256-bit **Target**:
$$\mathbf{\text{SHA256}(\text{SHA256}(\text{Block Header})) < \text{Target}}$$

### Mining Difficulty Definition
Difficulty $D$ is a relative measure of how hard it is to find a hash below the target, relative to the genesis block target ($\text{Target}_{\text{max}}$):
$$D = \frac{\text{Target}_{\text{max}}}{\text{Target}_{\text{current}}}$$
where $\text{Target}_{\text{max}} = 0x00000000FFFF0000000000000000000000000000000000000000000000000000$ (representing Difficulty = 1).

### The 2016-Block Difficulty Adjustment Algorithm
To maintain an average block creation time of exactly **10 minutes** ($600$ seconds) despite fluctuating global network hashrate, Bitcoin recalculates difficulty every **2016 blocks** (approx. 2 weeks):
$$\text{Expected Time} = 2016 \times 10 \text{ minutes} = 20160 \text{ minutes} = 1,209,600 \text{ seconds}$$

#### Adjustment Formula:
$$\mathbf{\text{Target}_{\text{new}} = \text{Target}_{\text{old}} \times \left( \frac{\text{Actual Time to Mine 2016 Blocks}}{\text{Expected Time (1,209,600 seconds)}} \right)}$$

- If $\text{Actual Time} < \text{Expected Time}$ (miners added hashrate), the target decreases $\implies$ **Difficulty increases**.
- If $\text{Actual Time} > \text{Expected Time}$ (miners left network), the target increases $\implies$ **Difficulty decreases**.
- **Damping Constraint:** To prevent wild oscillation, the adjustment factor is bounded between $[0.25, 4.0]$:
  $$\text{Target}_{\text{new}} \in \left[ \frac{\text{Target}_{\text{old}}}{4}, 4 \times \text{Target}_{\text{old}} \right]$$

---

## 2.5 Consensus Protocols Comparative Taxonomy
*(Appeared in: May 2024 Q2b [10M], Dec 2024 Q1c [5M], May 2025 Q4a [10M])*

```
+---------------------------------------------------------------------------------------------------+
|                                 CONSENSUS PROTOCOL TAXONOMY MATRIX                                |
+---------------------------------------------------------------------------------------------------+
| Parameter          | Proof of Work (PoW)         | Proof of Stake (PoS)        | Proof of Elapsed Time    |
|                    |                             |                             | (PoET)                   |
+--------------------+-----------------------------+-----------------------------+--------------------------+
| Resource Bound     | Computational Processing    | Financial Capital / Coin    | Trusted Execution Time   |
|                    | Power (Hashrate).           | Stake locked in contract.   | (Intel SGX CPU Enclaves).|
+--------------------+-----------------------------+-----------------------------+--------------------------+
| Block Selector     | First miner to find hash    | Pseudo-randomly weighted    | Node whose CPU enclave   |
|                    | below Target (Lottery).     | by size of staked coins.    | generates shortest timer.|
+--------------------+-----------------------------+-----------------------------+--------------------------+
| Energy Consumption | Extremely High (Gigawatts). | Negligible (99.95% less).   | Negligible (Standard CPU)|
+--------------------+-----------------------------+-----------------------------+--------------------------+
| Attack Resistance  | 51% Computational Hashrate  | 51% (or 33%) of total       | Compromising hardware    |
|                    | Attack.                     | staked capital (Slashing).  | security enclave (SGX).  |
+--------------------+-----------------------------+-----------------------------+--------------------------+
| Finality Speed     | Probabilistic (6 blocks ~1h)| Fast (Epoch finality ~15m). | Deterministic.           |
+--------------------+-----------------------------+-----------------------------+--------------------------+
| Primary Usage      | Bitcoin, Litecoin, Monero.  | Ethereum 2.0, Cardano.      | Hyperledger Sawtooth.    |
+---------------------------------------------------------------------------------------------------+
```

- **Proof of Burn (PoB):** Miners send coins to an unspendable "eater address" (burning them permanently). The probability of mining a block is proportional to the volume of burnt coins.

---

## MU Keyword Checklist: Module 2
- [ ] *Bitcoin, Altcoins, Tokens (ERC-20, ERC-721)*
- [ ] *Hot Wallet (Online, Software) vs Cold Wallet (Offline, Hardware, Air-gapped)*
- [ ] *UTXO Model: Inputs, Outputs, ScriptSig, ScriptPubKey, Change Outputs*
- [ ] *Double Spending Problem: Race Attack, Finney Attack, 51% Hashrate Attack*
- [ ] *Nakamoto Longest Chain Rule, 6 Confirmations Threshold*
- [ ] *PoW Equation: $\text{SHA256}(\text{SHA256}(\text{Header})) < \text{Target}$*
- [ ] *2016-Block Difficulty Adjustment: $\text{Target}_{\text{new}} = \text{Target}_{\text{old}} \times (\text{Actual Time} / 1209600)$*
- [ ] *PoW vs PoS (Staking, Slashing) vs PoB vs PoET (Intel SGX Wait Timer)*

---
---

# MODULE 3: PROGRAMMING FOR BLOCKCHAIN (SOLIDITY & SMART CONTRACTS)

---

## 3.1 Smart Contract Theory & State Machine Representation
*(Appeared in: Dec 2022 Q1b [5M], May 2023 Q3a [10M], Dec 2023 Q2a [10M], May 2024 Q5a [10M], Dec 2024 Q1d/Q3b [10M])*

### Definition & State Machine Replication
Coined by Nick Szabo (1994), a **Smart Contract** is a self-executing computerized transaction protocol that enforces terms directly via immutable code running on a decentralized virtual machine.

A smart contract is formally modeled as a **Deterministic Finite State Machine (FSM)**:
$$M = (S, s_0, T, \delta)$$
- $S$: Finite set of valid contract states.
- $s_0$: Initial deployment state.
- $T$: Set of valid transactions (inputs from EOAs).
- $\delta: S \times T \to S$: Deterministic state transition function executed by the EVM.

```
+---------------------------------------------------------------------------------------------------+
|                            CROWDFUNDING CONTRACT STATE MACHINE TRANSITIONS                        |
+---------------------------------------------------------------------------------------------------+
|                                  [ 1. FUNDING ACTIVE ]                                            |
|                                            |                                                      |
|                   +------------------------+------------------------+                             |
|                   | (Time <= Deadline      | (Time > Deadline       | (Time > Deadline            |
|                   |  AND Balance >= Goal)  |  AND Balance >= Goal)  |  AND Balance < Goal)        |
|                   v                        v                        v                             |
|         [ 2. GOAL REACHED ]      [ 3. SUCCESSFUL CLOSED ]   [ 4. FAILED / REFUND ]                |
|                   |                        |                        |                             |
|                   |                        v                        v                             |
|                   +----------------> (Manager Claims          (Contributors Claim                 |
|                                       Funds via Payout)        Refund via Payout)                 |
+---------------------------------------------------------------------------------------------------+
```

---

## 3.2 Solidity Language Fundamentals: Visibility, Mutability & Types
*(Appeared in: May 2023 Q5b [10M], Dec 2023 Q4b/Q5b [10M], May 2024 Q4a/b [10M], Dec 2024 Q5b [10M])*

### 1. Function Visibility Specifiers
- **`public`:** Accessible internally within the contract and externally by users and other contracts. Automatic getter generated if applied to state variables.
- **`private`:** Accessible **only** within the exact contract where defined. Not accessible by derived child contracts.
- **`internal`:** Accessible within the defining contract **and** all derived child contracts (analogous to `protected` in C++). Default for state variables.
- **`external`:** Accessible **only from outside** the contract (via transactions or external contract calls). Cannot be called internally without `this.func()`. Consumes less gas when reading large array arguments because data reads directly from `calldata`.

### 2. State Mutability Specifiers
- **`pure`:** Guarantees function **neither reads nor modifies** the blockchain state. Operates strictly on function arguments and constants. (Zero gas cost when invoked off-chain).
- **`view`:** Guarantees function **reads but does not modify** blockchain state (reads storage variables, balances). (Zero gas cost when called off-chain).
- **`payable`:** Explicitly allows the function to accept incoming Ether payments alongside function execution. Without `payable`, any transaction sending Ether to the function automatically reverts.

### 3. Address vs Address Payable
- `address`: Holds a 20-byte Ethereum account address. Cannot receive Ether directly.
- `address payable`: Holds a 20-byte address augmented with payment transfer primitives:
  - `recipient.transfer(amount)`: Forwards exactly $2300$ gas. Throws exception and reverts transaction on failure.
  - `recipient.send(amount)`: Forwards $2300$ gas. Returns boolean `false` on failure (requires manual error handling).
  - `(bool success, ) = recipient.call{value: amount}("")`: Modern recommended pattern. Forwards all available gas (or specified gas); returns boolean `success`.

### 4. Special Fallback Functions
- **`receive() external payable`:** Executed when a transaction sends plain Ether to the contract with **empty `calldata`**.
- **`fallback() external payable`:** Executed when incoming `calldata` does not match any existing function selector, or when Ether is received and no `receive()` function exists.

---

### 🌟 Deep-Dive: Fixed vs Dynamic Arrays in Solidity [5 Marks] — Nov'25 (Q1b)
**Question:** *"Explain Fixed and Dynamic arrays."*

In Solidity, an **Array** is a data structure storing a sequential collection of elements of identical data type. Arrays can be initialized with fixed compile-time lengths or dynamically resizable run-time lengths:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                       FIXED VS DYNAMIC ARRAYS IN SOLIDITY                        │
│                                                                                  │
│  [FIXED-SIZE ARRAY]:                   [DYNAMIC-SIZE ARRAY]:                     │
│  uint256[5] public fixedArr;           uint256[] public dynamicArr;              │
│  ┌───┬───┬───┬───┬───┐                 ┌───┬───┬───┬───┐ + push(val)            │
│  │ 0 │ 1 │ 2 │ 3 │ 4 │                 │ 0 │ 1 │ 2 │ 3 │ ───► [New Element]      │
│  └───┴───┴───┴───┴───┘                 └───┴───┴───┴───┘                         │
│  • Length fixed at compile time        • Length grows/shrinks dynamically        │
│  • Cannot call .push() or .pop()       • Supports .push() and .pop() (Storage)   │
│  • Contiguous memory slot layout       • Slot stores length; elements at keccak  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

#### 1. Fixed-Size Arrays:
- **Syntax:** `T[k] variableName;` where $T$ is the type and $k$ is an integer literal known at compile-time.
- **Characteristics:**
  - Length cannot change during execution; attempting to resize triggers a compilation error.
  - Can reside in `storage`, `memory`, or `calldata`.
  - Does **not** support `.push()` or `.pop()` member methods.
- **Example:**
  ```solidity
  uint256[3] public fixedGrades = [90, 85, 95];
  // Access: fixedGrades[0] == 90
  // fixedGrades.length == 3 (read-only)
  ```

#### 2. Dynamic-Size Arrays:
- **Syntax:** `T[] variableName;`
- **Characteristics:**
  - Length can expand or contract dynamically during runtime in `storage`.
  - Member functions available in storage:
    - `.push(value)`: Appends an element to the end; increments array length by 1.
    - `.pop()`: Removes the last element; decrements array length by 1.
    - `.length`: Returns current element count.
  - In `memory`, dynamic arrays must be instantiated with a fixed size using the `new` keyword and cannot be resized (e.g., `uint[] memory a = new uint[](5);` — `.push()` is invalid in memory).
- **Example:**
  ```solidity
  uint256[] public dynamicScores;

  function addScore(uint256 score) public {
      dynamicScores.push(score); // Expands array length dynamically
  }

  function removeLast() public {
      require(dynamicScores.length > 0, "Array is empty");
      dynamicScores.pop(); // Shrinks array length
  }
  ```

---

## 3.3 SOLVED SOLIDITY PROGRAM 1: Check If a Number Is Prime
*(Appeared in: Dec 2022 Q1e [5M], May 2025 Q1b [5M])*

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title PrimeChecker
 * @dev Contract to determine whether an unsigned integer is prime.
 */
contract PrimeChecker {

    /**
     * @notice Checks if a number n is prime.
     * @dev Marked as 'pure' because it neither reads nor modifies contract storage.
     * @param n The number to test.
     * @return bool True if n is prime, false otherwise.
     */
    function isPrime(uint256 n) public pure returns (bool) {
        // Numbers less than or equal to 1 are not prime
        if (n <= 1) {
            return false;
        }
        // 2 and 3 are prime numbers
        if (n <= 3) {
            return true;
        }
        // Eliminate even numbers and multiples of 3
        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }

        // Test potential factors up to sqrt(n) using 6k +/- 1 optimization
        for (uint256 i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }

        return true;
    }
}
```

---

## 3.4 SOLVED SOLIDITY PROGRAM 2: Multi-Level Inheritance
*(Appeared in: Dec 2022 Q4b [10M], Dec 2024 Q4b [10M], May 2025 Q3a [10M])*

Multi-level inheritance occurs when a derived contract inherits from a parent contract which itself inherits from another base contract ($A \to B \to C$).

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title GrandParent (Level 1 Base Contract)
 */
contract GrandParent {
    string public familyName;

    constructor() {
        familyName = "SolidityLineage";
    }

    // Virtual function permitted to be overridden by child contracts
    function getRole() public pure virtual returns (string memory) {
        return "GrandParent: Founder";
    }
}

/**
 * @title Parent (Level 2 Intermediate Contract)
 */
contract Parent is GrandParent {
    uint256 public generation;

    constructor() {
        generation = 2;
    }

    // Overrides Level 1 function and remains virtual for Level 3
    function getRole() public pure virtual override returns (string memory) {
        return "Parent: Intermediate Builder";
    }
}

/**
 * @title Child (Level 3 Derived Contract)
 */
contract Child is Parent {
    string public childName;

    constructor(string memory _name) {
        childName = _name;
        generation = 3; // Modifies state variable inherited from Parent
    }

    // Overrides Level 2 function
    function getRole() public pure override returns (string memory) {
        return "Child: Final Inheritor";
    }

    // Function demonstrating multi-level access across all ancestors
    function getLineageDetails() public view returns (string memory, uint256, string memory) {
        return (familyName, generation, childName);
    }
}
```

---

## 3.5 SOLVED SOLIDITY PROGRAM 3: Single Inheritance
*(Appeared in: May 2023 Q4b [10M])*

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Ownable (Base Contract)
 */
contract Ownable {
    address public owner;

    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Error: Caller is not the contract owner");
        _;
    }

    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "Error: New owner is zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}

/**
 * @title BankAccount (Derived Contract demonstrating Single Inheritance)
 */
contract BankAccount is Ownable {
    uint256 public balance;

    event Deposited(address indexed sender, uint256 amount);
    event Withdrawn(uint256 amount);

    // Any user can deposit Ether
    function deposit() public payable {
        require(msg.value > 0, "Error: Deposit must be greater than zero");
        balance += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    // Only the inherited 'owner' can withdraw funds
    function withdraw(uint256 amount) public onlyOwner {
        require(amount <= address(this).balance, "Error: Insufficient balance");
        balance -= amount;
        payable(owner).transfer(amount);
        emit Withdrawn(amount);
    }
}
```

---

## 3.6 SOLVED SOLIDITY PROGRAM 4: Find Second Largest Element in an Array
*(Appeared in: May 2023 Q1e [5M])*

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SecondLargestFinder
 * @dev Computes second largest element in a dynamic array in O(n) time and O(1) extra space.
 */
contract SecondLargestFinder {

    /**
     * @notice Finds second largest element in array.
     * @param arr Dynamic array passed in calldata/memory.
     * @return secondLargest The second maximum value.
     */
    function findSecondLargest(uint256[] memory arr) public pure returns (uint256) {
        require(arr.length >= 2, "Array must contain at least two elements");

        uint256 largest = 0;
        uint256 secondLargest = 0;
        bool foundSecond = false;

        // Step 1: Find largest
        for (uint256 i = 0; i < arr.length; i++) {
            if (arr[i] > largest) {
                largest = arr[i];
            }
        }

        // Step 2: Find largest strictly strictly less than largest
        for (uint256 i = 0; i < arr.length; i++) {
            if (arr[i] < largest) {
                if (!foundSecond || arr[i] > secondLargest) {
                    secondLargest = arr[i];
                    foundSecond = true;
                }
            }
        }

        require(foundSecond, "All elements in the array are identical; no second largest exists");
        return secondLargest;
    }
}
```

---

## 3.7 SOLVED SOLIDITY PROGRAM 5: Multiple Inheritance & C3 Linearization
*(Appeared in: May 2024 Q1d [5M])*

When a contract inherits from multiple parents ($C \text{ is } A, B$), Solidity resolves ambiguity (the Diamond Problem) using **C3 Linearization** (ordered from most base-like to most derived).

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Base {
    event Log(string message);

    function foo() public virtual {
        emit Log("Base.foo");
    }
}

contract A is Base {
    function foo() public virtual override {
        emit Log("A.foo");
        super.foo(); // Calls next in C3 linearization order
    }
}

contract B is Base {
    function foo() public virtual override {
        emit Log("B.foo");
        super.foo(); // Calls next in C3 linearization order
    }
}

// Order of inheritance matters: Base-like to most derived
// C3 Linearization order for C: C -> B -> A -> Base
contract C is A, B {
    function foo() public override(A, B) {
        emit Log("C.foo");
        super.foo(); // Triggers B.foo, which triggers A.foo, which triggers Base.foo
    }
}
```

---

## MU Keyword Checklist: Module 3
- [ ] *Smart Contract, Deterministic State Machine Replication (SMR)*
- [ ] *Function Visibility: `public`, `private`, `internal`, `external`*
- [ ] *Function Mutability: `pure` (no read/write), `view` (read only), `payable` (accepts Ether)*
- [ ] *Address vs Address Payable, `.transfer(2300 gas)`, `.call{value: x}("")`*
- [ ] *`receive() external payable` (empty calldata) vs `fallback() external payable`*
- [ ] *Fixed Arrays (`uint[5]`) vs Dynamic Arrays (`uint[]`), Storage vs Memory*
- [ ] *Single, Multi-Level ($A \to B \to C$), and Multiple Inheritance ($C \text{ is } A, B$)*
- [ ] *C3 Linearization (Most base-like to most derived)*
