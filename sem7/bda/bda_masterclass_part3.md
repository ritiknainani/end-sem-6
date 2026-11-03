# 📘 BDA ULTIMATE MASTERCLASS — Part 3: Modules 5 & 6

# MODULE 5: REAL-TIME BIG DATA MODELS

---

## Q21. Explain Content-Based Recommendation System with Example. [10 Marks] — 3/6

**Question Type:** Theory / Architecture

### Definition
A **Content-Based Recommendation System** recommends items to a user based on the **features/properties of items** the user has previously liked or interacted with. It matches item attributes to user preferences.

### Architecture
```
┌────────────────────────────────────────────────────────────┐
│           CONTENT-BASED RECOMMENDATION SYSTEM              │
│                                                            │
│  ┌──────────────┐         ┌──────────────────┐            │
│  │ ITEM PROFILES │         │  USER PROFILE     │            │
│  │               │         │                  │            │
│  │ Item 1: [F1,  │         │ User likes:      │            │
│  │  F2, F3...]   │         │ [F1=high,         │            │
│  │ Item 2: [F1,  │         │  F2=medium,       │            │
│  │  F2, F3...]   │         │  F3=low]           │            │
│  └───────┬──────┘         └────────┬─────────┘            │
│          │                         │                       │
│          └──────────┬──────────────┘                       │
│                     ▼                                      │
│          ┌──────────────────┐                              │
│          │ MATCHING ENGINE   │                              │
│          │ (Cosine Similarity│                              │
│          │  TF-IDF, etc.)   │                              │
│          └────────┬─────────┘                              │
│                   ▼                                        │
│          ┌──────────────────┐                              │
│          │ RANKED            │                              │
│          │ RECOMMENDATIONS   │                              │
│          │ Item 5 (0.95)     │                              │
│          │ Item 8 (0.87)     │                              │
│          │ Item 3 (0.72)     │                              │
│          └──────────────────┘                              │
└────────────────────────────────────────────────────────────┘
```

### How it Works (Step-by-step):
1. **Item Profile Creation:** Extract features/attributes of each item (genre, director, actors for movies; brand, color, material for products)
2. **User Profile Construction:** Build a weighted feature vector from items the user has liked/rated highly
3. **Similarity Computation:** Calculate similarity (cosine similarity, Euclidean distance) between user profile and each unseen item
4. **Ranking & Recommendation:** Sort items by similarity score; recommend top-N

### Example — Movie Recommendation:
```
User has liked: "The Dark Knight" (Action, Thriller), "Inception" (Sci-Fi, Thriller)
User Profile: {Action: 0.5, Thriller: 1.0, Sci-Fi: 0.5}

Available movies:
  "Interstellar" (Sci-Fi, Drama)     → Similarity = 0.78
  "John Wick" (Action, Thriller)     → Similarity = 0.92  ← RECOMMENDED
  "Titanic" (Romance, Drama)         → Similarity = 0.10

Recommendation: "John Wick" (highest similarity to user profile)
```

### Advantages & Limitations:

| Advantages | Limitations |
|-----------|-------------|
| No cold-start for items (uses item features) | **Over-specialization:** Only recommends similar items; no diversity |
| Transparent reasoning (can explain why) | Cannot capture social/collaborative patterns |
| Works for single users (no need for community) | Requires good feature extraction |
| User independence — no data from other users needed | **Cold-start for new users** (no history to build profile) |

**MU Keyword Checklist:** Content-based, item profile, user profile, feature vector, cosine similarity, TF-IDF, over-specialization, cold-start problem, item attributes, matching engine

---

## Q22. Explain Collaborative Filtering in Recommendation Systems. [10 Marks] — 2/6

**Question Type:** Theory

### Definition
**Collaborative Filtering (CF)** recommends items based on the preferences of **similar users** or **similar items**, without needing to know item features. It uses the "wisdom of the crowd."

### Two Types:

```
┌──────────────────────────────────────────────────────────┐
│              COLLABORATIVE FILTERING                      │
│                                                          │
│  ┌────────────────────┐   ┌─────────────────────┐       │
│  │  USER-BASED CF      │   │  ITEM-BASED CF       │       │
│  │                    │   │                     │       │
│  │  "Users similar    │   │  "Items similar     │       │
│  │   to you liked X"  │   │   to what you liked"│       │
│  │                    │   │                     │       │
│  │  User A ≈ User B   │   │  Item X ≈ Item Y    │       │
│  │  B liked Item X    │   │  User liked X       │       │
│  │  ∴ Recommend X to A│   │  ∴ Recommend Y      │       │
│  └────────────────────┘   └─────────────────────┘       │
└──────────────────────────────────────────────────────────┘
```

### User-Based CF:
1. Build a **user-item rating matrix**
2. Find users most **similar** to the target user (using Pearson correlation or cosine similarity)
3. Recommend items that similar users liked but the target user hasn't seen

### Item-Based CF:
1. Compute **item-item similarity** from the rating matrix
2. For each item the user has liked, find the most similar items
3. Recommend the most similar items the user hasn't rated

### Example (E-commerce — Flipkart/Amazon):
```
User-Item Rating Matrix:
            Phone  Laptop  Tablet  Watch
User A:      5       4       ?       3
User B:      4       5       4       ?
User C:      ?       3       5       4
User D:      5       ?       4       3

User-Based CF for User A (predicting Tablet rating):
  Most similar to A: User D (both like Phone=5, Watch=3)
  D rated Tablet = 4
  ∴ Predicted rating for A on Tablet ≈ 4 → Recommend!
```

### Comparison Table

| Parameter | Content-Based | Collaborative Filtering |
|-----------|--------------|------------------------|
| **Input** | Item features + User history | User-item rating matrix |
| **Mechanism** | Feature matching | Similar users/items |
| **Cold Start (Items)** | No problem (uses features) | Problem (no ratings yet) |
| **Cold Start (Users)** | Problem (no history) | Problem (no ratings) |
| **Serendipity** | Low (similar items only) | High (unexpected recommendations) |
| **Scalability** | Scales with items | Scales with users × items |
| **Example** | Netflix suggesting similar genre movies | Amazon "Customers who bought X also bought Y" |

**MU Keyword Checklist:** Collaborative filtering, user-based, item-based, user-item matrix, cosine similarity, Pearson correlation, cold-start problem, serendipity, sparsity problem

---

## Q23. Girvan-Newman Algorithm for Community Detection. [10 Marks] — 6/6 GUARANTEED

**Question Type:** Numerical (MOST IMPORTANT — appears EVERY paper)

### Definition
The **Girvan-Newman algorithm** detects communities in a network by progressively removing edges with the highest **edge betweenness centrality**. Edge betweenness = number of shortest paths between all pairs of nodes that pass through that edge.

### Algorithm Steps:
```
┌──────────────────────────────────────────────┐
│       GIRVAN-NEWMAN ALGORITHM                 │
│                                              │
│  1. Calculate EDGE BETWEENNESS for all edges │
│  2. REMOVE the edge with highest betweenness │
│  3. RECALCULATE edge betweenness for         │
│     remaining edges                          │
│  4. REPEAT steps 2-3 until desired number    │
│     of communities is achieved               │
│  5. Connected components = COMMUNITIES       │
└──────────────────────────────────────────────┘
```

### How to Calculate Edge Betweenness:
For each pair of nodes (s, t):
1. Find ALL shortest paths from s to t
2. For each edge on a shortest path, add 1/(number of shortest paths) to that edge's betweenness
3. Sum across all (s,t) pairs

### Solved Example (May 2025 — Graph: A-B-E, C-D):
```
Given Graph:
    A ─── B ─── E
    │   / │
    │  /  │
    C ─── D
```

**Step 1: Calculate edge betweenness**

First, identify all shortest paths between all pairs:

| Pair | Shortest Path(s) | Edges Used |
|------|-------------------|------------|
| A-B | A-B | A-B |
| A-C | A-C | A-C |
| A-D | A-C-D or A-B-D | A-C,C-D or A-B,B-D |
| A-E | A-B-E | A-B, B-E |
| B-C | B-C | B-C |
| B-D | B-D | B-D |
| B-E | B-E | B-E |
| C-D | C-D | C-D |
| C-E | C-B-E | C-B, B-E |
| D-E | D-B-E | D-B, B-E |

Now compute betweenness for each edge:

**Edge A-B:**
- On path A-B: 1
- On path A-D: 0.5 (1 of 2 paths)
- On path A-E: 1
= **2.5**

**Edge A-C:**
- On path A-C: 1
- On path A-D: 0.5 (1 of 2 paths)
= **1.5**

**Edge B-C:**
- On path B-C: 1
- On path C-E: 1
= **2**

**Edge B-D:**
- On path B-D: 1
- On path A-D: 0.5
- On path D-E: 1
= **2.5**

**Edge B-E:**
- On path B-E: 1
- On path A-E: 1
- On path C-E: 1
- On path D-E: 1
= **4** ← HIGHEST

**Edge C-D:**
- On path C-D: 1
- On path A-D: 0.5
= **1.5**

**Step 2: Remove edge with highest betweenness → Remove B-E (4)**

```
After removing B-E:
    A ─── B       E (isolated)
    │   / │
    │  /  │
    C ─── D

Communities: {A, B, C, D} and {E}
```

**Step 3: Continue if more communities needed**
Recalculate betweenness on remaining graph and remove next highest edge.

### General Tips for Solving:
1. Draw the graph clearly with all edges
2. Systematically list ALL pairs of nodes
3. Find shortest path(s) for each pair
4. Accumulate betweenness for each edge
5. Remove the highest, redraw, repeat
6. Connected components after removal = communities

**MU Keyword Checklist:** Girvan-Newman, edge betweenness, shortest paths, community detection, remove highest betweenness edge, connected components, recalculate, modularity

---

## Q24. Explain Clique Percolation Method (CPM) for Community Detection. [10 Marks] — Dec'24

**Question Type:** Theory + Numerical

### Definition
The **Clique Percolation Method (CPM)** discovers overlapping communities by finding **adjacent k-cliques** (complete subgraphs of k nodes) and merging them.

### Algorithm:
1. **Find all k-cliques** in the graph (complete subgraphs of size k)
2. Two k-cliques are **adjacent** if they share (k−1) nodes
3. A **community** = union of all k-cliques reachable from each other through a chain of adjacent k-cliques

### Example (k=3):
A 3-clique is a triangle (3 nodes all connected to each other).

```
Given graph:     1───2───5
                 │╲  │  ╱│
                 │ ╲ │ ╱ │
                 3───4───6

Step 1: Find all 3-cliques (triangles):
  {1,2,3}, {1,2,4}, {1,3,4}, {2,3,4}, {2,4,5}, {2,5,6}, {4,5,6}

Step 2: Build adjacency (share 2 nodes):
  {1,2,3} adj {1,2,4} (share 1,2)
  {1,2,3} adj {1,3,4} (share 1,3)
  {1,2,3} adj {2,3,4} (share 2,3)
  ... and so on

Step 3: All cliques containing {1,2,3,4} form Community 1
        All cliques containing {2,4,5,6} form Community 2
        Node 2 and 4 belong to BOTH → overlapping communities

Communities: {1,2,3,4} and {2,4,5,6}
Overlap: Nodes 2 and 4
```

**MU Keyword Checklist:** Clique Percolation Method, k-clique, adjacent cliques, overlapping communities, complete subgraph, k-1 shared nodes, CFinder

---

# MODULE 6: DATA ANALYTICS WITH R

---

## Q25. R: Create Data Frame, Display Structure and Summary. [10 Marks] — 6/6 GUARANTEED

**Question Type:** Code/Numerical

### Core R Concepts:

```r
# Creating vectors
x <- c(1, 2, 3, 4, 5)
names <- c("Alice", "Bob", "Charlie")

# Creating a Data Frame
df <- data.frame(
  Name = c("Alice", "Bob", "Charlie"),
  Age = c(25, 30, 28),
  Salary = c(50000, 60000, 55000)
)

# Display data frame
print(df)        # or just: df

# Structure
str(df)           # Shows types of each column

# Summary statistics
summary(df)       # Min, 1Q, Median, Mean, 3Q, Max for numeric columns
```

### Solved Example 1 (Dec 2024):
**Create a data frame for project data and display output:**

```r
# Step 1: Create the data frame
projects <- data.frame(
  ProjectId = c(1, 2, 3, 4, 5),
  ProjectName = c("Website Redesign", "Mobile App Launch",
                   "Data Migration", "AI Development",
                   "Cybersecurity Audit"),
  Budget = c(150000, 100000, 80000, 200000, 50000)
)

# Step 2: Display the data frame
print(projects)
```
**Output:**
```
  ProjectId        ProjectName Budget
1         1   Website Redesign 150000
2         2  Mobile App Launch 100000
3         3    Data Migration   80000
4         4    AI Development  200000
5         5 Cybersecurity Audit  50000
```

```r
# Step 3: Show structure
str(projects)
```
**Output:**
```
'data.frame':   5 obs. of  3 variables:
 $ ProjectId  : num  1 2 3 4 5
 $ ProjectName: chr  "Website Redesign" "Mobile App Launch" ...
 $ Budget     : num  150000 100000 80000 200000 50000
```

```r
# Step 4: Summary statistics
summary(projects)
```
**Output:**
```
   ProjectId   ProjectName            Budget
 Min.   :1    Length:5          Min.   : 50000
 1st Qu.:2    Class :character  1st Qu.: 80000
 Median :3    Mode  :character  Median :100000
 Mean   :3                     Mean   :116000
 3rd Qu.:4                     3rd Qu.:150000
 Max.   :5                     Max.   :200000
```

### Solved Example 2 (May 2025):
**Create data frame, then add new rows:**

```r
# Step 1: Create original data frame
projects <- data.frame(
  ProjectId = c(1, 2, 3, 4, 5),
  ProjectName = c("CRM Implementation", "Cloud Infrastructure",
                   "Network Upgrade", "E-Commerce Platform",
                   "Data Analytics"),
  Budget = c(120000, 180000, 60000, 220000, 90000),
  Status = c("In Progress", "Completed", "Not Started",
              "Completed", "In Progress")
)

# Step 2: Create new projects data frame
new_projects <- data.frame(
  ProjectId = c(6, 7),
  ProjectName = c("UX Research", "Cloud Integration"),
  Budget = c(160000, 190000),
  Status = c("Not Started", "Not Started")
)

# Step 3: Combine using rbind()
projects <- rbind(projects, new_projects)
print(projects)
```
**Output:**
```
  ProjectId         ProjectName Budget      Status
1         1  CRM Implementation 120000 In Progress
2         2 Cloud Infrastructure 180000   Completed
3         3     Network Upgrade  60000 Not Started
4         4 E-Commerce Platform 220000   Completed
5         5      Data Analytics  90000 In Progress
6         6         UX Research 160000 Not Started
7         7   Cloud Integration 190000 Not Started
```

**MU Keyword Checklist:** data.frame(), c(), print(), str(), summary(), rbind(), column types, observations

---

## Q26. R: Subset Operations using `subset()` and `[]` brackets. [10 Marks] — 6/6 GUARANTEED

**Question Type:** Code

### Two Methods for Subsetting:

**Method 1: `subset()` function**
```r
subset(dataframe, condition)
```

**Method 2: `[]` bracket notation**
```r
dataframe[condition, ]     # Note the comma!
```

### Solved Example (May 2024, Dec 2022):
**Data frame with course, id, class, marks:**

```r
df <- data.frame(
  course = c(1, 2, 3, 4, 5, 6),
  id = c(11, 12, 13, 14, 15, 16),
  class = c(1, 2, 1, 2, 1, 2),
  marks = c(56, 75, 48, 69, 84, 53)
)
```

**i. Subset: course < 5 using `[]` brackets:**
```r
result <- df[df$course < 5, ]
print(result)
```
**Output:**
```
  course id class marks
1      1 11     1    56
2      2 12     2    75
3      3 13     1    48
4      4 14     2    69
```

**ii. Subset: course < 4 OR class == 1 using `subset()`:**
```r
result <- subset(df, course < 4 | class == 1)
print(result)
```
**Output:**
```
  course id class marks
1      1 11     1    56
2      2 12     2    75
3      3 13     1    48
5      5 15     1    84
```

### Solved Example 2 (Dec 2022):
**subject < 3 AND class == 2:**
```r
df <- data.frame(
  subject = c(1, 2, 3, 4, 5, 6),
  marks = c(56, 75, 48, 69, 84, 53),
  class = c(1, 2, 1, 2, 1, 2)
)

# Using subset()
result <- subset(df, subject < 4)
print(result)

# Using [] brackets
result2 <- df[df$subject < 3 & df$class == 2, ]
print(result2)
```
**Output for result2:**
```
  subject marks class
2       2    75     2
```

**MU Keyword Checklist:** subset(), square brackets [], $, logical operators (& | == < >), comma in brackets, data.frame, filtering rows

---

## Q27. R: Sort, Combine Functions, and Data Operations. [10 Marks] — 4/6

**Question Type:** Code

### Sorting Vectors:
```r
x <- c(23, 45, 10, 34, 89, 20, 67, 99)

# Ascending order
sort(x)
# Output: 10 20 23 34 45 67 89 99

# Descending order
sort(x, decreasing = TRUE)
# Output: 99 89 67 45 34 23 20 10

# Using order() — returns indices
order(x)
# Output: 3 6 1 4 2 7 5 8  (positions in sorted order)
```

### Solved Example (Dec 2024):
```r
x <- c(46, 23, 15, 38, 98, 56, 28, 78)

# Ascending
sort(x)
# Output: 15 23 28 38 46 56 78 98

# Descending
sort(x, decreasing = TRUE)
# Output: 98 78 56 46 38 28 23 15
```

### Combining Data Functions:
```r
# c() — Combine values into a vector
x <- c(1, 2, 3, 4)

# rbind() — Combine data frames by rows (stack vertically)
df1 <- data.frame(Name = "Alice", Age = 25)
df2 <- data.frame(Name = "Bob", Age = 30)
combined <- rbind(df1, df2)

# cbind() — Combine by columns (side by side)
col1 <- c(1, 2, 3)
col2 <- c("a", "b", "c")
combined <- cbind(col1, col2)

# merge() — SQL-like join on common columns
merge(df1, df2, by = "common_column")

# append() — Add elements to a vector
x <- c(1, 2, 3)
x <- append(x, c(4, 5))
# x = 1, 2, 3, 4, 5
```

### Solved Example (Dec 2023):
```r
# Combine two datasets
A <- c(6, 7, 8, 9)
B <- c(1, 2, 4, 5)

# Using c()
C <- c(A, B)
print(C)
# Output: 6 7 8 9 1 2 4 5

# Using append()
C <- append(A, B)
print(C)
# Output: 6 7 8 9 1 2 4 5
```

**MU Keyword Checklist:** sort(), order(), decreasing=TRUE, c(), rbind(), cbind(), merge(), append(), ascending, descending, combine vectors

---

## Q28. R: Data Structures in R. [10 Marks] — 2/6

**Question Type:** Theory

### Six Main Data Structures:

| # | Data Structure | Dimensions | Homogeneous? | Example |
|---|---------------|-----------|-------------|---------|
| 1 | **Vector** | 1D | Yes (all same type) | `c(1, 2, 3)` |
| 2 | **Matrix** | 2D | Yes | `matrix(1:6, nrow=2)` |
| 3 | **Array** | nD | Yes | `array(1:24, dim=c(2,3,4))` |
| 4 | **List** | 1D | No (mixed types) | `list("a", 1, TRUE)` |
| 5 | **Data Frame** | 2D | No (columns can differ) | `data.frame(x=1:3, y=c("a","b","c"))` |
| 6 | **Factor** | 1D | Categorical | `factor(c("M","F","M"))` |

```
┌──────────────────────────────────────────────────┐
│              R DATA STRUCTURES                    │
│                                                  │
│  Homogeneous:           Heterogeneous:           │
│  ┌────────────┐         ┌────────────────┐       │
│  │ Vector (1D)│         │ List (1D)       │       │
│  │ c(1,2,3)   │         │ list("a",1,T)  │       │
│  ├────────────┤         ├────────────────┤       │
│  │ Matrix (2D)│         │ Data Frame (2D)│       │
│  │ matrix()   │         │ data.frame()   │       │
│  ├────────────┤         └────────────────┘       │
│  │ Array (nD) │                                  │
│  │ array()    │         ┌────────────────┐       │
│  └────────────┘         │ Factor          │       │
│                         │ Categorical     │       │
│                         └────────────────┘       │
└──────────────────────────────────────────────────┘
```

### Key Operations:
```r
# Vector
v <- c(10, 20, 30)
length(v)       # 3
v[2]            # 20

# Matrix
m <- matrix(1:6, nrow = 2, ncol = 3)
m[1, 2]         # Element at row 1, col 2
dim(m)          # 2 3

# List (heterogeneous)
lst <- list(name = "John", age = 30, scores = c(90, 85))
lst$name        # "John"
lst[[3]]        # c(90, 85)

# Data Frame
df <- data.frame(x = 1:3, y = c("a", "b", "c"))
df$x            # Access column x
nrow(df)        # 3
ncol(df)        # 2

# Factor
f <- factor(c("High", "Low", "Medium", "High"))
levels(f)       # "High" "Low" "Medium"
table(f)        # Frequency table
```

**MU Keyword Checklist:** Vector, Matrix, Array, List, Data Frame, Factor, homogeneous, heterogeneous, c(), matrix(), list(), data.frame(), factor(), levels(), dim(), str()

---

## Q29. Explain Data Visualization: Types and Applications. [10 Marks] — May'24

**Question Type:** Theory

### Definition
**Data Visualization** is the graphical representation of data and information using visual elements like charts, graphs, and maps to identify patterns, trends, and outliers.

### Types of Visualizations:

| Type | R Function | Best For |
|------|-----------|----------|
| **Bar Chart** | `barplot()` | Comparing categories |
| **Histogram** | `hist()` | Distribution of continuous data |
| **Pie Chart** | `pie()` | Proportions/composition |
| **Line Chart** | `plot(type="l")` | Trends over time |
| **Scatter Plot** | `plot()` | Relationship between 2 variables |
| **Box Plot** | `boxplot()` | Distribution, quartiles, outliers |
| **Heatmap** | `heatmap()` | Matrix data, correlation |

### Applications:
1. **Business Analytics:** Sales dashboards, revenue trends, KPI monitoring
2. **Healthcare:** Disease spread maps (COVID dashboards), patient vitals monitoring
3. **Finance:** Stock price charts, portfolio allocation pie charts
4. **Social Media:** Engagement metrics, trending topic word clouds
5. **Scientific Research:** Genome visualization, climate change plots

### R Plotting Examples:
```r
# Bar chart
barplot(c(20, 35, 30, 15), names.arg = c("Q1","Q2","Q3","Q4"),
        main = "Quarterly Sales", col = "blue")

# Histogram
hist(rnorm(100), main = "Normal Distribution", col = "green")

# Scatter plot
plot(x = c(1,2,3,4,5), y = c(2,4,5,4,6),
     main = "X vs Y", xlab = "X", ylab = "Y", pch = 19)

# Box plot
boxplot(mtcars$mpg ~ mtcars$cyl, main = "MPG by Cylinders")
```

**MU Keyword Checklist:** barplot, hist, pie, plot, boxplot, heatmap, scatter, line chart, trends, patterns, outliers, dashboard, visualization types

---

## Q30. Functions vs Scripts in R. Advantages of Functions. [10 Marks] — Dec'23

**Question Type:** Theory

### Comparison Table

| Parameter | Script | Function |
|-----------|--------|----------|
| **Definition** | Sequence of R commands saved in a .R file | Reusable block of code with defined inputs/outputs |
| **Reusability** | Must copy-paste code | Call by name with different arguments |
| **Parameters** | Uses hardcoded values | Takes parameters — flexible |
| **Return Value** | No explicit return | Returns a value via `return()` |
| **Scope** | Global environment | Local scope (variables don't leak) |
| **Execution** | `source("script.R")` | `function_name(args)` |
| **Modularity** | Monolithic | Modular, testable |

### Advantages of Functions:
1. **Code Reusability:** Write once, use many times with different inputs
2. **Modularity:** Break complex problems into smaller, manageable pieces
3. **Debugging:** Isolate and test individual functions
4. **Readability:** Named functions make code self-documenting
5. **Scope Safety:** Local variables don't pollute global environment

### Example:
```r
# SCRIPT approach (inflexible):
x <- c(10, 20, 30, 40, 50)
mean_x <- mean(x)
sd_x <- sd(x)
cat("Mean:", mean_x, "SD:", sd_x)

# FUNCTION approach (reusable):
analyze <- function(data) {
  result <- list(
    mean = mean(data),
    sd = sd(data),
    min = min(data),
    max = max(data)
  )
  return(result)
}

# Can use with ANY data:
analyze(c(10, 20, 30))
analyze(c(100, 200, 300))
```

**MU Keyword Checklist:** function(), return(), source(), parameters, arguments, local scope, global scope, reusability, modularity, script vs function
