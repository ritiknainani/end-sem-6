# 📘 BDA ULTIMATE MASTERCLASS — Part 1: Modules 1 & 2

# MODULE 1: INTRODUCTION TO BIG DATA AND HADOOP

---

## Q1. What is Big Data? Explain the characteristics (V's) of Big Data. [5-10 Marks] — 4/6

**Question Type:** Theory

### Definition
**Big Data** refers to datasets that are so large, fast-moving, or complex that traditional data processing tools and methods are incapable of storing, managing, and analyzing them efficiently.

### The 5 V's of Big Data

| V | Characteristic | Definition | Example |
|---|---------------|------------|---------|
| **Volume** | Size of data | Enormous quantity of data generated | Facebook generates 4+ petabytes/day |
| **Velocity** | Speed of data | Rate at which data is generated and processed | Stock market trades in milliseconds |
| **Variety** | Types of data | Structured, semi-structured, unstructured | Text, images, videos, sensor data, logs |
| **Veracity** | Quality/Trust | Accuracy, reliability, and trustworthiness of data | Incomplete medical records, noisy social media |
| **Value** | Business worth | Ability to extract meaningful insights | Netflix recommendation → \$1B/year savings |

### Diagram — Big Data Characteristics
```
                    ┌──────────┐
                    │  VOLUME   │
                    │ Terabytes │
                    │ Petabytes │
                    └─────┬────┘
         ┌────────────────┼────────────────┐
         ▼                ▼                ▼
   ┌──────────┐    ┌──────────┐    ┌──────────┐
   │ VELOCITY  │    │ BIG DATA │    │ VARIETY   │
   │ Real-time │◄──►│  5 V's   │◄──►│Structured │
   │ Batch     │    │          │    │Unstructured│
   └──────────┘    └─────┬────┘    └──────────┘
         ┌────────────────┼────────────────┐
         ▼                                 ▼
   ┌──────────┐                     ┌──────────┐
   │ VERACITY  │                     │  VALUE    │
   │ Accuracy  │                     │ Business  │
   │ Trust     │                     │ Insights  │
   └──────────┘                     └──────────┘
```

### Social Media Context (as asked in May'23, May'25):
- **Volume:** 500 million tweets/day, 95 million Instagram photos/day
- **Velocity:** Real-time feeds, trending hashtags update every second
- **Variety:** Text posts, images, videos, stories, reels, check-ins
- **Veracity:** Fake news, bot accounts, misinformation
- **Value:** Targeted advertising, sentiment analysis, market trends

**MU Keyword Checklist:** Volume, Velocity, Variety, Veracity, Value, structured, unstructured, semi-structured, petabytes, real-time processing

---

## Q2. Differentiate between Traditional RDBMS and Hadoop. [5 Marks] — Dec'23

**Question Type:** Theory (Comparison)

| Parameter | Traditional RDBMS | Hadoop |
|-----------|------------------|--------|
| **Data Size** | Gigabytes | Petabytes to Exabytes |
| **Data Type** | Structured only | Structured, semi-structured, unstructured |
| **Schema** | Schema-on-Write (predefined) | Schema-on-Read (flexible) |
| **Processing** | Interactive, real-time queries | Batch processing |
| **Scaling** | Vertical (scale-up: bigger server) | Horizontal (scale-out: add more nodes) |
| **Cost** | Expensive (proprietary licenses) | Cost-effective (commodity hardware) |
| **Data Integrity** | ACID compliant | Eventual consistency (BASE) |
| **Best For** | OLTP transactions | Large-scale analytics, ETL |
| **Examples** | Oracle, MySQL, SQL Server | Hadoop, Spark, Hive |

**MU Keyword Checklist:** Schema-on-Write vs Schema-on-Read, vertical vs horizontal scaling, ACID vs BASE, batch processing, commodity hardware

---

## Q3. Explain the Concept of Hadoop and its Core Components. [10 Marks] — 3/6

**Question Type:** Architecture

### Definition
**Apache Hadoop** is an open-source framework that allows distributed processing of large datasets across clusters of commodity computers using simple programming models. It is designed to scale from a single server to thousands of machines.

### Core Components

```
┌─────────────────────────────────────────────────────────────┐
│                    HADOOP ECOSYSTEM                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────┐  ┌──────┐  ┌───────┐  ┌────────┐  ┌──────┐  │
│   │  Sqoop   │  │ Flume│  │  Pig  │  │  Hive  │  │Oozie │  │
│   │(Import/  │  │(Log  │  │(Script│  │(SQL-   │  │(Work-│  │
│   │ Export)  │  │Collect│  │  ing) │  │ like)  │  │ flow)│  │
│   └─────────┘  └──────┘  └───────┘  └────────┘  └──────┘  │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐   │
│   │              MapReduce (Processing Layer)            │   │
│   │   ┌──────────┐    ┌────────────┐    ┌────────────┐  │   │
│   │   │ Job      │    │  Map Tasks  │    │ Reduce     │  │   │
│   │   │ Tracker  │───►│ (Parallel)  │───►│ Tasks      │  │   │
│   │   └──────────┘    └────────────┘    └────────────┘  │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐   │
│   │                HDFS (Storage Layer)                   │   │
│   │                                                      │   │
│   │   ┌──────────┐     ┌──────────┐  ┌──────────┐      │   │
│   │   │ NameNode │     │DataNode 1│  │DataNode 2│ ...  │   │
│   │   │(Master)  │────►│(Slave)   │  │(Slave)   │      │   │
│   │   │Metadata  │     │Block     │  │Block     │      │   │
│   │   │Namespace │     │Storage   │  │Storage   │      │   │
│   │   └──────────┘     └──────────┘  └──────────┘      │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐   │
│   │                YARN (Resource Manager)               │   │
│   │   ResourceManager ──► NodeManager ──► Containers     │   │
│   └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Component Details:

**1. HDFS (Hadoop Distributed File System):**
- Distributed, scalable, fault-tolerant storage system
- Files split into **blocks** (default 128 MB), replicated across nodes (default replication factor = 3)
- **NameNode (Master):** Stores metadata (file names, permissions, block locations); manages namespace
- **DataNode (Slave):** Stores actual data blocks; sends heartbeat to NameNode every 3 seconds
- **Secondary NameNode:** NOT a backup of NameNode. It periodically merges the fsimage and edit logs to prevent edit log from growing too large (checkpointing)

**2. MapReduce (Processing Engine):**
- Programming model for parallel processing of large datasets
- Two phases: **Map** (transforms data into key-value pairs) → **Reduce** (aggregates values by key)
- **JobTracker (Master):** Schedules tasks, monitors progress
- **TaskTracker (Slave):** Executes Map and Reduce tasks on DataNodes

**3. YARN (Yet Another Resource Negotiator):**
- Resource management layer separating resource management from job scheduling
- **ResourceManager:** Global resource allocation
- **NodeManager:** Per-node agent managing containers
- **ApplicationMaster:** Per-application lifecycle management

**MU Keyword Checklist:** HDFS, MapReduce, YARN, NameNode, DataNode, Secondary NameNode, block size 128MB, replication factor 3, JobTracker, TaskTracker, ResourceManager, NodeManager, fault-tolerant, commodity hardware

---

## Q4. Distinguish between NameNode and DataNode. [5 Marks] — 5/6

**Question Type:** Theory (Comparison)

| Parameter | NameNode | DataNode |
|-----------|----------|----------|
| **Role** | Master node | Slave node |
| **Function** | Stores metadata & namespace | Stores actual data blocks |
| **Data Stored** | File names, permissions, block locations | Raw data blocks (128 MB each) |
| **Quantity** | Single (one per cluster) | Multiple (thousands per cluster) |
| **Heartbeat** | Receives heartbeats | Sends heartbeat every 3 seconds |
| **Failure Impact** | Critical — entire cluster goes down (SPOF) | Non-critical — data re-replicated to other nodes |
| **Memory** | High RAM required (all metadata in memory) | Moderate RAM |
| **Communication** | Communicates with all DataNodes | Reports to NameNode, serves read/write requests |

> **Important (Dec'24):** Secondary NameNode is **NOT** a backup/standby of NameNode. It performs **checkpointing** — periodically merging fsimage + edit logs. For true HA, Hadoop uses **Standby NameNode** with ZooKeeper.

**MU Keyword Checklist:** Master vs Slave, metadata vs data blocks, heartbeat, 128 MB, single point of failure, checkpointing, replication

---

## Q5. Why is HDFS suited for large datasets but not small files? [5 Marks] — Dec'22

**Question Type:** Theory

### HDFS is suited for large datasets because:
1. **Block-based storage:** Files split into large blocks (128 MB) — efficient for sequential reads of massive files
2. **High throughput:** Optimized for batch processing; streams data at high bandwidth
3. **Write-once, read-many:** Designed for append-only workloads — perfect for log processing, data warehousing
4. **Fault tolerance:** 3x replication ensures no data loss even if nodes fail
5. **Horizontal scalability:** Simply add more DataNodes to increase storage

### HDFS is NOT suited for small files because:
1. **NameNode memory overhead:** Each file/block requires ~150 bytes of metadata in NameNode's RAM. Millions of small files → NameNode memory exhaustion
2. **Block wastage:** A 1 KB file still occupies one block entry in metadata (though not 128 MB on disk)
3. **Excessive seeks:** Many small files = many disk seeks = poor performance (HDFS optimized for streaming, not random access)
4. **MapReduce inefficiency:** Each small file spawns a separate Map task → overhead exceeds actual processing

**MU Keyword Checklist:** 128 MB blocks, NameNode memory, metadata overhead, write-once read-many, sequential reads, streaming access, seek-to-transfer ratio

---

## Q6. How is Node Failure Handled in Hadoop? [5 Marks] — Dec'23

**Question Type:** Theory

1. **Heartbeat Mechanism:** Each DataNode sends a heartbeat signal to the NameNode every **3 seconds**
2. **Failure Detection:** If NameNode does not receive heartbeat for **10 minutes** (configurable), it marks the DataNode as **dead**
3. **Re-replication:** NameNode identifies all blocks that were stored on the dead DataNode and initiates **re-replication** to maintain the replication factor (default = 3)
4. **Task Re-execution:** If a MapReduce task was running on the failed node, the **JobTracker** re-assigns the task to another available node
5. **Speculative Execution:** Hadoop can also run **duplicate tasks** on different nodes; the first to complete is used, reducing impact of slow/failing nodes

```
Normal Operation:           Node Failure:
┌──────────┐               ┌──────────┐
│ NameNode │◄─heartbeat──  │ NameNode │  ✗ No heartbeat
│          │   every 3s    │          │   for 10 min
└──────────┘               └──────────┘
     │                          │
     ▼                          ▼
┌────┐┌────┐┌────┐        Mark dead → Re-replicate
│ DN1││ DN2││ DN3│        blocks to other live nodes
└────┘└────┘└────┘
```

**MU Keyword Checklist:** Heartbeat, 3 seconds, 10-minute timeout, re-replication, replication factor, speculative execution, JobTracker reassignment

---

# MODULE 2: HADOOP HDFS AND MAPREDUCE

---

## Q7. Explain Map Tasks and Reduce Tasks in MapReduce. [5-10 Marks] — 4/6

**Question Type:** Theory / Architecture

### Definition
**MapReduce** is a programming model for processing large datasets in parallel across a distributed cluster. It works in two main phases: **Map** and **Reduce**, with an intermediate **Shuffle & Sort** phase.

### Architecture / Execution Pipeline
```
┌──────────────────────────────────────────────────────────────────┐
│                    MapReduce Execution Pipeline                   │
│                                                                  │
│  ┌──────────┐    ┌──────────┐    ┌───────────┐    ┌──────────┐  │
│  │  INPUT    │    │   MAP     │    │ SHUFFLE   │    │  REDUCE  │  │
│  │  SPLITS   │───►│  PHASE    │───►│  & SORT   │───►│  PHASE   │──►OUTPUT
│  │           │    │           │    │           │    │          │  │
│  │ Split 1 ──┤    │ Mapper 1  │    │ Group by  │    │Reducer 1 │  │
│  │ Split 2 ──┤    │ Mapper 2  │    │   Key     │    │Reducer 2 │  │
│  │ Split 3 ──┤    │ Mapper 3  │    │           │    │          │  │
│  └──────────┘    └──────────┘    └───────────┘    └──────────┘  │
│                       │               │                │         │
│              (key, value)    (key, [v1,v2..])    (key, result)   │
└──────────────────────────────────────────────────────────────────┘
```

### Phase Details:

**1. Map Phase:**
- Input data is split into **input splits** (one per block, typically 128 MB)
- Each split is processed by one **Mapper** in parallel
- Mapper reads input as (key, value) pairs and produces **intermediate (key, value) pairs**
- Example: For word count, each word becomes a key with value 1: `("hello", 1)`

**2. Shuffle & Sort Phase (Intermediate):**
- System automatically sorts and groups all intermediate outputs by key
- All values for the same key are collected together
- Data is transferred from Mappers to Reducers across the network (this is the most I/O intensive phase)

**3. Reduce Phase:**
- Each Reducer receives a key and list of all its values: `("hello", [1, 1, 1])`
- Reducer applies aggregation function (sum, count, max, etc.)
- Produces final output: `("hello", 3)`

**4. Combiner (Optional — Local Reducer):**
- Runs on the Mapper node BEFORE shuffle
- Performs local aggregation to reduce network traffic
- Example: If Mapper produces `("the",1), ("the",1), ("the",1)` → Combiner outputs `("the",3)`

**MU Keyword Checklist:** Map phase, Reduce phase, Shuffle & Sort, input splits, key-value pairs, intermediate output, combiner, parallel processing, Mapper, Reducer

---

## Q8. Write MapReduce Pseudo Code for Word Count. Apply on given document. [10 Marks] — 4/6

**Question Type:** Numerical / Code

### Pseudo Code:
```
// MAP FUNCTION
function MAP(key: document_id, value: document_text):
    for each word w in document_text:
        EMIT(w, 1)

// REDUCE FUNCTION  
function REDUCE(key: word, values: list_of_counts):
    total = 0
    for each count in values:
        total = total + count
    EMIT(word, total)
```

### Solved Example 1: "This is an apple. Apple is red in color"

**Step 1: Input Split**
Document: "This is an apple. Apple is red in color"

**Step 2: MAP Phase — Tokenize and emit (word, 1)**
```
Mapper Output:
(This, 1), (is, 1), (an, 1), (apple, 1), (Apple, 1),
(is, 1), (red, 1), (in, 1), (color, 1)

Note: Case-sensitive. If case-insensitive, convert to lowercase first.
```

**Step 3: SHUFFLE & SORT — Group by key (alphabetical)**
```
(an,      [1])
(apple,   [1])
(Apple,   [1])
(color,   [1])
(in,      [1])
(is,      [1, 1])
(red,     [1])
(This,    [1])
```

**Step 4: REDUCE — Sum up values for each key**
```
┌──────────┬──────────────────┬─────────────┐
│   Word   │ Shuffle & Sort   │ Reduce (Sum)│
├──────────┼──────────────────┼─────────────┤
│ an       │ [1]              │ 1           │
│ apple    │ [1]              │ 1           │
│ Apple    │ [1]              │ 1           │
│ color    │ [1]              │ 1           │
│ in       │ [1]              │ 1           │
│ is       │ [1, 1]           │ 2           │
│ red      │ [1]              │ 1           │
│ This     │ [1]              │ 1           │
└──────────┴──────────────────┴─────────────┘
```

### Solved Example 2: "This is NoSQL. NoSQL handles complex data." (Dec'24)

**MAP Output:**
```
(This,1), (is,1), (NoSQL,1), (NoSQL,1), (handles,1), (complex,1), (data,1)
```

**SHUFFLE & SORT:**
```
(complex, [1])
(data,    [1])
(handles, [1])
(is,      [1])
(NoSQL,   [1, 1])
(This,    [1])
```

**REDUCE Output:**
```
(complex, 1), (data, 1), (handles, 1), (is, 1), (NoSQL, 2), (This, 1)
```

### Solved Example 3: "Big data is powerful. Big data drives decisions." (May'25)

**MAP Output:**
```
(Big,1), (data,1), (is,1), (powerful,1), (Big,1), (data,1), (drives,1), (decisions,1)
```

**SHUFFLE & SORT:**
```
(Big,       [1, 1])
(data,      [1, 1])
(decisions, [1])
(drives,    [1])
(is,        [1])
(powerful,  [1])
```

**REDUCE Output:**
```
┌────────────┬───────┐
│ Word       │ Count │
├────────────┼───────┤
│ Big        │   2   │
│ data       │   2   │
│ decisions  │   1   │
│ drives     │   1   │
│ is         │   1   │
│ powerful   │   1   │
└────────────┴───────┘
```

**MU Keyword Checklist:** MAP function, REDUCE function, EMIT, key-value pairs, tokenize, shuffle & sort, aggregation, combiner, parallel

---

## Q9. Explain MapReduce Matrix Multiplication with example. [10 Marks] — 2/6

**Question Type:** Numerical

### Core Concept
For matrix multiplication C = M × V, where M is an m×n matrix and V is an n-vector:
- C[i] = Σⱼ M[i][j] × V[j]

### MAP and REDUCE Functions:
```
MAP (for Matrix-Vector Multiplication):
  For each element m_ij of matrix M:
    EMIT(i, m_ij × v_j)

REDUCE:
  For each key i:
    Sum all values → C[i]
```

### Solved Example (May'23, Dec'23):
```
        ┌ 1  2  3 ┐       ┌ 1 ┐
M   =   │ 4  5  6 │   V = │ 2 │
        └ 7  8  9 ┘       └ 3 ┘
```

**Step 1: MAP Phase — Emit (row_index, m_ij × v_j)**
```
For Row 0 (i=0):
  m_00 × v_0 = 1 × 1 = 1  → EMIT(0, 1)
  m_01 × v_1 = 2 × 2 = 4  → EMIT(0, 4)
  m_02 × v_2 = 3 × 3 = 9  → EMIT(0, 9)

For Row 1 (i=1):
  m_10 × v_0 = 4 × 1 = 4  → EMIT(1, 4)
  m_11 × v_1 = 5 × 2 = 10 → EMIT(1, 10)
  m_12 × v_2 = 6 × 3 = 18 → EMIT(1, 18)

For Row 2 (i=2):
  m_20 × v_0 = 7 × 1 = 7  → EMIT(2, 7)
  m_21 × v_1 = 8 × 2 = 16 → EMIT(2, 16)
  m_22 × v_2 = 9 × 3 = 27 → EMIT(2, 27)
```

**Step 2: SHUFFLE & SORT**
```
Key 0 → [1, 4, 9]
Key 1 → [4, 10, 18]
Key 2 → [7, 16, 27]
```

**Step 3: REDUCE — Sum values for each key**
```
C[0] = 1 + 4 + 9   = 14
C[1] = 4 + 10 + 18 = 32
C[2] = 7 + 16 + 27 = 50

        ┌ 14 ┐
C   =   │ 32 │
        └ 50 ┘
```

**Verification:** 1×1+2×2+3×3 = 1+4+9 = 14 ✅

**MU Keyword Checklist:** Matrix-vector multiplication, EMIT(i, m_ij × v_j), row index as key, summation in reduce, parallel row computation

---

## Q10. Explain Relational Algebra Operations using MapReduce. [10 Marks] — 3/6

**Question Type:** Theory / Numerical

### a) Selection (σ)
Filters rows based on a condition.
```
MAP:  For each tuple t in relation R:
        if condition(t) is TRUE:
          EMIT(t, t)
REDUCE: Identity — just output each tuple

Example: σ(age > 25)(Employee)
MAP checks each row: if age > 25, emit it
```

### b) Projection (π)
Selects specific columns, removes duplicates.
```
MAP:  For each tuple t in relation R:
        t' = extract desired attributes from t
        EMIT(t', t')
REDUCE: Remove duplicates — for each key t', emit just one copy

Example: π(name, salary)(Employee)
MAP emits only (name, salary) pairs
REDUCE removes duplicates
```

### c) Natural Join (⋈)
Joins two relations on common attributes.
```
MAP:  For each tuple t in R: EMIT(t.join_key, ("R", t))
      For each tuple s in S: EMIT(s.join_key, ("S", s))

REDUCE: For each key k:
        Separate into R-tuples and S-tuples
        Output all combinations (Cartesian product of R × S for that key)
```

### d) Grouping and Aggregation (γ)
```
MAP:  For each tuple t:
        EMIT(t.group_attribute, t.agg_attribute)

REDUCE: For each group key:
        Apply aggregation (SUM, COUNT, AVG, MAX, MIN) on values

Example: γ(dept, SUM(salary))(Employee)
MAP: EMIT(dept, salary)
REDUCE: For each dept, sum all salaries
```

### e) Union, Intersection, Difference
```
Union (R ∪ S):
  MAP: Emit all tuples from R and S as (tuple, tuple)
  REDUCE: For each key, emit once (removes duplicates)

Intersection (R ∩ S):
  MAP: Tag tuples — EMIT(tuple, "R") and EMIT(tuple, "S")
  REDUCE: Emit only if BOTH "R" and "S" tags present

Difference (R − S):
  MAP: EMIT(tuple, "R") and EMIT(tuple, "S")
  REDUCE: Emit only if "R" tag present but NOT "S"
```

**MU Keyword Checklist:** Selection σ, Projection π, Natural Join ⋈, Grouping γ, Union, Intersection, Difference, MAP EMIT, REDUCE aggregate, join key, duplicate elimination

---

## Q11. Explain the Shuffle & Sort Phase in MapReduce. [5 Marks] — May'25

**Question Type:** Theory

### Definition
The **Shuffle & Sort** phase is the intermediate step between Map and Reduce that transfers, groups, and sorts the intermediate key-value pairs produced by Mappers before they are consumed by Reducers.

### Steps:
1. **Partitioning:** Intermediate keys are assigned to specific Reducers using a hash partitioner: `reducer = hash(key) mod num_reducers`
2. **Sorting:** Each partition is sorted by key on the Mapper side (local sort)
3. **Transferring (Shuffle):** Sorted partitions are transferred over the network to the appropriate Reducer nodes
4. **Merging:** At the Reducer, sorted streams from multiple Mappers are merged (merge sort) into a single sorted stream
5. **Grouping:** All values for the same key are grouped together as input to the Reduce function

```
Mapper 1 output:     Mapper 2 output:
(a,1)(b,2)(c,3)      (a,4)(b,5)(d,6)
       │                    │
       └───── SHUFFLE ──────┘
              (Network Transfer)
                    │
              ┌─────┴──────┐
              ▼            ▼
         Reducer 1     Reducer 2
         (a,[1,4])     (c,[3])
         (b,[2,5])     (d,[6])
```

**MU Keyword Checklist:** Partitioner, hash function, local sort, network transfer, merge sort, grouping by key, intermediate key-value pairs

---

## Q12. Explain MapReduce Execution Pipeline with example. [10 Marks] — 2/6

**Question Type:** Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│                   MapReduce Execution Pipeline                         │
│                                                                        │
│  ┌────────┐    ┌─────────────┐    ┌──────────┐    ┌──────────────┐    │
│  │ Client │───►│ JobTracker  │    │TaskTracker│    │  TaskTracker  │    │
│  │(Submit │    │(Master)     │───►│  Node 1   │    │   Node 2     │    │
│  │  Job)  │    │Schedule/    │    │           │    │              │    │
│  └────────┘    │Monitor      │    └──────────┘    └──────────────┘    │
│                └─────────────┘                                        │
│                                                                        │
│  Step-by-step execution flow:                                          │
│                                                                        │
│  1. CLIENT submits job to JobTracker                                   │
│  2. JobTracker queries NameNode for block locations                    │
│  3. JobTracker assigns Map tasks to TaskTrackers (data locality)       │
│  4. TaskTrackers execute Map tasks on local data                       │
│  5. Map output stored on local disk (intermediate files)               │
│  6. Shuffle & Sort: Framework transfers data to Reducer nodes          │
│  7. Reduce tasks aggregate results                                     │
│  8. Output written to HDFS                                            │
│                                                                        │
│  Timeline:                                                             │
│  ┌──────┐  ┌──────┐  ┌──────────┐  ┌──────┐  ┌────────┐              │
│  │INPUT │─►│ MAP  │─►│SHUFFLE & │─►│REDUCE│─►│ OUTPUT │              │
│  │SPLITS│  │PHASE │  │  SORT    │  │PHASE │  │(HDFS)  │              │
│  └──────┘  └──────┘  └──────────┘  └──────┘  └────────┘              │
└────────────────────────────────────────────────────────────────────────┘
```

### Key Concepts:
- **Data Locality:** Map tasks are preferably assigned to nodes where the data resides (to minimize network I/O)
- **Speculative Execution:** If a task is slow, a duplicate is launched on another node
- **Fault Tolerance:** If a TaskTracker fails, JobTracker reassigns its tasks to other nodes
- **Progress Tracking:** TaskTrackers send heartbeat + progress reports to JobTracker

**MU Keyword Checklist:** JobTracker, TaskTracker, data locality, speculative execution, input splits, intermediate output, shuffle & sort, fault tolerance, heartbeat, HDFS output
