# Mumbai University (MU) Semester 7 — Management Information Systems (MIS)
## Masterclass Part 2: Modules 4, 5 & 6 (Social Computing, Cloud, ERP & Hospital MIS Design)
**Course Code:** Department Level Optional Course (DLOC) | **Scheme:** Rev 2019 / C-Scheme | **Applicable Cycles:** Dec 2022 – Nov 2025 (7 Consecutive Exam Cycles)

---

# MODULE 4: SOCIAL COMPUTING, CRM & E-COMMERCE / M-COMMERCE

---

## 4.1 Evolution of the Web: Web 1.0 vs Web 2.0 vs Web 3.0
*(Appeared in: Dec 2022 Q1c [5M], Dec 2023 Q6b [10M], Nov 2025 Q2b [10M])*

The World Wide Web has evolved across three major technological and architectural paradigms:

```
+---------------------------------------------------------------------------------------------------+
|                                  THE THREE GENERATIONS OF THE WEB                                 |
+---------------------------------------------------------------------------------------------------+
| Parameter          | Web 1.0 (Syntactic Web)      | Web 2.0 (Social / Read-Write) | Web 3.0 (Semantic / Decentralized) |
+--------------------+------------------------------+-------------------------------+------------------------------------+
| Defining Paradigm  | **The Read-Only Web**        | **The Read-Write Web**        | **The Read-Write-Own Web**         |
|                    | (Information Consumption).   | (User-Generated Content).     | (User Sovereignty & AI Context).   |
+--------------------+------------------------------+-------------------------------+------------------------------------+
| Core Technologies  | Static HTML, CSS, CGI,       | AJAX, JavaScript Frameworks,  | Smart Contracts, Blockchain, IPFS, |
|                    | Personal web pages.          | REST APIs, Mobile Apps.       | RDF/OWL Semantic Ontologies, LLMs. |
+--------------------+------------------------------+-------------------------------+------------------------------------+
| Content Creators   | Select webmasters & corporate| Millions of global active     | Autonomous AI agents, decentralized|
|                    | publishers.                  | users (Social networks).      | DAOs, peer-to-peer creators.       |
+--------------------+------------------------------+-------------------------------+------------------------------------+
| Architecture       | Centralized server-client.   | Centralized tech oligopolies  | Decentralized P2P networks; zero   |
|                    |                              | (Meta, Google, Amazon cloud). | single point of corporate failure. |
+--------------------+------------------------------+-------------------------------+------------------------------------+
| Data Ownership     | Server owner.                | Platform owns and monetizes   | User owns private keys and data    |
|                    |                              | user behavioral telemetry.    | in self-custodial digital wallets. |
+--------------------+------------------------------+-------------------------------+------------------------------------+
| Archetypes         | Britannica Online, Yahoo!    | YouTube, Wikipedia, Twitter,  | Ethereum DApps, Uniswap, Brave,    |
|                    | Directory, Personal GeoCities| Facebook, Instagram, Reddit.  | Solid (Tim Berners-Lee).           |
+--------------------+------------------------------+-------------------------------+------------------------------------+
```

### Comprehensive Deep-Dive by Generation:
1. **Web 1.0 (The Syntactic / Read-Only Web: 1991 – 2004):**
   - *Technical Mechanics:* Static HTML files hosted on web servers delivered directly to client browsers over HTTP. No dynamic database-driven interaction; user interactivity was restricted to clicking hyperlinks and submitting basic web forms via CGI scripts.
   - *Business Model:* Banner advertising and directory listings.
   - *Real-World Examples:* Early CNN.com, Encyclopedia Britannica Online, personal GeoCities pages, Yahoo! Web Directory.
2. **Web 2.0 (The Social / Read-Write Web: 2004 – Present):**
   - *Technical Mechanics:* Dynamic client-server architecture powered by AJAX (Asynchronous JavaScript and XML) allowing asynchronous background data fetching without full page refreshes. Cloud-hosted relational/NoSQL databases, RESTful microservices, and mobile application ecosystems.
   - *Defining Characteristic:* Users transform from passive consumers into active content creators (blogs, videos, reviews, social graph interactions).
   - *Business Model:* Targeted programmatic advertising fueled by continuous behavioral surveillance and user data aggregation.
   - *Real-World Examples:* YouTube, Facebook/Instagram, Wikipedia, Twitter/X, Reddit, TikTok.
3. **Web 3.0 (The Semantic / Decentralized / Read-Write-Own Web: Emerging):**
   - *Technical Mechanics:* Built on distributed ledgers (Ethereum, Solana), decentralized file storage (IPFS, Arweave), and semantic web ontologies (RDF, OWL, SPARQL) enabling machines to understand contextual data relationships.
   - *Defining Characteristic:* Decentralization and cryptographic ownership. Users authenticate via asymmetric cryptographic keypairs (e.g., MetaMask wallets) rather than corporate OAuth (Sign-in with Google), granting true digital sovereignty over personal assets, identity, and content without platform intermediaries.
   - *Business Model:* Tokenomics, decentralized finance (DeFi) protocol fees, smart-contract royalties, and DAO governance tokens.
   - *Real-World Examples:* Uniswap (decentralized automated market maker), Brave Browser (BAT tokenomics), Lens Protocol (decentralized social graph), Solid Project.

---

## 4.2 Social Computing in Business: Customer Service, Marketing & Risks
*(Appeared in: Dec 2022 Q5a [10M], May 2023 Q1d [5M], May 2024 Q1d/Q5a [10M], Dec 2024 Q1d [5M], May 2025 Q3b [10M])*

Social computing combines social behaviors with information systems to create collaborative interactive platforms.

### Applications of Social Computing in Business:
1. **Social Customer Service:** Customers publicly post grievances on Twitter, Facebook, or Reddit. Real-time social listening tools (e.g., Brandwatch, Hootsuite) capture brand mentions, routing tickets to support agents. Rapid public resolution transforms detractors into brand advocates.
2. **Social Marketing & Crowdsourcing:** Viral marketing, user-generated content campaigns, and crowdsourcing product ideas (e.g., Starbucks Idea platform, Lego Ideas where community votes dictate production).
3. **Social Shopping & Collaborative Consumption:** Group buying discounts, social commerce feeds (Instagram Checkout), and peer-driven reviews (Yelp, TripAdvisor).

### Business Risks of Social Computing:
- **Negative Viral Public Relations:** Customer service lapses or employee misbehavior can escalate into a global brand boycott within hours.
- **Intellectual Property Leaks:** Employees inadvertently leaking unreleased product roadmaps or internal source code on social forums.
- **Loss of Employee Productivity:** Unrestricted access to social media during work hours resulting in measurable loss of billable hours.
- **Legal Liability for User-Generated Content:** Exposure to defamation, copyright infringement, or regulatory non-compliance resulting from toxic user comments on corporate channels.

---

## 4.3 Customer Relationship Management (CRM): Operational vs Analytical
*(Appeared in: Dec 2022 Q3a [10M], Dec 2023 Q3b [10M], May 2025 Q4a [10M])*

An enterprise CRM strategy builds customer equity by coordinating customer touchpoints across sales, marketing, and customer service.

```
+---------------------------------------------------------------------------------------------------+
|                                      ENTERPRISE CRM ARCHITECTURE                                  |
+---------------------------------------------------------------------------------------------------+
|  [ CUSTOMER TOUCHPOINTS ]                                                                         |
|  Email, Phone / Call Center, Web Chat, Mobile App, Physical Store, Social Media                  |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 1. OPERATIONAL CRM (Customer-Facing & Customer-Touching Applications):                            |
|    - Automates front-office interactions directly communicating with customers.                   |
|    - Sales Force Automation (SFA): Lead tracking, pipeline management, sales forecasting.         |
|    - Customer Service & Support (CSS): Helpdesk ticketing, automated interactive voice response.  |
|    - Marketing Automation: Targeted email drip campaigns, promotional discount distribution.      |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v (Transaction data loaded into EDW)
| 2. ANALYTICAL CRM (Back-Office Data Mining & Predictive Modeling):                                |
|    - Analyzes customer behavioral patterns behind the scenes.                                     |
|    - Customer Lifetime Value (CLV) Calculation.                                                   |
|    - Churn Prediction Modeling (Identifies at-risk customers likely to switch to competitors).    |
|    - Market Basket Analysis (Discovers affinities for cross-selling and up-selling).              |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 3. COLLABORATIVE CRM:                                                                             |
|    - Facilitates seamless communication across internal departments (Sales, Finance, Logistics)  |
|      and external partners (distributors, retail franchisees) to present a unified brand front.   |
+---------------------------------------------------------------------------------------------------+
```

---

## 4.4 E-Commerce, M-Commerce & Delivery Application Architecture
*(Appeared in: Dec 2022 Q2b [10M], May 2023 Q2b [10M], Dec 2023 Q2a/Q4b [10M], May 2024 Q1e [5M], Dec 2024 Q6b [10M], May 2025 Q4b/Q5b [10M])*

### E-Commerce Business Models:
1. **Business-to-Consumer (B2C):** Businesses sell retail goods or services directly to individual consumers (e.g., Amazon, Flipkart).
2. **Business-to-Business (B2B):** Businesses transact with other businesses (e.g., Boeing buying avionics from suppliers, Alibaba wholesale trading).
3. **Consumer-to-Consumer (C2C):** Consumers transact directly with peers via platform intermediaries (e.g., eBay, OLX).

### Mobile Commerce (M-Commerce) Drivers & Constraints:
- **Drivers:** Widespread smartphone penetration, ubiquitous 5G/Wi-Fi coverage, single-click frictionless mobile payments (UPI, Apple Pay), GPS location-based services (LBS).
- **Constraints & Challenges:** Limited mobile screen real estate, battery drain, intermittent cellular connectivity in transit, heightened security risks on unsecured public Wi-Fi networks.

### Architecture of a Social Delivery Application (e.g., Food / Grocery Logistics)
*(Appeared in: Dec 2023 Q2a [10M])*

```
+---------------------------------------------------------------------------------------------------+
|                                 SOCIAL DELIVERY APPLICATION ARCHITECTURE                          |
+---------------------------------------------------------------------------------------------------+
|  [ 1. CONSUMER APP ]              [ 2. MERCHANT APP ]             [ 3. DELIVERY PARTNER APP ]     |
|  - Real-time catalog browsing     - Menu & inventory management   - GPS route optimization        |
|  - Social peer reviews & ratings  - Order acceptance / prep time  - Turn-by-turn navigation       |
|  - Live delivery driver tracking  - Revenue & order analytics     - Real-time earnings dashboard  |
+-----------------------------------+-------------------------------+-------------------------------+
                   \                                |                               /
                    \                               |                              /
                     v                              v                             v
| 4. CENTRAL LOGISTICS & MATCHING CLOUD BACKEND (Microservices Architecture):                       |
|    - Geospatial Dispatching Engine: Matches nearest active rider using Voronoi / Haversine.       |
|    - Payment Gateway Integration: Manages automated payment escrow, refunds, tip distribution.    |
|    - Social Computing Layer: In-app chat, crowd-sourced food recommendations, driver tips/reviews|
+---------------------------------------------------------------------------------------------------+
```

---

## 4.5 Architectural Comparison: WhatsApp vs Telegram
*(Appeared in: May 2023 Q1b [5M], Dec 2024 Q1b [5M])*

| Parameter | WhatsApp (Meta) | Telegram (Pavel Durov) |
|:---|:---|:---|
| **Encryption & Security** | **End-to-End Encrypted (E2EE) by default** across all 1-on-1 and group chats using the open-source Signal Protocol. | **Cloud-based MTProto encryption by default**; E2EE is **opt-in only** via separate "Secret Chats". |
| **Data Storage & Sync** | Hybrid local storage: Chat history resides locally on device; cloud backups stored on Google Drive / iCloud. | **Pure Cloud-First Storage:** All chats, media, and files reside permanently on Telegram servers; seamless real-time multi-device sync. |
| **File Sharing Limit** | Limited to **2 GB** per file. | Massive file sharing up to **2 GB (Free)** or **4 GB (Premium)** per file. |
| **Broadcast Channels & Groups**| Group size capped at **1,024 members**; broadcast channels have limited discovery tools. | Massive supergroups up to **200,000 members**; public broadcast channels supporting unlimited subscribers and automated bots. |
| **User Privacy** | Identity strictly tied to a physical **phone number** visible to group contacts. | Supports public **Usernames**; phone numbers can be completely hidden from contacts and groups. |

---

## MU Keyword Checklist: Module 4
- [ ] *Web 1.0 (Read-only, static), Web 2.0 (Read-write, social), Web 3.0 (Read-write-own, semantic/blockchain)*
- [ ] *Social Customer Service, Social Shopping, Crowdsourcing, Social PR Risks*
- [ ] *Operational CRM (Front-office: SFA, CSS, Marketing Automation)*
- [ ] *Analytical CRM (Back-office: Data mining, CLV, Churn prediction, Market Basket)*
- [ ] *Collaborative CRM (Inter-departmental and partner integration)*
- [ ] *B2B vs B2C vs C2C Business Models*
- [ ] *M-Commerce Drivers (GPS, Mobile Wallets) & Delivery App Architecture*
- [ ] *WhatsApp (Default E2EE, local storage, 2GB) vs Telegram (Cloud sync, MTProto, 200k groups, usernames)*

---
---

# MODULE 5: COMPUTER NETWORKS & CLOUD COMPUTING

---

## 5.1 Transmission Media: Wired vs Wireless Technologies
*(Appeared in: Dec 2022 Q1e [5M], Dec 2023 Q1d [5M], May 2025 Q1c [5M])*

```
+---------------------------------------------------------------------------------------------------+
|                                 WIRED VS WIRELESS TRANSMISSION MEDIA                              |
+---------------------------------------------------------------------------------------------------+
| Parameter          | Wired (Guided / Bounded Media)        | Wireless (Unguided / Unbounded Media)|
+--------------------+---------------------------------------+--------------------------------------+
| Transmission Path  | Confined strictly within physical     | Radiates openly through atmospheric  |
|                    | cables or metallic / glass conduits.  | air or vacuum as electromagnetic wave|
+--------------------+---------------------------------------+--------------------------------------+
| Media Varieties    | 1. Twisted Pair (Cat 6, 1 Gbps)       | 1. Radio Waves (Wi-Fi 6, 5G Cellular)|
|                    | 2. Coaxial Cable (Cable TV, broadband)| 2. Microwaves (Line-of-sight satellite)|
|                    | 3. Fiber Optic Cable (Photonic glass, | 3. Infrared (Short range remote)     |
|                    |    >100 Gbps, zero EMI interference)  | 4. Bluetooth Low Energy (BLE IoT)    |
+--------------------+---------------------------------------+--------------------------------------+
| Security & Tap Risk| High Security (Physical cable tap is  | Lower Security (Vulnerable to remote |
|                    | easily detected; localized perimeter).| sniffing, MitM, signal jamming).     |
+--------------------+---------------------------------------+--------------------------------------+
| Mobility           | Zero Mobility (Devices tethered to    | High Mobility (Seamless roaming      |
|                    | physical RJ-45 jacks).                | across cellular base stations).      |
+--------------------+---------------------------------------+--------------------------------------+
```

---

## 5.2 Network Topologies: Architectures & Trade-offs
*(Appeared in: May 2025 Q1c [5M])*

A network topology defines the geometric arrangement of links and nodes.

```
+---------------------------------------------------------------------------------------------------+
|                                    NETWORK TOPOLOGY ARCHITECTURES                                 |
+---------------------------------------------------------------------------------------------------+
|  1. STAR TOPOLOGY                       2. BUS TOPOLOGY                                           |
|       [Node A]    [Node B]                   +----+---------+---------+----+ (Terminator)         |
|           \          /                       |    |         |         |    |                      |
|            v        v                      [Node][Node]   [Node]    [Node] (Backbone Cable)       |
|          [CENTRAL SWITCH]                                                                         |
|            ^        ^                   3. MESH TOPOLOGY (Full Mesh)                              |
|           /          \                       [Node A] <---------> [Node B]                        |
|       [Node C]    [Node D]                      ^   \             /   ^                           |
|                                                 |    \           /    |                           |
|                                                 |     v         v     |                           |
|                                              [Node C] <---------> [Node D]                        |
+---------------------------------------------------------------------------------------------------+
```

### Comparative Trade-off Table:
1. **Star Topology:**
   - *Architecture:* Every node connects directly to a central hub/switch via point-to-point cable.
   - *Pros:* Single cable fault does not affect other nodes; easy to troubleshoot.
   - *Cons:* Central switch represents a single point of failure (if switch dies, entire network halts).
2. **Bus Topology:**
   - *Architecture:* Nodes tap into a single shared backbone cable terminated at both ends.
   - *Pros:* Minimal cabling required; economical.
   - *Cons:* Backbone cable break collapses entire network; heavy packet collisions under load.
3. **Ring Topology:**
   - *Architecture:* Nodes form a continuous circular loop; tokens pass unidirectionally.
   - *Pros:* Equal access for all nodes; zero packet collisions.
   - *Cons:* A single node or link failure breaks the ring (unless dual counter-rotating ring is used).
4. **Mesh Topology:**
   - *Architecture:* Every node connects to every other node via dedicated links ($\frac{N(N-1)}{2}$ cables).
   - *Pros:* Extreme fault tolerance and security; zero traffic congestion.
   - *Cons:* Prohibitively expensive and complex cabling for large $N$.

---

## 5.3 Cloud Computing Service Models: IaaS vs PaaS vs SaaS vs CaaS
*(Appeared in: Dec 2022 Q6b [10M], May 2023 Q4b [10M], Dec 2023 Q4a [10M], May 2024 Q2b/Q6a [10M], May 2025 Q6b [10M], Nov 2025 Q2a [10M])*

Cloud computing delivers on-demand computing resources over the internet on a utility pay-as-you-go pricing model.

```
+---------------------------------------------------------------------------------------------------+
|                                 THE SHARED RESPONSIBILITY CLOUD STACK                             |
+---------------------------------------------------------------------------------------------------+
|  COMPONENT STACK      | ON-PREMISES   | IaaS          | PaaS          | SaaS                      |
+-----------------------+---------------+---------------+---------------+---------------------------+
|  Applications         | YOU MANAGE    | YOU MANAGE    | YOU MANAGE    | CLOUD PROVIDER            |
|  Data                 | YOU MANAGE    | YOU MANAGE    | YOU MANAGE    | CLOUD PROVIDER            |
|  Runtime              | YOU MANAGE    | YOU MANAGE    | CLOUD PROVIDER| CLOUD PROVIDER            |
|  Middleware           | YOU MANAGE    | YOU MANAGE    | CLOUD PROVIDER| CLOUD PROVIDER            |
|  Operating System     | YOU MANAGE    | YOU MANAGE    | CLOUD PROVIDER| CLOUD PROVIDER            |
|  Virtualization       | YOU MANAGE    | CLOUD PROVIDER| CLOUD PROVIDER| CLOUD PROVIDER            |
|  Servers              | YOU MANAGE    | CLOUD PROVIDER| CLOUD PROVIDER| CLOUD PROVIDER            |
|  Storage              | YOU MANAGE    | CLOUD PROVIDER| CLOUD PROVIDER| CLOUD PROVIDER            |
|  Networking           | YOU MANAGE    | CLOUD PROVIDER| CLOUD PROVIDER| CLOUD PROVIDER            |
+---------------------------------------------------------------------------------------------------+
```

### Detailed Breakdown:
1. **Infrastructure as a Service (IaaS):**
   - Provides raw compute instances, storage volumes, and network firewalls.
   - User installs OS, manages patching, and configures databases.
   - *Examples:* Amazon EC2, Google Compute Engine, Microsoft Azure VMs.
2. **Platform as a Service (PaaS):**
   - Provides a managed environment for developers to build, test, and deploy applications without managing underlying operating systems or hardware provisioning.
   - *Examples:* AWS Elastic Beanstalk, Heroku, Google App Engine.
3. **Software as a Service (SaaS):**
   - Complete, turn-key software applications accessed directly via web browser. Cloud provider manages entire technical stack.
   - *Examples:* Google Workspace, Microsoft Office 365, Salesforce CRM, Zoom.
4. **Container as a Service (CaaS):**
   - Cloud framework allowing users to upload, organize, run, and scale containerized applications (Docker) using managed orchestration (Kubernetes).
   - *Examples:* Amazon EKS / ECS, Google Kubernetes Engine (GKE).

### Cloud Deployment Models:
- **Public Cloud:** Multi-tenant infrastructure owned by commercial cloud vendors (AWS, Azure) shared across public clients.
- **Private Cloud:** Single-tenant cloud infrastructure dedicated exclusively to one organization, hosted on-premises or by a third party.
- **Hybrid Cloud:** Integrates private cloud (retaining sensitive financial/medical data) with public cloud (bursting compute capacity for high web traffic).
- **Community Cloud:** Infrastructure shared collaboratively by multiple organizations possessing shared compliance goals (e.g., healthcare research consortium).

---

## MU Keyword Checklist: Module 5
- [ ] *Wired (Twisted Pair, Coaxial, Fiber Optic) vs Wireless (Radio, Microwave, Infrared, BLE)*
- [ ] *Network Topologies: Star (Central switch single point of failure), Bus (Backbone break), Ring, Mesh ($N(N-1)/2$ links)*
- [ ] *IaaS (Raw compute, OS managed by user: EC2) vs PaaS (Managed runtime: Heroku) vs SaaS (Turnkey app: Office 365)*
- [ ] *CaaS (Container as a Service, Managed Kubernetes: GKE)*
- [ ] *Cloud Deployment: Public (Multi-tenant), Private (Single-tenant), Hybrid (Private + Public burst), Community*

---
---

# MODULE 6: ENTERPRISE SYSTEMS & SYSTEM DEVELOPMENT

---

## 6.1 Functional Area Information Systems (FAIS) & Types of Reports
*(Appeared in: May 2023 Q3b [10M], Dec 2024 Q5a [10M], May 2025 Q2a [10M], Nov 2025 Q4b [10M], Nov 2025 Q5a [10M])*

**Functional Area Information Systems (FAIS)** are specialized information systems tailored to support the specific business activities, workflows, and operational decision-making of distinct functional departments within an enterprise.

```
+---------------------------------------------------------------------------------------------------+
|                         FUNCTIONAL AREA INFORMATION SYSTEMS (FAIS) ARCHITECTURE                   |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  +--------------------+  +--------------------+  +--------------------+  +--------------------+   |
|  |   ACCOUNTING IS    |  |     FINANCE IS     |  |    POM IS (OPS)    |  |    MARKETING IS    |   |
|  | - Ledger & Invoices|  | - Capital budgeting|  | - MRP & Scheduling |  | - Campaign tracking|   |
|  | - AR / AP & Audits |  | - Cash forecasting |  | - Quality & BOM    |  | - Pricing & Churn  |   |
|  +--------------------+  +--------------------+  +--------------------+  +--------------------+   |
|            \                       |                       |                      /               |
|             \                      |                       |                     /                |
|              +---------------------+-----------------------+--------------------+                 |
|                                                |                                                  |
|                                                v                                                  |
|                                    +-----------------------+                                      |
|                                    |     HUMAN RESOURCE    |                                      |
|                                    |       IS (HRIS)       |                                      |
|                                    | - Payroll & Benefits  |                                      |
|                                    | - Talent & Compliance |                                      |
|                                    +-----------------------+                                      |
|                                                |                                                  |
|                                                v                                                  |
|                         [ SHARED TRANSACTION & REPORTING DATABASE ]                               |
+---------------------------------------------------------------------------------------------------+
```

### 1. Types of Support Provided by Functional Area Information Systems (FAIS)
*(Mandatory 10-Mark Answer Breakdown for Nov 2025 Q5a)*

| Functional Area | Operational Support (Day-to-Day) | Tactical Support (Management Control) | Strategic Support (Long-Term Planning) |
| :--- | :--- | :--- | :--- |
| **1. Accounting IS** | - Automated General Ledger posting<br>- Accounts Payable (AP) & Invoicing<br>- Accounts Receivable (AR) & billing<br>- Payroll ledger integration | - Monthly budgetary variance analysis<br>- Cash-flow reconciliations<br>- Internal audit compliance reports<br>- Tax filing preparation (GST/TDS) | - Multi-year capital depreciation strategies<br>- Global accounting standard compliance (IFRS vs GAAP)<br>- Profit center performance evaluation |
| **2. Finance IS** | - Daily cash float tracking<br>- Real-time bank transaction feeds<br>- Credit limit approvals for orders<br>- FX currency exchange conversions | - Working capital management<br>- Investment portfolio monitoring<br>- Short-term credit risk scoring<br>- Budget allocation & reforecasting | - Long-term capital budgeting decisions<br>- Mergers & Acquisitions (M&A) valuation modeling<br>- Capital structure (debt-to-equity) optimization |
| **3. Production / Operations Management (POM) IS** | - Shop-floor machine scheduling<br>- Bill of Materials (BOM) management<br>- Work-in-Progress (WIP) tracking<br>- Barcode inventory receiving | - Material Requirements Planning (MRP)<br>- Just-In-Time (JIT) replenishment<br>- Statistical Process Control (SPC)<br>- Equipment preventive maintenance alerts | - Plant location and capacity planning<br>- Supply chain network design<br>- Transition to advanced manufacturing (Industry 4.0 / Robotics) |
| **4. Marketing IS** | - Point-of-Sale (POS) order logging<br>- Direct email campaign delivery<br>- Lead capture and assignment<br>- Promotional discount authorization | - Customer churn prediction analysis<br>- Product pricing elasticity analysis<br>- Channel sales performance reports<br>- Advertising ROI calculation | - New product development strategy<br>- Brand market share penetration modeling<br>- Long-term customer demographic shift forecasting |
| **5. Human Resources IS (HRIS)** | - Time & biometric attendance tracking<br>- Monthly net salary disbursement<br>- Employee health benefits enrollment<br>- Job applicant resume parsing | - Employee turnover/retention analysis<br>- Performance appraisal management<br>- Skill gap and training need identification<br>- Workplace safety incident logs | - Long-term workforce succession planning<br>- Organizational restructuring modeling<br>- Strategic executive compensation planning |

### 2. Enterprise Reporting Taxonomy:
- **Scheduled Reports:** Produced at regular calendar intervals (e.g., Daily cash reconciliation report, Weekly sales summary).
- **On-Demand (Ad-hoc) Reports:** Generated dynamically when a manager requests specific non-routine data.
- **Exception Reports:** Highlight only critical anomalies or metrics that breach predefined operating thresholds (e.g., *"Report all warehouse items with stock < 10 units"* or *"Expenses exceeding budget by > 15%"*).
- **Drill-Down Reports:** Enable interactive exploration from high-level corporate numbers down to specific store receipts.
- **Key-Indicator Reports:** Highly condensed executive summaries of vital operational health indicators.

---

## 6.2 Enterprise Resource Planning (ERP): Architecture & Business Process Support
*(Appeared in: Dec 2022 Q4a [10M], May 2023 Q3b [10M], May 2024 Q4b [10M])*

Before ERP, traditional enterprises suffered from **Information Silos** (isolated departmental databases where Sales, Finance, and Warehouse data contradicted each other).

```
+---------------------------------------------------------------------------------------------------+
|                                 ENTERPRISE RESOURCE PLANNING (ERP)                                |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|               [ Financial / Accounting ]               [ Supply Chain / POM ]                     |
|                           \                                 /                                     |
|                            \                               /                                      |
|                             v                             v                                       |
|                       +-----------------------------------------+                                 |
|                       |         CENTRALIZED ENTERPRISE          |                                 |
|                       |               DATABASE                  |                                 |
|                       |     (Single Source of Truth - ACID)     |                                 |
|                       +-----------------------------------------+                                 |
|                             ^                             ^                                       |
|                            /                               \                                      |
|                           /                                 \                                     |
|                 [ Sales & Marketing ]                  [ Human Resources ]                        |
|                                                                                                   |
+---------------------------------------------------------------------------------------------------+
```

### Business Process Support & Advantages of ERP:
1. **Single Source of Truth:** A sale entered by a field representative instantly updates warehouse inventory, alerts manufacturing, generates a customer invoice, and updates financial revenue projections in real time.
2. **Streamlined Standardized Workflows:** Enforces industry best-practice processes across all global subsidiaries.
3. **Elimination of Data Redundancy:** Eradicates duplicate manual data entry across departments.

### Primary Pitfalls & Failure Causes in ERP Deployments:
- **Underestimating Organizational Change Management:** Employees resist learning complex new SAP/Oracle interfaces.
- **Excessive Software Customization:** Customizing off-the-shelf ERP code inflates costs and breaks future update paths.
- **Poor Data Cleansing:** Migrating dirty, duplicate data from legacy systems corrupts the new ERP database.

---

## 6.3 System Development Life Cycle (SDLC) & Modern Augmenting Tools
*(Appeared in: May 2023 Q1c [5M], Dec 2023 Q5b [10M], Dec 2024 Q1c [5M], May 2025 Q1d/e [10M], Nov 2025 Q6b [10M])*

The **System Development Life Cycle (SDLC)** is a structured, phased framework used by IT organizations and system analysts to conceive, analyze, design, build, test, deploy, and maintain robust enterprise information systems.

```
+---------------------------------------------------------------------------------------------------+
|                                       TRADITIONAL SDLC CASCADE                                    |
+---------------------------------------------------------------------------------------------------+
| 1. Feasibility Study & Planning (Technical, Economic, Operational, Legal, Schedule feasibility)   |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 2. Systems Analysis (Requirements Gathering, Use Cases, Data Flow Diagrams - DFDs)               |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 3. Systems Design (Architectural blueprints, Database ER Diagrams, UI/UX Wireframes)              |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 4. Programming & Testing (Unit Testing, Integration Testing, System & Acceptance Testing - UAT)   |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 5. Implementation / Deployment (Direct Cutover, Pilot Study, Phased Rollout, Parallel Running)    |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 6. Operations & Maintenance (Bug fixes, security patching, feature enhancements)                 |
+---------------------------------------------------------------------------------------------------+
```

### Exhaustive 6-Phase Breakdown & Deliverables:
*(Required for 10-Mark Answer in Nov 2025 Q6b)*

1. **Phase 1: Systems Investigation & Feasibility Study:**
   - *Core Objective:* Determine whether a proposed business problem or opportunity warrants building a new system.
   - *TELOS Feasibility Framework:*
     - **T - Technical Feasibility:** Does the enterprise possess the hardware, software, and engineering expertise to build and operate the solution?
     - **E - Economic Feasibility (Cost-Benefit Analysis):** Calculates ROI, Net Present Value (NPV), and Payback Period to evaluate financial viability.
     - **L - Legal & Contractual Feasibility:** Ensures compliance with copyright laws, GDPR, HIPAA, and existing vendor contracts.
     - **O - Operational Feasibility:** Assesses organizational culture, employee willingness to adopt, and union/stakeholder resistance.
     - **S - Schedule Feasibility:** Determines if the system can realistically be delivered before statutory or competitive deadlines.
   - *Key Deliverable:* Formal **Feasibility Study Report** and Project Charter signed by executive sponsors.

2. **Phase 2: Systems Analysis (What the System Must Do):**
   - *Core Objective:* Thoroughly understand the existing legacy workflow and document complete end-user functional and non-functional requirements.
   - *Techniques:* Contextual user interviews, focus groups, employee observation, document reviews, survey questionnaires.
   - *Modeling Tools:* Data Flow Diagrams (DFD Level 0/1/2), Entity-Relationship (ER) conceptual modeling, UML Use Case Diagrams.
   - *Key Deliverable:* **Software Requirements Specification (SRS)** document serving as the binding contractual baseline.

3. **Phase 3: Systems Design (How the System Will Deliver Capabilities):**
   - *Logical Design:* Abstract specifications of input forms, output reports, relational database schemas (3NF normalization), business validation logic, and workflow state machines.
   - *Physical Design:* Concrete hardware procurement specifications, network topologies, server clustering, database index schemas, cybersecurity firewalls, and API endpoint contracts.
   - *Key Deliverable:* **System Design Document (SDD)**, high-fidelity UI/UX wireframes, and physical database schemas.

4. **Phase 4: Programming, Integration & Verification Testing:**
   - *Core Objective:* Translate architectural specifications into clean, executable, documented code and verify zero-defect execution.
   - *Testing Hierarchy:*
     - **Unit Testing:** Individual software modules or microservices tested in isolation.
     - **Integration Testing:** Verifying data exchanges and API contracts between interacting modules.
     - **System Testing:** Validating overall system performance under load, stress, and security penetration testing.
     - **User Acceptance Testing (UAT):** Real business end-users test the system in staging using actual operational scenarios to grant sign-off.
   - *Key Deliverable:* Production-ready software build, automated test suites, and UAT sign-off documentation.

5. **Phase 5: Implementation & Conversion Strategies:**
   - *Core Objective:* Transition organizational operations from the obsolete legacy system to the new production system.
   - *The 4 Conversion Strategies:*
     - **Direct Cutover (Plunge / Big Bang):** Old system is shut down on Friday night; new system boots Monday morning. Highly risky with zero fallback if failure occurs.
     - **Parallel Running:** Old and new systems run simultaneously for a period (e.g., 1 month). Safest strategy; outputs are compared for parity, but incurs double operational costs and workload.
     - **Pilot Conversion:** System deployed entirely within one branch or department (e.g., Pune branch first). Bugs are resolved before enterprise-wide expansion.
     - **Phased Rollout:** System modules are activated sequentially across the enterprise (e.g., Module 1 Accounting launched in Jan, Module 2 Inventory in Mar).
   - *Key Deliverable:* Data migration scripts, user training manuals, and cutover sign-off.

6. **Phase 6: Operations & Maintenance:**
   - *Core Objective:* Ensure post-launch operational stability and accommodate evolving business requirements over the system's operational lifespan.
   - *Maintenance Categories:*
     - **Corrective Maintenance:** Fixing unanticipated production bugs and crashes.
     - **Adaptive Maintenance:** Updating software to run on new OS versions or comply with newly enacted government tax regulations.
     - **Perfective Maintenance:** Adding high-value user enhancement requests and optimizing query speeds.
     - **Preventive Maintenance:** Routine database index defragmentation, log rotations, and security vulnerability patching.
   - *Key Deliverable:* Post-implementation audit review, maintenance ticket logs, and continuous service level agreements (SLAs).

### Modern Tools Augmenting the Traditional SDLC:
*(Appeared in: May 2023 Q1c, Dec 2024 Q1c, May 2025 Q1e)*
1. **Agile Methodologies (Scrum / Kanban):** Replaces rigid multi-year waterfall schedules with 2-week iterative sprints delivering functional software increments.
2. **Computer-Aided Software Engineering (CASE) Tools:** Automated tools that model schemas, generate entity-relationship diagrams, and auto-generate boilerplate code.
3. **Prototyping & Rapid Application Development (RAD):** Builds working mockups early to gather user feedback before writing production code.
4. **DevOps & Automated CI/CD Pipelines:** Jenkins, GitHub Actions, and Docker automating test suites and production deployments within minutes.
5. **Low-Code / No-Code Platforms:** Enables non-technical business analysts to construct internal workflow tools using visual drag-and-drop builders.

---

## 6.4 SYSTEM DESIGN CASE STUDY: Hospital Management Information System (HMIS)
*(Appeared in: December 2022 Paper, Question 5(b) [10 Marks])*

### Comprehensive Architecture of an Enterprise Hospital MIS

```
+---------------------------------------------------------------------------------------------------+
|                           HOSPITAL MANAGEMENT INFORMATION SYSTEM (HMIS)                           |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|  +---------------------------------------------------------------------------------------------+  |
|  | FRONT-DESK / OUTPATIENT (OPD) MODULE:                                                       |  |
|  | - Patient Demographics Registration, Unique Health ID (UHID) Generation                     |  |
|  | - Doctor Appointment Scheduling, Queue Token Display Systems                                |  |
|  +---------------------------------------------------------------------------------------------+  |
|                                                |                                                  |
|                                                v                                                  |
|  +---------------------------------------------------------------------------------------------+  |
|  | ELECTRONIC HEALTH RECORD (EHR) & CLINICAL MODULE:                                           |  |
|  | - Doctor Consultation Notes, Digital Prescription Entry (e-Prescription)                     |  |
|  | - Patient Medical History, ICD-10 Diagnosis Coding, Allergy Alerts                          |  |
|  +---------------------------------------------------------------------------------------------+  |
|             |                                  |                                  |               |
|             v                                  v                                  v               |
|  +----------------------+          +----------------------+          +----------------------+     |
|  | DIAGNOSTIC LAB /     |          | PHARMACY & DRUG      |          | INPATIENT (IPD) &    |     |
|  | RADIOLOGY (LIS/PACS) |          | INVENTORY MODULE     |          | WARD ALLOCATION      |     |
|  | - Test order sync    |          | - Auto prescription  |          | - Bed & ICU tracking |     |
|  | - Blood analyzer telemetry         dispense            |          | - Surgery scheduling |     |
|  | - Digital X-Ray/MRI  |          | - Batch expiry alert |          | - Nurse charting vitals    |
|  +----------------------+          +----------------------+          +----------------------+     |
|             \                                  |                                  /               |
|              \                                 |                                 /                |
|               v                                v                                v                 |
|  +---------------------------------------------------------------------------------------------+  |
|  | BILLING, INSURANCE & DISCHARGE MODULE:                                                      |  |
|  | - Consolidated Invoice Generation (Bed charges + Labs + Pharmacy + Doctor fees)             |  |
|  | - Health Insurance TPA Cashless Claim Processing & Approvals                                |  |
|  +---------------------------------------------------------------------------------------------+  |
|                                                |                                                  |
|                                                v                                                  |
|  +---------------------------------------------------------------------------------------------+  |
|  | EXECUTIVE / MEDICAL SUPERINTENDENT BI DASHBOARD:                                            |  |
|  | - Bed Occupancy Rates, Emergency Wait Times, Infection Rates, Pharmacy Stock Alerts         |  |
|  +---------------------------------------------------------------------------------------------+  |
|                                                                                                   |
+---------------------------------------------------------------------------------------------------+
```

### Key Technical Implementation Features:
1. **Central Database:** ACID-compliant relational DB storing all patient records indexed by Unique Health ID (UHID).
2. **Access Security & Compliance:** Strict Role-Based Access Control (RBAC); doctors can read clinical notes, billing clerks see only invoices, nurses record vitals. Compliant with HIPAA and India's Ayushman Bharat Digital Mission (ABDM).
3. **Disaster Recovery:** High-availability database cluster with automated failover and encrypted off-site cloud backups to guarantee 24/7 patient record availability.

---

## MU Keyword Checklist: Module 6
- [ ] *FAIS: Accounting IS, Finance IS, POM IS, Marketing IS, HRIS*
- [ ] *Enterprise Reports: Scheduled, On-demand, Exception, Drill-down, Key-indicator*
- [ ] *ERP: Shared Central Database, Single Source of Truth, Overcoming Information Silos*
- [ ] *ERP Failure Pitfalls: Change management resistance, excessive customization, dirty data*
- [ ] *SDLC 6 Phases: Feasibility, Analysis, Design, Programming/Testing, Implementation, Maintenance*
- [ ] *Augmenting Tools: Agile Scrum Sprints, CASE tools, Prototyping, DevOps CI/CD, Low-Code*
- [ ] *Hospital MIS (HMIS) Architecture: OPD Registration (UHID), EHR, LIS/PACS, Pharmacy, IPD Beds, Billing, Executive KPI Dashboard*
