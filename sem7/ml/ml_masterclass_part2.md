# 📘 ML ULTIMATE MASTERCLASS — Part 2: TIER 2 & TIER 3 (HIGH YIELD & EXTENSIONS)
## Course: Machine Learning (DLOC) | Scheme: Mumbai University Rev 2019 / C-Scheme
### Applicable Exam Cycles: Dec 2022, May 2023, Dec 2023, May 2024, Dec 2024, May 2025, Nov 2025 (7 Cycles Calibrated)

---

> ### 🎯 Tier 2 & Tier 3 Structure & Roadmap
> **Tier 2 (High Yield: 3–6 appearances) & Tier 3 (Core Extensions / Short Notes: 1–3 appearances).**
> - **Q8.** Linear Discriminant Analysis (LDA): Fisher's Criterion Derivation & Solved 2D Projection Numerical [10 Marks] — *(6/7 Papers — Tier 1/2 High Yield)*
> - **Q9.** Logistic Regression: Sigmoid Hypothesis, Odds Ratio, Log-Loss Cost Function & Gradient Descent [10 Marks] — *(6/7 Papers — Tier 1/2 High Yield)*
> - **Q10.** Multiclass Classification Strategies: One-vs-Rest, One-vs-One & Softmax Multinomial Logistic Regression [10 Marks] — *(5/7 Papers — Tier 2 High Yield)*
> - **Q11.** Principal Component Analysis (PCA) & Singular Value Decomposition (SVD): Covariance Derivation & Solved Numerical [10 Marks] — *(4/7 Papers — Tier 2 High Yield)*
> - **Q12.** Graph-Based Clustering: Minimum Spanning Tree (MST) Algorithm & Cluster Extraction [10 Marks] — *(4/7 Papers — Tier 2 High Yield)*
> - **Q13.** Model-Based Clustering: Expectation-Maximization (EM) Algorithm for Gaussian Mixture Models (GMM) [10 Marks] — *(3/7 Papers — Tier 2 High Yield)*
> - **Q14.** Distance & Similarity Metrics in ML: Euclidean, Manhattan, Minkowski, Cosine & Mahalanobis [5–10 Marks] — *(Nov 2025 & Recurring Core Theory)*
> - **Q15.** Model Validation, Resampling Strategies & Bias-Variance Decomposition: K-Fold CV & Mathematical Trade-Off [10 Marks] — *(Recurring Core Theory)*

---
---

## Q8. Linear Discriminant Analysis (LDA): Fisher's Criterion Derivation & Solved 2D Projection Numerical [10 Marks]
*(Appeared in: Dec 2022 Q5a [10M], May 2023 Q6b [10M], Dec 2023 Q1b [5M], May 2024 Q5b [10M], May 2025 Q2b [10M], Nov 2025 Q3b [10M])*

### a) Core Concept: Supervised Dimensionality Reduction vs Unsupervised PCA
**Linear Discriminant Analysis (LDA)** is a supervised dimensionality reduction and linear classification technique developed by Ronald Fisher.
While **PCA** is unsupervised and searches for directions of maximum total variance (ignoring class labels), **LDA** finds a projection subspace w that maximizes the separation between distinct class distributions while minimizing the variance within each class.

```
+---------------------------------------------------------------------------------------------------+
|                                     PCA VS LDA PROJECTION OBJECTIVE                               |
+---------------------------------------------------------------------------------------------------+
|  x₂ ^                                                                                            |
|      |        (Class 1: O)              (Class 2: X)                                              |
|      |           O  O  O                   X  X  X                                                |
|      |         O   O  O  O               X   X  X  X                                              |
|      |            O  O  O                   X  X  X                                               |
|      |                  \                         /                                               |
|      |                   \  PCA Projection Axis  /  LDA Projection Axis                           |
|      |                    \ (Max Overall Var)   /   (Max Class Separation)                        |
|      |                     \                   /                                                  |
|      +----------------------\-----------------/---------------------------> x₁                   |
|                              v               v                                                    |
|                   Overlapping Classes   Distinct Separated Classes                                |
+---------------------------------------------------------------------------------------------------+
```

---

### b) Mathematical Formulation: Scatter Matrices
For a binary classification task with classes C₁ and C₂:
- Class means in input space:
  ```
  μ₁ = (1/N₁) · ∑ x   (for x in C₁)
  μ₂ = (1/N₂) · ∑ x   (for x in C₂)
  ```
- **Between-Class Scatter Matrix (S_B):** Measures the distance between class centroids:
  ```
  S_B = (μ₁ − μ₂) · (μ₁ − μ₂)ᵀ
  ```
- **Within-Class Scatter Matrix (S_W):** Measures the internal dispersion within each individual class:
  ```
  S₁ = ∑ (x − μ₁) · (x − μ₁)ᵀ   (for x in C₁)
  S₂ = ∑ (x − μ₂) · (x − μ₂)ᵀ   (for x in C₂)
  S_W = S₁ + S₂
  ```

---

### c) Derivation of Fisher's Linear Discriminant
Fisher's objective function maximizes the ratio of between-class variance to within-class variance in the projected 1D space y = wᵀ·x:
```
J(w) = (μ̃₁ − μ̃₂)² / (s̃₁² + s̃₂²) = [ wᵀ · S_B · w ] / [ wᵀ · S_W · w ]
```

To maximize J(w), take the gradient with respect to w and equate to zero:
```
∂J / ∂w = [ 2·S_B·w · (wᵀ·S_W·w) − 2·S_W·w · (wᵀ·S_B·w) ] / [ wᵀ·S_W·w ]² = 0
```
Dividing by 2(wᵀ·S_W·w):
```
S_B·w − [ (wᵀ·S_B·w) / (wᵀ·S_W·w) ] · S_W·w = 0
```
Since [ (wᵀ·S_B·w) / (wᵀ·S_W·w) ] = J(w) = λ (a scalar constant):
```
S_B·w = λ · S_W·w  -->  (S_W)⁻¹ · S_B · w = λ · w
```
Notice that S_B·w = (μ₁ − μ₂) · [ (μ₁ − μ₂)ᵀ · w ].
Since [ (μ₁ − μ₂)ᵀ · w ] is a scalar factor, the vector S_B·w always points in the direction of (μ₁ − μ₂).
Therefore, the optimal projection vector direction is:
```
w* = (S_W)⁻¹ · (μ₁ − μ₂)
```

---

### d) Solved Numerical 1 (Dec 2022): 2-Class 2D LDA Optimal Projection Matrix
*(Appeared in: December 2022 Paper, Question 5(a) [10 Marks])*

#### Problem Statement:
Given two classes with two features x₁ and x₂:
- **Class 1 (C₁):** (1, 2), (2, 3), (3, 3), (4, 5), (5, 5)
- **Class 2 (C₂):** (4, 2), (5, 0), (5, 2), (3, 2), (5, 3), (6, 3)
Find the optimal projection vector w* and the decision boundary threshold.

#### Step 1: Compute Class Means
```
N₁ = 5,   N₂ = 6

μ₁ = (1/5) · [ (1+2+3+4+5), (2+3+3+5+5) ]ᵀ = [ 15/5, 18/5 ]ᵀ = [ 3.0, 3.6 ]ᵀ
μ₂ = (1/6) · [ (4+5+5+3+5+6), (2+0+2+2+3+3) ]ᵀ = [ 28/6, 12/6 ]ᵀ = [ 4.667, 2.0 ]ᵀ

Difference Vector:
μ₁ − μ₂ = [ 3.0 − 4.667, 3.6 − 2.0 ]ᵀ = [ −1.667, 1.600 ]ᵀ
```

#### Step 2: Compute Scatter Matrices S₁ and S₂
Center the data for C₁:
```
x_i − μ₁:
Point 1: [ 1−3.0, 2−3.6 ] = [ −2.0, −1.6 ]
Point 2: [ 2−3.0, 3−3.6 ] = [ −1.0, −0.6 ]
Point 3: [ 3−3.0, 3−3.6 ] = [  0.0, −0.6 ]
Point 4: [ 4−3.0, 5−3.6 ] = [  1.0,  1.4 ]
Point 5: [ 5−3.0, 5−3.6 ] = [  2.0,  1.4 ]

S₁ = ∑ (x − μ₁)(x − μ₁)ᵀ
   = [ 10.0,  8.0 ]
     [  8.0,  7.2 ]
```

Center the data for C₂:
```
S₂ = [ 5.333, 0.667 ]
     [ 0.667, 6.000 ]
```

#### Step 3: Compute Within-Class Scatter Matrix S_W and its Inverse
```
S_W = S₁ + S₂ = [ 10.0 + 5.333,  8.0 + 0.667 ] = [ 15.333,  8.667 ]
                [  8.0 + 0.667,  7.2 + 6.000 ]   [  8.667, 13.200 ]

Determinant of S_W:
det(S_W) = (15.333)(13.200) − (8.667)² = 202.3956 − 75.1169 = 127.2787

Inverse (S_W)⁻¹:
(S_W)⁻¹ = (1 / 127.2787) · [  13.200, −8.667 ]
                           [  −8.667, 15.333 ]
        = [  0.1037, −0.0681 ]
          [ −0.0681,  0.1205 ]
```

#### Step 4: Compute Optimal Projection Vector w*
```
w* = (S_W)⁻¹ · (μ₁ − μ₂)
   = [  0.1037, −0.0681 ] · [ −1.667 ]
     [ −0.0681,  0.1205 ]   [  1.600 ]

w₁ = (0.1037)(−1.667) + (−0.0681)(1.600) = −0.1729 − 0.1090 = −0.2819
w₂ = (−0.0681)(−1.667) + (0.1205)(1.600) =  0.1135 + 0.1928 =  0.3063

Optimal Projection Vector:
w* = [ −0.2819, 0.3063 ]ᵀ
```

#### Step 5: Decision Boundary Threshold (w₀)
```
Projected class centroids:
μ̃₁ = w*ᵀ · μ₁ = (−0.2819)(3.0) + (0.3063)(3.6) = −0.8457 + 1.1027 =  0.2570
μ̃₂ = w*ᵀ · μ₂ = (−0.2819)(4.667) + (0.3063)(2.0) = −1.3156 + 0.6126 = −0.7030

Optimal separating threshold:
w₀ = (μ̃₁ + μ̃₂) / 2 = [ 0.2570 + (−0.7030) ] / 2 = −0.4460 / 2 = −0.2230

Classification Rule:
If w*ᵀ · x ≥ −0.2230  -->  Assign to Class 1
Else                  -->  Assign to Class 2
```

---
---

## Q9. Logistic Regression: Sigmoid Hypothesis, Odds Ratio, Log-Loss Cost Function & Gradient Descent [10 Marks]
*(Appeared in: Dec 2022 Q1e [5M], May 2023 Q1e [5M], Dec 2023 Q1d [5M], Dec 2024 Q1c [5M]/Q2b [10M], May 2025 Q1e [5M], Nov 2025 Q6c [10M])*

### a) Sigmoid Activation & Hypothesis Function
Logistic Regression models the posterior probability of a binary categorical label y in {0, 1} by mapping a linear combination of features through the non-linear **Standard Sigmoid (Logistic)** function:
```
z = wᵀ·x + b
h_w(x) = σ(z) = 1 / (1 + exp(−z)) = 1 / (1 + exp(−(wᵀ·x + b)))
```

```
                σ(z) ^
                 1.0 |                              +--------
                     |                             /
                     |                            /
                 0.5 |---------------------------+ (Threshold z = 0)
                     |                          /
                     |                         /
                 0.0 +------------------------+-------------> z
                    -6   -4   -2    0    2    4    6
```

#### Key Mathematical Properties of Sigmoid:
1. **Range:** Maps R  --> (0, 1), matching valid probability axioms: P(y = 1 | x) = h_w(x).
2. **Derivative Property:** The derivative expresses cleanly in terms of the function itself:
   ```
   dσ / dz = σ(z) · (1 − σ(z))
   ```

---

### b) Odds Ratio & Logit (Log-Odds) Formulation
The **Odds** of an event is the ratio of probability of occurrence to probability of non-occurrence:
```
Odds = P / (1 − P) = [ 1 / (1 + exp(−z)) ] / [ exp(−z) / (1 + exp(−z)) ] = exp(z)
```
Taking the natural logarithm yields the **Logit (Log-Odds)** function:
```
ln(Odds) = ln( P / (1 − P) ) = ln(exp(z)) = z = wᵀ·x + b
```
*Interpretation:* While probability is bounded in (0, 1), the log-odds is completely linear and unbounded across (−∞, +∞), establishing a clean linear decision boundary at z = 0  <-->  P = 0.5.

---

### c) Cost Function: Cross-Entropy (Log-Loss)
If we use Mean Squared Error (MSE) for Logistic Regression, the resulting loss surface is non-convex with numerous sub-optimal local minima.
To guarantee a convex optimization surface with a unique global minimum, we derive the **Binary Cross-Entropy (Log-Loss)** using Maximum Likelihood Estimation:
```
P(y | x) = [ h_w(x) ]^y · [ 1 − h_w(x) ]^(1 − y)

Likelihood:
L(w) = ∏ [ h_w(x_i) ]^(y_i) · [ 1 − h_w(x_i) ]^(1 − y_i)

Cost Function (Negative Log-Likelihood normalized by N):
J(w) = − (1/N) · ∑ [ y_i · ln(h_w(x_i)) + (1 − y_i) · ln(1 − h_w(x_i)) ]
```

---

### d) Gradient Descent Parameter Update Derivation
Computing the partial derivative with respect to weight w_j:
```
∂J / ∂w_j = (1/N) · ∑ [ ( h_w(x_i) − y_i ) · x_ij ]
```
The batch gradient descent parameter update rule with learning rate α is:
```
w_j  <--  w_j − α · (1/N) · ∑ [ ( ŷ_i − y_i ) · x_ij ]
```

---
---

## Q10. Multiclass Classification Architectures: One-vs-Rest (OvR), One-vs-One (OvO) & Softmax [10 Marks]
*(Appeared in: Dec 2022 Q3b [10M], May 2023 Q5a [10M], Dec 2023 Q6a [10M], May 2025 Q5a [10M], Nov 2025 Q5a [10M])*

### a) Decomposing Multi-Class Problems
Standard binary classifiers (Logistic Regression, Hard/Soft Margin SVM) naturally output binary decisions ({-1, +1} or {0, 1}). When classifying K > 2 discrete classes, two primary architectural decomposition heuristics are utilized:

```
+---------------------------------------------------------------------------------------------------+
|                            MULTICLASS CLASSIFICATION STRATEGIES                                   |
+---------------------------------------------------------------------------------------------------+
|  1. ONE-VS-REST (OvR / One-vs-All)                  2. ONE-VS-ONE (OvO)                           |
|     - Trains K binary classifiers.                     - Trains K(K-1)/2 binary classifiers.      |
|     - Classifier k separates class k from ALL others.  - Classifier (i, j) separates class i vs j.|
|                                                                                                   |
|       [Class 1] vs [Class 2 + 3 + 4]                     [Class 1] vs [Class 2]                   |
|       [Class 2] vs [Class 1 + 3 + 4]                     [Class 1] vs [Class 3]                   |
|       [Class 3] vs [Class 1 + 2 + 4]                     [Class 2] vs [Class 3]                   |
|       [Class 4] vs [Class 1 + 2 + 3]                     ... (Pairwise Tournaments)               |
+---------------------------------------------------------------------------------------------------+
```

---

### b) One-vs-Rest (OvR / One-vs-All)
1. **Model Training:** Constructs exactly K distinct binary classifiers f₁, f₂, ..., f_K. For classifier k, instances of class k serve as positive examples (+1), while all remaining samples from classes j ≠ k are pooled into the negative class (−1).
2. **Inference Decision Rule:** Evaluates confidence scores across all K models; assigns sample x to the class with maximum confidence score:
   ```
   ŷ = argmax_{k in {1, ..., K}} f_k(x)
   ```
3. **Key Trade-Offs:**
   - *Pros:* Computational efficiency; requires only K trained classifiers.
   - *Cons:* Severe class imbalance during training (1 positive vs K−1 pooled negatives); uncalibrated confidence scale disparities between different models.

---

### c) One-vs-One (OvO / Pairwise Classification)
1. **Model Training:** Constructs a dedicated binary classifier for every distinct pair of classes:
   ```
   Total Classifiers = K · (K − 1) / 2
   ```
   Each classifier f_{ij} is trained strictly on the subset of data belonging to classes i and j (ignoring all other classes).
2. **Inference Decision Rule (Majority Voting):** Test instance x is evaluated by all K(K−1)/2 classifiers. Each classifier casts a vote for its predicted winner. The class receiving the highest cumulative vote tally wins.
3. **Key Trade-Offs:**
   - *Pros:* No class imbalance per classifier; training set per learner is small (≈ 2N/K on average).
   - *Cons:* Quadratic scaling of model count (O(K²)). For K = 20 classes, 20×19/2 = 190 separate classifiers must be trained and stored in memory.

---

### d) Softmax Regression (Multinomial Logistic Regression)
Instead of decomposing into binary models, Softmax directly generalizes logistic regression to K classes:
```
P(y = k | x) = exp( w_kᵀ·x ) / [ ∑ exp( w_jᵀ·x ) ],   for k = 1, 2, ..., K
```
Optimized end-to-end using Categorical Cross-Entropy Loss:
```
Loss(W) = − ∑∑ [ I(y_i = k) · ln( P(y_i = k | x_i) ) ]
```

---

### e) Comprehensive Architectural Comparison Table

| Evaluation Criterion | One-vs-Rest (OvR) | One-vs-One (OvO) | Softmax Regression |
| :--- | :--- | :--- | :--- |
| **Number of Classifiers** | Exactly K | K(K−1)/2 (Quadratic) | Single unified model (K weight vectors) |
| **Training Set Size per Model** | Full dataset N | Small subset ≈ 2N/K | Full dataset N |
| **Susceptibility to Imbalance** | High (1 : K−1) | Balanced (Pairwise equal) | Handled natively via softmax denominator |
| **Inference Time** | Fast (O(K)) | Slow (O(K²)) | Extremely fast (Single matrix multiplication) |
| **Preferred Base Learner** | Logistic Regression, Neural Nets | Support Vector Machines (SVM) | Multinomial Deep Networks |

---
---

## Q11. Principal Component Analysis (PCA) & Singular Value Decomposition (SVD) [10 Marks]
*(Appeared in: Dec 2022 Q6b [10M], May 2023 Q6b [10M], Dec 2023 Q6b [10M], Dec 2024 Q5a [10M], May 2025 Q6b [10M])*

### a) The Curse of Dimensionality & Need for Dimensionality Reduction
As feature dimensionality D increases:
1. **Volume Explosion & Data Sparsity:** The volume of the hypercube grows exponentially (V = s^D). Available data points become isolated islands; to maintain uniform sample density, sample size must scale exponentially (N ∝ e^D).
2. **Distance Metric Collapse:** In high dimensions, the ratio between the distance to the nearest neighbor and the farthest neighbor approaches 1. Euclidean distance becomes completely non-discriminative.
3. **Overfitting:** High feature-to-sample ratios allow algorithms to find spurious chance correlations.

---

### b) PCA Mathematical Foundations & Covariance Derivation
**PCA** is an orthogonal linear transformation that projects continuous data from R^D to a lower-dimensional subspace R^d (d << D) while **maximizing retained variance**:

#### Step 1: Centering Data
Compute the empirical sample mean vector and center the data matrix X (size N × D):
```
μ = (1/N) · ∑ x_i
X_c = X − 1 · μᵀ
```

#### Step 2: Sample Covariance Matrix (Σ)
```
Σ = [ 1 / (N − 1) ] · X_cᵀ · X_c
```
Where diagonal entries Σ_jj = Var(X_j) and off-diagonals Σ_jk = Cov(X_j, X_k).

#### Step 3: Maximizing Projected Variance via Rayleigh Quotient
Projecting a sample onto unit direction u (uᵀ·u = 1):
```
Var(uᵀ·X_c) = uᵀ · Σ · u
```
Formulating the constrained Lagrangian:
```
L(u, λ) = uᵀ·Σ·u − λ·(uᵀ·u − 1)
∂L / ∂u = 2·Σ·u − 2·λ·u = 0  -->  Σ·u = λ·u
```
*Conclusion:* The optimal projection directions u are the **eigenvectors** of covariance matrix Σ, and the projected variance equals the corresponding **eigenvalues** λ.

#### Step 4: Component Selection & Explained Variance Ratio
Sort eigenvalues descending: λ₁ ≥ λ₂ ≥ ... ≥ λ_D.
Retain top d eigenvectors forming projection matrix W_d = [ u₁, u₂, ..., u_d ] (size D × d).
```
Cumulative Explained Variance = [ ∑ λ_k (for k=1 to d) ] / [ ∑ λ_j (for j=1 to D) ] ≥ 0.95 (95% Threshold)
```
Projected low-dimensional representation:
```
Z = X_c · W_d   (size N × d)
```

---

### c) Solved Numerical: Singular Value Decomposition (SVD) Matrix Decomposition
*(Appeared in: May 2023 Paper, Question 6(b) [10 Marks])*

#### Problem Statement:
Decompose the matrix A = [ [3, 1], [1, 3] ] using Singular Value Decomposition:
```
A = U · Σ · Vᵀ
```

#### Step 1: Compute Aᵀ·A
```
Aᵀ·A = [ 3, 1 ] · [ 3, 1 ] = [ 9+1, 3+3 ] = [ 10,  6 ]
       [ 1, 3 ]   [ 1, 3 ]   [ 3+3, 1+9 ]   [  6, 10 ]
```

#### Step 2: Compute Eigenvalues of Aᵀ·A
Characteristic equation: det(Aᵀ·A − λ·I) = 0
```
det [ 10−λ,   6   ] = (10 − λ)² − 36 = 0
    [   6,  10−λ  ]

(10 − λ)² = 36  -->  10 − λ = ±6
λ₁ = 10 + 6 = 16
λ₂ = 10 − 6 = 4

Singular values (square roots of eigenvalues):
σ₁ = √16 = 4
σ₂ = √4  = 2

Diagonal Singular Matrix Σ:
Σ = [ 4, 0 ]
    [ 0, 2 ]
```

#### Step 3: Compute Right Singular Vectors (V)
- For λ₁ = 16:
  ```
  [ 10−16,   6   ] · [ v₁₁ ] = [ −6,  6 ] · [ v₁₁ ] = [ 0 ]  -->  v₁₁ = v₂₁
  [   6,   10−16 ]   [ v₂₁ ]   [  6, −6 ]   [ v₂₁ ]   [ 0 ]
  Normalized: v₁ = [ 1/√2, 1/√2 ]ᵀ
  ```
- For λ₂ = 4:
  ```
  [ 10−4,   6  ] · [ v₁₂ ] = [ 6, 6 ] · [ v₁₂ ] = [ 0 ]  -->  v₁₂ = −v₂₂
  [  6,   10−4 ]   [ v₂₂ ]   [ 6, 6 ]   [ v₂₂ ]   [ 0 ]
  Normalized: v₂ = [ 1/√2, −1/√2 ]ᵀ
  ```
```
V = [ 1/√2,  1/√2 ]
    [ 1/√2, −1/√2 ]

Vᵀ = [ 1/√2,  1/√2 ]
     [ 1/√2, −1/√2 ]
```

#### Step 4: Compute Left Singular Vectors (U)
Using u_i = (1 / σ_i) · A · v_i:
```
u₁ = (1/4) · [ 3, 1 ] · [ 1/√2 ] = (1/4) · [ 4/√2 ] = [ 1/√2 ]
             [ 1, 3 ]   [ 1/√2 ]           [ 4/√2 ]   [ 1/√2 ]

u₂ = (1/2) · [ 3, 1 ] · [  1/√2 ] = (1/2) · [  2/√2 ] = [  1/√2 ]
             [ 1, 3 ]   [ −1/√2 ]           [ −2/√2 ]   [ −1/√2 ]

U = [ 1/√2,  1/√2 ]
    [ 1/√2, −1/√2 ]
```

#### Final SVD Factorization:
```
A = U · Σ · Vᵀ
  = [ 1/√2,  1/√2 ] · [ 4, 0 ] · [ 1/√2,  1/√2 ]
    [ 1/√2, −1/√2 ]   [ 0, 2 ]   [ 1/√2, −1/√2 ]
```

---
---

## Q12. Graph-Based Clustering: Minimum Spanning Tree (MST) Algorithm [10 Marks]
*(Appeared in: Dec 2023 Q2a [10M], May 2024 Q4a [10M], Dec 2024 Q2a [10M], May 2025 Q5b [10M])*

### a) Graph-Theoretic Clustering Foundations
**MST Clustering** is an unsupervised graph-partitioning technique that treats data samples as vertices V in a fully connected weighted undirected graph G = (V, E), where edge weights w_ij = ||x_i − x_j|| represent pairwise Euclidean distances.
By computing the Minimum Spanning Tree and strategically severing **inconsistent edges**, the graph naturally separates into K connected components representing distinct clusters.

```
+---------------------------------------------------------------------------------------------------+
|                                  MST GRAPH-BASED CLUSTERING WORKFLOW                              |
+---------------------------------------------------------------------------------------------------+
|  1. FULLY CONNECTED GRAPH G:          2. MINIMUM SPANNING TREE (MST):                             |
|       (A)-----(B)                          (A)-----(B)                                            |
|        | \   / |                            |                                                     |
|        |  \ /  |            ===>            |        (INCONSISTENT LONG EDGE)                     |
|        |   X   |                            |               |                                     |
|        |  / \  |                           (C)             === [CUT EDGE]                         |
|       (C)-----(D)                                           |                                     |
|                                                            (D)-----(E)                            |
|                                                                                                   |
|  3. SEVER INCONSISTENT EDGES:         4. RESULTING 2 CLUSTERS:                                    |
|       (A)-----(B)                          CLUSTER 1: {A, B, C}                                   |
|        |                                                                                          |
|       (C)          (D)-----(E)             CLUSTER 2: {D, E}                                      |
+---------------------------------------------------------------------------------------------------+
```

---

### b) Step-by-Step MST Clustering Algorithm
1. **Distance Graph Construction:** Compute pairwise distance matrix D_ij = ||x_i − x_j|| across all N points.
2. **MST Construction:** Use **Kruskal's Algorithm** (sorting edges ascending and adding them avoiding cycles via Disjoint-Set Union) or **Prim's Algorithm** to generate the tree containing N−1 edges with minimal total weight.
3. **Inconsistent Edge Detection:**
   An edge e is declared inconsistent if its weight significantly exceeds the weights of adjacent edges:
   - *Global Criterion:* Remove the K − 1 edges with the largest absolute weights in the entire MST to produce exactly K clusters.
   - *Local Statistical Criterion:* Compute the mean μ_e and standard deviation σ_e of edge weights within depth d of edge e. If weight w_e > μ_e + k·σ_e, sever the edge.
4. **Cluster Extraction:** Each disconnected subgraph forms an individual cluster.

---
---

## Q13. Model-Based Clustering: Expectation-Maximization (EM) Algorithm for Gaussian Mixture Models (GMM) [10 Marks]
*(Appeared in: Dec 2022 Q5b [10M], May 2023 Q5b [10M], Nov 2025 Q6b [10M])*

### a) Gaussian Mixture Models Formulation
While K-Means performs **hard assignment** (each point belongs exclusively to one cluster) and assumes spherical variance, a **Gaussian Mixture Model (GMM)** is a probabilistic generative model performing **soft assignment**.
The overall data distribution is modeled as a weighted superposition of K multivariate Gaussian component densities:
```
P(x) = ∑ [ π_k · N(x | μ_k, Σ_k) ]   (summed for k = 1 to K)
```
Where:
- **π_k** is the mixing coefficient for cluster k (0 ≤ π_k ≤ 1 and ∑ π_k = 1).
- **μ_k** is the D-dimensional mean vector of cluster k.
- **Σ_k** is the D × D covariance matrix defining cluster dispersion and elliptical orientation.
- **N(x | μ_k, Σ_k)** is the multivariate Gaussian probability density function:
  ```
  N(x | μ_k, Σ_k) = [ 1 / ( (2π)^(D/2) · |Σ_k|^(1/2) ) ] · exp[ −(1/2) · (x − μ_k)ᵀ · (Σ_k)⁻¹ · (x − μ_k) ]
  ```

---

### b) The Expectation-Maximization (EM) Algorithmic Workflow

```
+---------------------------------------------------------------------------------------------------+
|                                 THE EM ALGORITHM ITERATIVE CYCLE                                  |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|     +------------------------- INITIALIZATION --------------------------+                         |
|     | Initialize μ_k (via K-Means), Σ_k (Sample Cov), π_k = 1/K         |                         |
|     +-------------------------------------------------------------------+                         |
|                                       |                                                           |
|                                       v                                                           |
|     +------------------------- 1. E-STEP (EXPECTATION) -----------------+                         |
|     | Compute soft responsibilities γ_ik using current parameters:      |                         |
|     | γ_ik = P(z_ik = 1 | x_i)                                          |                         |
|     +-------------------------------------------------------------------+                         |
|                                       |                                                           |
|                                       v                                                           |
|     +------------------------- 2. M-STEP (MAXIMIZATION) -----------------+                         |
|     | Update parameters using weighted responsibilities:                |                         |
|     | N_k = ∑ γ_ik                                                      |                         |
|     | μ_k_new = (1/N_k) · ∑ (γ_ik · x_i)                                |                         |
|     | Σ_k_new = (1/N_k) · ∑ [ γ_ik · (x_i − μ_k)(x_i − μ_k)ᵀ ]          |                         |
|     | π_k_new = N_k / N                                                 |                         |
|     +-------------------------------------------------------------------+                         |
|                                       |                                                           |
|                                       v                                                           |
|     +------------------------- CONVERGENCE CHECK -----------------------+                         |
|     | Has log-likelihood change |Δ ln L| < ε?                           |                         |
|     | - NO: Loop back to E-Step                                         |                         |
|     | - YES: Terminate & output optimal soft cluster assignments        |                         |
|     +-------------------------------------------------------------------+                         |
|                                                                                                   |
+---------------------------------------------------------------------------------------------------+
```

#### Step 1: E-Step (Expectation)
Using Bayes' rule, compute the **posterior responsibility** γ_ik that Gaussian component k generated observation x_i:
```
γ_ik = [ π_k · N(x_i | μ_k, Σ_k) ] / [ ∑ π_j · N(x_i | μ_j, Σ_j) ]
```

#### Step 2: M-Step (Maximization)
Re-estimate parameters using the soft responsibilities computed in the E-step:
```
Effective points in cluster k:  N_k = ∑ γ_ik   (summed over all i = 1 to N)

Updated Mean Centroid:          μ_k_new = (1/N_k) · ∑ (γ_ik · x_i)

Updated Covariance Matrix:      Σ_k_new = (1/N_k) · ∑ [ γ_ik · (x_i − μ_k_new)(x_i − μ_k_new)ᵀ ]

Updated Mixing Coefficient:     π_k_new = N_k / N
```

#### Monotonic Convergence Guarantee:
Jensen's inequality mathematically guarantees that the incomplete data log-likelihood ln P(X) increases monotonically at every EM iteration until reaching a local optimum:
```
ln P(X | θ^(t+1)) ≥ ln P(X | θ^(t))
```

---
---

## Q14. Distance & Similarity Metrics in Machine Learning [5–10 Marks]
*(Appeared in: Nov 2025 Q1a [5M] & Core Metric Theory)*

### a) Mathematical Axioms of a Valid Metric Distance
For a distance function d(x, y) across space X, four mathematical axioms must hold:
1. **Non-Negativity:** d(x, y) ≥ 0, for all x, y
2. **Identity of Indiscernibles:** d(x, y) = 0  <-->  x = y
3. **Symmetry:** d(x, y) = d(y, x), for all x, y
4. **Triangle Inequality:** d(x, z) ≤ d(x, y) + d(y, z), for all x, y, z

---

### b) Metric Taxonomy & Mathematical Formulations

```
+---------------------------------------------------------------------------------------------------+
|                                 DISTANCE METRIC GEOMETRIC ISO-CONTOURS                            |
+---------------------------------------------------------------------------------------------------+
|  1. MANHATTAN (L1 Norm)               2. EUCLIDEAN (L2 Norm)              3. CHEBYSHEV (L∞)       |
|         |    /\    |                         |   .---.   |                       |  +-----+  |    |
|         |   /  \   |                         |  /     \  |                       |  |     |  |    |
|         |  /    \  |                         | |   +   | |                       |  |  +  |  |    |
|         |  \    /  |                         |  \     /  |                       |  |     |  |    |
|         |   \  /   |                         |   '---'   |                       |  +-----+  |    |
|         |    \/    |                         |           |                       |           |    |
|         (Diamond Contour)                     (Circle Contour)                    (Square Contour)|
+---------------------------------------------------------------------------------------------------+
```

1. **Euclidean Distance (L₂ Norm):**
   ```
   d_Euc(x, y) = ||x − y||₂ = √[ ∑ (x_i − y_i)² ]
   ```
   - *Physical Meaning:* Straight-line geometric ruler distance.
   - *Best Used For:* Low-dimensional, isotropic, dense continuous features.
2. **Manhattan Distance (L₁ Norm / City Block / Taxicab):**
   ```
   d_Man(x, y) = ||x − y||₁ = ∑ |x_i − y_i|
   ```
   - *Physical Meaning:* Grid movement along orthogonal coordinate axes.
   - *Best Used For:* High-dimensional spaces; robust against outliers compared to L₂.
3. **Minkowski Distance (L_p Generalization):**
   ```
   d_Mink(x, y) = ||x − y||_p = [ ∑ |x_i − y_i|^p ]^(1/p)
   ```
   - When p = 1  --> Manhattan; when p = 2  --> Euclidean; when p  --> ∞  --> Chebyshev d_∞ = max_i |x_i − y_i|.
4. **Cosine Similarity & Cosine Distance:**
   ```
   Cosine Similarity = (x · y) / ( ||x||₂ · ||y||₂ ) = [ ∑ x_i·y_i ] / [ √∑(x_i²) · √∑(y_i²) ]
   Cosine Distance   = 1 − Cosine Similarity
   ```
   - *Physical Meaning:* Evaluates the cosine of the angle between two vectors, completely invariant to absolute magnitude/length.
   - *Best Used For:* Sparse high-dimensional text vectors (TF-IDF, word embeddings).
5. **Mahalanobis Distance:**
   *(Explicitly tested in Nov 2025 Q1a [5 Marks])*
   Measures distance relative to the centroid of a probability distribution, incorporating the covariance matrix Σ:
   ```
   D_M(x, y) = √[ (x − y)ᵀ · Σ⁻¹ · (x − y) ]
   ```
   - *Advantage:* Automatically scales axes by standard deviations and decorrelates features. If Σ = I (identity matrix), Mahalanobis collapses exactly to Euclidean distance.

---
---

## Q15. Model Validation, Resampling Strategies & Bias-Variance Decomposition [10 Marks]
*(Appeared in: Dec 2023 Q3b [10M], May 2024 Q1e [5M], Nov 2025 Q4a [10M] & Core Evaluation Theory)*

### a) Generalization Error & The Bias-Variance Decomposition
For regression model y = f(x) + ε with noise ε ~ N(0, σ²), the expected test Mean Squared Error decomposes into three mutually exclusive components:
```
E[ (y − f̂(x))² ] = ( Bias[f̂(x)] )² + Var[f̂(x)] + σ²
```
Where:
- **Bias[f̂(x)] = E[f̂(x)] − f(x):** Error stemming from erroneous simplifying assumptions in the learning algorithm (Underfitting).
- **Var[f̂(x)] = E[ (f̂(x) − E[f̂(x)])² ]:** Error resulting from sensitivity to small fluctuations in the training dataset (Overfitting).
- **σ²:** Irreducible noise in the true underlying data-generating process.

```
       Error ^
             |
             |       \               Total Generalization Error              /
             |        \                    (Bias² + Variance)               /
             |         \                      /-----------\                /
             |          \                    /             \              /
             |           \                  /               \            /
             |            \                /                 \          /
             |             \              /                   \        /
             |              \------------/                     \------/
             |               Bias²                               Variance
             |                                             
             |------------------------------------------------------------- Irreducible Error (σ²)
             +------------------------------------------------------------> Model Complexity
             Underfitting (High Bias)     Optimal Capacity     Overfitting (High Variance)
```

---

### b) Resampling & Cross-Validation Strategies

```
+---------------------------------------------------------------------------------------------------+
|                                  5-FOLD CROSS VALIDATION WORKFLOW                                 |
+---------------------------------------------------------------------------------------------------+
|  Iteration 1: [ TEST ] [ TRAIN ] [ TRAIN ] [ TRAIN ] [ TRAIN ]  --> Score 1                       |
|  Iteration 2: [ TRAIN ] [ TEST ] [ TRAIN ] [ TRAIN ] [ TRAIN ]  --> Score 2                       |
|  Iteration 3: [ TRAIN ] [ TRAIN ] [ TEST ] [ TRAIN ] [ TRAIN ]  --> Score 3                       |
|  Iteration 4: [ TRAIN ] [ TRAIN ] [ TRAIN ] [ TEST ] [ TRAIN ]  --> Score 4                       |
|  Iteration 5: [ TRAIN ] [ TRAIN ] [ TRAIN ] [ TRAIN ] [ TEST ]  --> Score 5                       |
|                                                                                                   |
|  FINAL CROSS-VALIDATION PERFORMANCE = Mean(Score 1, Score 2, Score 3, Score 4, Score 5)           |
+---------------------------------------------------------------------------------------------------+
```

1. **Holdout Validation:** Splits data into fixed Train (70%), Validation (15%), and Test (15%) partitions.
   - *Limitation:* High variance depending on which samples fall into the test split.
2. **K-Fold Cross-Validation:** Partitions dataset D into K equal mutually exclusive folds. Trains K models, each using K−1 folds for training and 1 fold for validation. Final score is the mean performance across all K runs. Typically K = 5 or K = 10.
3. **Stratified K-Fold Cross-Validation:**
   - Essential for imbalanced classification tasks. Enforces that each fold maintains the exact same class percentage ratio as the original global population.
4. **Leave-One-Out Cross-Validation (LOOCV):**
   - Extreme case where K = N. In each iteration, N−1 samples train the model and exactly 1 single sample tests it.
   - *Pros:* Unbiased estimate of generalization error.
   - *Cons:* Computationally prohibitive for large N (O(N) full retraining cycles).
