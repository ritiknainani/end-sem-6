# 📘 BDA ULTIMATE MASTERCLASS — Part 2: Modules 3 & 4

# MODULE 3: NoSQL

---

## Q13. List and Explain the Core Business Drivers behind the NoSQL Movement. [5-10 Marks] — 4/6

**Question Type:** Theory

### Definition
**NoSQL (Not Only SQL)** databases are non-relational databases designed to handle large volumes of unstructured, semi-structured, and structured data with high scalability and availability.

### Core Business Drivers:

| # | Driver | Explanation |
|---|--------|-------------|
| 1 | **Volume & Variety of Data** | Explosion of unstructured data (social media, IoT, logs) that RDBMS cannot handle efficiently |
| 2 | **Horizontal Scalability** | Need to scale out by adding commodity servers rather than scaling up expensive hardware |
| 3 | **Agile Development** | Schema-less design allows rapid iteration; no need for rigid predefined schemas |
| 4 | **High Availability** | 24/7 applications (e-commerce, social media) demand zero downtime — NoSQL supports replication and auto-failover |
| 5 | **Cost Efficiency** | Runs on commodity hardware clusters vs expensive enterprise RDBMS licenses |
| 6 | **Performance at Scale** | Optimized for specific access patterns (key lookups, document retrieval) with low latency |
| 7 | **Cloud & Distributed Computing** | Cloud-native architectures need databases that work across distributed, geographically spread clusters |

### Google's Bigtable Case Study (Dec'22, May'25):
- **Problem:** Google needed to store petabytes of web crawl data, Gmail, Google Maps data
- **Solution:** Bigtable — a distributed, column-family NoSQL database
- **Business Drivers:** Volume (trillions of URLs), Velocity (real-time indexing), Availability (global access)
- **Findings:** Bigtable processes 1M+ operations/sec, scales to thousands of nodes, influenced HBase

**MU Keyword Checklist:** Horizontal scalability, schema-less, commodity hardware, high availability, unstructured data, agile development, CAP theorem, distributed computing

---

## Q14. Explain NoSQL Architectural Patterns. [10 Marks] — 5/6

**Question Type:** Architecture

### Four Main NoSQL Data Models:

```
┌──────────────────────────────────────────────────────────────┐
│                  NoSQL Architectural Patterns                 │
│                                                              │
│  ┌─────────────┐  ┌─────────────┐  ┌────────────┐  ┌──────┐│
│  │ Key-Value   │  │  Document   │  │Column      │  │Graph ││
│  │   Store     │  │   Store     │  │Family      │  │Store ││
│  │             │  │             │  │            │  │      ││
│  │ key → value │  │ key → JSON  │  │Row→Columns │  │Nodes ││
│  │ (opaque     │  │  document   │  │(dynamic    │  │Edges ││
│  │  blob)      │  │  (nested)   │  │ columns)   │  │Props ││
│  └─────────────┘  └─────────────┘  └────────────┘  └──────┘│
│  Redis, DynamoDB  MongoDB, CouchDB  Cassandra,HBase Neo4j  │
└──────────────────────────────────────────────────────────────┘
```

### 1. Key-Value Store
```
┌──────────────────────────────┐
│       KEY-VALUE STORE        │
│                              │
│  Key        │  Value         │
│  ──────────────────────────  │
│  "user:101" │ {blob/string}  │
│  "cart:55"  │ {serialized}   │
│  "session:x"│ {opaque data}  │
└──────────────────────────────┘
```
- **Structure:** Simple key → value mapping (value is opaque blob)
- **Characteristics:** Fastest lookups, O(1) access, no querying by value
- **Use Cases:** Session management, caching, shopping carts, user preferences
- **Examples:** Redis, Amazon DynamoDB, Riak, Memcached
- **Limitations:** Cannot query by value content; only exact-key lookups

### 2. Document Store
```
┌────────────────────────────────────────┐
│          DOCUMENT STORE                │
│                                        │
│  Key: "user:101"                       │
│  Value (JSON Document):               │
│  {                                     │
│    "name": "John",                     │
│    "age": 30,                          │
│    "address": {                        │
│      "city": "Mumbai",                 │
│      "pin": "400001"                   │
│    },                                  │
│    "orders": [101, 205, 308]           │
│  }                                     │
└────────────────────────────────────────┘
```
- **Structure:** Key → structured document (JSON, BSON, XML) with nested fields
- **Characteristics:** Schema-flexible, supports querying on any field within document, indexing on nested fields
- **Use Cases:** Content management systems, user profiles, product catalogs, blogs
- **Examples:** MongoDB, CouchDB, Amazon DocumentDB
- **Advantages over Key-Value:** Can query inside the value (document fields)

### 3. Column-Family Store (Bigtable Model)
```
┌────────────────────────────────────────────────┐
│         COLUMN-FAMILY STORE                     │
│                                                 │
│ Row Key │ CF: Personal      │ CF: Contact       │
│ ────────┼───────────────────┼──────────────────│
│ user1   │ name:"John"       │ email:"j@x.com"  │
│         │ age:"30"          │ phone:"999..."    │
│ ────────┼───────────────────┼──────────────────│
│ user2   │ name:"Jane"       │ email:"j@y.com"  │
│         │                   │                   │
│ (Sparse — each row can have different columns)  │
└────────────────────────────────────────────────┘
```
- **Structure:** Rows identified by row key; columns grouped into **column families**; each row can have different columns (sparse)
- **Characteristics:** Column-oriented storage, excellent compression, high write throughput
- **Use Cases:** Time-series data, IoT sensor data, web analytics, event logging
- **Examples:** Apache Cassandra, HBase, Google Bigtable

### 4. Graph Store
```
┌─────────────────────────────────────────┐
│            GRAPH STORE                   │
│                                         │
│    (Alice)──FRIENDS──►(Bob)             │
│       │                  │               │
│     LIKES              WORKS_AT          │
│       │                  │               │
│       ▼                  ▼               │
│   (Movie:X)          (Company:Y)         │
│                                         │
│  Nodes = Entities                        │
│  Edges = Relationships                   │
│  Properties = Attributes on both         │
└─────────────────────────────────────────┘
```
- **Structure:** Data stored as nodes (entities), edges (relationships), and properties
- **Characteristics:** Optimized for traversing relationships, pattern matching
- **Use Cases:** Social networks, fraud detection, knowledge graphs, recommendation engines
- **Examples:** Neo4j, Amazon Neptune, ArangoDB

### Comparison Table

| Parameter | Key-Value | Document | Column-Family | Graph |
|-----------|-----------|----------|--------------|-------|
| **Data Model** | Key→Opaque Value | Key→JSON Doc | Row→Column Families | Nodes+Edges |
| **Schema** | None | Flexible | Semi-flexible | Flexible |
| **Query** | By key only | By any field | By row key + column | Traversals |
| **Best For** | Caching, sessions | CMS, profiles | Time-series, logs | Social networks |
| **Scalability** | Highest | High | Very High | Moderate |
| **Example** | Redis | MongoDB | Cassandra | Neo4j |

**MU Keyword Checklist:** Key-Value store, Document store, Column-Family, Graph store, schema-less, horizontal scalability, JSON, BSON, column families, nodes, edges, Redis, MongoDB, Cassandra, Neo4j, HBase, Bigtable

---

## Q15. Explain CAP Theorem. How is it different from ACID? [5 Marks] — Dec'24

**Question Type:** Theory

### CAP Theorem (Brewer's Theorem)
States that a distributed database can guarantee at most **two** of the following three properties simultaneously:

```
           Consistency (C)
              / \
             /   \
            /     \
           / CA  CP \
          /         \
         /           \
    Availability (A)────Partition Tolerance (P)
               AP
```

| Property | Meaning |
|----------|---------|
| **Consistency (C)** | Every read receives the most recent write (all nodes see same data at same time) |
| **Availability (A)** | Every request receives a response (success/failure), even during failures |
| **Partition Tolerance (P)** | System continues to operate despite network partitions between nodes |

### CAP vs ACID

| Parameter | ACID | CAP |
|-----------|------|-----|
| **Context** | Single-node/RDBMS transactions | Distributed systems |
| **A** | Atomicity (all-or-nothing) | Availability (always responsive) |
| **C** | Consistency (valid state transitions) | Consistency (all nodes see same data) |
| **I** | Isolation (concurrent txn independence) | — |
| **D** | Durability (committed data persists) | — |
| **P** | — | Partition Tolerance |
| **Focus** | Transaction correctness | System-level trade-offs |
| **Used By** | MySQL, PostgreSQL, Oracle | Cassandra (AP), HBase (CP), MongoDB (CP) |

**MU Keyword Checklist:** CAP theorem, Brewer's theorem, Consistency, Availability, Partition Tolerance, ACID, trade-off, CP systems, AP systems, CA systems

---

# MODULE 4: MINING DATA STREAMS

---

## Q16. Explain the Data-Stream Management System (DSMS) Architecture. [10 Marks] — 3/6

**Question Type:** Architecture

### Definition
A **Data-Stream Management System (DSMS)** is a software system designed to manage continuous, real-time data streams. Unlike a DBMS that manages stored data, a DSMS processes data "in motion."

### Architecture Diagram
```
┌──────────────────────────────────────────────────────────────────┐
│                    DSMS ARCHITECTURE                             │
│                                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │ Stream 1 │  │ Stream 2 │  │ Stream N │  ← Input Streams      │
│  │ (Sensor) │  │ (Logs)   │  │ (Social) │    (continuous,        │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘     unbounded)        │
│       │              │              │                             │
│       └──────────────┼──────────────┘                             │
│                      ▼                                            │
│  ┌──────────────────────────────────────┐                        │
│  │         INPUT MANAGER                │  ← Receives streams    │
│  │  • Buffering    • Sampling           │    manages arrivals    │
│  │  • Load Shedding • Punctuation       │                        │
│  └──────────────────┬───────────────────┘                        │
│                     ▼                                             │
│  ┌──────────────────────────────────────┐                        │
│  │      QUERY PROCESSING ENGINE         │  ← Continuous queries  │
│  │                                      │                        │
│  │  ┌──────────┐  ┌──────────────────┐  │                        │
│  │  │ Working  │  │ Query Processor  │  │                        │
│  │  │ Storage  │  │ • Window Ops     │  │                        │
│  │  │ (Limited │  │ • Aggregation    │  │                        │
│  │  │  Memory) │  │ • Join/Filter    │  │                        │
│  │  └──────────┘  └──────────────────┘  │                        │
│  └──────────────────┬───────────────────┘                        │
│                     ▼                                             │
│  ┌──────────────────────────────────────┐                        │
│  │         OUTPUT MANAGER               │                        │
│  │  • Push results to applications      │                        │
│  │  • Alerts, dashboards, storage       │                        │
│  └──────────────────────────────────────┘                        │
│                                                                  │
│  ┌──────────────────────────────────────┐                        │
│  │      STORED DATA (OPTIONAL)          │  ← Archival/DBMS      │
│  │  Historical data for comparison      │    for historical      │
│  └──────────────────────────────────────┘    queries              │
└──────────────────────────────────────────────────────────────────┘
```

### Key Characteristics of Data Streams:
1. **Continuous:** Data arrives constantly and endlessly
2. **Unbounded:** No predefined end to the stream
3. **Order matters:** Elements arrive in temporal sequence
4. **Real-time:** Must be processed immediately (one-pass processing)
5. **Transient:** Cannot store entire stream — must use limited memory

### Issues in Stream Processing:
- **Single Pass:** Cannot revisit data; must process in one scan
- **Memory Limitation:** Must use approximation algorithms (Bloom Filter, FM, DGIM)
- **Arrival Rate Variation:** Bursty arrivals require buffering or load shedding
- **Query Types:** Standing queries (continuous) vs Ad-hoc queries (one-time)

**MU Keyword Checklist:** DSMS, continuous data stream, unbounded, single-pass, working storage, sliding window, load shedding, input manager, query processor, standing queries, ad-hoc queries

---

## Q17. Explain Bloom Filter with Example. [5-10 Marks] — 3/6

**Question Type:** Theory + Numerical

### Definition
A **Bloom Filter** is a space-efficient probabilistic data structure used to test whether an element is a member of a set. It can produce **false positives** (says "yes" when element is absent) but **never false negatives** (never says "no" when element is present).

### Components:
- **Bit array** of size m (initially all 0s)
- **k hash functions** h₁, h₂, ..., hₖ mapping elements to positions 0 to m−1

### Operations:
```
INSERT(x):
  For each hash function hᵢ:
    Set bit_array[hᵢ(x)] = 1

LOOKUP(x):
  For each hash function hᵢ:
    If bit_array[hᵢ(x)] == 0: return "DEFINITELY NOT IN SET"
  return "PROBABLY IN SET" (could be false positive)
```

### Diagram
```
Before insertion:
Bit Array: [0] [0] [0] [0] [0] [0] [0] [0]
Position:   0    1    2    3    4    5    6    7

After inserting element x (h1(x)=1, h2(x)=4, h3(x)=6):
Bit Array: [0] [1] [0] [0] [1] [0] [1] [0]
Position:   0    1    2    3    4    5    6    7

Lookup element y (h1(y)=1, h2(y)=3, h3(y)=6):
Check: pos 1=1✅, pos 3=0❌ → DEFINITELY NOT IN SET
```

### Solved Numerical (Dec'24 — Full 10-mark question):

**Given:**
- Bit array size m = 8
- Hash functions: h1(x) = x mod 8, h2(x) = (2x+1) mod 8, h3(x) = (3x+2) mod 8
- Insert: 12, 25, 30, 5
- Check: 6, 55

**Step 1: Initialize bit array**
```
Position: [0] [1] [2] [3] [4] [5] [6] [7]
Value:     0   0   0   0   0   0   0   0
```

**Step 2: Insert element 12**
```
h1(12) = 12 mod 8 = 4
h2(12) = (2×12+1) mod 8 = 25 mod 8 = 1
h3(12) = (3×12+2) mod 8 = 38 mod 8 = 6

Set positions 4, 1, 6 to 1:
Position: [0] [1] [2] [3] [4] [5] [6] [7]
Value:     0   1   0   0   1   0   1   0
```

**Step 3: Insert element 25**
```
h1(25) = 25 mod 8 = 1
h2(25) = (2×25+1) mod 8 = 51 mod 8 = 3
h3(25) = (3×25+2) mod 8 = 77 mod 8 = 5

Set positions 1, 3, 5 to 1:
Position: [0] [1] [2] [3] [4] [5] [6] [7]
Value:     0   1   0   1   1   1   1   0
```

**Step 4: Insert element 30**
```
h1(30) = 30 mod 8 = 6
h2(30) = (2×30+1) mod 8 = 61 mod 8 = 5
h3(30) = (3×30+2) mod 8 = 92 mod 8 = 4

Set positions 6, 5, 4 to 1 (already set):
Position: [0] [1] [2] [3] [4] [5] [6] [7]
Value:     0   1   0   1   1   1   1   0
```

**Step 5: Insert element 5**
```
h1(5) = 5 mod 8 = 5
h2(5) = (2×5+1) mod 8 = 11 mod 8 = 3
h3(5) = (3×5+2) mod 8 = 17 mod 8 = 1

Set positions 5, 3, 1 to 1 (already set):
Position: [0] [1] [2] [3] [4] [5] [6] [7]
Value:     0   1   0   1   1   1   1   0
```

**Step 6: Check element 6**
```
h1(6) = 6 mod 8 = 6 → bit[6] = 1 ✅
h2(6) = (2×6+1) mod 8 = 13 mod 8 = 5 → bit[5] = 1 ✅
h3(6) = (3×6+2) mod 8 = 20 mod 8 = 4 → bit[4] = 1 ✅

All bits are 1 → "PROBABLY IN SET"
But 6 was NEVER inserted! → This is a FALSE POSITIVE ⚠️
```

**Step 7: Check element 55**
```
h1(55) = 55 mod 8 = 7 → bit[7] = 0 ❌

At least one bit is 0 → "DEFINITELY NOT IN SET" → TRUE NEGATIVE ✅
```

**Results Summary:**
| Element | h1 | h2 | h3 | Bits | Result |
|---------|----|----|----|----|--------|
| Check 6 | 6(1) | 5(1) | 4(1) | All 1 | **False Positive** |
| Check 55 | 7(0) | — | — | Has 0 | **True Negative** |

---

### 🌟 Solved Numerical (Nov 2025 — Official Exam Paper with MU Corrections) [10 Marks]
> **MU Official Exam Question (Paper Code 42172, Q3a):**
> *"Discuss Blooms filter in detail and insert elements 10 and 7 in Blooms filter of size 5 using following hash functions: 1) $h_1(x) = x \pmod 5$  2) $h_2(x) = (2x + 6) \pmod 5$."*

**Given:**
- Bit Array Size: $m = 5$ (Indices: 0, 1, 2, 3, 4)
- Number of Hash Functions: $k = 2$
- Hash Functions:
  1. $h_1(x) = x \pmod 5$
  2. $h_2(x) = (2x + 6) \pmod 5$
- Elements to Insert: $10$ and $7$

#### Step 1: Initialize Bit Array
All $m = 5$ bit positions are initialized to `0`.
```
Position: [0]  [1]  [2]  [3]  [4]
Value:     0    0    0    0    0
```

#### Step 2: Insert Element $x = 10$
Compute the hash values:
- $h_1(10) = 10 \pmod 5 = \mathbf{0}$
- $h_2(10) = (2 \times 10 + 6) \pmod 5 = (20 + 6) \pmod 5 = 26 \pmod 5 = \mathbf{1}$

Set bit positions $0$ and $1$ to `1`:
```
Operation: Set bit[0] = 1, bit[1] = 1
Position: [0]  [1]  [2]  [3]  [4]
Value:     1    1    0    0    0
```

#### Step 3: Insert Element $x = 7$
Compute the hash values:
- $h_1(7) = 7 \pmod 5 = \mathbf{2}$
- $h_2(7) = (2 \times 7 + 6) \pmod 5 = (14 + 6) \pmod 5 = 20 \pmod 5 = \mathbf{0}$

Set bit positions $2$ and $0$ to `1` (Note: bit position $0$ is already `1` from $x = 10$):
```
Operation: Set bit[2] = 1, bit[0] = 1 (already 1)
Position: [0]  [1]  [2]  [3]  [4]
Value:     1    1    1    0    0
```

#### Final Bit Array State After All Insertions:
$$\text{Bit Array } B = [1, 1, 1, 0, 0]$$
- **Occupied bit positions:** $\{0, 1, 2\}$ (Fraction of 1s = $3/5 = 60\%$)
- **Empty bit positions:** $\{3, 4\}$

#### Step 4: Membership Testing & Verification of Queries
1. **Query $x = 10$ (Inserted item):**
   - $h_1(10) = 0 \to B[0] = 1$ ✅
   - $h_2(10) = 1 \to B[1] = 1$ ✅
   - **Conclusion:** Both bits are 1 $\implies$ **"Probably Present" (True Positive)**.
2. **Query $x = 7$ (Inserted item):**
   - $h_1(7) = 2 \to B[2] = 1$ ✅
   - $h_2(7) = 0 \to B[0] = 1$ ✅
   - **Conclusion:** Both bits are 1 $\implies$ **"Probably Present" (True Positive)**.
3. **Query $x = 3$ (Uninserted item):**
   - $h_1(3) = 3 \pmod 5 = 3 \to B[3] = \mathbf{0}$ ❌
   - **Conclusion:** Since $B[3] = 0$, $x = 3$ was **definitely never inserted** $\implies$ **"Definitely NOT in Set" (True Negative)**.
4. **Query $x = 5$ (Uninserted item demonstrating Collision):**
   - $h_1(5) = 5 \pmod 5 = 0 \to B[0] = 1$ ✅
   - $h_2(5) = (2 \times 5 + 6) \pmod 5 = 16 \pmod 5 = 1 \to B[1] = 1$ ✅
   - **Conclusion:** Both $B[0]$ and $B[1]$ are set, even though 5 was **never inserted**! $\implies$ **"Probably Present" (FALSE POSITIVE)**.

---

### 🎯 Why Recall is 100% for Bloom Filter [5 Marks] — Nov'25 (Q1d)

**Question:** *"Why recall is 100% for blooms filter, explain in detail."*

#### 1. Mathematical Proof:
In classification and information retrieval, **Recall** (Sensitivity) is defined as:
$$\text{Recall} = \frac{\text{True Positives (TP)}}{\text{True Positives (TP)} + \text{False Negatives (FN)}}$$

For a Bloom Filter to achieve a recall of less than 100%, there must exist at least one **False Negative** ($\text{FN} > 0$).
A **False Negative** means:
> An element $x$ was previously inserted into the set $S$, but when queried, the Bloom filter incorrectly asserts that $x \notin S$ ("Definitely NOT in set").

#### 2. Why False Negatives Are Strictly Impossible ($\text{FN} = 0$):
1. **Deterministic Hashing:** The $k$ hash functions $h_1, h_2, \dots, h_k$ are completely deterministic. For any input $x$, $h_i(x)$ will always produce the identical position index $p_i$.
2. **Monotonic Bit Updates (Write-Only `1`s):** During `INSERT(x)`, every bit at index $h_i(x)$ is explicitly set to `1`:
   $$B[h_i(x)] \leftarrow 1 \quad \forall i \in \{1, 2, \dots, k\}$$
3. **No Bit Reset / No Eviction:** Standard Bloom Filters do **not** support deletions. Bits in the filter are never cleared or reset back to `0`. Once a bit transitions from `0` to `1`, it remains `1` forever.
4. **Lookup Condition:** A lookup operation returns "Definitely NOT in set" **if and only if** at least one bit $B[h_i(x)] == 0$.
5. **Conclusion:** If $x$ was inserted, every bit $B[h_i(x)]$ was set to `1` and could never have been set back to `0`. Therefore, a lookup on an inserted element can **never** encounter a `0` bit:
   $$P(\text{False Negative}) = 0 \implies \text{FN} = 0$$

Substituting $\text{FN} = 0$ into the Recall equation:
$$\text{Recall} = \frac{\text{TP}}{\text{TP} + 0} = \frac{\text{TP}}{\text{TP}} = 1.00 = \mathbf{100\%}$$

#### 3. Trade-off: Precision vs Recall:
- **Recall = 100%:** Guaranteed zero misses. If an item exists, the filter will NEVER miss it.
- **Precision < 100%:** Because multiple keys can map to the same bit positions (hash collisions), uninserted elements can accidentally find all their corresponding bits set to `1`, causing **False Positives** ($\text{FP} > 0$).
$$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}} < 100\%$$

**MU Keyword Checklist:** Bloom filter, bit array, hash functions, false positive, true negative, never false negative, probabilistic, space-efficient, membership testing, 100% recall proof, TP/(TP+FN), deterministic hashing.

---

## Q18. Flajolet-Martin Algorithm for Counting Distinct Elements. [10 Marks] — 6/6 GUARANTEED

**Question Type:** Numerical (MOST IMPORTANT — appears in EVERY paper)

### Core Concept
The **Flajolet-Martin algorithm** estimates the number of **distinct elements** in a data stream using hash functions and bit patterns.

### Key Idea:
- Hash each stream element to a binary integer
- Find r(a) = position of the **rightmost 1-bit** (trailing zeros count)
- Track R = max(r(a)) across all stream elements
- Estimated distinct count = **2^R**

### Formula:
```
r(a) = position of least significant 1-bit in binary(h(a))
     = number of trailing zeros + 1
     (equivalently: if binary ends in ...1, r=0; ...10, r=1; ...100, r=2)

R = max of all r(a) values

Estimated distinct elements ≈ 2^R
```

> **IMPORTANT NOTE on r(a) convention:** Different textbooks use different conventions. The most common MU convention is:
> - r(a) = number of trailing 0s in the binary representation of h(a)
> - Estimate = 2^R where R = max(r(a))

---

### ✅ SOLVED EXAMPLE 1 (Dec 2022)
**Stream:** 1, 3, 2, 1, 2, 3, 4, 3, 1, 2, 3, 1
**h(x) = 6x + 1 mod 5**

**Step 1: Compute hash values for distinct elements only**
Distinct elements: {1, 2, 3, 4}

| x | h(x) = (6x+1) mod 5 | Binary | Trailing 0s = r(x) |
|---|---------------------|--------|---------------------|
| 1 | (6+1) mod 5 = 7 mod 5 = **2** | 10 | 1 |
| 2 | (12+1) mod 5 = 13 mod 5 = **3** | 11 | 0 |
| 3 | (18+1) mod 5 = 19 mod 5 = **4** | 100 | 2 |
| 4 | (24+1) mod 5 = 25 mod 5 = **0** | 0 | ∞ (special case) |

**Step 2: R = max(r(x)) = 2** (ignoring the special case of 0)

**Step 3: Estimated distinct elements = 2^R = 2² = 4**

**Actual distinct elements = 4** {1, 2, 3, 4} ✅ Exact match!

---

### ✅ SOLVED EXAMPLE 2 (May 2023)
**Stream:** S = {2, 1, 6, 1, 5, 9, 2, 3, 5}
**h(x) = 4x + 1 mod 16, treat as 4-bit binary**

Distinct elements: {1, 2, 3, 5, 6, 9}

| x | h(x) = (4x+1) mod 16 | 4-bit Binary | Trailing 0s = r(x) |
|---|----------------------|-------------|---------------------|
| 1 | (4+1) mod 16 = **5** | 0101 | 0 |
| 2 | (8+1) mod 16 = **9** | 1001 | 0 |
| 3 | (12+1) mod 16 = **13** | 1101 | 0 |
| 5 | (20+1) mod 16 = **5** | 0101 | 0 |
| 6 | (24+1) mod 16 = **9** | 1001 | 0 |
| 9 | (36+1) mod 16 = **5** | 0101 | 0 |

**R = max(r(x)) = 0**

**Estimated distinct elements = 2⁰ = 1**

**Actual = 6.** Poor estimate — this shows FM requires **multiple hash functions** and averaging for accuracy in practice.

---

### ✅ SOLVED EXAMPLE 3 (Dec 2023)
**Stream:** S = {4, 2, 5, 9, 1, 6, 3, 7}
**h(x) = x + 6 mod 32, treat as 5-bit binary**

All elements are distinct. Count = 8.

| x | h(x) = (x+6) mod 32 | 5-bit Binary | Trailing 0s = r(x) |
|---|---------------------|-------------|---------------------|
| 4 | 10 | 01010 | 1 |
| 2 | 8 | 01000 | 3 |
| 5 | 11 | 01011 | 0 |
| 9 | 15 | 01111 | 0 |
| 1 | 7 | 00111 | 0 |
| 6 | 12 | 01100 | 2 |
| 3 | 9 | 01001 | 0 |
| 7 | 13 | 01101 | 0 |

**R = max(r(x)) = 3**

**Estimated distinct elements = 2³ = 8**

**Actual = 8** ✅ Exact match!

---

### ✅ SOLVED EXAMPLE 4 (May 2024)
**Stream:** S = {4, 2, 5, 9, 1, 6, 3, 7}
**h(x) = 3x + 7 mod 32, treat as 5-bit binary**

| x | h(x) = (3x+7) mod 32 | 5-bit Binary | Trailing 0s = r(x) |
|---|----------------------|-------------|---------------------|
| 4 | (12+7) mod 32 = **19** | 10011 | 0 |
| 2 | (6+7) mod 32 = **13** | 01101 | 0 |
| 5 | (15+7) mod 32 = **22** | 10110 | 1 |
| 9 | (27+7) mod 32 = **2** | 00010 | 1 |
| 1 | (3+7) mod 32 = **10** | 01010 | 1 |
| 6 | (18+7) mod 32 = **25** | 11001 | 0 |
| 3 | (9+7) mod 32 = **16** | 10000 | 4 |
| 7 | (21+7) mod 32 = **28** | 11100 | 2 |

**R = max(r(x)) = 4**

**Estimated distinct elements = 2⁴ = 16**

**Actual = 8.** Overestimate by factor of 2 — expected for single hash function.

---

### ✅ SOLVED EXAMPLE 5 (Dec 2024)
**Stream:** 9, 8, 7, 6, 5, 4, 3, 2
**h(x) = (2x+1) mod 32, treat as 5-bit binary**

| x | h(x) = (2x+1) mod 32 | 5-bit Binary | Trailing 0s = r(x) |
|---|----------------------|-------------|---------------------|
| 9 | (18+1) mod 32 = **19** | 10011 | 0 |
| 8 | (16+1) mod 32 = **17** | 10001 | 0 |
| 7 | (14+1) mod 32 = **15** | 01111 | 0 |
| 6 | (12+1) mod 32 = **13** | 01101 | 0 |
| 5 | (10+1) mod 32 = **11** | 01011 | 0 |
| 4 | (8+1) mod 32 = **9** | 01001 | 0 |
| 3 | (6+1) mod 32 = **7** | 00111 | 0 |
| 2 | (4+1) mod 32 = **5** | 00101 | 0 |

**R = max(r(x)) = 0**

**Estimated distinct elements = 2⁰ = 1**

**Actual = 8.** Very poor estimate — hash function maps all to odd numbers (all ending in 1). This demonstrates the need for better hash functions and multiple hash averaging.

---

### ✅ SOLVED EXAMPLE 6 (May 2025)
**Stream:** S = {10, 12, 8, 15, 6, 9, 14, 7}
**h(x) = 5x + 11 mod 32, treat as 5-bit binary**

| x | h(x) = (5x+11) mod 32 | 5-bit Binary | Trailing 0s = r(x) |
|---|----------------------|-------------|---------------------|
| 10 | (50+11) mod 32 = 61 mod 32 = **29** | 11101 | 0 |
| 12 | (60+11) mod 32 = 71 mod 32 = **7** | 00111 | 0 |
| 8 | (40+11) mod 32 = 51 mod 32 = **19** | 10011 | 0 |
| 15 | (75+11) mod 32 = 86 mod 32 = **22** | 10110 | 1 |
| 6 | (30+11) mod 32 = 41 mod 32 = **9** | 01001 | 0 |
| 9 | (45+11) mod 32 = 56 mod 32 = **24** | 11000 | 3 |
| 14 | (70+11) mod 32 = 81 mod 32 = **17** | 10001 | 0 |
| 7 | (35+11) mod 32 = 46 mod 32 = **14** | 01110 | 1 |

**R = max(r(x)) = 3**

**Estimated distinct elements = 2³ = 8**

**Actual = 8** ✅ Exact match!

---

### ✅ SOLVED EXAMPLE 7 (Nov 2025 — Official Paper with MU Corrections) [10 Marks]
> **MU Official Exam Question (Paper Code 42172, Q5a):**
> *"Suppose our stream consists of the integers 3, 1, 4, 1, 5, 9, 2, 6, 5. Determine the number of distinct elements if the hash function is: $h(x) = (3x + 7) \pmod 8$, treat the result as a 5-bit binary integer."*

#### Step 1: Identify Stream and Distinct Elements
- **Stream:** $S = [3, 1, 4, 1, 5, 9, 2, 6, 5]$ (Length $N = 9$)
- **Distinct Elements:** The set of unique values is $\{1, 2, 3, 4, 5, 6, 9\}$ $\implies \mathbf{7 \text{ actual distinct elements}}$.
- **Hash function:** $h(x) = (3x + 7) \pmod 8$
- **Format:** Represent hash output as a **5-bit binary integer** (e.g., $0 \to 00000_2$, $5 \to 00101_2$).

#### Step 2: Compute Hash Values, 5-bit Binary Representation, and Trailing Zeros $r(x)$

| Stream Element ($x$) | Arithmetic: $(3x + 7)$ | $h(x) = (3x+7) \pmod 8$ | 5-Bit Binary | Trailing Zeros $r(x)$ | Calculation Detail |
|:---:|:---:|:---:|:---:|:---:|:---|
| **3** | $3(3) + 7 = 16$ | $16 \pmod 8 = \mathbf{0}$ | **00000** | **5** | All 5 bits are zero; full 5-bit trailing zero string |
| **1** | $3(1) + 7 = 10$ | $10 \pmod 8 = \mathbf{2}$ | **00010** | **1** | Ends in `...10` $\to$ 1 trailing zero |
| **4** | $3(4) + 7 = 19$ | $19 \pmod 8 = \mathbf{3}$ | **00011** | **0** | Ends in `...1` $\to$ 0 trailing zeros |
| 1 | Duplicate (already hashed) | — | — | — | Skip redundant evaluation |
| **5** | $3(5) + 7 = 22$ | $22 \pmod 8 = \mathbf{6}$ | **00110** | **1** | Ends in `...10` $\to$ 1 trailing zero |
| **9** | $3(9) + 7 = 34$ | $34 \pmod 8 = \mathbf{2}$ | **00010** | **1** | Ends in `...10` $\to$ 1 trailing zero |
| **2** | $3(2) + 7 = 13$ | $13 \pmod 8 = \mathbf{5}$ | **00101** | **0** | Ends in `...1` $\to$ 0 trailing zeros |
| **6** | $3(6) + 7 = 25$ | $25 \pmod 8 = \mathbf{1}$ | **00001** | **0** | Ends in `...1` $\to$ 0 trailing zeros |
| 5 | Duplicate (already hashed) | — | — | — | Skip redundant evaluation |

#### Step 3: Determine Maximum Trailing Zeros ($R$)
$$R = \max_{x \in S} \{r(x)\} = \max \{5, 1, 0, 1, 1, 0, 0\} = \mathbf{5}$$

#### Step 4: Compute Flajolet-Martin Distinct Count Estimate
$$\text{Estimated Distinct Elements} = 2^R = 2^5 = \mathbf{32}$$

> [!NOTE]
> **Technical Examination Analysis & Academic Justification:**
> - **Actual Distinct Count:** $7$
> - **Basic FM Estimate:** $2^5 = 32$
> - **Standard Flajolet-Martin Correction Factor:**
>   The theoretical FM unbiased estimator applies constant $\phi \approx 0.77351$:
>   $$\text{Estimate}_{\text{corrected}} = \frac{2^R}{\phi} = \frac{32}{0.77351} \approx 41.37$$
> - **Why the Discrepancy Occurs:**
>   1. **Boundary Condition on Modulo 8:** Modulo 8 only yields numbers $0 \le y \le 7$. When $h(3) = 16 \pmod 8 = 0$, representing zero as a 5-bit integer (`00000`) creates an artificial tail of 5 trailing zeros.
>   2. **Small Stream Size:** Flajolet-Martin is designed for massive streams with millions of elements. On very small streams ($N = 9$) using a single hash function, stochastic variance is naturally high. In production systems (like HyperLogLog), stochastic averaging across $m = 2^p$ registers is mandatory to suppress variance.

---

### 🌟 Distinct Elements in Data Streams: Algorithm & Real-World Applications [5 Marks] — Nov'25 (Q1b)

**Question:** *"Which algorithm can be used for finding distinct elements in a long data stream? Give two real life applications for the same."*

#### 1. Algorithm: Flajolet-Martin (FM) Algorithm / HyperLogLog (HLL)
The **Flajolet-Martin algorithm** (and its modern derivative **HyperLogLog**) is the industry-standard probabilistic algorithm used to count unique elements (cardinality estimation) in an unbounded data stream using strictly logarithmic space:
$$\mathcal{O}(\log(\log N)) \text{ space compared to } \mathcal{O}(N) \text{ required by a Hash Set}$$

#### 2. Two Real-Life Industrial Applications:

##### Application 1: Unique Website Visitors / Daily Active Users (DAU) at Scale
- **Problem:** Tech giants like Google, Meta, and Netflix process billions of web access logs per second. Storing every unique user ID or IP address in a distributed hash table consumes tens of gigabytes of RAM per hour and introduces massive network synchronization latency.
- **Solution:** A stream of incoming request logs is routed through a Flajolet-Martin / HyperLogLog estimator. By maintaining only tiny register arrays (a few kilobytes), the analytics infrastructure continuously computes real-time unique active users (DAU/MAU) with less than 1% relative standard error.

##### Application 2: Network Intrusion Detection & DDoS Attack Mitigation
- **Problem:** High-speed internet backbone routers (Cisco, Juniper) monitor millions of concurrent network packets. A Denial of Service (DDoS) attack or network port scan is characterized by a malicious IP scanning thousands of distinct destination IP addresses or port numbers in milliseconds.
- **Solution:** Routers execute Flajolet-Martin cardinality counting on incoming TCP SYN packets grouped by source IP. If the estimated number of distinct destination ports or destination IP addresses for a single source IP spikes exponentially beyond a defined threshold within a sliding window, the router immediately flags an active DDoS/port-scanning attack and drops the traffic at wire speed.

---

## Q19. DGIM Algorithm for Counting Ones in a Stream. [5-10 Marks] — 4/6

**Question Type:** Theory + Numerical

### Definition
The **DGIM (Datar-Gionis-Indyk-Motwani) algorithm** provides an approximate count of the number of **1-bits** in the last N bits of a binary stream using limited memory.

### Key Concept: Buckets
Each bucket stores:
- **Size:** Number of 1s in the bucket (always a power of 2: 1, 2, 4, 8, ...)
- **Timestamp:** Position of the most recent bit in the bucket

### Six Constraints for Buckets:

| # | Constraint | Explanation |
|---|-----------|-------------|
| 1 | Bucket sizes are powers of 2 | Sizes: 1, 2, 4, 8, 16, ... |
| 2 | Buckets are ordered by timestamp | Most recent first, oldest last |
| 3 | Sizes are non-decreasing from right to left | Recent buckets are smaller or equal |
| 4 | At most 2 buckets of any given size | If 3 buckets of same size → merge the two oldest |
| 5 | At least 1 bucket of each size | Between smallest and largest |
| 6 | Buckets do not overlap | Each bit belongs to at most one bucket |

### How DGIM Works:
```
When a new bit arrives:
  If bit = 0: Just update timestamps (drop expired buckets)
  If bit = 1:
    1. Create a new bucket of size 1
    2. If there are now 3 buckets of size 1:
       Merge the two OLDEST into one bucket of size 2
    3. If there are now 3 buckets of size 2:
       Merge the two oldest into one bucket of size 4
    4. Continue cascading merges as needed

To QUERY "How many 1s in last k bits?":
  1. Find all buckets that overlap with the last k positions
  2. Sum up all complete buckets
  3. For the OLDEST bucket that partially overlaps: add HALF its size
  4. This gives an approximate answer
```

### Example:
```
Binary stream (left = oldest):  ...1 0 1 1 0 1 1 0 1 0 1 1

Buckets (right to left):
  [1] [1] [2]   [2]    [4]
   ↑    ↑   ↑     ↑      ↑
  most recent          oldest

Query: "How many 1s in last 10 bits?"
- Count complete buckets within window: 1 + 1 + 2 + 2 = 6
- Oldest bucket (size 4) partially overlaps: add 4/2 = 2
- Estimate = 6 + 2 = 8

Error bound: At most 50% of the largest bucket size
```

**MU Keyword Checklist:** DGIM, buckets, powers of 2, timestamp, merge rule, at most 2 per size, approximate count, 50% error bound, sliding window, binary stream

---

## Q20. Explain the Flajolet-Martin Algorithm in Detail. [Theory — for understanding]

### Algorithm Summary:
```
┌──────────────────────────────────────────────┐
│      FLAJOLET-MARTIN ALGORITHM               │
│                                              │
│  INPUT: Stream S = {a₁, a₂, ..., aₙ}        │
│  GOAL: Estimate number of DISTINCT elements  │
│                                              │
│  1. Choose hash function h mapping elements  │
│     to integers in [0, 2^L - 1]             │
│                                              │
│  2. For each element a in stream:            │
│     • Compute h(a)                           │
│     • Convert to L-bit binary               │
│     • Find r(a) = # trailing zeros           │
│     • Update R = max(R, r(a))               │
│                                              │
│  3. Estimated distinct count = 2^R           │
│                                              │
│  IMPROVING ACCURACY:                         │
│  • Use multiple hash functions h₁,h₂,...,hₖ │
│  • Compute R for each                       │
│  • Group results, take median of averages    │
│  • This reduces variance significantly       │
└──────────────────────────────────────────────┘
```

### Why it works (Intuition):
- If there are d distinct elements, the probability that the maximum trailing zeros = log₂(d) is highest
- More distinct elements → higher chance of seeing a hash value ending in many zeros
- Like flipping a coin: with d flips, you expect to see a run of about log₂(d) consecutive heads

**MU Keyword Checklist:** Flajolet-Martin, hash function, trailing zeros, rightmost 1-bit, R = max, 2^R estimate, distinct elements, data stream, space-efficient, multiple hash functions, median of averages
