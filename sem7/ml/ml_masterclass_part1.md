# Mumbai University (MU) Semester 7 — Machine Learning (ML)
## Masterclass Part 1: Modules 1, 2 & 3 (Foundations, Regression, Decision Trees & Ensembles)
**Course Code:** Department Level Optional Course (DLOC) | **Scheme:** Rev 2019 / C-Scheme | **Applicable Cycles:** Dec 2022 – May 2025

---

# MODULE 1: INTRODUCTION TO MACHINE LEARNING

---

## 1.1 Machine Learning Paradigm & Formal Definitions
*(Appeared in: Dec 2022 Q1a [5M], May 2023 Q1a [5M], Dec 2023 Q1a [5M], May 2024 Q1a [5M], Dec 2024 Q1d [5M], May 2025 Q1a [5M])*

### Definitions
1. **Arthur Samuel (1959):** *"Machine Learning is the field of study that gives computers the ability to learn without being explicitly programmed."*
2. **Tom Mitchell (1997 - Operational Engineering Definition):** *"A computer program is said to learn from experience $E$ with respect to some class of tasks $T$ and performance measure $P$, if its performance at tasks in $T$, as measured by $P$, improves with experience $E$."*
   - *Example (Spam Classification):*
     - Task $T$: Classify incoming emails as spam or not-spam.
     - Performance $P$: Fraction of emails correctly classified (Accuracy / F1-score).
     - Experience $E$: Corpus of human-labeled historical emails.

```
+---------------------------------------------------------------------------------------------------+
|                           TRADITIONAL PROGRAMMING VS MACHINE LEARNING                             |
+---------------------------------------------------------------------------------------------------+
|  Traditional Programming:   [Data] + [Rules / Program]  ----->  [Computer]  ----->  [Output]      |
|                                                                                                   |
|  Machine Learning:          [Data] + [Output / Labels]  ----->  [Learning Algorithm] ----> [Model]|
+---------------------------------------------------------------------------------------------------+
```

---

## 1.2 Taxonomy of Machine Learning
*(Appeared in: Dec 2024 Q1b [5M], May 2024 Q1a [5M])*

```
+---------------------------------------------------------------------------------------------------+
|                                  MACHINE LEARNING TAXONOMY                                        |
+---------------------------------------------------------------------------------------------------+
| 1. SUPERVISED LEARNING:                                                                           |
|    - Training dataset contains paired inputs and ground-truth targets: D = {(x_i, y_i)}_{i=1}^N.  |
|    - Classification: Target y is discrete / categorical (Spam vs Non-Spam, Cancer detection).     |
|      Algorithms: Logistic Regression, Decision Trees, SVM, Naive Bayes, Random Forest.            |
|    - Regression: Target y is continuous real-valued (House prices, stock returns, temperature).   |
|      Algorithms: Linear Regression, Ridge/Lasso, Support Vector Regression (SVR).                 |
+---------------------------------------------------------------------------------------------------+
| 2. UNSUPERVISED LEARNING:                                                                         |
|    - Training dataset contains unlabeled inputs only: D = {x_i}_{i=1}^N. Discover latent patterns.|
|    - Clustering: Grouping similar instances (K-Means, DBSCAN, Hierarchical / MST Clustering).    |
|    - Dimensionality Reduction: Compressing feature space (PCA, LDA, SVD, t-SNE).                  |
|    - Density Estimation: Modeling underlying probability distribution (GMM with EM Algorithm).    |
+---------------------------------------------------------------------------------------------------+
| 3. SEMI-SUPERVISED LEARNING:                                                                      |
|    - Leverages a tiny labeled dataset D_L alongside a massive unlabeled pool D_U.                 |
|    - Self-training, Co-training, Graph-based label propagation, Pseudo-labeling.                  |
+---------------------------------------------------------------------------------------------------+
| 4. REINFORCEMENT LEARNING (RL):                                                                   |
|    - Goal-directed learning by trial-and-error interaction with a dynamic environment.            |
|    - Tuple: (Agent, Environment, State S, Action A, Reward R, Policy pi, Value function V).       |
|    - Q-Learning, Deep Q-Networks (DQN), Policy Gradient methods (PPO, Actor-Critic).              |
+---------------------------------------------------------------------------------------------------+
```

---

## 1.3 Steps in Developing a Machine Learning Application
*(Appeared in: Dec 2022 Q2a [10M], May 2023 Q2a [10M], Dec 2024 Q3a [10M], May 2025 Q2a [10M])*

```
+---------------------------------------------------------------------------------------------------+
|                          7-STAGE END-TO-END ML DEVELOPMENT PIPELINE                               |
+---------------------------------------------------------------------------------------------------+
| 1. PROBLEM FORMULATION & FEASIBILITY ANALYSIS                                                     |
|    - Translate business goal into ML problem type (Binary/Multiclass Classification, Regression). |
|    - Define primary success metrics (ROC-AUC, RMSE, Latency, Throughput).                         |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 2. DATA ACQUISITION & INTEGRATION                                                                 |
|    - Extract data from relational DBs, data warehouses, streaming APIs, or web scraping.          |
|    - Ensure ethical compliance, data privacy, and sufficient sample volume.                       |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 3. EXPLORATORY DATA ANALYSIS (EDA) & PREPROCESSING                                                |
|    - Handle Missing Values: Mean/Median/Mode imputation, KNN imputation, row dropping.            |
|    - Outlier Detection: Z-Score thresholding, Interquartile Range (IQR) clipping.                 |
|    - Encoding: One-Hot Encoding for nominal variables, Label Encoding for ordinal variables.      |
|    - Feature Scaling: Min-Max Normalization [0, 1] vs Standardization (Z-score: mean 0, std 1).   |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 4. FEATURE ENGINEERING & DIMENSIONALITY REDUCTION                                                 |
|    - Feature Extraction: Mathematical transforms, polynomial interaction terms, text embeddings.  |
|    - Feature Selection: Filter methods (Variance, Correlation), Wrapper methods (RFE), PCA/LDA.   |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 5. MODEL SELECTION & TRAINING                                                                     |
|    - Split dataset into Train (70%), Validation (15%), Test (15%) or K-Fold Cross-Validation.     |
|    - Train baseline models (Linear/Logistic Regression, Decision Trees), then advanced ensembles. |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 6. HYPERPARAMETER TUNING & EVALUATION                                                             |
|    - Systematic search: Grid Search CV, Random Search CV, or Bayesian Optimization.               |
|    - Evaluate on unseen holdout test set using Confusion Matrix, ROC-AUC, F1-Score, RMSE.         |
+---------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
| 7. DEPLOYMENT, MONITORING & MODEL MAINTENANCE                                                     |
|    - Export model (ONNX, Pickle, TorchScript); deploy via REST API (FastAPI) or edge container.   |
|    - Continuous telemetry: Monitor Concept Drift (P(Y|X) changes) and Data Drift (P(X) changes).  |
+---------------------------------------------------------------------------------------------------+
```

---

## 1.4 Core Issues & Challenges in Machine Learning
*(Appeared in: Dec 2022 Q1a [5M], May 2024 Q2a [10M], Dec 2024 Q1d [5M], May 2025 Q1a [5M])*

1. **The Curse of Dimensionality:**
   - As the number of features $d$ grows, the volume of feature space grows exponentially ($O(2^d)$). Data points become extremely sparse, pairwise Euclidean distances converge to identical values, and models overfit dramatically.
2. **Data Quality & Scarcity:**
   - Noise, missing sensor readings, incorrect labels, and unrepresentative sampling distort the learned decision boundary.
3. **Class Imbalance:**
   - Real-world fraud, cancer, or fault detection datasets typically feature $99.9\%$ negative class vs $0.1\%$ positive class. Standard loss functions optimize trivial majority predictions. (Requires SMOTE, focal loss, or threshold tuning).
4. **Overfitting & Underfitting:**
   - Balancing generalization capacity on unseen data versus empirical memorization of training instances.
5. **Data Drift & Concept Drift:**
   - Statistical properties of inputs $P(X)$ or conditional relations $P(Y \mid X)$ shift over time in production environments.
6. **Interpretability vs Accuracy Tradeoff:**
   - High-accuracy deep models and gradient-boosted ensembles operate as opaque "black boxes," making validation in medical, financial, and legal domains difficult.

---

## 1.5 Training Error vs Generalization Error & The Bias-Variance Tradeoff
*(Appeared in: Dec 2023 Q2b [10M], Dec 2024 Q1a [5M], Dec 2024 Q3b [10M])*

### Definitions
- **Training Error (Empirical Risk):** The average loss evaluated directly on the training dataset $D_{\text{train}}$: $E_{\text{train}}(\hat{f}) = \frac{1}{N} \sum_{i=1}^N L(y_i, \hat{f}(x_i))$
- **Generalization Error (True Risk):** The expected loss over the entire unseen true population distribution $\mathcal{D}$:
$E_{\text{gen}}(\hat{f}) = \mathbb{E}_{(x, y) \sim \mathcal{D}}[L(y, \hat{f}(x))]$

### Overfitting vs Underfitting

| Condition | Training Error | Generalization / Test Error | Symptom | Underlying Cause | Remedy |
|:---|:---:|:---:|:---|:---|:---|
| **Underfitting** | **High** | **High** | High Bias | Model is too simple; cannot capture underlying data patterns. | Increase model capacity, add polynomial features, reduce regularization. |
| **Good Fit** | **Low** | **Low** (close to train) | Balanced | Model captures true signal, ignores noise. | Optimal hyperparameter setting. |
| **Overfitting** | **Very Low** | **High** | High Variance | Model is excessively complex; memorizes noise and sample quirks. | Pruning, L1/L2 regularization, dropout, increase training data. |

---

### Mathematical Derivation of the Bias-Variance Decomposition
Assume true relation $y = f(x) + \epsilon$, where noise $\epsilon$ has zero mean $\mathbb{E}[\epsilon] = 0$ and variance $\text{Var}(\epsilon) = \sigma^2$. Let $\hat{f}(x)$ be the estimator learned from a training set $\mathcal{D}$. The expected Mean Squared Error on an unseen point $x$ is: $\mathbb{E}_{\mathcal{D}} [(y - \hat{f}(x))^2]$

Substitute $y = f(x) + \epsilon$: $\mathbb{E}[(f(x) + \epsilon - \hat{f}(x))^2] = \mathbb{E}[((f(x) - \hat{f}(x)) + \epsilon)^2] = \mathbb{E}[(f(x) - \hat{f}(x))^2] + 2 \mathbb{E}[(f(x) - \hat{f}(x))\epsilon] + \mathbb{E}[\epsilon^2]$

Since noise $\epsilon$ is independent of the model $\hat{f}(x)$ and $\mathbb{E}[\epsilon] = 0$, the cross-term vanishes: $= \mathbb{E}[(f(x) - \hat{f}(x))^2] + \sigma^2$

Now expand $\mathbb{E}[(f(x) - \hat{f}(x))^2]$ by adding and subtracting $\mathbb{E}[\hat{f}(x)]$: $\mathbb{E}\left[ \left( (f(x) - \mathbb{E}[\hat{f}(x)]) + (\mathbb{E}[\hat{f}(x)] - \hat{f}(x)) \right)^2 \right]$
$= \mathbb{E}[(f(x) - \mathbb{E}[\hat{f}(x)])^2] + \mathbb{E}[(\hat{f}(x) - \mathbb{E}[\hat{f}(x)])^2] - 2(f(x) - \mathbb{E}[\hat{f}(x)])\mathbb{E}[\hat{f}(x) - \mathbb{E}[\hat{f}(x)]]$

Since $\mathbb{E}[\hat{f}(x) - \mathbb{E}[\hat{f}(x)]] = 0$, we arrive at the master decomposition:

$$\mathbf{\mathbb{E}_{\mathcal{D}} \left[ (y - \hat{f}(x))^2 \right] = \underbrace{\left( f(x) - \mathbb{E}[\hat{f}(x)] \right)^2}_{\text{Bias}^2} + \underbrace{\mathbb{E}\left[ (\hat{f}(x) - \mathbb{E}[\hat{f}(x)])^2 \right]}_{\text{Variance}} + \underbrace{\sigma^2}_{\text{Irreducible Error}}}$$

```
+---------------------------------------------------------------------------------------------------+
|                                 THE BIAS-VARIANCE TRADEOFF CURVE                                  |
+---------------------------------------------------------------------------------------------------+
|  Error                                                                                            |
|    ^                                                                                              |
|    |           \                                     /  Total Generalization Error                |
|    |            \                                   /                                             |
|    |             \          Optimal Model          /    Variance                                  |
|    |              \          Complexity           /     (Overfitting)                             |
|    |   High Bias   \              |              /      /                                         |
|    | (Underfitting) \             v             /      /                                          |
|    |                 \_______..........._______/      /                                           |
|    |                  \                       /      /                                            |
|    |                   \                     /      /                                             |
|    |                    \                   /      /                                              |
|    |  Bias^2             \                 /      /                                               |
|    |  ....................\.............../....../                                                |
|    |                       \                    /                                                 |
|    |  ------------------------------------------------------------- Irreducible Error (sigma^2)   |
|    |                                                                                              |
|    +----------------------------------------------------------------------------> Model Complexity|
|       (Simple: Linear Model)                         (Complex: Deep Trees / Polynomial)           |
+---------------------------------------------------------------------------------------------------+
```

---

## MU Keyword Checklist: Module 1
- [ ] *Tom Mitchell Definition: Task $T$, Performance $P$, Experience $E$*
- [ ] *Supervised (Continuous Regression, Discrete Classification) vs Unsupervised (Clustering, Dim Reduction)*
- [ ] *7 Development Steps: Problem Formulation, Data Ingestion, EDA, Feature Engineering, Training, Tuning, Deployment*
- [ ] *Curse of Dimensionality, Class Imbalance, Concept Drift, Data Drift*
- [ ] *Empirical Risk (Training Error) vs Generalization Error*
- [ ] *Bias-Variance Decomposition: $\text{MSE} = \text{Bias}^2 + \text{Variance} + \sigma^2$*
- [ ] *U-Shaped Total Error Curve, High Bias (Underfitting), High Variance (Overfitting)*

---
---

# MODULE 2: LEARNING WITH REGRESSION & DECISION TREES

---

## 2.1 Linear Regression: Formulations & Derivations
*(Appeared in: Dec 2022 Q1b/Q2b [10M], May 2023 Q1b/Q2b/Q6a [10M], Dec 2023 Q3a [10M], May 2024 Q3a [10M], Dec 2024 Q1c [5M], May 2025 Q1b/Q3b [10M])*

### Simple Linear Regression Model
Hypothesis: $Y = \beta_0 + \beta_1 X$ where:
- $\beta_0$ is the intercept (bias).
- $\beta_1$ is the regression slope.
- Residual (prediction error) for instance $i$: $e_i = Y_i - \hat{Y}_i = Y_i - (\beta_0 + \beta_1 X_i)$.

### Cost Function (Sum of Squared Errors - SSE)

$$J(\beta_0, \beta_1) = \sum_{i=1}^N (Y_i - (\beta_0 + \beta_1 X_i))^2$$

### Analytical Derivation of Ordinary Least Squares (OLS)

To find $\beta_0, \beta_1$ that minimize $J$, take partial derivatives and set to zero:

$$\frac{\partial J}{\partial \beta_0} = -2 \sum_{i=1}^N (Y_i - \beta_0 - \beta_1 X_i) = 0 \implies \sum Y_i = N \beta_0 + \beta_1 \sum X_i \quad \text{--- (Equation 1)}$$

Dividing by $N$:

$$\beta_0 = \bar{Y} - \beta_1 \bar{X}$$

$$\frac{\partial J}{\partial \beta_1} = -2 \sum_{i=1}^N X_i (Y_i - \beta_0 - \beta_1 X_i) = 0 \implies \sum X_i Y_i = \beta_0 \sum X_i + \beta_1 \sum X_i^2 \quad \text{--- (Equation 2)}$$

Substitute $\beta_0 = \frac{\sum Y - \beta_1 \sum X}{N}$ into Equation 2:

$$\sum XY = \left(\frac{\sum Y - \beta_1 \sum X}{N}\right) \sum X + \beta_1 \sum X^2$$

$$N \sum XY = \sum X \sum Y - \beta_1 \left(\sum X\right)^2 + N \beta_1 \sum X^2$$

$$N \sum XY - \sum X \sum Y = \beta_1 \left[ N \sum X^2 - \left(\sum X\right)^2 \right]$$

$$\mathbf{\beta_1 = \frac{N \sum X_i Y_i - \left(\sum X_i\right) \left(\sum Y_i\right)}{N \sum X_i^2 - \left(\sum X_i\right)^2} = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sum (X_i - \bar{X})^2}}$$

## 2.2 SOLVED NUMERICAL 1: Clinical BMI vs Cholesterol Regression
*(Appeared in: December 2023 Paper, Question 3(a) [10 Marks])*

### Problem Statement:
A clinical test gave data for BMI ($X$) and Cholesterol level ($Y$) for 10 patients as shown below:
- $X$ (BMI): $17, 21, 24, 28, 14, 16, 19, 22, 15, 18$
- $Y$ (Cholesterol): $144, 189, 214, 243, 133, 160, 169, 166, 135, 150$

*Tasks:*
1. Identify the machine learning method used to solve the problem.
2. Formulate the mathematical model.
3. Predict the likely value of Cholesterol level for someone who has a **BMI of 27**.

---

### Step 1: Method Identification
The target variable (Cholesterol level) is a continuous real-valued quantity conditioned on a continuous predictor variable (BMI).
Therefore, the appropriate machine learning method is **Simple Linear Regression** via **Ordinary Least Squares (OLS)**.

---

### Step 2: Step-by-Step Calculation Table ($N = 10$)

| Patient $i$ | BMI ($X_i$) | Cholesterol ($Y_i$) | $X_i^2$ | $X_i Y_i$ |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 17 | 144 | 289 | 2448 |
| 2 | 21 | 189 | 441 | 3969 |
| 3 | 24 | 214 | 576 | 5136 |
| 4 | 28 | 243 | 784 | 6804 |
| 5 | 14 | 133 | 196 | 1862 |
| 6 | 16 | 160 | 256 | 2560 |
| 7 | 19 | 169 | 361 | 3211 |
| 8 | 22 | 166 | 484 | 3652 |
| 9 | 15 | 135 | 225 | 2025 |
| 10 | 18 | 150 | 324 | 2700 |
| **Sum ($\sum$)** | **194** | **1703** | **3936** | **34367** |

---

### Step 3: Mean Calculations
$$\bar{X} = \frac{\sum X_i}{N} = \frac{194}{10} = \mathbf{19.4}$$

$$\bar{Y} = \frac{\sum Y_i}{N} = \frac{1703}{10} = \mathbf{170.3}$$

---

### Step 4: Calculate Slope $\beta_1$ and Intercept $\beta_0$

Using the OLS slope formula:

$$\beta_1 = \frac{N \sum X_i Y_i - \left(\sum X_i\right) \left(\sum Y_i\right)}{N \sum X_i^2 - \left(\sum X_i\right)^2}$$

Substitute exact values:

$$\beta_1 = \frac{10(34367) - (194)(1703)}{10(3936) - (194)^2}$$

$$\beta_1 = \frac{343670 - 330382}{39360 - 37636} = \frac{13288}{1724} \approx \mathbf{7.7077}$$

Now calculate intercept $\beta_0$:

$$\beta_0 = \bar{Y} - \beta_1 \bar{X}$$

$$\beta_0 = 170.3 - (7.7077 \times 19.4) = 170.3 - 149.5294 = \mathbf{20.7706} \approx \mathbf{20.77}$$

---

### Step 5: Regression Equation
$$\mathbf{\hat{Y} = 20.77 + 7.71 X}$$

*(Meaning: For every 1-unit increase in BMI, Cholesterol increases by $7.71$ mg/dL on average).*

---

### Step 6: Prediction for $\text{BMI} = 27$
Substitute $X = 27$ into the fitted regression equation:

$$\hat{Y}_{X=27} = 20.7706 + 7.7077 \times 27$$

$$\hat{Y}_{X=27} = 20.7706 + 208.1079 = \mathbf{228.8785} \approx \mathbf{228.88}$$

> **Final Answer:** The predicted Cholesterol level for a patient with a BMI of 27 is **$228.88$** mg/dL.

---

## 2.3 SOLVED NUMERICAL 2: Midterm vs Final Exam Grade Prediction
*(Appeared in: May 2025 Paper, Question 3(b) [10 Marks])*

### Problem Statement:
Following table shows the midterm ($X$) and final exam ($Y$) grades obtained by 12 students in a database course:
- $X$: $72, 50, 81, 74, 94, 86, 59, 83, 65, 33, 88, 81$
- $Y$: $84, 63, 77, 78, 90, 75, 49, 79, 77, 52, 74, 90$

*Task:* Using linear regression, predict the final exam grade of a student who received **86 in the midterm exam**.

---

### Step 1: Step-by-Step Calculation Table ($N = 12$)

| Student $i$ | Midterm ($X_i$) | Final ($Y_i$) | $X_i^2$ | $X_i Y_i$ |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 72 | 84 | 5184 | 6048 |
| 2 | 50 | 63 | 2500 | 3150 |
| 3 | 81 | 77 | 6561 | 6237 |
| 4 | 74 | 78 | 5476 | 5772 |
| 5 | 94 | 90 | 8836 | 8460 |
| 6 | 86 | 75 | 7396 | 6450 |
| 7 | 59 | 49 | 3481 | 2891 |
| 8 | 83 | 79 | 6889 | 6557 |
| 9 | 65 | 77 | 4225 | 5005 |
| 10 | 33 | 52 | 1089 | 1716 |
| 11 | 88 | 74 | 7744 | 6512 |
| 12 | 81 | 90 | 6561 | 7290 |
| **Sum ($\sum$)** | **866** | **888** | **65942** | **66088** |

---

### Step 2: Mean Calculations
$$\bar{X} = \frac{\sum X_i}{N} = \frac{866}{12} \approx \mathbf{72.1667}$$

$$\bar{Y} = \frac{\sum Y_i}{N} = \frac{888}{12} = \mathbf{74.0000}$$

---

### Step 3: Compute Slope $\beta_1$ and Intercept $\beta_0$
$$\beta_1 = \frac{N \sum X_i Y_i - \left(\sum X_i\right) \left(\sum Y_i\right)}{N \sum X_i^2 - \left(\sum X_i\right)^2}$$

Substitute values:

$$\beta_1 = \frac{12(66088) - (866)(888)}{12(65942) - (866)^2}$$

$$\beta_1 = \frac{793056 - 769008}{791304 - 749956} = \frac{24048}{41348} \approx \mathbf{0.5816}$$

Compute $\beta_0$:

$$\beta_0 = \bar{Y} - \beta_1 \bar{X} = 74.0000 - (0.5816 \times 72.1667) = 74.0000 - 41.9721 = \mathbf{32.0279}$$

---

### Step 4: Regression Equation
$$\mathbf{\hat{Y} = 32.03 + 0.5816 X}$$

---

### Step 5: Prediction for Midterm Exam Grade $X = 86$
$$\hat{Y}_{X=86} = 32.0279 + 0.5816 \times 86$$

$$\hat{Y}_{X=86} = 32.0279 + 50.0176 = \mathbf{82.0455} \approx \mathbf{82.05}$$

> **Final Answer:** The predicted final exam grade for a student with a midterm grade of 86 is **$82.05$** (or approximately **$82$ marks**).

---

## 2.4 SOLVED NUMERICAL 3: Mass vs Time Regression
*(Appeared in: May 2024 Paper, Question 3(a) [10 Marks])*

### Problem Statement:
The mass $y$ (grams) of a chemical is related to time $x$ (seconds) according to the table:
- Time, $x$: $3, 5, 12, 16, 20$
- Mass, $y$: $40, 120, 180, 210, 240$

*Tasks:*
1. Find the equation of the regression line.
2. Explain performance evaluation measures for regression.

---

### Step 1: Calculation Table ($N = 5$)

| Observation $i$ | Time $x_i$ | Mass $y_i$ | $x_i^2$ | $x_i y_i$ |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 3 | 40 | 9 | 120 |
| 2 | 5 | 120 | 25 | 600 |
| 3 | 12 | 180 | 144 | 2160 |
| 4 | 16 | 210 | 256 | 3360 |
| 5 | 20 | 240 | 400 | 4800 |
| **Sum ($\sum$)** | **56** | **790** | **834** | **11040** |

---

### Step 2: Mean Calculations
$$\bar{x} = \frac{56}{5} = \mathbf{11.2}, \quad \bar{y} = \frac{790}{5} = \mathbf{158.0}$$

---

### Step 3: Compute Parameters $\beta_1$ and $\beta_0$
$$\beta_1 = \frac{5(11040) - (56)(790)}{5(834) - (56)^2} = \frac{55200 - 44240}{4170 - 3136} = \frac{10960}{1034} \approx \mathbf{10.5996}$$

$$\beta_0 = \bar{y} - \beta_1 \bar{x} = 158.0 - (10.5996 \times 11.2) = 158.0 - 118.7155 = \mathbf{39.2845}$$

---

### Step 4: Regression Equation
$$\mathbf{\hat{y} = 39.28 + 10.60 x}$$

### Regression Performance Evaluation Measures:
1. **Mean Absolute Error (MAE):**

$$\text{MAE} = \frac{1}{N} \sum_{i=1}^N |y_i - \hat{y}_i|$$

2. **Mean Squared Error (MSE):**

$$\text{MSE} = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2$$

3. **Root Mean Squared Error (RMSE):**

$$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2}$$

4. **Coefficient of Determination ($R^2$ Score):**

$$R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$

   Measures the proportion of total variance explained by the regression line ($0 \le R^2 \le 1$).

---

## 2.5 Logistic Regression: Theory, Sigmoid Function & Log-Loss
*(Appeared in: Dec 2022 Q1e [5M], May 2023 Q1e [5M], Dec 2023 Q1d [5M], Dec 2024 Q1c/Q2b [10M], May 2025 Q1e [5M])*

### Why Linear Regression Fails for Classification
1. **Non-Bounded Predictions:** Linear hypothesis $h_\theta(x) = \theta^T x$ can output values in $(-\infty, +\infty)$, which cannot be interpreted as probabilities in $[0, 1]$.
2. **Extreme Outlier Sensitivity:** Linear regression shifts the decision boundary significantly when distant non-essential outliers are introduced.

### The Logistic (Sigmoid) Function
To map any real-valued number into a probability $P(Y=1 \mid X) \in [0, 1]$, Logistic Regression wraps linear combinations with the **sigmoid function**:

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

```
+---------------------------------------------------------------------------------------------------+
|                                 THE SIGMOID ACTIVATION FUNCTION                                   |
+---------------------------------------------------------------------------------------------------+
|  sigma(z)                                                                                         |
|    1.0 +----------------------------------------------...............                             |
|        |                                          ..''                                            |
|        |                                       .''                                                |
|    0.5 |------------------------------------/------------------------ Decision Threshold (z=0)    |
|        |                                 .''                                                      |
|        |                              .''                                                         |
|    0.0 +................''''------------------------------------------                            |
|       -inf                        -2        0        +2                       +inf  (z = w^T x)   |
+---------------------------------------------------------------------------------------------------+
```

#### Properties of Sigmoid:
- $\lim_{z \to +\infty} \sigma(z) = 1$, $\lim_{z \to -\infty} \sigma(z) = 0$, $\sigma(0) = 0.5$.
- **Derivative:** $\sigma'(z) = \sigma(z)(1 - \sigma(z))$.

### Odds and Log-Odds (Logit)
$$\text{Odds} = \frac{P(Y=1 \mid X)}{1 - P(Y=1 \mid X)} = \frac{\frac{1}{1 + e^{-z}}}{1 - \frac{1}{1 + e^{-z}}} = e^z$$

Taking the natural logarithm yields the linear predictor (**Logit function**):

$$\ln\left(\frac{P}{1 - P}\right) = z = \theta_0 + \theta_1 x_1 + \dots + \theta_n x_n$$

### Cost Function: Binary Cross-Entropy (Log-Loss)
Mean squared error generates a non-convex surface for logistic regression with numerous local minima. Instead, we use the convex **Log-Loss**:

$$J(\theta) = -\frac{1}{m} \sum_{i=1}^m \left[ y^{(i)} \ln(h_\theta(x^{(i)})) + (1 - y^{(i)}) \ln(1 - h_\theta(x^{(i)})) \right]$$

- If $y = 1$, cost is $-\ln(h_\theta(x))$. As $h_\theta(x) \to 1$, cost $\to 0$. As $h_\theta(x) \to 0$, cost $\to \infty$.
- If $y = 0$, cost is $-\ln(1 - h_\theta(x))$. As $h_\theta(x) \to 0$, cost $\to 0$. As $h_\theta(x) \to 1$, cost $\to \infty$.

---

## 2.6 Classification Performance Evaluation Metrics
*(Appeared in: Dec 2022 Q6a [10M], Dec 2023 Q1c/Q1e [10M], May 2024 Q1c [5M], Dec 2024 Q1e/Q2b [10M], May 2025 Q1d/Q6a [10M])*

```
+---------------------------------------------------------------------------------------------------+
|                                 THE 2x2 BINARY CONFUSION MATRIX                                   |
+---------------------------------------------------------------------------------------------------+
|                             |        ACTUAL POSITIVE (1)     |        ACTUAL NEGATIVE (0)         |
+-----------------------------+--------------------------------+------------------------------------+
| PREDICTED POSITIVE (1)      |    True Positive (TP)          |    False Positive (FP)             |
|                             |    (Correctly diagnosed ill)   |    (Type I Error - False alarm)    |
+-----------------------------+--------------------------------+------------------------------------+
| PREDICTED NEGATIVE (0)      |    False Negative (FN)         |    True Negative (TN)              |
|                             |    (Type II Error - Missed ill)|    (Correctly rejected healthy)    |
+-----------------------------+--------------------------------+------------------------------------+
```

### Comprehensive Formula Catalog:

1. **Accuracy:**

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

   *(Caution: Misleading on imbalanced datasets).*
2. **Precision (Positive Predictive Value):**

$$\text{Precision} = \frac{TP}{TP + FP}$$

   *(Answers: "Out of all predicted positives, how many were actually positive?").*
3. **Recall / Sensitivity / True Positive Rate (TPR):**

$$\text{Recall} = \frac{TP}{TP + FN}$$

   *(Answers: "Out of all actual positives, how many did the model detect?").*
4. **Specificity / True Negative Rate (TNR):**

$$\text{Specificity} = \frac{TN}{TN + FP}$$

5. **False Positive Rate (FPR):**

$$\text{FPR} = 1 - \text{Specificity} = \frac{FP}{TN + FP}$$

6. **F1-Score (Harmonic Mean of Precision and Recall):**

$$\text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2 TP}{2 TP + FP + FN}$$

   *(Uses Harmonic Mean because it heavily penalizes extreme imbalances between Precision and Recall).*
7. **Receiver Operating Characteristic (ROC) & AUC:**
   - **ROC Curve:** Plots **TPR (Sensitivity)** on the Y-axis against **FPR ($1 - \text{Specificity}$)** on the X-axis across all classification decision thresholds $\tau \in [0, 1]$.
   - **Area Under Curve (AUC):** Represents the probability that the classifier ranks a randomly chosen positive instance higher than a randomly chosen negative instance. (Perfect classifier: $\text{AUC} = 1.0$; Random guess: $\text{AUC} = 0.5$).

---

## 2.7 Decision Trees: Gini Index vs Information Gain & Pruning
*(Appeared in: Dec 2022 Q3a [10M], May 2023 Q3a [10M], Dec 2023 Q4b [10M], May 2024 Q1d/Q4b [10M], Dec 2024 Q4b [10M], May 2025 Q3a [10M])*

### Splitting Criteria: ID3 vs CART

```
+---------------------------------------------------------------------------------------------------+
|                                     ID3 VS CART COMPARISON                                        |
+---------------------------------------------------------------------------------------------------+
| Parameter          | ID3 / C4.5                             | CART (Classification & Regression)  |
+--------------------+----------------------------------------+-------------------------------------+
| Target Variable    | Categorical only (ID3); Numerical C4.5 | Categorical AND Continuous          |
| Splitting Metric   | Entropy & Information Gain             | Gini Impurity (Index)               |
| Tree Structure     | Multi-way splits                       | Strictly Binary splits              |
+---------------------------------------------------------------------------------------------------+
```

### Mathematical Formulations:
1. **Entropy (Shannon Entropy):**

$$\text{Entropy}(D) = - \sum_{i=1}^k p_i \log_2(p_i)$$

2. **Information Gain:**

$$\text{Gain}(D, A) = \text{Entropy}(D) - \sum_{v \in \text{Values}(A)} \frac{|D_v|}{|D|} \text{Entropy}(D_v)$$

3. **Gini Impurity (Index):**
   Measures the probability of misclassifying a randomly chosen element from the set:

$$\text{Gini}(D) = 1 - \sum_{i=1}^k p_i^2$$

   For a binary classification problem ($p$ positive, $q = 1-p$ negative):

$$\text{Gini}(D) = 1 - (p^2 + q^2) = 2p(1-p)$$

4. **Weighted Gini Index for Attribute Split $A$:**

$$\text{Gini}_A(D) = \sum_{v \in \text{Values}(A)} \frac{|D_v|}{|D|} \text{Gini}(D_v)$$

$$\mathbf{\text{Gini Gain}(D, A) = \text{Gini}(D) - \text{Gini}_A(D)}$$

   **The attribute with the MINIMUM split Gini index (or MAXIMUM Gini Gain) is chosen as the splitting node.**

---

## 2.8 SOLVED NUMERICAL 4: Decision Tree Root Selection for Car Stolen Dataset
*(Appeared in: December 2024 Paper, Question 4(b) [10 Marks])*

### Problem Statement:
Suppose we want Gini index to decide whether the car will be stolen or not. The target classification is "car is stolen?" which can be Yes or No. Create a decision tree (identify root node) for the given data below:

| Car No | Colour | Type | Origin | Stolen? |
|:---:|:---:|:---:|:---:|:---:|
| 1 | Red | Sports | Domestic | Yes |
| 2 | Red | Sports | Domestic | No |
| 3 | Red | Sports | Domestic | Yes |
| 4 | Yellow | Sports | Domestic | No |
| 5 | Yellow | Sports | Imported | Yes |
| 6 | Yellow | SUV | Imported | No |
| 7 | Yellow | SUV | Imported | Yes |
| 8 | Yellow | SUV | Domestic | No |
| 9 | Red | SUV | Imported | No |
| 10 | Red | Sports | Imported | Yes |

---

### Step 1: Overall Dataset Impurity $\text{Gini}(D)$
Total instances $|D| = 10$.
Count of target class `Stolen?`:
- `Yes`: 5 (Cars 1, 3, 5, 7, 10)
- `No`: 5 (Cars 2, 4, 6, 8, 9)

$$\text{Gini}(D) = 1 - \left[ \left(\frac{5}{10}\right)^2 + \left(\frac{5}{10}\right)^2 \right] = 1 - [0.25 + 0.25] = \mathbf{0.5000}$$

---

### Step 2: Evaluate Attribute 1 — `Colour`
Values of `Colour`: `Red` and `Yellow`.

1. **Subset `Colour = Red` ($|D_{\text{Red}}| = 5$):**
   - Cars: 1, 2, 3, 9, 10.
   - `Yes`: 3 (Cars 1, 3, 10)
   - `No`: 2 (Cars 2, 9)

$$\text{Gini}(D_{\text{Red}}) = 1 - \left[ \left(\frac{3}{5}\right)^2 + \left(\frac{2}{5}\right)^2 \right] = 1 - [0.36 + 0.16] = 1 - 0.52 = \mathbf{0.4800}$$

2. **Subset `Colour = Yellow` ($|D_{\text{Yellow}}| = 5$):**
   - Cars: 4, 5, 6, 7, 8.
   - `Yes`: 2 (Cars 5, 7)
   - `No`: 3 (Cars 4, 6, 8)

$$\text{Gini}(D_{\text{Yellow}}) = 1 - \left[ \left(\frac{2}{5}\right)^2 + \left(\frac{3}{5}\right)^2 \right] = 1 - [0.16 + 0.36] = \mathbf{0.4800}$$

3. **Weighted Split Gini for `Colour`:**

$$\text{Gini}_{\text{Colour}}(D) = \frac{5}{10}(0.4800) + \frac{5}{10}(0.4800) = \mathbf{0.4800}$$

---

### Step 3: Evaluate Attribute 2 — `Type`
Values of `Type`: `Sports` and `SUV`.

1. **Subset `Type = Sports` ($|D_{\text{Sports}}| = 6$):**
   - Cars: 1, 2, 3, 4, 5, 10.
   - `Yes`: 4 (Cars 1, 3, 5, 10)
   - `No`: 2 (Cars 2, 4)

$$\text{Gini}(D_{\text{Sports}}) = 1 - \left[ \left(\frac{4}{6}\right)^2 + \left(\frac{2}{6}\right)^2 \right] = 1 - \left[ \frac{16}{36} + \frac{4}{36} \right] = 1 - \frac{20}{36} = \frac{16}{36} = \frac{4}{9} \approx \mathbf{0.4444}$$

2. **Subset `Type = SUV` ($|D_{\text{SUV}}| = 4$):**
   - Cars: 6, 7, 8, 9.
   - `Yes`: 1 (Car 7)
   - `No`: 3 (Cars 6, 8, 9)

$$\text{Gini}(D_{\text{SUV}}) = 1 - \left[ \left(\frac{1}{4}\right)^2 + \left(\frac{3}{4}\right)^2 \right] = 1 - \left[ \frac{1}{16} + \frac{9}{16} \right] = 1 - \frac{10}{16} = \frac{6}{16} = \mathbf{0.3750}$$

3. **Weighted Split Gini for `Type`:**

$$\text{Gini}_{\text{Type}}(D) = \frac{6}{10}(0.4444) + \frac{4}{10}(0.3750) = 0.2667 + 0.1500 = \mathbf{0.4167}$$

---

### Step 4: Evaluate Attribute 3 — `Origin`
Values of `Origin`: `Domestic` and `Imported`.

1. **Subset `Origin = Domestic` ($|D_{\text{Domestic}}| = 5$):**
   - Cars: 1, 2, 3, 4, 8.
   - `Yes`: 2 (Cars 1, 3)
   - `No`: 3 (Cars 2, 4, 8)

$$\text{Gini}(D_{\text{Domestic}}) = 1 - \left[ \left(\frac{2}{5}\right)^2 + \left(\frac{3}{5}\right)^2 \right] = 1 - 0.52 = \mathbf{0.4800}$$

2. **Subset `Origin = Imported` ($|D_{\text{Imported}}| = 5$):**
   - Cars: 5, 6, 7, 9, 10.
   - `Yes`: 3 (Cars 5, 7, 10)
   - `No`: 2 (Cars 6, 9)

$$\text{Gini}(D_{\text{Imported}}) = 1 - \left[ \left(\frac{3}{5}\right)^2 + \left(\frac{2}{5}\right)^2 \right] = 1 - 0.52 = \mathbf{0.4800}$$

3. **Weighted Split Gini for `Origin`:**

$$\text{Gini}_{\text{Origin}}(D) = \frac{5}{10}(0.4800) + \frac{5}{10}(0.4800) = \mathbf{0.4800}$$

---

### Step 5: Comparison & Root Node Selection

| Attribute | Split Gini Index $\text{Gini}(D, A)$ | Gini Gain $\text{Gini}(D) - \text{Gini}(D, A)$ | Ranking |
|:---|:---:|:---:|:---:|
| **`Type`** | $\mathbf{0.4167}$ | $\mathbf{0.0833}$ | **1 (Best Split - Selected as Root)** |
| `Colour` | $0.4800$ | $0.0200$ | 2 |
| `Origin` | $0.4800$ | $0.0200$ | 2 |

```
                                  [ Type? ]  <--- ROOT NODE
                                 /         \
                         (Sports)           (SUV)
                           /                     \
                   [6 Cars: 4 Yes, 2 No]        [4 Cars: 1 Yes, 3 No]
```

> **Final Decision:** The attribute **`Type`** achieves the lowest split Gini index ($0.4167$) and highest Gini gain ($0.0833$). Therefore, **`Type` is chosen as the ROOT NODE** of the decision tree.

---

## 2.9 SOLVED NUMERICAL 5: Stock Trend Decision Tree Root Selection
*(Appeared in: December 2023 Paper, Question 4(b) [10 Marks])*

### Problem Statement:
The dataset has 3 features: `Past Trend`, `Open Interest`, `Trading Volume` and one class label `Return` (Up / Down). Compute the Gini Index for all features and specify which node will be chosen as a root node.

| Row | Past Trend | Open Interest | Trading Volume | Return |
|:---:|:---:|:---:|:---:|:---:|
| 1 | Positive | Low | High | Up |
| 2 | Negative | High | Low | Down |
| 3 | Positive | Low | High | Up |
| 4 | Positive | High | High | Up |
| 5 | Negative | Low | High | Down |
| 6 | Positive | Low | Low | Down |
| 7 | Negative | High | High | Down |
| 8 | Negative | Low | High | Down |
| 9 | Positive | Low | Low | Down |
| 10 | Positive | High | High | Up |

---

### Step 1: Overall Dataset Impurity $\text{Gini}(D)$
Total instances $|D| = 10$.
Target `Return`:
- `Up`: 4 (Rows 1, 3, 4, 10)
- `Down`: 6 (Rows 2, 5, 6, 7, 8, 9)

$$\text{Gini}(D) = 1 - \left[ \left(\frac{4}{10}\right)^2 + \left(\frac{6}{10}\right)^2 \right] = 1 - [0.16 + 0.36] = \mathbf{0.4800}$$

---

### Step 2: Attribute 1 — `Past Trend` (Positive vs Negative)
- **Subset `Past Trend = Negative` ($|D| = 4$):**
  - Rows: 2, 5, 7, 8.
  - `Up`: 0, `Down`: 4 (Pure node!)

$$\text{Gini}(D_{\text{Neg}}) = 1 - \left[ \left(\frac{0}{4}\right)^2 + \left(\frac{4}{4}\right)^2 \right] = \mathbf{0.0000}$$

- **Subset `Past Trend = Positive` ($|D| = 6$):**
  - Rows: 1, 3, 4, 6, 9, 10.
  - `Up`: 4 (Rows 1, 3, 4, 10), `Down`: 2 (Rows 6, 9).

$$\text{Gini}(D_{\text{Pos}}) = 1 - \left[ \left(\frac{4}{6}\right)^2 + \left(\frac{2}{6}\right)^2 \right] = 1 - \left[ \frac{16}{36} + \frac{4}{36} \right] = \frac{16}{36} \approx \mathbf{0.4444}$$

- **Weighted Split Gini:**

$$\text{Gini}_{\text{Past Trend}}(D) = \frac{4}{10}(0.0) + \frac{6}{10}(0.4444) = \mathbf{0.2667}$$

---

### Step 3: Attribute 2 — `Open Interest` (High vs Low)
- **Subset `Open Interest = High` ($|D| = 4$):**
  - Rows: 2, 4, 7, 10.
  - `Up`: 2 (Rows 4, 10), `Down`: 2 (Rows 2, 7).

$$\text{Gini}(D_{\text{High}}) = 1 - \left[ \left(\frac{2}{4}\right)^2 + \left(\frac{2}{4}\right)^2 \right] = \mathbf{0.5000}$$

- **Subset `Open Interest = Low` ($|D| = 6$):**
  - Rows: 1, 3, 5, 6, 8, 9.
  - `Up`: 2 (Rows 1, 3), `Down`: 4 (Rows 5, 6, 8, 9).

$$\text{Gini}(D_{\text{Low}}) = 1 - \left[ \left(\frac{2}{6}\right)^2 + \left(\frac{4}{6}\right)^2 \right] = 1 - \frac{20}{36} \approx \mathbf{0.4444}$$

- **Weighted Split Gini:**

$$\text{Gini}_{\text{Open Interest}}(D) = \frac{4}{10}(0.5000) + \frac{6}{10}(0.4444) = 0.2000 + 0.2667 = \mathbf{0.4667}$$

---

### Step 4: Attribute 3 — `Trading Volume` (High vs Low)
- **Subset `Trading Volume = High` ($|D| = 7$):**
  - Rows: 1, 3, 4, 5, 7, 8, 10.
  - `Up`: 4 (Rows 1, 3, 4, 10), `Down`: 3 (Rows 5, 7, 8).

$$\text{Gini}(D_{\text{High}}) = 1 - \left[ \left(\frac{4}{7}\right)^2 + \left(\frac{3}{7}\right)^2 \right] = 1 - \frac{25}{49} = \frac{24}{49} \approx \mathbf{0.4898}$$

- **Subset `Trading Volume = Low` ($|D| = 3$):**
  - Rows: 2, 6, 9.
  - `Up`: 0, `Down`: 3 (Pure node!)

$$\text{Gini}(D_{\text{Low}}) = 1 - [0 + 1] = \mathbf{0.0000}$$

- **Weighted Split Gini:**

$$\text{Gini}_{\text{Trading Volume}}(D) = \frac{7}{10}(0.4898) + \frac{3}{10}(0.0000) = \mathbf{0.3429}$$

---

### Step 5: Summary & Root Selection

| Attribute | Weighted Split Gini Index | Gini Gain $\Delta \text{Gini}$ | Decision |
|:---|:---:|:---:|:---:|
| **`Past Trend`** | $\mathbf{0.2667}$ | $\mathbf{0.2133}$ | **ROOT NODE (Minimum Split Gini)** |
| `Trading Volume` | $0.3429$ | $0.1371$ | Subordinate |
| `Open Interest` | $0.4667$ | $0.0133$ | Subordinate |

> **Final Decision:** **`Past Trend` is chosen as the ROOT NODE** of the decision tree.

---

## MU Keyword Checklist: Module 2
- [ ] *Simple Linear Regression, OLS Closed-Form Formulas for $\beta_1$ and $\beta_0$*
- [ ] *Sum of Squared Errors (SSE), Mean Squared Error (MSE), $R^2$ Determination Coefficient*
- [ ] *Logistic Regression Sigmoid $\sigma(z) = \frac{1}{1 + e^{-z}}$, Odds Ratio, Logit Function*
- [ ] *Binary Cross-Entropy (Log-Loss) Convex Cost Function*
- [ ] *Confusion Matrix: TP, TN, FP, FN, Precision, Recall, Specificity, F1-Score*
- [ ] *ROC Curve (TPR vs FPR), Area Under Curve (AUC)*
- [ ] *Decision Tree: Gini Impurity $1 - \sum p_i^2$, Split Gini, Minimum Gini Split Criterion*
- [ ] *ID3 (Entropy/Gain) vs CART (Gini/Binary Split)*

---
---

# MODULE 3: ENSEMBLE LEARNING & MODEL VALIDATION

---

## 3.1 Understanding Ensembles: Bagging, Boosting & Stacking
*(Appeared in: Dec 2022 Q4b [10M], May 2023 Q4b [10M], May 2024 Q2b [10M], Dec 2024 Q4a [10M], May 2025 Q4b [10M])*

Ensemble learning combines multiple base estimators (weak learners) to produce a unified predictive model that outperforms any constituent model.

```
+---------------------------------------------------------------------------------------------------+
|                                  THE 3 ENSEMBLE PARADIGMS                                         |
+---------------------------------------------------------------------------------------------------+
| 1. BAGGING (Bootstrap Aggregation):                                                               |
|    - Goal: REDUCE VARIANCE of high-variance, unpruned base learners (Deep Decision Trees).         |
|    - Mechanism: Trains base learners INDEPENDENTLY and in PARALLEL on bootstrap subsets.          |
|    - Aggregation: Hard/Soft Majority Voting (Classification) or Simple Averaging (Regression).     |
|    - Archetype: Random Forest.                                                                    |
+---------------------------------------------------------------------------------------------------+
| 2. BOOSTING:                                                                                      |
|    - Goal: REDUCE BIAS of high-bias base learners (Shallow Decision Stumps).                      |
|    - Mechanism: Trains base learners SEQUENTIALLY. Each subsequent learner concentrates on        |
|      errors / misclassifications made by prior learners.                                          |
|    - Aggregation: Weighted sum of predictions based on learner accuracy.                          |
|    - Archetypes: AdaBoost, Gradient Boosted Decision Trees (GBDT), XGBoost, LightGBM.             |
+---------------------------------------------------------------------------------------------------+
| 3. STACKING (Stacked Generalization):                                                             |
|    - Goal: Exploit diverse inductive biases of heterogeneous base model families.                 |
|    - Mechanism: Level-0 models (e.g., SVM, Random Forest, Logistic Regression) generate           |
|      out-of-fold predictions. Level-1 Meta-Learner trains on these predictions to output final.   |
+---------------------------------------------------------------------------------------------------+
```

### Comprehensive Comparison: Bagging vs Boosting

| Parameter | Bagging (Bootstrap Aggregation) | Boosting |
|:---|:---|:---|
| **Primary Error Reduction** | **Variance** (eliminates overfitting). | **Bias** (turns weak learners into strong). |
| **Base Learner Type** | Complex, deep, unpruned trees (low bias, high variance). | Shallow trees / decision stumps (high bias, low variance). |
| **Execution Flow** | **Parallel / Independent**. | **Sequential / Dependent**. |
| **Data Sampling** | Bootstrap sampling with replacement (uniform weights). | Re-weights data points based on prior residual errors. |
| **Combining Mechanism** | Equal voting / arithmetic averaging. | Weighted voting based on stage performance $\alpha_t$. |
| **Overfitting Susceptibility**| Extremely robust against overfitting. | Can overfit if iterations $T$ or learning rate are too high on noisy data. |

---

## 3.2 Random Forest: Double Randomness Architecture
*(Appeared in: Dec 2022 Q4a [10M], May 2023 Q4a [10M], May 2024 Q6b [10M], Dec 2024 Q4a [10M], May 2025 Q4a [10M])*

Random Forest (Breiman, 2001) injects **double randomness** into standard Bagging to decorrelate individual trees:

```
+---------------------------------------------------------------------------------------------------+
|                                 RANDOM FOREST ARCHITECTURAL PIPELINE                              |
+---------------------------------------------------------------------------------------------------+
|  Original Training Set D (N samples, M features)                                                  |
+---------------------------------------------------------------------------------------------------+
              |                                     |                                   |
              | (Bootstrap Sample 1)                | (Bootstrap Sample 2)              | (Bootstrap Sample B)
              v                                     v                                   v
       [ D_1 (size N) ]                      [ D_2 (size N) ]                    [ D_B (size N) ]
              |                                     |                                   |
              v (At each node:                      v (At each node:                    v (At each node:
                 Pick m << M random features)          Pick m << M random features)        Pick m << M random features)
     [ Decision Tree T_1 ]                 [ Decision Tree T_2 ]               [ Decision Tree T_B ]
              |                                     |                                   |
              +-------------------------------------+-----------------------------------+
                                                    |
                                                    v
                               [ Majority Voting / Averaging Aggregator ]
                                                    |
                                                    v
                                            Final Prediction Y^
+---------------------------------------------------------------------------------------------------+
```

### The Two Sources of Randomness:
1. **Bagging of Data Points (Row Subsampling):** Each tree $T_b$ is trained on an independent bootstrap sample $D_b$ created by drawing $N$ instances with replacement from $D$.
   - *Out-of-Bag (OOB) Samples:* Approximately $(1 - \frac{1}{N})^N \approx \frac{1}{e} \approx 36.8\%$ of instances are omitted from each bootstrap sample and serve as a built-in cross-validation set.
2. **Random Subspace Method (Feature Subsampling):** At *every split node* inside each tree, only a random subset of $m$ features is considered out of total $M$ features:
   - For classification: $m = \lfloor \sqrt{M} \rfloor$
   - For regression: $m = \lfloor M / 3 \rfloor$
   - *Why decorrelation matters:* If one feature is overwhelmingly strong, every standard bagging tree will pick it as root. Subsampling features forces trees to explore alternative features, driving average tree covariance $\rho \to 0$ in the variance formula:

$$\text{Var}(\bar{T}) = \rho \sigma^2 + \frac{1 - \rho}{B} \sigma^2$$

---

## 3.3 Boosting Algorithms: AdaBoost & XGBoost Architecture
*(Appeared in: Dec 2024 Q6a [10M])*

### 1. Adaptive Boosting (AdaBoost)
- **Initialization:** Uniform sample weights $w_i^{(1)} = \frac{1}{N}$.
- **Iterative Loop ($t = 1 \dots T$):**
  1. Train weak learner $h_t(x)$ on weighted dataset.
  2. Compute weighted training error:

$$\epsilon_t = \sum_{i: h_t(x_i) \ne y_i} w_i^{(t)}$$

  3. Compute learner voting weight (stage importance):

$$\alpha_t = \frac{1}{2} \ln\left( \frac{1 - \epsilon_t}{\epsilon_t} \right)$$

  4. Update sample weights:

$$w_i^{(t+1)} = \frac{w_i^{(t)} \exp(-\alpha_t y_i h_t(x_i))}{Z_t}$$

     *(Misclassified samples receive higher weights; correctly classified samples receive lower weights).*
- **Final Strong Ensemble Classifier:**

$$H(x) = \text{sign}\left( \sum_{t=1}^T \alpha_t h_t(x) \right)$$

### 2. Extreme Gradient Boosting (XGBoost)
XGBoost optimizes an objective function containing an explicit tree complexity penalty:

$$\mathcal{L}^{(t)} = \sum_{i=1}^N l\left(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)\right) + \Omega(f_t)$$

where tree regularization is:

$$\Omega(f) = \gamma T + \frac{1}{2}\lambda \sum_{j=1}^T w_j^2$$

- $T$: Number of terminal leaf nodes.
- $w_j$: Output weight assigned to leaf $j$.
- **Second-Order Taylor Approximation:** Uses first-order gradients $g_i = \partial_{\hat{y}^{(t-1)}} l(y_i, \hat{y}^{(t-1)})$ and second-order Hessians $h_i = \partial^2_{\hat{y}^{(t-1)}} l(y_i, \hat{y}^{(t-1)})$.

---

## 3.4 Model Resampling & Validation: K-Fold Cross Validation
*(Appeared in: Dec 2023 Q3b [10M], May 2024 Q1e [5M])*

```
+---------------------------------------------------------------------------------------------------+
|                                  5-FOLD CROSS VALIDATION WORKFLOW                                 |
+---------------------------------------------------------------------------------------------------+
|  Full Dataset D (Split into 5 equal folds)                                                        |
+---------------------------------------------------------------------------------------------------+
| Iteration 1: | [ TEST FOLD 1 ] |  Train Fold 2  |  Train Fold 3  |  Train Fold 4  |  Train Fold 5  | --> Score 1
| Iteration 2: |  Train Fold 1  | [ TEST FOLD 2 ] |  Train Fold 3  |  Train Fold 4  |  Train Fold 5  | --> Score 2
| Iteration 3: |  Train Fold 1  |  Train Fold 2  | [ TEST FOLD 3 ] |  Train Fold 4  |  Train Fold 5  | --> Score 3
| Iteration 4: |  Train Fold 1  |  Train Fold 2  |  Train Fold 3  | [ TEST FOLD 4 ] |  Train Fold 5  | --> Score 4
| Iteration 5: |  Train Fold 1  |  Train Fold 2  |  Train Fold 3  |  Train Fold 4  | [ TEST FOLD 5 ] | --> Score 5
+---------------------------------------------------------------------------------------------------+
|  Overall Generalization Performance = Mean(Score 1, Score 2, Score 3, Score 4, Score 5)           |
+---------------------------------------------------------------------------------------------------+
```

### Varieties of Cross-Validation:
1. **Standard K-Fold Cross-Validation:** Partitions data randomly into $K$ disjoint folds of size $N/K$.
2. **Stratified K-Fold:** Ensures each fold maintains the identical percentage of class labels as the complete dataset (mandatory for imbalanced data).
3. **Leave-One-Out Cross-Validation (LOOCV):** Extreme variant where $K = N$. In each run, $N-1$ points train the model and exactly 1 point tests it. (Deterministic, but computationally prohibitive for large datasets).

---

## MU Keyword Checklist: Module 3
- [ ] *Bagging (Reduces Variance, Parallel) vs Boosting (Reduces Bias, Sequential) vs Stacking (Meta-Learner)*
- [ ] *Random Forest Double Randomness: Bootstrap Data Subsampling + Random Feature Subspace $m = \sqrt{M}$*
- [ ] *Out-of-Bag (OOB) Error Estimation ($36.8\%$ samples unselected)*
- [ ] *Tree Decorrelation Mechanism: $\text{Var}(\bar{T}) = \rho \sigma^2 + \frac{1-\rho}{B}\sigma^2$*
- [ ] *AdaBoost: Weighted Sample Updates, Stage Weight $\alpha_t = \frac{1}{2}\ln((1-\epsilon_t)/\epsilon_t)$*
- [ ] *XGBoost: Regularized Objective $\Omega(f) = \gamma T + \frac{1}{2}\lambda \sum w_j^2$, 2nd-Order Gradients & Hessians*
- [ ] *K-Fold Cross Validation: Equal Folds, Iterative Validation, Stratified K-Fold for Imbalanced Data*
