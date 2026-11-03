# Mumbai University (MU) Semester 7 — Machine Learning (ML)
## Comprehensive 6-Paper PYQ Trend Analysis & Priority Roadmap
*(Exam Cycles Analyzed: December 2022, May 2023, December 2023, May 2024, December 2024, May 2025)*
**Course Code:** Department Level Optional Course (DLOC) | **Scheme:** Rev 2019 / C-Scheme | **Total Marks:** 80 per paper

---

## 1. Executive Summary & Syllabus Module Architecture

Machine Learning in Mumbai University Semester 7 follows a structured 6-module curriculum. Analysis of the last six consecutive examination cycles reveals extreme consistency, recurring 10-mark numerical questions, and mandatory algorithmic derivations.

```
+---------------------------------------------------------------------------------------------------+
|                                 MU SEM 7 ML MODULE ARCHITECTURE                                   |
+---------------------------------------------------------------------------------------------------+
|  M1: Introduction to Machine Learning (10-15 Marks)                                               |
|      - Types: Supervised, Unsupervised, Semi-supervised, Reinforcement Learning                    |
|      - Core Issues in ML: Data Quality, Overfitting, Underfitting, Curse of Dimensionality         |
|      - Steps in Developing Machine Learning Applications (Data Collection --> Deployment)         |
|      - Training Error vs Generalization Error | Bias-Variance Tradeoff (Mathematical & Graphical)  |
+---------------------------------------------------------------------------------------------------+
|  M2: Learning with Regression & Decision Trees (25-35 Marks) -- [CRITICAL NUMERICAL HUB]          |
|      - Linear Regression: Cost Function, Normal Equation, Gradient Descent, OLS Derivations       |
|      - Solved Numericals: BMI-Cholesterol Prediction, Exam Grade Prediction, Mass vs Time          |
|      - Logistic Regression: Sigmoid Function, Odds Ratio, Log-Loss Cost Function                   |
|      - Decision Trees: ID3 vs CART, Gini Index vs Information Gain, Overfitting & Tree Pruning     |
|      - Solved Numericals: Gini Index Root Node Selection (Car Stolen, Stock Trend, Profit, Car)    |
|      - Performance Evaluation Metrics: Confusion Matrix, Precision, Recall, F1, Specificity, ROC/AUC|
+---------------------------------------------------------------------------------------------------+
|  M3: Ensemble Learning (15-20 Marks)                                                              |
|      - Understanding Ensembles: Bagging vs Boosting vs Stacking                                   |
|      - Random Forest Algorithm (Bootstrap Aggregating + Random Subspace Method)                   |
|      - Boosting Paradigms: AdaBoost Formulation & XGBoost Gradient Tree Boosting Architecture     |
|      - Model Validation: K-Fold Cross Validation, Stratified K-Fold, Leave-One-Out (LOOCV)        |
+---------------------------------------------------------------------------------------------------+
|  M4: Learning with Classification (SVM & Multiclass) (15-20 Marks)                                |
|      - Support Vector Machines (SVM): Hyperplane, Maximum Margin Classifier, Support Vectors      |
|      - SVM as Constrained Optimization: Primal Formulation, Lagrangian Multipliers, Dual Problem  |
|      - Hard Margin vs Soft Margin (Slack Variables $\xi_i$, Penalty C)                            |
|      - The Kernel Trick: Mercer's Theorem, Linear, Polynomial, RBF/Gaussian, Sigmoid Kernels      |
|      - Multiclass Classification Strategies: One-vs-All (OvA) vs One-vs-One (OvO)                 |
+---------------------------------------------------------------------------------------------------+
|  M5: Learning with Clustering (15-20 Marks)                                                       |
|      - Distance Metrics: Euclidean, Manhattan, Minkowski, Cosine, Mahalanobis                     |
|      - Partitioning Clustering: K-Means Algorithm (Convergence, Elbow Method)                     |
|      - Graph-Based Clustering: Minimum Spanning Tree (MST) Clustering (Prim's / Kruskal's)        |
|      - Model-Based Clustering: Expectation-Maximization (EM) Algorithm for Gaussian Mixture (GMM) |
|      - Density-Based Clustering: DBSCAN Algorithm (Core Points, Border Points, Noise, MinPts, Eps)|
+---------------------------------------------------------------------------------------------------+
|  M6: Dimensionality Reduction (15-20 Marks) -- [CRITICAL NUMERICAL HUB]                           |
|      - Curse of Dimensionality & Need for Dimensionality Reduction                                |
|      - Principal Component Analysis (PCA): Covariance Matrix, Eigenvalues/Eigenvectors, Projection|
|      - Linear Discriminant Analysis (LDA): Within-class ($S_W$) vs Between-class ($S_B$) Scatter  |
|      - Solved Numericals: Dec'22 2-Class 2D LDA Projection Matrix, May'23 SVD Decomposition ($2x2$)|
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Topic-by-Topic 6-Paper Frequency Matrix

The following matrix records every appearance of a topic across the 6 analyzed papers (Dec 2022 to May 2025).

| # | Topic / Concept Description | Dec 22 | May 23 | Dec 23 | May 24 | Dec 24 | May 25 | Total Count | Frequency Tier |
|---|-----------------------------|:------:|:------:|:------:|:------:|:------:|:------:|:-----------:|:--------------:|
| **1** | **Decision Tree Construction using Gini Index (Numerical)** | Q3a (10M) | Q3a (10M) | Q4b (10M) | Q4b (10M) | Q4b (10M) | Q3a (10M) | **6 times** | **Tier 1 (100% Guaranteed 10M)** |
| **2** | **Linear Regression (Derivation / Numerical / Theory)** | Q1b (5M), Q2b (10M) | Q1b (5M), Q2b (10M), Q6a (10M) | Q3a (10M) | Q3a (10M) | Q1c (5M) | Q1b (5M), Q3b (10M) | **7 times** | **Tier 1 (100% Guaranteed 10M)** |
| **3** | **Random Forest & Classifier Combining / Ensembles** | Q4a (10M), Q4b (10M) | Q4a (10M), Q4b (10M) | Q5b (10M) | Q2b (10M), Q6b (10M) | Q4a (10M) | Q4a (10M), Q4b (10M) | **7 times** | **Tier 1 (Guaranteed 10M)** |
| **4** | **Support Vector Machines (Constrained Optimization & Kernel Trick)** | Q1c (5M) | — | Q1d (5M), Q4a (10M), Q5a (10M) | Q6a (10M) | Q6b (10M), Q6c (10M) | Q1c (5M) | **6 times** | **Tier 1 (Guaranteed 10M)** |
| **5** | **DBSCAN Clustering (Density-Based Algorithm & Parameters)** | Q6c (10M) | Q6c (10M) | Q6c (10M) | Q3b (10M) | Q5b (10M) | Q6c (10M) | **6 times** | **Tier 1 (Guaranteed 10M)** |
| **6** | **Linear Discriminant Analysis (LDA Theory & Numerical)** | Q5a (10M) | Q6b (10M) | Q1b (5M) | Q5b (10M) | — | Q2b (10M) | **5 times** | **Tier 1 (High Yield)** |
| **7** | **Principal Component Analysis (PCA Steps & Covariance)** | Q6b (10M) | — | Q6b (10M) | — | Q5a (10M) | Q6b (10M) | **4 times** | **Tier 1 (High Yield)** |
| **8** | **Minimal Spanning Tree (MST) Graph-Based Clustering** | — | — | Q2a (10M) | Q4a (10M) | Q2a (10M) | Q5b (10M) | **4 times** | **Tier 1 (High Yield)** |
| **9** | **Steps in Developing ML Applications & ML Issues** | Q1a (5M), Q2a (10M) | Q1a (5M), Q2a (10M) | Q1a (5M), Q2b (10M) | Q2a (10M) | Q1d (5M), Q3a (10M) | Q1a (5M), Q2a (10M) | **8 times** | **Tier 1 (Guaranteed Theory)** |
| **10** | **Classification Performance Metrics (Confusion Matrix, ROC/AUC)** | Q6a (10M) | — | Q1c (5M), Q1e (5M) | Q1c (5M) | Q1e (5M), Q2b (10M) | Q1d (5M), Q6a (10M) | **6 times** | **Tier 1 (Guaranteed)** |
| **11** | **Logistic Regression (Sigmoid, Odds, Cost Function)** | Q1e (5M) | Q1e (5M) | Q1d (5M) | — | Q1c (5M), Q2b (10M) | Q1e (5M) | **5 times** | **Tier 2 (High Yield)** |
| **12** | **K-Fold Cross Validation & Resampling** | — | — | Q3b (10M) | Q1e (5M) | — | — | **2 times** | **Tier 2 (Core Theory)** |
| **13** | **Multiclass Classification (One-vs-Rest / One-vs-One)** | Q3b (10M) | Q5a (10M) | Q6a (10M) | — | — | Q5a (10M) | **4 times** | **Tier 2 (High Yield)** |
| **14** | **Expectation-Maximization (EM) Algorithm** | Q5b (10M) | Q5b (10M) | — | — | — | — | **2 times** | **Tier 2 (Standard 10M)** |
| **15** | **Singular Value Decomposition (SVD Numerical)** | — | Q3b (10M) | — | — | — | — | **1 time** | **Tier 3 (Special Numerical)** |

---

## 3. High-Priority Preparation Tiers (Exam Survival Strategy)

To score 70+ out of 80 marks in MU Semester 7 Machine Learning, students must master:

### Tier 1: Non-Negotiable Core (Guarantees 55-60 Marks)
1. **Decision Tree Construction using Gini Index (10 Marks):**
   - Formulations: $\text{Gini}(D) = 1 - \sum_{i=1}^m p_i^2$, and Split Gini: $\text{Gini}_A(D) = \frac{|D_1|}{|D|}\text{Gini}(D_1) + \frac{|D_2|}{|D|}\text{Gini}(D_2)$.
   - Compute Gini index for all candidate features, pick feature with minimum Gini index (maximum Gini gain) as root.
   - All 5 distinct past paper tables solved step-by-step in Masterclass Part 1.
2. **Linear Regression Derivations & Solved Numericals (10 Marks):**
   - Ordinary Least Squares (OLS) formula:
     $$\beta_1 = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sum (X_i - \bar{X})^2} = \frac{N \sum XY - \sum X \sum Y}{N \sum X^2 - (\sum X)^2}, \quad \beta_0 = \bar{Y} - \beta_1 \bar{X}$$
   - Exact numericals: BMI vs Cholesterol (Predict for BMI=27), Midterm vs Final Exam (Predict for Midterm=86), Mass vs Time.
3. **Support Vector Machines (SVM) Formulation (10 Marks):**
   - Primal optimization problem: $\min_{w, b} \frac{1}{2}\|w\|^2$ subject to $y_i(w^T x_i + b) \ge 1$.
   - Lagrangian dual problem with KKT conditions ($\alpha_i \ge 0, \alpha_i [y_i(w^T x_i + b) - 1] = 0$).
   - Slack variables $\xi_i$ for soft margins and Kernel trick ($K(x_i, x_j) = \phi(x_i)^T \phi(x_j)$).
4. **DBSCAN Density-Based Clustering (10 Marks):**
   - Parameters: $\epsilon$ (Eps neighborhood radius) and $\text{MinPts}$.
   - Classifications: Core point, Border point, Noise point.
   - Concepts: Directly density-reachable, Density-reachable, Density-connected.
   - Step-by-step algorithm and comparison with K-Means.
5. **Dimensionality Reduction: PCA & LDA (10 Marks):**
   - PCA: Mean centering, Covariance matrix $\Sigma = \frac{1}{n} X^T X$, Eigen decomposition $\Sigma v = \lambda v$, projection onto top $k$ eigenvectors.
   - LDA: Maximizing Fisher's criterion $J(w) = \frac{w^T S_B w}{w^T S_W w} \implies w \propto S_W^{-1}(\mu_1 - \mu_2)$. Full numerical solved for Dec'22 paper.

### Tier 2: High-Yield Theory & Algorithms (20-25 Marks)
1. **Steps in Developing ML Applications & Machine Learning Issues:**
   - 7-step pipeline: Problem definition $\to$ Data collection $\to$ Preprocessing/Feature Engineering $\to$ Model selection $\to$ Training $\to$ Evaluation $\to$ Deployment/Monitoring.
   - Core Issues: Overfitting/Underfitting, Curse of Dimensionality, Data Drift, Class Imbalance.
2. **Bias-Variance Tradeoff:**
   - Mathematical decomposition of Mean Squared Error: $\text{MSE} = \text{Bias}^2 + \text{Variance} + \sigma^2$ (Irreducible error).
   - Graphical trade-off curve vs model complexity.
3. **Ensemble Methods:**
   - Bagging (Bootstrap Aggregation) vs Boosting (Iterative re-weighting) vs Stacking (Meta-learner).
   - Random Forest: Bootstrap sampling + Random feature subspace selection at each node split.
   - XGBoost: Gradient boosting framework with regularized objective function and second-order Taylor expansion.
4. **Graph-Based Minimal Spanning Tree (MST) Clustering:**
   - Construct complete graph with pairwise Euclidean distances $\to$ Compute MST (Kruskal/Prim) $\to$ Delete $k-1$ edges with largest weights to partition into $k$ clusters.
5. **Performance Evaluation Metrics:**
   - Binary Confusion Matrix: TP, TN, FP, FN.
   - Accuracy, Precision, Recall/Sensitivity, Specificity, F1-Score, ROC Curve, AUC.

---

## 4. Masterclass Content Division

- **`ml_masterclass_part1.md`**:
  - **Module 1:** Introduction, Types of ML, Issues in ML, Application Pipeline, Training Error vs Generalization Error, Bias-Variance Tradeoff (Math derivation & Curves).
  - **Module 2:** Linear Regression (Derivation of OLS, Gradient Descent), **Full Numerical Solution 1 (Dec'23: BMI vs Cholesterol, Predict for BMI=27)**, **Full Numerical Solution 2 (May'25: Midterm vs Final Exam, Predict for Midterm=86)**, **Full Numerical Solution 3 (May'24: Mass vs Time)**, Logistic Regression (Sigmoid derivation, Odds ratio, Log-loss cost function), Performance Metrics (Formulas & Confusion Matrix).
  - **Module 2 (Decision Trees):** ID3 vs CART, Information Gain vs Gini Index, Overfitting & Pruning, **Full Numerical Solution 4 (Dec'24: Car Stolen Dataset Gini Index Root Selection)**, **Full Numerical Solution 5 (Dec'23: Stock Trend Dataset Gini Index)**, **Full Numerical Solution 6 (May'23: Profit Dataset Gini Index)**.
  - **Module 3:** Ensemble Learning (Bagging vs Boosting vs Stacking), Random Forest Algorithm, XGBoost, K-Fold Cross Validation.

- **`ml_masterclass_part2.md`**:
  - **Module 4:** Support Vector Machines (Constrained optimization, Primal to Dual derivation, KKT conditions, Soft margins, Kernel trick with Mercer's condition, SVR), Multiclass Classification (One-vs-Rest vs One-vs-One).
  - **Module 5:** Clustering Distance Metrics, K-Means Clustering & Elbow method, Minimal Spanning Tree (MST) Clustering (Algorithm & step-by-step example), Expectation-Maximization (EM) Algorithm for GMMs, DBSCAN Algorithm (Density reachability, Core/Border/Noise points, complete walk).
  - **Module 6:** Dimensionality Reduction Need & Taxonomy, Principal Component Analysis (PCA full algorithm & 2D worked derivation), **Linear Discriminant Analysis (LDA) Full Numerical Solution (Dec'22: 2-Class 2D Dataset)**, **Singular Value Decomposition (SVD) Full Numerical Solution (May'23: $2 \times 2$ Matrix)**.
