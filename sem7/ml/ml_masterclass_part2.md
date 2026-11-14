# Mumbai University (MU) Semester 7 — Machine Learning (ML)
## Masterclass Part 2: Modules 4, 5 & 6 (SVM, Multiclass, Clustering & Dimensionality Reduction)
**Course Code:** Department Level Optional Course (DLOC) | **Scheme:** Rev 2019 / C-Scheme | **Applicable Cycles:** Dec 2022 – May 2025

---

# MODULE 4: LEARNING WITH CLASSIFICATION (SVM & MULTICLASS)

---

## 4.1 Support Vector Machines (SVM): Geometric Intuition & Concepts
*(Appeared in: Dec 2022 Q1c [5M], Dec 2023 Q1d/Q4a [10M], May 2024 Q6a [10M], Dec 2024 Q6b [10M], May 2025 Q1c [5M])*

A Support Vector Machine (Vapnik, 1995) is a maximum-margin linear or non-linear classifier based on Structural Risk Minimization from statistical learning theory.

```
+---------------------------------------------------------------------------------------------------+
|                                 SVM OPTIMAL DECISION BOUNDARY & MARGIN                            |
+---------------------------------------------------------------------------------------------------+
|  x_2                                                                                              |
|   ^                                                                                               |
|   |                  Positive Margin Hyperplane: w^T x + b = +1                                   |
|   |                  .......................................                                      |
|   |                     (+)                                                                       |
|   |                 (+)       (+) [Support Vector]                                                |
|   |                             \                                                                 |
|   |          Optimal Decision    \  <--- Distance = 1 / ||w||                                     |
|   |          Hyperplane:          \                                                               |
|   |          w^T x + b = 0  =======================================                               |
|   |                               /                                                               |
|   |                              /  <--- Distance = 1 / ||w||                                     |
|   |                             /                                                                 |
|   |                            (-) [Support Vector]                                               |
|   |                   (-)                                                                         |
|   |                  .......................................                                      |
|   |                  Negative Margin Hyperplane: w^T x + b = -1                                   |
|   |                                                                                               |
|   |                  <-------------- Total Margin gamma = 2 / ||w|| -------------->               |
|   +-----------------------------------------------------------------------------> x_1             |
+---------------------------------------------------------------------------------------------------+
```

### Essential Terminology:
1. **Decision Hyperplane:** An affine subspace of dimension $d-1$ dividing $d$-dimensional space into two half-spaces:
   $$w^T x + b = 0$$
   where $w$ is the normal weight vector and $b$ is the scalar bias.
2. **Support Vectors:** The critical training data points that lie directly on the boundary margins ($w^T x_i + b = \pm 1$). Removing all other training points leaves the decision boundary unchanged; moving a support vector alters the entire boundary.
3. **Geometric Margin ($\gamma$):** The perpendicular distance between the positive margin ($w^T x + b = +1$) and negative margin ($w^T x + b = -1$):
   $$\gamma = \frac{(w^T x_+ + b) - (w^T x_- + b)}{\|w\|} = \frac{1 - (-1)}{\|w\|} = \mathbf{\frac{2}{\|w\|}}$$

### 🌟 Significance of the Optimal Separating Hyperplane [5 Marks] — Nov'25 (Q1c)
**Question:** *"What is the significance of optimal separating hyper plane in SVM?"*

1. **Maximum Margin Guarantee ($\frac{2}{\|w\|} \to \max$):**
   - Among the infinite possible hyperplanes that can linearly separate two classes, the optimal hyperplane is the **unique** plane that maximizes the minimum perpendicular distance to the closest training points of each class.
2. **Minimization of Generalization Error (Vapnik-Chervonenkis Bound):**
   - Statistical Learning Theory proves that the upper bound on expected risk $R(h) \le R_{\text{emp}}(h) + \mathcal{O}\left(\sqrt{\frac{h_{\text{VC}}}{N}}\right)$.
   - Larger geometric margins directly minimize the **VC Dimension** ($h_{\text{VC}} \le \min\left(d, \frac{R^2}{\gamma^2}\right) + 1$). By maximizing $\gamma$, SVM minimizes model complexity and provably prevents overfitting.
3. **Convex Quadratic Optimization (Zero Local Minima):**
   - The formulation $\min \frac{1}{2}\|w\|^2$ subject to linear constraints forms a strictly convex objective function. It guarantees a **globally unique optimum**—unlike neural networks which trap in suboptimal local minima.
4. **Sparsity & Noise Robustness (Support Vector Property):**
   - The optimal plane depends solely on the small subset of boundary points (Support Vectors). Points lying outside the margins can be removed or perturbed without shifting the decision boundary, providing natural immunity against non-boundary noise.

---

## 4.2 SVM as a Constrained Optimization Problem (Primal to Dual Derivation)
*(Appeared in: Dec 2023 Q4a [10M], Dec 2024 Q6b [10M])*

### 1. Primal Problem Formulation (Hard Margin)
To maximize the margin $\gamma = \frac{2}{\|w\|}$, we minimize its reciprocal $\frac{1}{2}\|w\|^2$.
Every training point $(x_i, y_i)$ with $y_i \in \{-1, +1\}$ must lie on the correct side of its margin:
$$w^T x_i + b \ge +1 \quad \text{for } y_i = +1$$
$$w^T x_i + b \le -1 \quad \text{for } y_i = -1$$
Combined compact constraint:
$$y_i (w^T x_i + b) \ge 1, \quad \forall i = 1, \ldots, N$$

$$\mathbf{\min_{w, b} \frac{1}{2} \|w\|^2 \quad \text{subject to} \quad y_i (w^T x_i + b) - 1 \ge 0, \quad \forall i = 1, \ldots, N}$$

---

### 2. The Lagrangian Formulation
We introduce Lagrange multipliers $\alpha_i \ge 0$ for each inequality constraint:
$$\mathcal{L}_P(w, b, \alpha) = \frac{1}{2} \|w\|^2 - \sum_{i=1}^N \alpha_i \left[ y_i (w^T x_i + b) - 1 \right]$$

To find the saddle point, take partial derivatives with respect to primal variables $w$ and $b$ and set to zero:
$$\frac{\partial \mathcal{L}_P}{\partial w} = w - \sum_{i=1}^N \alpha_i y_i x_i = 0 \implies \mathbf{w = \sum_{i=1}^N \alpha_i y_i x_i} \quad \text{--- (Condition 1)}$$
$$\frac{\partial \mathcal{L}_P}{\partial b} = - \sum_{i=1}^N \alpha_i y_i = 0 \implies \mathbf{\sum_{i=1}^N \alpha_i y_i = 0} \quad \text{--- (Condition 2)}$$

---

### 3. The Wolfe Dual Problem
Substitute Condition 1 and Condition 2 back into the primal Lagrangian $\mathcal{L}_P$:
$$\mathcal{L}_D(\alpha) = \frac{1}{2} \left( \sum_{i=1}^N \alpha_i y_i x_i \right)^T \left( \sum_{j=1}^N \alpha_j y_j x_j \right) - \sum_{i=1}^N \alpha_i y_i \left( \sum_{j=1}^N \alpha_j y_j x_j \right)^T x_i - b \underbrace{\sum_{i=1}^N \alpha_i y_i}_{=0} + \sum_{i=1}^N \alpha_i$$
$$= \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N \alpha_i \alpha_j y_i y_j (x_i^T x_j) - \sum_{i=1}^N \sum_{j=1}^N \alpha_i \alpha_j y_i y_j (x_i^T x_j) + \sum_{i=1}^N \alpha_i$$

$$\mathbf{\max_{\alpha} \sum_{i=1}^N \alpha_i - \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N \alpha_i \alpha_j y_i y_j (x_i^T x_j)}$$
$$\text{subject to} \quad \alpha_i \ge 0 \quad \forall i, \quad \text{and} \quad \sum_{i=1}^N \alpha_i y_i = 0$$

---

### 4. Karush-Kuhn-Tucker (KKT) Complementarity Conditions
At the optimal solution $(\hat{w}, \hat{b}, \hat{\alpha})$, the KKT conditions require:
$$\alpha_i \left[ y_i (w^T x_i + b) - 1 \right] = 0, \quad \forall i = 1, \ldots, N$$
- **Case 1 ($\alpha_i = 0$):** The point $x_i$ does not lie on the margin ($y_i(w^T x_i + b) > 1$). It contributes nothing to $w = \sum \alpha_i y_i x_i$.
- **Case 2 ($\alpha_i > 0$):** The bracketed term must be exactly zero:
  $$y_i (w^T x_i + b) = 1$$
  **These points are the Support Vectors!**

---

## 4.3 Soft-Margin SVM & The Kernel Trick
*(Appeared in: Dec 2023 Q5a [10M], May 2024 Q6a [10M], Dec 2024 Q6c [10M])*

### 1. Soft-Margin SVM (Non-Separable Case)
To tolerate outliers and noisy training data, introduce **slack variables** $\xi_i \ge 0$:
$$y_i(w^T x_i + b) \ge 1 - \xi_i$$
- $\xi_i = 0$: Point correctly classified outside or on the margin.
- $0 < \xi_i \le 1$: Point correctly classified but inside the margin.
- $\xi_i > 1$: Point misclassified.

#### Primal Soft-Margin Objective:
$$\min_{w, b, \xi} \frac{1}{2} \|w\|^2 + C \sum_{i=1}^N \xi_i \quad \text{subject to} \quad y_i(w^T x_i + b) \ge 1 - \xi_i, \quad \xi_i \ge 0$$
- **Regularization Parameter $C$:**
  - *Large $C$:* High penalty on misclassification. Forces narrow margin (vulnerable to overfitting / high variance).
  - *Small $C$:* Low penalty on misclassification. Produces wider margin with higher error tolerance (risk of underfitting / high bias).
- **Dual Formulation:** Identical to hard-margin dual, with an upper bound (**Box Constraint**) on multipliers:
  $$0 \le \alpha_i \le C, \quad \forall i = 1, \ldots, N$$

---

### 2. The Kernel Trick & Mercer's Theorem
Non-linearly separable data in input space $\mathbb{R}^d$ becomes linearly separable when mapped to a higher-dimensional feature space $\mathcal{H}$ via transformation $\phi(x)$.

Notice that in the Dual formulation, data appears **strictly as inner products**: $x_i^T x_j$.
A **Kernel Function** computes the inner product in high-dimensional feature space directly from low-dimensional inputs **without ever explicitly computing $\phi(x)$**:
$$K(x_i, x_j) = \phi(x_i)^T \phi(x_j)$$

#### Mercer's Theorem Condition:
A function $K(x, z)$ is a valid kernel if and only if for any finite set of points $\{x_1, \ldots, x_n\}$, the resulting Gram matrix $G_{ij} = K(x_i, x_j)$ is **symmetric and positive semi-definite** ($c^T G c \ge 0, \forall c \in \mathbb{R}^n$).

#### Major Kernel Functions:
1. **Linear Kernel:** $K(x, z) = x^T z$
2. **Polynomial Kernel:** $K(x, z) = (x^T z + c)^d$ (degree $d$)
3. **Radial Basis Function (RBF) / Gaussian Kernel:**
   $$K(x, z) = \exp\left( -\gamma \|x - z\|^2 \right) = \exp\left( -\frac{\|x - z\|^2}{2\sigma^2} \right)$$
   *(Maps input data into an infinite-dimensional Hilbert space!)*
4. **Sigmoid / Hyperbolic Tangent Kernel:** $K(x, z) = \tanh(\alpha x^T z + c)$

---

### 🌟 Concrete Worked Example of the Kernel Trick [10 Marks] — Nov'25 (Q3a)
> **Question:** *"Explain kernel functions of SVM along with an example."*

#### 1. Problem: Non-Linear Separability in 2D Space ($\mathbb{R}^2$)
Consider a 2D binary classification problem where positive points form a circular cluster centered at the origin, and negative points surround them in a concentric outer ring:
- Positive class ($+1$): $x_1^2 + x_2^2 \le 1$
- Negative class ($-1$): $x_1^2 + x_2^2 > 1$

No straight 2D line ($w_1 x_1 + w_2 x_2 + b = 0$) can possibly separate these concentric rings!

#### 2. Explicit Non-Linear Feature Mapping ($\phi: \mathbb{R}^2 \to \mathbb{R}^3$)
Define a mapping function that projects each 2D vector $\vec{x} = (x_1, x_2)$ into a 3D feature space:
$$\phi(\vec{x}) = \left( x_1^2, \; \sqrt{2}x_1 x_2, \; x_2^2 \right)^T \in \mathbb{R}^3$$

Let $z_1 = x_1^2$, $z_2 = \sqrt{2}x_1 x_2$, $z_3 = x_2^2$. In this transformed 3D coordinate system, the circular decision boundary becomes a **flat 3D linear plane**:
$$z_1 + z_3 = 1 \iff 1 \cdot z_1 + 0 \cdot z_2 + 1 \cdot z_3 - 1 = 0$$
Which is easily separated by a linear SVM!

#### 3. The Power of the Kernel Function ($K(\vec{x}, \vec{y})$):
Calculating $\phi(\vec{x})$ and $\phi(\vec{y})$ explicitly and then taking their dot product in high-dimensional space requires heavy computational storage and arithmetic.
Instead, evaluate the inner product directly using the **degree-2 homogeneous polynomial kernel**:
$$K(\vec{x}, \vec{y}) = (\vec{x} \cdot \vec{y})^2 = (x_1 y_1 + x_2 y_2)^2$$

Expand algebraically:
$$K(\vec{x}, \vec{y}) = (x_1 y_1 + x_2 y_2)^2 = x_1^2 y_1^2 + 2(x_1 y_1)(x_2 y_2) + x_2^2 y_2^2$$

Now compute the explicit 3D dot product $\phi(\vec{x}) \cdot \phi(\vec{y})$:
$$\phi(\vec{x}) \cdot \phi(\vec{y}) = \begin{bmatrix} x_1^2 \\ \sqrt{2}x_1 x_2 \\ x_2^2 \end{bmatrix} \cdot \begin{bmatrix} y_1^2 \\ \sqrt{2}y_1 y_2 \\ y_2^2 \end{bmatrix} = x_1^2 y_1^2 + 2 x_1 x_2 y_1 y_2 + x_2^2 y_2^2$$

$$\mathbf{K(\vec{x}, \vec{y}) \equiv \phi(\vec{x}) \cdot \phi(\vec{y})}$$

> **Conclusion:** By using the kernel function $K(\vec{x}, \vec{y}) = (\vec{x}^T \vec{y})^2$, we compute the exact inner product in 3D feature space using **only 2D coordinates**, without ever storing or calculating the 3D transformed vectors!

---

## 4.4 Multiclass Classification Strategies
*(Appeared in: Dec 2022 Q3b [10M], May 2023 Q5a [10M], Dec 2023 Q6a [10M], May 2025 Q5a [10M])*

Binary classifiers (such as SVM and Logistic Regression) can be extended to $K$-class problems via two primary decomposition architectures:

```
+---------------------------------------------------------------------------------------------------+
|                                 MULTICLASS CLASSIFICATION STRATEGIES                              |
+---------------------------------------------------------------------------------------------------+
| 1. ONE-VS-REST (ONE-VS-ALL / OvR / OvA):                                                          |
|    - Trains K independent binary classifiers.                                                     |
|    - Classifier k treats Class k as positive (+1) and ALL other K-1 classes as negative (-1).     |
|    - Prediction: x assigned to class with highest continuous confidence score:                     |
|                  y* = argmax_{k=1..K} f_k(x)                                                      |
|    - Total Models: K                                                                              |
|    - Pro: Fast, scalable.                                                                         |
|    - Con: Suffers from severe class imbalance during training (1 positive vs K-1 negatives).      |
+---------------------------------------------------------------------------------------------------+
| 2. ONE-VS-ONE (OvO):                                                                              |
|    - Trains a dedicated binary classifier for EVERY pair of classes (i, j) where i < j.           |
|    - Evaluates data containing ONLY instances belonging to class i and class j.                   |
|    - Prediction: Every classifier casts 1 vote. Instance assigned to class with MOST votes        |
|                  (Majority Voting / Max-Wins rule).                                               |
|    - Total Models: K(K - 1) / 2                                                                   |
|    - Pro: Each classifier trains on a small, perfectly balanced subset.                           |
|    - Con: Model count grows quadratically with K (e.g., K=10 --> 45 models; K=100 --> 4950 models)|
+---------------------------------------------------------------------------------------------------+
```

---

## MU Keyword Checklist: Module 4
- [ ] *Optimal Separating Hyperplane $w^T x + b = 0$, Geometric Margin $\gamma = 2 / \|w\|$*
- [ ] *Support Vectors: Points satisfying $y_i(w^T x_i + b) = 1$*
- [ ] *Primal Formulation $\min \frac{1}{2}\|w\|^2$ subject to $y_i(w^T x_i + b) \ge 1$*
- [ ] *Lagrangian Dual Formulation: $\max \sum \alpha_i - \frac{1}{2}\sum \alpha_i \alpha_j y_i y_j x_i^T x_j$*
- [ ] *KKT Complementarity Condition: $\alpha_i [y_i(w^T x_i + b) - 1] = 0$*
- [ ] *Soft-Margin SVM: Slack Variables $\xi_i$, Box Constraint $0 \le \alpha_i \le C$*
- [ ] *Mercer's Theorem, Kernel Trick $K(x_i, x_j) = \phi(x_i)^T \phi(x_j)$, RBF Gaussian Kernel*
- [ ] *One-vs-Rest (OvR: $K$ models) vs One-vs-One (OvO: $K(K-1)/2$ models, Majority Voting)*

---
---

# MODULE 5: LEARNING WITH CLUSTERING

---

## 5.1 Clustering Distance Metrics
*(Appeared in: Dec 2022 Q1d [5M])*

The fundamental mathematical prerequisite for clustering is measuring pairwise dissimilarity between feature vectors $x, y \in \mathbb{R}^d$:

1. **Euclidean Distance ($L_2$ Norm):**
   $$d_{\text{Euclidean}}(x, y) = \sqrt{\sum_{i=1}^d (x_i - y_i)^2}$$
2. **Manhattan Distance ($L_1$ Norm / City-Block):**
   $$d_{\text{Manhattan}}(x, y) = \sum_{i=1}^d |x_i - y_i|$$
3. **Minkowski Distance ($L_p$ Norm):**
   $$d_{\text{Minkowski}}(x, y) = \left( \sum_{i=1}^d |x_i - y_i|^p \right)^{\frac{1}{p}}$$
   - $p = 1 \implies$ Manhattan Distance.
   - $p = 2 \implies$ Euclidean Distance.
   - $p = \infty \implies$ Chebyshev Distance ($\max_i |x_i - y_i|$).
4. **Cosine Distance (Angle between vectors, ignores magnitude):**
   $$d_{\text{Cosine}}(x, y) = 1 - \frac{x \cdot y}{\|x\| \|y\|} = 1 - \frac{\sum x_i y_i}{\sqrt{\sum x_i^2} \sqrt{\sum y_i^2}}$$
5. **Mahalanobis Distance (Scale-Invariant & Covariance-Aware) [Nov'25 Q1a]:**
   $$d_{\text{Mahalanobis}}(x, y) = \sqrt{(x - y)^T \Sigma^{-1} (x - y)}$$
   - Where $\Sigma$ is the covariance matrix of the dataset.
   - Unlike Euclidean distance which assumes spherical, un-correlated clusters, Mahalanobis distance accounts for statistical correlations and varying variances along different coordinate axes (ellipsoidal cluster contours).
   - If features are completely uncorrelated with unit variance ($\Sigma = I$), Mahalanobis distance simplifies exactly to Euclidean distance.

---

## 5.2 K-Means Clustering & The Elbow Method
*(Appeared in: May 2023 Q1d [5M])*

K-Means is a partitioning algorithm minimizing the **Within-Cluster Sum of Squares (WCSS)**:
$$J = \sum_{k=1}^K \sum_{x_i \in C_k} \|x_i - \mu_k\|^2$$

### Algorithm Steps:
1. Initialize $K$ centroids $\mu_1, \ldots, \mu_K$ randomly (or via K-Means++).
2. **Assignment Step:** Assign each data point $x_i$ to its nearest centroid:
   $$C_k = \{ x_i : \|x_i - \mu_k\|^2 \le \|x_i - \mu_j\|^2, \forall j \ne k \}$$
3. **Update Step:** Recalculate centroids as the center of mass of their assigned points:
   $$\mu_k = \frac{1}{|C_k|} \sum_{x_i \in C_k} x_i$$
4. Repeat Steps 2 and 3 until centroids converge (no reassignment occurs).

---

## 5.3 Graph-Based Clustering: Minimum Spanning Tree (MST) Algorithm
*(Appeared in: Dec 2023 Q2a [10M], May 2024 Q4a [10M], Dec 2024 Q2a [10M], May 2025 Q5b [10M])*

MST Clustering views data points as vertices $V$ in a complete weighted graph $G = (V, E)$, where edge weight $w(u, v)$ is the Euclidean distance between data points $u$ and $v$.

```
+---------------------------------------------------------------------------------------------------+
|                                 MST-BASED CLUSTERING ARCHITECTURE                                 |
+---------------------------------------------------------------------------------------------------+
| Step 1: Compute pairwise Euclidean distance matrix for all N points.                              |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 2: Construct the Minimum Spanning Tree (MST) spanning all N vertices                        |
|         using Kruskal's or Prim's Algorithm (total N - 1 edges, minimum weight sum).             |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 3: To partition the dataset into K clusters:                                                 |
|         Identify and DELETE the K - 1 edges having the LARGEST weights in the MST.                |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 4: The resulting K disconnected connected components form the final K clusters!              |
+---------------------------------------------------------------------------------------------------+
```

### Concrete Walkthrough Example:
Consider 6 points on a line: $A(1), B(2), C(3), D(10), E(11), F(12)$.
- Distances: $AB=1, BC=1, CD=7, DE=1, EF=1$.
- MST consists of edges: $(A, B, 1), (B, C, 1), (C, D, 7), (D, E, 1), (E, F, 1)$.
- To split into $K = 2$ clusters:
  - Delete $K - 1 = 1$ edge with largest weight $\implies$ Delete edge $(C, D)$ with weight $7$.
  - Resulting disconnected components:
    - **Cluster 1:** $\{A, B, C\}$
    - **Cluster 2:** $\{D, E, F\}$

---

## 5.4 Density-Based Spatial Clustering of Applications with Noise (DBSCAN)
*(Appeared in: Dec 2022 Q6c [10M], May 2023 Q6c [10M], Dec 2023 Q6c [10M], May 2024 Q3b [10M], Dec 2024 Q5b [10M], May 2025 Q6c [10M])*

DBSCAN (Ester et al., 1996) clusters dense regions separated by low-density noise without requiring pre-specification of cluster count $K$.

```
+---------------------------------------------------------------------------------------------------+
|                                  DBSCAN POINT CLASSIFICATION                                      |
+---------------------------------------------------------------------------------------------------+
|                                                                                                   |
|                       .   *   .                                                                   |
|                    *    (CORE)   *  <--- Core Point: >= MinPts points within radius Eps           |
|                       .   *   . \                                                                 |
|                                  \ (Distance <= Eps)                                              |
|                                   v                                                               |
|                                (BORDER) <--- Border Point: < MinPts points, but inside            |
|                                   .          Eps-neighborhood of a Core point                     |
|                                                                                                   |
|                                                     (NOISE) <--- Noise Point: Neither Core        |
|                                                                  nor Border (Outlier)             |
+---------------------------------------------------------------------------------------------------+
```

### Core Parameters & Fundamental Definitions:
1. **Hyperparameters:**
   - $\epsilon$ (Epsilon): Maximum distance radius defining neighborhood.
   - $\text{MinPts}$: Minimum number of data points required within $\epsilon$-neighborhood to form a dense region.
2. **Point Classifications:**
   - **Core Point:** Point $p$ whose $\epsilon$-neighborhood contains at least $\text{MinPts}$ points: $|N_\epsilon(p)| \ge \text{MinPts}$.
   - **Border Point:** Point $q$ that is not a Core point ($|N_\epsilon(q)| < \text{MinPts}$), but falls within the $\epsilon$-neighborhood of at least one Core point.
   - **Noise Point:** Any point that is neither a Core point nor a Border point.
3. **Density Connectivity Relations:**
   - **Directly Density-Reachable:** Point $q$ is directly density-reachable from $p$ if $p$ is a Core point and $q \in N_\epsilon(p)$.
   - **Density-Reachable:** Point $q$ is density-reachable from $p$ if there exists a chain of core points $p_1, p_2, \ldots, p_k$ where $p_1 = p, p_k = q$ and each $p_{i+1}$ is directly density-reachable from $p_i$.
   - **Density-Connected:** Points $p$ and $q$ are density-connected if there exists a common intermediate point $o$ such that both $p$ and $q$ are density-reachable from $o$.
4. **Formal Definition of a Cluster:** A maximal set of density-connected points.

---

## 5.5 Expectation-Maximization (EM) Algorithm for Gaussian Mixture Models
*(Appeared in: Dec 2022 Q5b [10M], May 2023 Q5b [10M])*

The EM algorithm performs maximum likelihood estimation when data has latent (unobserved) cluster assignments $Z$.

A **Gaussian Mixture Model (GMM)** models data as a mixture of $K$ multivariate Gaussian components:
$$P(x) = \sum_{k=1}^K \pi_k \mathcal{N}(x \mid \mu_k, \Sigma_k), \quad \sum_{k=1}^K \pi_k = 1$$

### Two-Step Iterative Optimization:
1. **Expectation Step (E-Step):** Compute the posterior probability (responsibility $\gamma_{ik}$) that data point $x_i$ was generated by Gaussian component $k$:
   $$\gamma_{ik} = P(z_i = k \mid x_i) = \frac{\pi_k \mathcal{N}(x_i \mid \mu_k, \Sigma_k)}{\sum_{j=1}^K \pi_j \mathcal{N}(x_i \mid \mu_j, \Sigma_j)}$$
2. **Maximization Step (M-Step):** Re-estimate parameters using the soft responsibility weights:
   $$N_k = \sum_{i=1}^N \gamma_{ik}$$
   $$\mu_k^{\text{new}} = \frac{1}{N_k} \sum_{i=1}^N \gamma_{ik} x_i$$
   $$\Sigma_k^{\text{new}} = \frac{1}{N_k} \sum_{i=1}^N \gamma_{ik} (x_i - \mu_k^{\text{new}})(x_i - \mu_k^{\text{new}})^T$$
   $$\pi_k^{\text{new}} = \frac{N_k}{N}$$
3. Repeat E-step and M-step until log-likelihood converges.

---

## MU Keyword Checklist: Module 5
- [ ] *Euclidean, Manhattan, Minkowski ($L_p$), Cosine Distance Metrics*
- [ ] *K-Means WCSS Objective, Centroid Reassignment, Elbow Method*
- [ ] *Minimum Spanning Tree (MST) Clustering, Complete Graph, Deleting $K-1$ Largest Edges*
- [ ] *DBSCAN: $\epsilon$ (Epsilon), MinPts, Core Point, Border Point, Noise Point*
- [ ] *Directly Density-Reachable, Density-Reachable, Density-Connected*
- [ ] *EM Algorithm for GMM, E-step (Responsibilities $\gamma_{ik}$), M-step (Update $\mu_k, \Sigma_k, \pi_k$)*

---
---

# MODULE 6: DIMENSIONALITY REDUCTION

---

## 6.1 Principal Component Analysis (PCA): Mathematics & Algorithm
*(Appeared in: Dec 2022 Q6b [10M], Dec 2023 Q6b [10M], Dec 2024 Q5a [10M], May 2025 Q6b [10M])*

PCA is an unsupervised linear dimensionality reduction technique that projects high-dimensional data onto orthogonal axes (**principal components**) maximizing variance and minimizing reconstruction error.

```
+---------------------------------------------------------------------------------------------------+
|                                   THE 7 STEPS OF THE PCA ALGORITHM                                |
+---------------------------------------------------------------------------------------------------+
| Step 1: Standardize / Mean-Center the Dataset:                                                    |
|         Subtract feature means so each feature has zero mean: X_c = X - mu                        |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 2: Compute the Sample Covariance Matrix (size d x d):                                        |
|         Sigma = (1 / (N - 1)) * X_c^T * X_c                                                       |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 3: Compute Eigenvalues (lambda) and Eigenvectors (v):                                        |
|         Solve characteristic equation: det(Sigma - lambda * I) = 0                                |
|         For each lambda_i, solve: (Sigma - lambda_i * I) v_i = 0                                  |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 4: Sort Eigenpairs in Descending Order:                                                      |
|         lambda_1 >= lambda_2 >= ... >= lambda_d                                                   |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 5: Compute Explained Variance Ratio:                                                         |
|         EVR_k = (sum_{i=1}^k lambda_i) / (sum_{j=1}^d lambda_j)                                   |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 6: Form Projection Matrix W (size d x k):                                                    |
|         W = [ v_1, v_2, ..., v_k ]  (Columns are top-k orthonormal eigenvectors)                  |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| Step 7: Transform Original Data into Lower-Dimensional Subspace:                                  |
|         Z = X_c * W   (Output size: N x k)                                                        |
+---------------------------------------------------------------------------------------------------+
```

---

## 6.2 SOLVED NUMERICAL 1: Linear Discriminant Analysis (LDA) Projection
*(Appeared in: December 2022 Paper, Question 5(a) [10 Marks])*

### Problem Statement:
Compute the Linear Discriminant projection for the following two-dimensional, two-class dataset:
- **Class 1 ($X_1$):** $\{(9, 1), (7, 4), (7, 7), (7, 8), (4, 9)\}$ ($N_1 = 5$)
- **Class 2 ($X_2$):** $\{(9, 10), (6, 8), (7, 5), (8, 7), (10, 8)\}$ ($N_2 = 5$)

---

### Step 1: Compute Class Mean Vectors $\mu_1$ and $\mu_2$

#### For Class 1 ($X_1$):
$$\mu_{1, x} = \frac{9 + 7 + 7 + 7 + 4}{5} = \frac{34}{5} = \mathbf{6.8}$$
$$\mu_{1, y} = \frac{1 + 4 + 7 + 8 + 9}{5} = \frac{29}{5} = \mathbf{5.8}$$
$$\mathbf{\mu_1 = \begin{bmatrix} 6.8 \\ 5.8 \end{bmatrix}}$$

#### For Class 2 ($X_2$):
$$\mu_{2, x} = \frac{9 + 6 + 7 + 8 + 10}{5} = \frac{40}{5} = \mathbf{8.0}$$
$$\mu_{2, y} = \frac{10 + 8 + 5 + 7 + 8}{5} = \frac{38}{5} = \mathbf{7.6}$$
$$\mathbf{\mu_2 = \begin{bmatrix} 8.0 \\ 7.6 \end{bmatrix}}$$

#### Difference Vector $(\mu_1 - \mu_2)$:
$$\mathbf{\mu_1 - \mu_2 = \begin{bmatrix} 6.8 - 8.0 \\ 5.8 - 7.6 \end{bmatrix} = \begin{bmatrix} -1.2 \\ -1.8 \end{bmatrix}}$$

---

### Step 2: Compute Scatter Matrix $S_1$ for Class 1
Scatter formula:
$$S_1 = \sum_{x \in X_1} (x - \mu_1)(x - \mu_1)^T$$

Let's compute deviations $(x - 6.8)$ and $(y - 5.8)$ for each point in $X_1$:
1. Point $(9, 1)$: $dx = 9 - 6.8 = 2.2, \; dy = 1 - 5.8 = -4.8$
   - $dx^2 = 4.84, \; dy^2 = 23.04, \; dx \cdot dy = -10.56$
2. Point $(7, 4)$: $dx = 7 - 6.8 = 0.2, \; dy = 4 - 5.8 = -1.8$
   - $dx^2 = 0.04, \; dy^2 = 3.24, \; dx \cdot dy = -0.36$
3. Point $(7, 7)$: $dx = 7 - 6.8 = 0.2, \; dy = 7 - 5.8 = 1.2$
   - $dx^2 = 0.04, \; dy^2 = 1.44, \; dx \cdot dy = 0.24$
4. Point $(7, 8)$: $dx = 7 - 6.8 = 0.2, \; dy = 8 - 5.8 = 2.2$
   - $dx^2 = 0.04, \; dy^2 = 4.84, \; dx \cdot dy = 0.44$
5. Point $(4, 9)$: $dx = 4 - 6.8 = -2.8, \; dy = 9 - 5.8 = 3.2$
   - $dx^2 = 7.84, \; dy^2 = 10.24, \; dx \cdot dy = -8.96$

Summing deviations:
- $S_{1, 11} = 4.84 + 0.04 + 0.04 + 0.04 + 7.84 = \mathbf{12.80}$
- $S_{1, 22} = 23.04 + 3.24 + 1.44 + 4.84 + 10.24 = \mathbf{42.80}$
- $S_{1, 12} = S_{1, 21} = -10.56 - 0.36 + 0.24 + 0.44 - 8.96 = \mathbf{-19.20}$

$$\mathbf{S_1 = \begin{bmatrix} 12.80 & -19.20 \\ -19.20 & 42.80 \end{bmatrix}}$$

---

### Step 3: Compute Scatter Matrix $S_2$ for Class 2
Deviations $(x - 8.0)$ and $(y - 7.6)$ for each point in $X_2$:
1. Point $(9, 10)$: $dx = 9 - 8 = 1.0, \; dy = 10 - 7.6 = 2.4$
   - $dx^2 = 1.00, \; dy^2 = 5.76, \; dx \cdot dy = 2.40$
2. Point $(6, 8)$: $dx = 6 - 8 = -2.0, \; dy = 8 - 7.6 = 0.4$
   - $dx^2 = 4.00, \; dy^2 = 0.16, \; dx \cdot dy = -0.80$
3. Point $(7, 5)$: $dx = 7 - 8 = -1.0, \; dy = 5 - 7.6 = -2.6$
   - $dx^2 = 1.00, \; dy^2 = 6.76, \; dx \cdot dy = 2.60$
4. Point $(8, 7)$: $dx = 8 - 8 = 0.0, \; dy = 7 - 7.6 = -0.6$
   - $dx^2 = 0.00, \; dy^2 = 0.36, \; dx \cdot dy = 0.00$
5. Point $(10, 8)$: $dx = 10 - 8 = 2.0, \; dy = 8 - 7.6 = 0.4$
   - $dx^2 = 4.00, \; dy^2 = 0.16, \; dx \cdot dy = 0.80$

Summing deviations:
- $S_{2, 11} = 1.00 + 4.00 + 1.00 + 0.00 + 4.00 = \mathbf{10.00}$
- $S_{2, 22} = 5.76 + 0.16 + 6.76 + 0.36 + 0.16 = \mathbf{13.20}$
- $S_{2, 12} = S_{2, 21} = 2.40 - 0.80 + 2.60 + 0.00 + 0.80 = \mathbf{5.00}$

$$\mathbf{S_2 = \begin{bmatrix} 10.00 & 5.00 \\ 5.00 & 13.20 \end{bmatrix}}$$

---

### Step 4: Compute Within-Class Scatter Matrix $S_W = S_1 + S_2$
$$S_W = \begin{bmatrix} 12.80 + 10.00 & -19.20 + 5.00 \\ -19.20 + 5.00 & 42.80 + 13.20 \end{bmatrix} = \mathbf{\begin{bmatrix} 22.80 & -14.20 \\ -14.20 & 56.00 \end{bmatrix}}$$

---

### Step 5: Invert Within-Class Scatter Matrix $S_W^{-1}$
For a $2 \times 2$ matrix $M = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, $M^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$.

Determinant of $S_W$:
$$\det(S_W) = (22.80)(56.00) - (-14.20)^2 = 1276.80 - 201.64 = \mathbf{1075.16}$$

Inverting $S_W$:
$$S_W^{-1} = \frac{1}{1075.16} \begin{bmatrix} 56.00 & 14.20 \\ 14.20 & 22.80 \end{bmatrix} = \mathbf{\begin{bmatrix} 0.052085 & 0.013207 \\ 0.013207 & 0.021206 \end{bmatrix}}$$

---

### Step 6: Compute Optimal Projection Vector $w$
According to Fisher's Linear Discriminant, the vector $w$ maximizing separation between classes is:
$$w = S_W^{-1} (\mu_1 - \mu_2)$$

Substitute exact values:
$$w = \begin{bmatrix} 0.052085 & 0.013207 \\ 0.013207 & 0.021206 \end{bmatrix} \begin{bmatrix} -1.2 \\ -1.8 \end{bmatrix}$$
$$w_x = 0.052085(-1.2) + 0.013207(-1.8) = -0.062502 - 0.023773 = \mathbf{-0.086275} \approx \mathbf{-0.0863}$$
$$w_y = 0.013207(-1.2) + 0.021206(-1.8) = -0.015848 - 0.038171 = \mathbf{-0.054019} \approx \mathbf{-0.0540}$$

$$\mathbf{w = \begin{bmatrix} -0.0863 \\ -0.0540 \end{bmatrix}}$$

Multiplying by a constant scalar does not change the 1D projection line. Dividing by $-0.0540$:
$$\mathbf{w \propto \begin{bmatrix} 1.60 \\ 1.00 \end{bmatrix}}$$

> **Final Answer:** The optimal Fisher Linear Discriminant projection vector is **$w = \begin{bmatrix} -0.0863 \\ -0.0540 \end{bmatrix}$** (direction ratio: $1.60 : 1.00$).

---

## 6.3 SOLVED NUMERICAL 2: Singular Value Decomposition (SVD)
*(Appeared in: May 2023 Paper, Question 3(b) [10 Marks])*

### Problem Statement:
Find the Singular Value Decomposition (SVD) for the matrix:
$$A = \begin{bmatrix} 2 & 2 \\ -1 & 1 \end{bmatrix}$$

---

### Step 1: Theoretical SVD Definition
Any real $m \times n$ matrix $A$ can be factored as:
$$A = U \Sigma V^T$$
where:
- $U$ is an $m \times m$ orthogonal matrix whose columns are the **left singular vectors** (eigenvectors of $A A^T$).
- $\Sigma$ is an $m \times n$ diagonal matrix containing the **singular values** $\sigma_i = \sqrt{\lambda_i}$ in descending order.
- $V$ is an $n \times n$ orthogonal matrix whose columns are the **right singular vectors** (eigenvectors of $A^T A$).

---

### Step 2: Compute $A^T A$
$$A^T = \begin{bmatrix} 2 & -1 \\ 2 & 1 \end{bmatrix}$$
$$A^T A = \begin{bmatrix} 2 & -1 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} 2 & 2 \\ -1 & 1 \end{bmatrix} = \begin{bmatrix} (4 + 1) & (4 - 1) \\ (4 - 1) & (4 + 1) \end{bmatrix} = \mathbf{\begin{bmatrix} 5 & 3 \\ 3 & 5 \end{bmatrix}}$$

---

### Step 3: Compute Eigenvalues & Singular Values $\sigma_i$
Solve characteristic equation:
$$\det(A^T A - \lambda I) = 0 \implies \begin{vmatrix} 5 - \lambda & 3 \\ 3 & 5 - \lambda \end{vmatrix} = 0$$
$$(5 - \lambda)^2 - 9 = 0$$
$$(5 - \lambda)^2 = 9 \implies 5 - \lambda = \pm 3$$
- $\lambda_1 = 5 + 3 = \mathbf{8}$
- $\lambda_2 = 5 - 3 = \mathbf{2}$

#### Singular Values:
$$\sigma_1 = \sqrt{\lambda_1} = \sqrt{8} = \mathbf{2\sqrt{2}} \approx 2.8284$$
$$\sigma_2 = \sqrt{\lambda_2} = \mathbf{\sqrt{2}} \approx 1.4142$$

The diagonal matrix $\Sigma$ is:
$$\mathbf{\Sigma = \begin{bmatrix} 2\sqrt{2} & 0 \\ 0 & \sqrt{2} \end{bmatrix}}$$

---

### Step 4: Compute Right Singular Vectors $V$ (Eigenvectors of $A^T A$)

#### 1. For $\lambda_1 = 8$:
$$(A^T A - 8 I) v_1 = 0 \implies \begin{bmatrix} 5 - 8 & 3 \\ 3 & 5 - 8 \end{bmatrix} \begin{bmatrix} v_{11} \\ v_{12} \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
$$\begin{bmatrix} -3 & 3 \\ 3 & -3 \end{bmatrix} \begin{bmatrix} v_{11} \\ v_{12} \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies -3 v_{11} + 3 v_{12} = 0 \implies v_{11} = v_{12}$$
Unnormalized vector: $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$.
Normalize to unit length:
$$\mathbf{v_1 = \begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix}}$$

#### 2. For $\lambda_2 = 2$:
$$(A^T A - 2 I) v_2 = 0 \implies \begin{bmatrix} 3 & 3 \\ 3 & 3 \end{bmatrix} \begin{bmatrix} v_{21} \\ v_{22} \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \implies 3 v_{21} + 3 v_{22} = 0 \implies v_{21} = -v_{22}$$
Unnormalized vector: $\begin{bmatrix} -1 \\ 1 \end{bmatrix}$.
Normalize to unit length:
$$\mathbf{v_2 = \begin{bmatrix} -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix}}$$

Therefore, matrix $V$ and $V^T$ are:
$$\mathbf{V = \begin{bmatrix} \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix}}, \quad \mathbf{V^T = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix}}$$

---

### Step 5: Compute Left Singular Vectors $U$
We can obtain columns of $U$ directly using relation $u_i = \frac{1}{\sigma_i} A v_i$:

#### For $u_1$:
$$u_1 = \frac{1}{\sigma_1} A v_1 = \frac{1}{2\sqrt{2}} \begin{bmatrix} 2 & 2 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix} = \frac{1}{2\sqrt{2}} \begin{bmatrix} \frac{2}{\sqrt{2}} + \frac{2}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} \end{bmatrix} = \frac{1}{2\sqrt{2}} \begin{bmatrix} \frac{4}{\sqrt{2}} \\ 0 \end{bmatrix} = \frac{1}{2\sqrt{2}} \begin{bmatrix} 2\sqrt{2} \\ 0 \end{bmatrix} = \mathbf{\begin{bmatrix} 1 \\ 0 \end{bmatrix}}$$

#### For $u_2$:
$$u_2 = \frac{1}{\sigma_2} A v_2 = \frac{1}{\sqrt{2}} \begin{bmatrix} 2 & 2 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} -\frac{2}{\sqrt{2}} + \frac{2}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} 0 \\ \frac{2}{\sqrt{2}} \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} 0 \\ \sqrt{2} \end{bmatrix} = \mathbf{\begin{bmatrix} 0 \\ 1 \end{bmatrix}}$$

Therefore:
$$\mathbf{U = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I_2}$$

---

### Step 6: Verification of $A = U \Sigma V^T$
$$U \Sigma V^T = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 2\sqrt{2} & 0 \\ 0 & \sqrt{2} \end{bmatrix} \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix}$$
$$= \begin{bmatrix} 2\sqrt{2} & 0 \\ 0 & \sqrt{2} \end{bmatrix} \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix} = \begin{bmatrix} 2\sqrt{2} \cdot \frac{1}{\sqrt{2}} & 2\sqrt{2} \cdot \frac{1}{\sqrt{2}} \\ \sqrt{2} \cdot \left(-\frac{1}{\sqrt{2}}\right) & \sqrt{2} \cdot \frac{1}{\sqrt{2}} \end{bmatrix} = \mathbf{\begin{bmatrix} 2 & 2 \\ -1 & 1 \end{bmatrix} = A}$$
*(Decomposition verified with exact arithmetic).*

> **Final SVD Decomposition Result:**
> $$\mathbf{A = U \Sigma V^T = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 2\sqrt{2} & 0 \\ 0 & \sqrt{2} \end{bmatrix} \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix}}$$

---

## MU Keyword Checklist: Module 6
- [ ] *Curse of Dimensionality, Feature Selection vs Extraction*
- [ ] *PCA: Mean Centering, Covariance Matrix $\Sigma = \frac{1}{N-1}X_c^T X_c$, Eigen decomposition, Projection Matrix $W$*
- [ ] *Linear Discriminant Analysis (LDA), Fisher's Criterion $J(w) = \frac{w^T S_B w}{w^T S_W w}$*
- [ ] *Within-Class Scatter Matrix $S_W = S_1 + S_2$, Projection Vector $w = S_W^{-1}(\mu_1 - \mu_2)$*
- [ ] *Singular Value Decomposition (SVD): $A = U \Sigma V^T$, Singular Values $\sigma_i = \sqrt{\lambda_i}$*
- [ ] *Left Singular Vectors $U$ (Eigenvectors of $A A^T$), Right Singular Vectors $V$ (Eigenvectors of $A^T A$)*
