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
While **PCA** is unsupervised and searches for directions of maximum total variance (ignoring class labels), **LDA** finds a projection subspace $\mathbf{w}$ that maximizes the separation between distinct class distributions while minimizing the variance within each class.

```
+---------------------------------------------------------------------------------------------------+
|                                     PCA VS LDA PROJECTION OBJECTIVE                               |
+---------------------------------------------------------------------------------------------------+
|  x_2 ^                                                                                            |
|      |        (Class 1: O)              (Class 2: X)                                              |
|      |           O  O  O                   X  X  X                                                |
|      |         O   O  O  O               X   X  X  X                                              |
|      |            O  O  O                   X  X  X                                               |
|      |                  \                         /                                               |
|      |                   \  PCA Projection Axis  /  LDA Projection Axis                           |
|      |                    \ (Max Overall Var)   /   (Max Class Separation)                        |
|      |                     \                   /                                                  |
|      +----------------------\-----------------/---------------------------> x_1                   |
|                              v               v                                                    |
|                   Overlapping Classes   Distinct Separated Classes                                |
+---------------------------------------------------------------------------------------------------+
```

---

### b) Mathematical Formulation: Scatter Matrices
For a binary classification task with classes $C_1$ and $C_2$:
- Class means in input space:
  $$\mathbf{\mu}_1 = \frac{1}{N_1} \sum_{\mathbf{x} \in C_1} \mathbf{x}, \quad \mathbf{\mu}_2 = \frac{1}{N_2} \sum_{\mathbf{x} \in C_2} \mathbf{x}$$
- **Between-Class Scatter Matrix ($S_B$):** Measures the distance between class centroids:
  $$S_B = (\mathbf{\mu}_1 - \mathbf{\mu}_2)(\mathbf{\mu}_1 - \mathbf{\mu}_2)^T$$
- **Within-Class Scatter Matrix ($S_W$):** Measures the internal dispersion within each individual class:
  $$S_1 = \sum_{\mathbf{x} \in C_1} (\mathbf{x} - \mathbf{\mu}_1)(\mathbf{x} - \mathbf{\mu}_1)^T, \quad S_2 = \sum_{\mathbf{x} \in C_2} (\mathbf{x} - \mathbf{\mu}_2)(\mathbf{x} - \mathbf{\mu}_2)^T$$
  $$S_W = S_1 + S_2$$

---

### c) Derivation of Fisher's Linear Discriminant
Fisher's objective function maximizes the ratio of between-class variance to within-class variance in the projected 1D space $y = \mathbf{w}^T \mathbf{x}$:
$$J(\mathbf{w}) = \frac{(\tilde{\mu}_1 - \tilde{\mu}_2)^2}{\tilde{s}_1^2 + \tilde{s}_2^2} = \frac{\mathbf{w}^T S_B \mathbf{w}}{\mathbf{w}^T S_W \mathbf{w}}$$

To maximize $J(\mathbf{w})$, take the gradient with respect to $\mathbf{w}$ and equate to zero:
$$\frac{\partial J}{\partial \mathbf{w}} = \frac{2 S_B \mathbf{w} (\mathbf{w}^T S_W \mathbf{w}) - 2 S_W \mathbf{w} (\mathbf{w}^T S_B \mathbf{w})}{(\mathbf{w}^T S_W \mathbf{w})^2} = 0$$
Dividing by $2(\mathbf{w}^T S_W \mathbf{w})$:
$$S_B \mathbf{w} - \left( \frac{\mathbf{w}^T S_B \mathbf{w}}{\mathbf{w}^T S_W \mathbf{w}} \right) S_W \mathbf{w} = 0$$
Since $\frac{\mathbf{w}^T S_B \mathbf{w}}{\mathbf{w}^T S_W \mathbf{w}} = J(\mathbf{w}) = \lambda$ (a scalar):
$$S_B \mathbf{w} = \lambda S_W \mathbf{w} \implies S_W^{-1} S_B \mathbf{w} = \lambda \mathbf{w}$$
This is a generalized eigenvalue problem. Notice that $S_B \mathbf{w} = (\mathbf{\mu}_1 - \mathbf{\mu}_2)(\mathbf{\mu}_1 - \mathbf{\mu}_2)^T \mathbf{w}$.
Since $(\mathbf{\mu}_1 - \mathbf{\mu}_2)^T \mathbf{w}$ is a scalar factor, $S_B \mathbf{w}$ is always in the direction of $(\mathbf{\mu}_1 - \mathbf{\mu}_2)$.
Therefore, the optimal projection vector direction is:
$$\mathbf{w}^* = S_W^{-1} (\mathbf{\mu}_1 - \mathbf{\mu}_2)$$

---

### d) Solved Numerical 1 (Dec 2022): 2-Class 2D LDA Optimal Projection Matrix
*(Appeared in: December 2022 Paper, Question 5(a) [10 Marks])*

#### Problem Statement:
Given two classes with two features $x_1$ and $x_2$:
- **Class 1 ($C_1$):** $(1, 2), (2, 3), (3, 3), (4, 5), (5, 5)$
- **Class 2 ($C_2$):** $(4, 2), (5, 0), (5, 2), (3, 2), (5, 3), (6, 3)$
Find the optimal projection vector $\mathbf{w}^*$ and the decision boundary threshold.

#### Step 1: Compute Class Means
$$N_1 = 5, \quad N_2 = 6$$
$$\mathbf{\mu}_1 = \frac{1}{5} \begin{bmatrix} 1 + 2 + 3 + 4 + 5 \\ 2 + 3 + 3 + 5 + 5 \end{bmatrix} = \frac{1}{5} \begin{bmatrix} 15 \\ 18 \end{bmatrix} = \begin{bmatrix} 3.0 \\ 3.6 \end{bmatrix}$$
$$\mathbf{\mu}_2 = \frac{1}{6} \begin{bmatrix} 4 + 5 + 5 + 3 + 5 + 6 \\ 2 + 0 + 2 + 2 + 3 + 3 \end{bmatrix} = \frac{1}{6} \begin{bmatrix} 28 \\ 12 \end{bmatrix} = \begin{bmatrix} 4.667 \\ 2.0 \end{bmatrix}$$
Difference vector:
$$\mathbf{\mu}_1 - \mathbf{\mu}_2 = \begin{bmatrix} 3.0 - 4.667 \\ 3.6 - 2.0 \end{bmatrix} = \begin{bmatrix} -1.667 \\ 1.6 \end{bmatrix}$$

#### Step 2: Compute Scatter Matrices $S_1$ and $S_2$
Center the data for $C_1$:
$$\mathbf{x}_i - \mathbf{\mu}_1: \begin{bmatrix} -2 & -1.6 \\ -1 & -0.6 \\ 0 & -0.6 \\ 1 & 1.4 \\ 2 & 1.4 \end{bmatrix}$$
$$S_1 = \sum (\mathbf{x} - \mathbf{\mu}_1)(\mathbf{x} - \mathbf{\mu}_1)^T = \begin{bmatrix} 4+1+0+1+4 & 3.2+0.6+0+1.4+2.8 \\ 3.2+0.6+0+1.4+2.8 & 2.56+0.36+0.36+1.96+1.96 \end{bmatrix} = \begin{bmatrix} 10.0 & 8.0 \\ 8.0 & 7.2 \end{bmatrix}$$

Center the data for $C_2$:
$$\mathbf{x}_i - \mathbf{\mu}_2: \begin{bmatrix} -0.667 & 0 \\ 0.333 & -2.0 \\ 0.333 & 0 \\ -1.667 & 0 \\ 0.333 & 1.0 \\ 1.333 & 1.0 \end{bmatrix}$$
$$S_2 = \begin{bmatrix} 5.333 & 0.667 \\ 0.667 & 6.0 \end{bmatrix}$$

#### Step 3: Compute Within-Class Scatter Matrix $S_W$ and its Inverse
$$S_W = S_1 + S_2 = \begin{bmatrix} 10.0 + 5.333 & 8.0 + 0.667 \\ 8.0 + 0.667 & 7.2 + 6.0 \end{bmatrix} = \begin{bmatrix} 15.333 & 8.667 \\ 8.667 & 13.200 \end{bmatrix}$$
Determinant:
$$\det(S_W) = (15.333)(13.200) - (8.667)^2 = 202.3956 - 75.1169 = \mathbf{127.2787}$$
Inverse $S_W^{-1}$:
$$S_W^{-1} = \frac{1}{127.2787} \begin{bmatrix} 13.200 & -8.667 \\ -8.667 & 15.333 \end{bmatrix} = \begin{bmatrix} 0.1037 & -0.0681 \\ -0.0681 & 0.1205 \end{bmatrix}$$

#### Step 4: Compute Optimal Projection Vector $\mathbf{w}^*$
$$\mathbf{w}^* = S_W^{-1} (\mathbf{\mu}_1 - \mathbf{\mu}_2) = \begin{bmatrix} 0.1037 & -0.0681 \\ -0.0681 & 0.1205 \end{bmatrix} \begin{bmatrix} -1.667 \\ 1.600 \end{bmatrix}$$
$$w_1 = (0.1037)(-1.667) + (-0.0681)(1.600) = -0.1729 - 0.1090 = \mathbf{-0.2819}$$
$$w_2 = (-0.0681)(-1.667) + (0.1205)(1.600) = 0.1135 + 0.1928 = \mathbf{0.3063}$$
$$\mathbf{w}^* = \begin{bmatrix} -0.2819 \\ 0.3063 \end{bmatrix}$$

#### Step 5: Decision Boundary Threshold ($w_0$)
Projected class centroids:
$$\tilde{\mu}_1 = \mathbf{w}^{*T} \mathbf{\mu}_1 = (-0.2819)(3.0) + (0.3063)(3.6) = -0.8457 + 1.1027 = \mathbf{0.2570}$$
$$\tilde{\mu}_2 = \mathbf{w}^{*T} \mathbf{\mu}_2 = (-0.2819)(4.667) + (0.3063)(2.0) = -1.3156 + 0.6126 = \mathbf{-0.7030}$$
Optimal separating threshold:
$$w_0 = \frac{\tilde{\mu}_1 + \tilde{\mu}_2}{2} = \frac{0.2570 + (-0.7030)}{2} = \frac{-0.4460}{2} = \mathbf{-0.2230}$$
Classification Rule: If $\mathbf{w}^{*T} \mathbf{x} \ge -0.2230 \implies \text{Class } 1$, else $\text{Class } 2$.

---
---

## Q9. Logistic Regression: Sigmoid Hypothesis, Odds Ratio, Log-Loss Cost Function & Gradient Descent [10 Marks]
*(Appeared in: Dec 2022 Q1e [5M], May 2023 Q1e [5M], Dec 2023 Q1d [5M], Dec 2024 Q1c [5M]/Q2b [10M], May 2025 Q1e [5M], Nov 2025 Q6c [10M])*

### a) Sigmoid Activation & Hypothesis Function
Logistic Regression models the posterior probability of a binary categorical label $y \in \{0, 1\}$ by mapping a linear combination of features through the non-linear **Standard Sigmoid (Logistic)** function:
$$z = \mathbf{w}^T \mathbf{x} + b$$
$$h_{\mathbf{w}}(\mathbf{x}) = \sigma(z) = \frac{1}{1 + e^{-z}} = \frac{1}{1 + e^{-(\mathbf{w}^T \mathbf{x} + b)}}$$

```
                \sigma(z) ^
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
1. **Range:** Maps $\mathbb{R} \to (0, 1)$, matching valid probability axioms: $P(y = 1 \mid \mathbf{x}) = h_{\mathbf{w}}(\mathbf{x})$.
2. **Derivative Property:** The derivative expresses cleanly in terms of the function itself:
   $$\sigma'(z) = \frac{d}{dz} \left( \frac{1}{1 + e^{-z}} \right) = \frac{e^{-z}}{(1 + e^{-z})^2} = \sigma(z)(1 - \sigma(z))$$

---

### b) Odds Ratio & Logit (Log-Odds) Formulation
The **Odds** of an event is the ratio of probability of occurrence to probability of non-occurrence:
$$\mathrm{Odds} = \frac{P}{1 - P} = \frac{\frac{1}{1 + e^{-z}}}{1 - \frac{1}{1 + e^{-z}}} = \frac{\frac{1}{1 + e^{-z}}}{\frac{e^{-z}}{1 + e^{-z}}} = \frac{1}{e^{-z}} = e^z$$
Taking the natural logarithm yields the **Logit (Log-Odds)** function:
$$\ln(\mathrm{Odds}) = \ln\left( \frac{P}{1 - P} \right) = \ln(e^z) = z = \mathbf{w}^T \mathbf{x} + b$$
*Interpretation:* While probability is bounded in $(0, 1)$, the log-odds is completely linear and unbounded across $(-\infty, +\infty)$, establishing a clean linear decision boundary at $z = 0 \iff P = 0.5$.

---

### c) Cost Function: Cross-Entropy (Log-Loss)
If we use Mean Squared Error (MSE) for Logistic Regression, the resulting loss surface is non-convex with numerous sub-optimal local minima.
To guarantee a convex optimization surface with a unique global minimum, we derive the **Binary Cross-Entropy (Log-Loss)** using Maximum Likelihood Estimation:
$$P(y \mid \mathbf{x}) = [h_{\mathbf{w}}(\mathbf{x})]^y [1 - h_{\mathbf{w}}(\mathbf{x})]^{1 - y}$$
Likelihood for $N$ independent training samples:
$$L(\mathbf{w}) = \prod_{i=1}^N [h_{\mathbf{w}}(\mathbf{x}_i)]^{y_i} [1 - h_{\mathbf{w}}(\mathbf{x}_i)]^{1 - y_i}$$
Taking the negative log-likelihood and normalizing by $N$:
$$J(\mathbf{w}) = -\frac{1}{N} \ln L(\mathbf{w}) = -\frac{1}{N} \sum_{i=1}^N \left[ y_i \ln(h_{\mathbf{w}}(\mathbf{x}_i)) + (1 - y_i) \ln(1 - h_{\mathbf{w}}(\mathbf{x}_i)) \right]$$

---

### d) Gradient Descent Parameter Update Derivation
Computing the partial derivative with respect to weight $w_j$:
$$\frac{\partial J}{\partial w_j} = -\frac{1}{N} \sum_{i=1}^N \left[ \frac{y_i}{h_i} \frac{\partial h_i}{\partial z_i} \frac{\partial z_i}{\partial w_j} - \frac{1 - y_i}{1 - h_i} \frac{\partial h_i}{\partial z_i} \frac{\partial z_i}{\partial w_j} \right]$$
Since $\frac{\partial h_i}{\partial z_i} = h_i(1 - h_i)$ and $\frac{\partial z_i}{\partial w_j} = x_{ij}$:
$$\frac{\partial J}{\partial w_j} = -\frac{1}{N} \sum_{i=1}^N \left[ \frac{y_i}{h_i} h_i(1 - h_i) x_{ij} - \frac{1 - y_i}{1 - h_i} h_i(1 - h_i) x_{ij} \right]$$
$$\frac{\partial J}{\partial w_j} = -\frac{1}{N} \sum_{i=1}^N \left[ y_i (1 - h_i) - (1 - y_i) h_i \right] x_{ij} = -\frac{1}{N} \sum_{i=1}^N [y_i - y_i h_i - h_i + y_i h_i] x_{ij}$$
$$\mathbf{\frac{\partial J}{\partial w_j} = \frac{1}{N} \sum_{i=1}^N (h_{\mathbf{w}}(\mathbf{x}_i) - y_i) x_{ij}}$$
The batch gradient descent parameter update rule with learning rate $\alpha$ is:
$$\mathbf{w_j \leftarrow w_j - \alpha \frac{1}{N} \sum_{i=1}^N (\hat{y}_i - y_i) x_{ij}}$$

---
---

## Q10. Multiclass Classification Architectures: One-vs-Rest (OvR), One-vs-One (OvO) & Softmax [10 Marks]
*(Appeared in: Dec 2022 Q3b [10M], May 2023 Q5a [10M], Dec 2023 Q6a [10M], May 2025 Q5a [10M], Nov 2025 Q5a [10M])*

### a) Decomposing Multi-Class Problems
Standard binary classifiers (Logistic Regression, Hard/Soft Margin SVM) naturally output binary decisions ($\{-1, +1\}$ or $\{0, 1\}$). When classifying $K > 2$ discrete classes, two primary architectural decomposition heuristics are utilized:

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
1. **Model Training:** Constructs exactly $K$ distinct binary classifiers $f_1, f_2, \dots, f_K$. For classifier $k$, instances of class $k$ serve as positive examples ($+1$), while all remaining samples from classes $j \ne k$ are pooled into the negative class ($-1$).
2. **Inference Decision Rule:** Evaluates confidence scores across all $K$ models; assigns sample $\mathbf{x}$ to the class with maximum confidence score:
   $$\hat{y} = \arg\max_{k \in \{1, \dots, K\}} f_k(\mathbf{x})$$
3. **Key Trade-Offs:**
   - *Pros:* Computational efficiency; requires only $K$ trained classifiers.
   - *Cons:* Severe class imbalance during training (1 positive vs $K-1$ pooled negatives); uncalibrated confidence scale disparities between different models.

---

### c) One-vs-One (OvO / Pairwise Classification)
1. **Model Training:** Constructs a dedicated binary classifier for every distinct pair of classes:
   $$\text{Total Classifiers} = \binom{K}{2} = \frac{K(K - 1)}{2}$$
   Each classifier $f_{ij}$ is trained strictly on the subset of data belonging to classes $i$ and $j$ (ignoring all other classes).
2. **Inference Decision Rule (Majority Voting):** Test instance $\mathbf{x}$ is evaluated by all $\frac{K(K-1)}{2}$ classifiers. Each classifier casts a vote for its predicted winner. The class receiving the highest cumulative vote tally wins.
3. **Key Trade-Offs:**
   - *Pros:* No class imbalance per classifier; training set per learner is small ($2N/K$ on average).
   - *Cons:* Quadratic scaling of model count ($\mathcal{O}(K^2)$). For $K = 20$ classes, $\frac{20 \times 19}{2} = 190$ separate classifiers must be trained and stored in memory.

---

### d) Softmax Regression (Multinomial Logistic Regression)
Instead of decomposing into binary models, Softmax directly generalizes logistic regression to $K$ classes:
$$P(y = k \mid \mathbf{x}) = \frac{e^{\mathbf{w}_k^T \mathbf{x}}}{\sum_{j=1}^K e^{\mathbf{w}_j^T \mathbf{x}}}, \quad k = 1, \dots, K$$
Optimized end-to-end using Categorical Cross-Entropy Loss:
$$\mathcal{L}(\mathbf{W}) = -\sum_{i=1}^N \sum_{k=1}^K \mathbb{I}(y_i = k) \ln\left( \frac{e^{\mathbf{w}_k^T \mathbf{x}_i}}{\sum_{j=1}^K e^{\mathbf{w}_j^T \mathbf{x}_i}} \right)$$

---

### e) Comprehensive Architectural Comparison Table

| Evaluation Criterion | One-vs-Rest (OvR) | One-vs-One (OvO) | Softmax Regression |
| :--- | :--- | :--- | :--- |
| **Number of Classifiers** | Exactly $K$ | $\frac{K(K-1)}{2}$ (Quadratic) | Single unified model ($K$ weight vectors) |
| **Training Set Size per Model** | Full dataset $N$ | Small subset $\approx \frac{2N}{K}$ | Full dataset $N$ |
| **Susceptibility to Imbalance** | High ($1 : K-1$) | Balanced (Pairwise equal) | Handled natively via softmax denominator |
| **Inference Time** | Fast ($\mathcal{O}(K)$) | Slow ($\mathcal{O}(K^2)$) | Extremely fast (Single matrix multiplication) |
| **Preferred Base Learner** | Logistic Regression, Neural Nets | Support Vector Machines (SVM) | Multinomial Deep Networks |

---
---

## Q11. Principal Component Analysis (PCA) & Singular Value Decomposition (SVD) [10 Marks]
*(Appeared in: Dec 2022 Q6b [10M], May 2023 Q6b [10M], Dec 2023 Q6b [10M], Dec 2024 Q5a [10M], May 2025 Q6b [10M])*

### a) The Curse of Dimensionality & Need for Dimensionality Reduction
As feature dimensionality $D$ increases:
1. **Volume Explosion & Data Sparsity:** The volume of the hypercube grows exponentially ($V = s^D$). Available data points become isolated islands; to maintain uniform sample density, sample size must scale exponentially ($N \propto e^D$).
2. **Distance Metric Collapse:** In high dimensions, the ratio between the distance to the nearest neighbor and the farthest neighbor approaches 1:
   $$\lim_{D \to \infty} \frac{\mathrm{dist}_{\max} - \mathrm{dist}_{\min}}{\mathrm{dist}_{\min}} = 0$$
   Euclidean distance becomes completely non-discriminative.
3. **Overfitting:** High feature-to-sample ratios allow algorithms to find spurious chance correlations.

---

### b) PCA Mathematical Foundations & Covariance Derivation
**PCA** is an orthogonal linear transformation that projects continuous data from $\mathbb{R}^D$ to a lower-dimensional subspace $\mathbb{R}^d$ ($d \ll D$) while **maximizing retained variance**:

#### Step 1: Centering Data
Compute the empirical sample mean vector and center the data matrix $X \in \mathbb{R}^{N \times D}$:
$$\mathbf{\mu} = \frac{1}{N} \sum_{i=1}^N \mathbf{x}_i, \quad X_c = X - \mathbf{1} \mathbf{\mu}^T$$

#### Step 2: Sample Covariance Matrix ($\Sigma$)
$$\Sigma = \frac{1}{N-1} X_c^T X_c \in \mathbb{R}^{D \times D}$$
Where diagonal entries $\Sigma_{jj} = \mathrm{Var}(X_j)$ and off-diagonals $\Sigma_{jk} = \mathrm{Cov}(X_j, X_k)$.

#### Step 3: Maximizing Projected Variance via Rayleigh Quotient
Projecting a sample onto unit direction $\mathbf{u}$ ($\mathbf{u}^T \mathbf{u} = 1$):
$$\mathrm{Var}(\mathbf{u}^T X_c) = \frac{1}{N-1} \sum_{i=1}^N (\mathbf{u}^T \mathbf{x}_{c,i})^2 = \mathbf{u}^T \left( \frac{1}{N-1} X_c^T X_c \right) \mathbf{u} = \mathbf{u}^T \Sigma \mathbf{u}$$
Formulating the constrained Lagrangian:
$$\mathcal{L}(\mathbf{u}, \lambda) = \mathbf{u}^T \Sigma \mathbf{u} - \lambda (\mathbf{u}^T \mathbf{u} - 1)$$
Taking partial derivative with respect to $\mathbf{u}$:
$$\frac{\partial \mathcal{L}}{\partial \mathbf{u}} = 2 \Sigma \mathbf{u} - 2 \lambda \mathbf{u} = 0 \implies \mathbf{\Sigma \mathbf{u} = \lambda \mathbf{u}}$$
*Conclusion:* The optimal projection directions $\mathbf{u}$ are the **eigenvectors** of covariance matrix $\Sigma$, and the projected variance equals the corresponding **eigenvalues** $\lambda$.

#### Step 4: Component Selection & Explained Variance Ratio
Sort eigenvalues descending: $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_D$.
Retain top $d$ eigenvectors forming projection matrix $W_d = [\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_d] \in \mathbb{R}^{D \times d}$.
$$\text{Cumulative Explained Variance Ratio} = \frac{\sum_{k=1}^d \lambda_k}{\sum_{j=1}^D \lambda_j} \ge 0.95 \quad (95\% \text{ Threshold})$$
Projected low-dimensional representation:
$$Z = X_c W_d \in \mathbb{R}^{N \times d}$$

---

### c) Solved Numerical: Singular Value Decomposition (SVD) Matrix Decomposition
*(Appeared in: May 2023 Paper, Question 6(b) [10 Marks])*

#### Problem Statement:
Decompose the matrix $A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}$ using Singular Value Decomposition ($A = U \Sigma V^T$).

#### Step 1: Compute $A^T A$
$$A^T A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix} = \begin{bmatrix} 9+1 & 3+3 \\ 3+3 & 1+9 \end{bmatrix} = \begin{bmatrix} 10 & 6 \\ 6 & 10 \end{bmatrix}$$

#### Step 2: Compute Eigenvalues of $A^T A$
Characteristic equation: $\det(A^T A - \lambda I) = 0$
$$\det \begin{bmatrix} 10 - \lambda & 6 \\ 6 & 10 - \lambda \end{bmatrix} = (10 - \lambda)^2 - 36 = 0$$
$$(10 - \lambda)^2 = 36 \implies 10 - \lambda = \pm 6$$
$$\lambda_1 = 10 + 6 = \mathbf{16}, \quad \lambda_2 = 10 - 6 = \mathbf{4}$$
Singular values:
$$\sigma_1 = \sqrt{\lambda_1} = \sqrt{16} = \mathbf{4}, \quad \sigma_2 = \sqrt{\lambda_2} = \sqrt{4} = \mathbf{2}$$
$$\Sigma = \begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix}$$

#### Step 3: Compute Right Singular Vectors ($V$)
- For $\lambda_1 = 16$:
  $$\begin{bmatrix} 10-16 & 6 \\ 6 & 10-16 \end{bmatrix} \begin{bmatrix} v_{11} \\ v_{21} \end{bmatrix} = \begin{bmatrix} -6 & 6 \\ 6 & -6 \end{bmatrix} \begin{bmatrix} v_{11} \\ v_{21} \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies v_{11} = v_{21}$$
  Normalized: $\mathbf{v}_1 = \begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix}$
- For $\lambda_2 = 4$:
  $$\begin{bmatrix} 10-4 & 6 \\ 6 & 10-4 \end{bmatrix} \begin{bmatrix} v_{12} \\ v_{22} \end{bmatrix} = \begin{bmatrix} 6 & 6 \\ 6 & 6 \end{bmatrix} \begin{bmatrix} v_{12} \\ v_{22} \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies v_{12} = -v_{22}$$
  Normalized: $\mathbf{v}_2 = \begin{bmatrix} 1/\sqrt{2} \\ -1/\sqrt{2} \end{bmatrix}$
$$V = \begin{bmatrix} 1/\sqrt{2} & 1/\sqrt{2} \\ 1/\sqrt{2} & -1/\sqrt{2} \end{bmatrix}, \quad V^T = \begin{bmatrix} 1/\sqrt{2} & 1/\sqrt{2} \\ 1/\sqrt{2} & -1/\sqrt{2} \end{bmatrix}$$

#### Step 4: Compute Left Singular Vectors ($U$)
Using $\mathbf{u}_i = \frac{1}{\sigma_i} A \mathbf{v}_i$:
$$\mathbf{u}_1 = \frac{1}{4} \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix} = \frac{1}{4} \begin{bmatrix} 4/\sqrt{2} \\ 4/\sqrt{2} \end{bmatrix} = \begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix}$$
$$\mathbf{u}_2 = \frac{1}{2} \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} 1/\sqrt{2} \\ -1/\sqrt{2} \end{bmatrix} = \frac{1}{2} \begin{bmatrix} 2/\sqrt{2} \\ -2/\sqrt{2} \end{bmatrix} = \begin{bmatrix} 1/\sqrt{2} \\ -1/\sqrt{2} \end{bmatrix}$$
$$U = \begin{bmatrix} 1/\sqrt{2} & 1/\sqrt{2} \\ 1/\sqrt{2} & -1/\sqrt{2} \end{bmatrix}$$

#### Final SVD Factorization:
$$\mathbf{A = U \Sigma V^T = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix} \begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}}$$

---
---

## Q12. Graph-Based Clustering: Minimum Spanning Tree (MST) Algorithm [10 Marks]
*(Appeared in: Dec 2023 Q2a [10M], May 2024 Q4a [10M], Dec 2024 Q2a [10M], May 2025 Q5b [10M])*

### a) Graph-Theoretic Clustering Foundations
**MST Clustering** is an unsupervised graph-partitioning technique that treats data samples as vertices $V$ in a fully connected weighted undirected graph $G = (V, E)$, where edge weights $w_{ij} = \|\mathbf{x}_i - \mathbf{x}_j\|$ represent pairwise Euclidean distances.
By computing the Minimum Spanning Tree and strategically severing **inconsistent edges**, the graph naturally separates into $K$ connected components representing distinct clusters.

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
1. **Distance Graph Construction:** Compute pairwise distance matrix $D_{ij} = \|\mathbf{x}_i - \mathbf{x}_j\|_2$ across all $N$ points.
2. **MST Construction:** Use **Kruskal's Algorithm** (sorting edges ascending and adding them avoiding cycles via Disjoint-Set Union) or **Prim's Algorithm** to generate the tree containing $N-1$ edges with minimal total weight:
   $$\min \sum_{e \in T} w(e)$$
3. **Inconsistent Edge Detection:**
   An edge $e$ is declared inconsistent if its weight significantly exceeds the weights of adjacent edges:
   - *Global Criterion:* Remove the $K - 1$ edges with the largest absolute weights in the entire MST to produce exactly $K$ clusters.
   - *Local Statistical Criterion:* Compute the mean $\mu_e$ and standard deviation $\sigma_e$ of edge weights within depth $d$ of edge $e$. If $w_e > \mu_e + k \sigma_e$, sever the edge.
4. **Cluster Extraction:** Each disconnected subgraph forms an individual cluster.

---

### c) Advantages & Limitations of MST Clustering
- **Advantages:**
  - Capable of identifying non-spherical clusters of arbitrary geometric topologies.
  - Zero requirement to assume spherical cluster centroids or equal cluster sizes.
  - Insensitive to point ordering.
- **Limitations:**
  - Highly sensitive to noise points acting as bridges between distinct clusters (the chaining effect).
  - Construction of dense distance graph requires $\mathcal{O}(N^2)$ memory and time.

---
---

## Q13. Model-Based Clustering: Expectation-Maximization (EM) Algorithm for Gaussian Mixture Models (GMM) [10 Marks]
*(Appeared in: Dec 2022 Q5b [10M], May 2023 Q5b [10M], Nov 2025 Q6b [10M])*

### a) Gaussian Mixture Models Formulation
While K-Means performs **hard assignment** (each point belongs exclusively to one cluster) and assumes spherical variance, a **Gaussian Mixture Model (GMM)** is a probabilistic generative model performing **soft assignment**.
The overall data distribution is modeled as a weighted superposition of $K$ multivariate Gaussian component densities:
$$P(\mathbf{x}) = \sum_{k=1}^K \pi_k \mathcal{N}(\mathbf{x} \mid \mathbf{\mu}_k, \Sigma_k)$$
Where:
- $\pi_k$ is the mixing coefficient for cluster $k$ ($0 \le \pi_k \le 1$ and $\sum_{k=1}^K \pi_k = 1$).
- $\mathbf{\mu}_k$ is the $D$-dimensional mean vector of cluster $k$.
- $\Sigma_k$ is the $D \times D$ covariance matrix defining cluster dispersion and elliptical orientation.
- The multivariate Gaussian probability density function is:
  $$\mathcal{N}(\mathbf{x} \mid \mathbf{\mu}_k, \Sigma_k) = \frac{1}{(2\pi)^{D/2} |\Sigma_k|^{1/2}} \exp\left( -\frac{1}{2} (\mathbf{x} - \mathbf{\mu}_k)^T \Sigma_k^{-1} (\mathbf{x} - \mathbf{\mu}_k) \right)$$

---

### b) The Expectation-Maximization (EM) Algorithmic Workflow
Direct maximum likelihood estimation of GMM parameters via gradient descent is analytically intractable due to the summation inside the logarithm:
$$\ln P(X \mid \mathbf{\pi}, \mathbf{\mu}, \Sigma) = \sum_{i=1}^N \ln \left( \sum_{k=1}^K \pi_k \mathcal{N}(\mathbf{x}_i \mid \mathbf{\mu}_k, \Sigma_k) \right)$$
The **EM algorithm** resolves this by introducing a latent binary indicator variable $\mathbf{z}_i \in \{0, 1\}^K$:

```
+---------------------------------------------------------------------------------------------------+
|                                 THE EM ALGORITHM ITERATIVE CYCLE                                  |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|     +------------------------- INITIALIZATION --------------------------+                         |
|     | Initialize \mu_k (via K-Means), \Sigma_k (Sample Cov), \pi_k = 1/K |                         |
|     +-------------------------------------------------------------------+                         |
|                                       |                                                           |
|                                       v                                                           |
|     +------------------------- 1. E-STEP (EXPECTATION) -----------------+                         |
|     | Compute soft responsibilities \gamma_{ik} using current parameters:   |                         |
|     | \gamma_{ik} = P(z_{ik} = 1 | x_i)                                 |                         |
|     +-------------------------------------------------------------------+                         |
|                                       |                                                           |
|                                       v                                                           |
|     +------------------------- 2. M-STEP (MAXIMIZATION) -----------------+                         |
|     | Update parameters using weighted responsibilities:                |                         |
|     | N_k = \sum \gamma_{ik}                                            |                         |
|     | \mu_k^{new} = (1/N_k) \sum \gamma_{ik} x_i                         |                         |
|     | \Sigma_k^{new} = (1/N_k) \sum \gamma_{ik} (x_i-\mu_k)(x_i-\mu_k)^T|                         |
|     | \pi_k^{new} = N_k / N                                             |                         |
|     +-------------------------------------------------------------------+                         |
|                                       |                                                           |
|                                       v                                                           |
|     +------------------------- CONVERGENCE CHECK -----------------------+                         |
|     | Has log-likelihood change |\Delta \ln L| < \epsilon?                |                         |
|     | - NO: Loop back to E-Step                                         |                         |
|     | - YES: Terminate & output optimal soft cluster assignments        |                         |
|     +-------------------------------------------------------------------+                         |
|                                                                                                   |
+---------------------------------------------------------------------------------------------------+
```

#### Step 1: E-Step (Expectation)
Using Bayes' rule, compute the **posterior responsibility** $\gamma_{ik}$ that Gaussian component $k$ generated observation $\mathbf{x}_i$:
$$\mathbf{\gamma_{ik} = \frac{\pi_k \mathcal{N}(\mathbf{x}_i \mid \mathbf{\mu}_k, \Sigma_k)}{\sum_{j=1}^K \pi_j \mathcal{N}(\mathbf{x}_i \mid \mathbf{\mu}_j, \Sigma_j)}}$$

#### Step 2: M-Step (Maximization)
Re-estimate parameters using the soft responsibilities computed in the E-step:
- Effective number of points assigned to cluster $k$:
  $$N_k = \sum_{i=1}^N \gamma_{ik}$$
- Updated Mean Centroid:
  $$\mathbf{\mu}_k^{\mathrm{new}} = \frac{1}{N_k} \sum_{i=1}^N \gamma_{ik} \mathbf{x}_i$$
- Updated Covariance Matrix:
  $$\Sigma_k^{\mathrm{new}} = \frac{1}{N_k} \sum_{i=1}^N \gamma_{ik} (\mathbf{x}_i - \mathbf{\mu}_k^{\mathrm{new}})(\mathbf{x}_i - \mathbf{\mu}_k^{\mathrm{new}})^T$$
- Updated Mixing Coefficient:
  $$\pi_k^{\mathrm{new}} = \frac{N_k}{N}$$

#### Monotonic Convergence Guarantee:
Jensen's inequality mathematically guarantees that the incomplete data log-likelihood $\ln P(X)$ increases monotonically at every EM iteration until reaching a local optimum:
$$\ln P(X \mid \theta^{(t+1)}) \ge \ln P(X \mid \theta^{(t)})$$

---
---

## Q14. Distance & Similarity Metrics in Machine Learning [5–10 Marks]
*(Appeared in: Nov 2025 Q1a [5M] & Core Metric Theory)*

### a) Mathematical Axioms of a Valid Metric Distance
For a distance function $d(\mathbf{x}, \mathbf{y})$ across space $\mathcal{X}$, four mathematical axioms must hold:
1. **Non-Negativity:** $d(\mathbf{x}, \mathbf{y}) \ge 0, \quad \forall \mathbf{x}, \mathbf{y}$
2. **Identity of Indiscernibles:** $d(\mathbf{x}, \mathbf{y}) = 0 \iff \mathbf{x} = \mathbf{y}$
3. **Symmetry:** $d(\mathbf{x}, \mathbf{y}) = d(\mathbf{y}, \mathbf{x}), \quad \forall \mathbf{x}, \mathbf{y}$
4. **Triangle Inequality:** $d(\mathbf{x}, \mathbf{z}) \le d(\mathbf{x}, \mathbf{y}) + d(\mathbf{y}, \mathbf{z}), \quad \forall \mathbf{x}, \mathbf{y}, \mathbf{z}$

---

### b) Metric Taxonomy & Mathematical Formulations

```
+---------------------------------------------------------------------------------------------------+
|                                 DISTANCE METRIC GEOMETRIC ISO-CONTOURS                            |
+---------------------------------------------------------------------------------------------------+
|  1. MANHATTAN (L1 Norm)               2. EUCLIDEAN (L2 Norm)              3. CHEBYSHEV (L\infty)  |
|         |    /\    |                         |   .---.   |                       |  +-----+  |    |
|         |   /  \   |                         |  /     \  |                       |  |     |  |    |
|         |  /    \  |                         | |   +   | |                       |  |  +  |  |    |
|         |  \    /  |                         |  \     /  |                       |  |     |  |    |
|         |   \  /   |                         |   '---'   |                       |  +-----+  |    |
|         |    \/    |                         |           |                       |           |    |
|         (Diamond Contour)                     (Circle Contour)                    (Square Contour)|
+---------------------------------------------------------------------------------------------------+
```

1. **Euclidean Distance ($L_2$ Norm):**
   $$d_{\mathrm{Euc}}(\mathbf{x}, \mathbf{y}) = \|\mathbf{x} - \mathbf{y}\|_2 = \sqrt{\sum_{i=1}^D (x_i - y_i)^2}$$
   - *Physical Meaning:* Straight-line geometric ruler distance.
   - *Best Used For:* Low-dimensional, isotropic, dense continuous features.
2. **Manhattan Distance ($L_1$ Norm / City Block / Taxicab):**
   $$d_{\mathrm{Man}}(\mathbf{x}, \mathbf{y}) = \|\mathbf{x} - \mathbf{y}\|_1 = \sum_{i=1}^D |x_i - y_i|$$
   - *Physical Meaning:* Grid movement along orthogonal coordinate axes.
   - *Best Used For:* High-dimensional spaces; robust against outliers compared to $L_2$.
3. **Minkowski Distance ($L_p$ Generalization):**
   $$d_{\mathrm{Mink}}(\mathbf{x}, \mathbf{y}) = \|\mathbf{x} - \mathbf{y}\|_p = \left( \sum_{i=1}^D |x_i - y_i|^p \right)^{1/p}$$
   - When $p = 1 \implies$ Manhattan; when $p = 2 \implies$ Euclidean; when $p \to \infty \implies$ Chebyshev $d_\infty = \max_i |x_i - y_i|$.
4. **Cosine Similarity & Cosine Distance:**
   $$S_{\mathrm{Cos}}(\mathbf{x}, \mathbf{y}) = \frac{\mathbf{x} \cdot \mathbf{y}}{\|\mathbf{x}\|_2 \|\mathbf{y}\|_2} = \frac{\sum x_i y_i}{\sqrt{\sum x_i^2}\sqrt{\sum y_i^2}}$$
   $$d_{\mathrm{Cos}}(\mathbf{x}, \mathbf{y}) = 1 - S_{\mathrm{Cos}}(\mathbf{x}, \mathbf{y})$$
   - *Physical Meaning:* Evaluates the cosine of the angle between two vectors, completely invariant to absolute magnitude/length.
   - *Best Used For:* Sparse high-dimensional text vectors (TF-IDF, word embeddings).
5. **Mahalanobis Distance:**
   *(Explicitly tested in Nov 2025 Q1a [5 Marks])*
   Measures distance relative to the centroid of a probability distribution, incorporating the covariance matrix $\Sigma$:
   $$D_{\mathrm{M}}(\mathbf{x}, \mathbf{y}) = \sqrt{(\mathbf{x} - \mathbf{y})^T \Sigma^{-1} (\mathbf{x} - \mathbf{y})}$$
   - *Advantage:* Automatically scales axes by standard deviations and decorrelates features. If $\Sigma = I$ (identity), Mahalanobis collapses exactly to Euclidean distance.

---
---

## Q15. Model Validation, Resampling Strategies & Bias-Variance Decomposition [10 Marks]
*(Appeared in: Dec 2023 Q3b [10M], May 2024 Q1e [5M], Nov 2025 Q4a [10M] & Core Evaluation Theory)*

### a) Generalization Error & The Bias-Variance Decomposition
For regression model $y = f(\mathbf{x}) + \epsilon$ with noise $\epsilon \sim \mathcal{N}(0, \sigma^2)$, the expected test Mean Squared Error decomposes into three mutually exclusive components:
$$\mathbb{E}[(y - \hat{f}(\mathbf{x}))^2] = (\operatorname{Bias}[\hat{f}(\mathbf{x})])^2 + \operatorname{Var}[\hat{f}(\mathbf{x})] + \sigma^2$$
Where:
- **$\operatorname{Bias}[\hat{f}(\mathbf{x})] = \mathbb{E}[\hat{f}(\mathbf{x})] - f(\mathbf{x})$:** Error stemming from erroneous simplifying assumptions in the learning algorithm (Underfitting).
- **$\operatorname{Var}[\hat{f}(\mathbf{x})] = \mathbb{E}[(\hat{f}(\mathbf{x}) - \mathbb{E}[\hat{f}(\mathbf{x})])^2]$:** Error resulting from sensitivity to small fluctuations in the training dataset (Overfitting).
- **$\sigma^2$:** Irreducible noise in the true underlying data-generating process.

```
       Error ^
             |
             |       \               Total Generalization Error              /
             |        \                    (Bias^2 + Variance)              /
             |         \                      /-----------\                /
             |          \                    /             \              /
             |           \                  /               \            /
             |            \                /                 \          /
             |             \              /                   \        /
             |              \------------/                     \------/
             |               Bias^2                               Variance
             |                                             
             |------------------------------------------------------------- Irreducible Error (\sigma^2)
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

1. **Holdout Validation:** Splits data into fixed Train ($70\%$), Validation ($15\%$), and Test ($15\%$) partitions.
   - *Limitation:* High variance depending on which samples fall into the test split.
2. **K-Fold Cross-Validation:** Partitions dataset $D$ into $K$ equal mutually exclusive folds. Trains $K$ models, each using $K-1$ folds for training and 1 fold for validation. Final score is the mean performance across all $K$ runs.
   - Typically $K = 5$ or $K = 10$.
3. **Stratified K-Fold Cross-Validation:**
   - Essential for imbalanced classification tasks. Enforces that each fold maintains the exact same class percentage ratio as the original global population.
4. **Leave-One-Out Cross-Validation (LOOCV):**
   - Extreme case where $K = N$. In each iteration, $N-1$ samples train the model and exactly 1 single sample tests it.
   - *Pros:* Unbiased estimate of generalization error.
   - *Cons:* Computationally prohibitive for large $N$ ($\mathcal{O}(N)$ full retraining cycles).
