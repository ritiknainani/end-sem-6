# 📘 QA ULTIMATE FULL-MARKS THEORY GUIDE — Modules 5 & 6

---

# MODULE 5: STATISTICAL INFERENCE

---

## Q20. What is a Random Sample? Explain Parametric Point Estimation in detail with its characteristics. [10 Marks] — 4/5

### a) Core Concept
A **random sample** is a set of n observations (X₁, X₂, ..., Xₙ) drawn from a population such that each observation is **independently** selected and each has an **equal probability** of being chosen. **Point estimation** uses a single value (statistic) computed from the sample to estimate an unknown population parameter.

### b) Detailed Explanation

**Key Terminology:**
| Term | Symbol | Example |
|------|--------|---------|
| **Parameter** | θ | Population mean μ, population variance σ² |
| **Statistic** | T(X) | Sample mean x̄, sample variance S² |
| **Estimator** | θ̂ | The formula/rule used to estimate θ |
| **Estimate** | θ̂ₒ | The specific numerical value from a particular sample |

### Four Desirable Properties (Characteristics):

### 1. UNBIASEDNESS
```
Definition: E(θ̂) = θ

An estimator is unbiased if its expected value equals
the true parameter value.

Bias = E(θ̂) − θ
If Bias = 0 → Unbiased
```

**Proof that S² is unbiased for σ²:**
```
S² = ∑(Xᵢ − X̄)² / (n−1)

Step 1: Expand
∑(Xᵢ − X̄)² = ∑Xᵢ² − nX̄²

Step 2: Take expectation
E[∑Xᵢ²] = n(σ² + μ²)       [since E(Xᵢ²) = Var(Xᵢ) + [E(Xᵢ)]²]
E[nX̄²]  = n(σ²/n + μ²)     [since E(X̄²) = Var(X̄) + [E(X̄)]²]
         = σ² + nμ²

Step 3: Subtract
E[∑(Xᵢ − X̄)²] = n(σ² + μ²) − (σ² + nμ²)
                = nσ² + nμ² − σ² − nμ²
                = (n−1)σ²

Step 4: Divide by (n−1)
E[S²] = E[∑(Xᵢ − X̄)²/(n−1)] = (n−1)σ²/(n−1) = σ²  ✅

Note: ∑(Xᵢ−X̄)²/n is BIASED because E[it] = (n−1)σ²/n ≠ σ²
This is WHY we divide by (n−1), not n.
```

### 2. CONSISTENCY
```
Definition: As n → ∞, θ̂ₙ converges in probability to θ

P(|θ̂ₙ − θ| < ε) → 1 as n → ∞, for any ε > 0

Sufficient conditions:
  (i)  lim E(θ̂ₙ) = θ       (asymptotically unbiased)
  (ii) lim Var(θ̂ₙ) = 0      (variance shrinks to zero)
```

**Example:** X̄ is consistent for μ because:
- E(X̄) = μ (unbiased for all n)
- Var(X̄) = σ²/n → 0 as n → ∞

### 3. EFFICIENCY
```
Definition: Among all unbiased estimators, the one with
MINIMUM VARIANCE is most efficient.

Relative Efficiency = Var(θ̂₁) / Var(θ̂₂)

Cramér-Rao Lower Bound (CRLB):
Var(θ̂) ≥ 1 / I(θ)

Where I(θ) = −E[∂²ln f(X|θ)/∂θ²] = Fisher Information

An estimator achieving CRLB is called "efficient" or
"minimum variance unbiased estimator (MVUE)".
```

### 4. SUFFICIENCY
```
Definition: T(X) is sufficient for θ if it captures ALL
information in the sample about θ — no other statistic
computed from the data can provide additional information.

Fisher-Neyman Factorization Theorem:
T is sufficient for θ if and only if the joint pdf can
be written as:

f(x₁,...,xₙ|θ) = g(T(x), θ) × h(x₁,...,xₙ)

Where:
g depends on data ONLY through T
h does not depend on θ at all
```

**Example:** For Normal(μ, σ²), X̄ is sufficient for μ.

---

## Q21. Explain the Method of Moments. [5 Marks]

### a) Core Concept
The **Method of Moments (MOM)** estimates population parameters by equating **sample moments** to corresponding **population (theoretical) moments** and solving the resulting equations.

### b) Procedure
```
Step 1: Compute sample moments
  m₁ = (1/n)∑Xᵢ = X̄              (first sample moment)
  m₂ = (1/n)∑Xᵢ²                  (second sample moment)

Step 2: Write population moments in terms of parameters
  μ₁' = E(X)                       (first population moment)
  μ₂' = E(X²)                      (second population moment)

Step 3: Set m₁ = μ₁', m₂ = μ₂'

Step 4: Solve for unknown parameters
```

### Example — Normal Distribution N(μ, σ²):
```
m₁ = X̄ = E(X) = μ   →   μ̂ = X̄

m₂ = (1/n)∑Xᵢ² = E(X²) = σ² + μ²
→ σ̂² = m₂ − m₁² = (1/n)∑Xᵢ² − X̄²
→ σ̂² = (1/n)∑(Xᵢ − X̄)²
```

Note: MOM estimate of σ² divides by n (biased), unlike the unbiased S² which divides by (n−1).

**Advantages:** Simple, always provides an estimate, works for complex distributions
**Disadvantages:** May be biased, not always efficient, may give estimates outside parameter space

---

## Q22. Explain the Method of Maximum Likelihood Estimation (MLE). [10 Marks] — 3/5

### a) Core Concept
**MLE** finds the parameter value θ̂ that **maximizes the probability (likelihood)** of observing the given sample data. It answers: "Which parameter value makes the observed data most probable?"

### b) Step-by-Step Procedure
```
Step 1: Write the LIKELIHOOD FUNCTION
  L(θ) = ∏ᵢ₌₁ⁿ f(xᵢ | θ) = f(x₁|θ) × f(x₂|θ) × ... × f(xₙ|θ)

Step 2: Take the LOG-LIKELIHOOD (simplifies products to sums)
  ln L(θ) = ∑ᵢ₌₁ⁿ ln f(xᵢ | θ)

Step 3: DIFFERENTIATE with respect to θ and set equal to zero
  d[ln L(θ)] / dθ = 0

Step 4: SOLVE for θ̂ (the MLE)

Step 5: VERIFY it is a maximum
  d²[ln L(θ)] / dθ² < 0 at θ = θ̂
```

### Example — MLE for Normal Distribution Mean:
```
Given: X₁, X₂, ..., Xₙ ~ N(μ, σ²), find MLE for μ.

L(μ) = ∏ (1/σ√2π) exp[−(xᵢ−μ)²/2σ²]

ln L = −(n/2)ln(2π) − (n/2)ln(σ²) − ∑(xᵢ−μ)²/(2σ²)

d(ln L)/dμ = ∑(xᵢ−μ)/σ² = 0
→ ∑xᵢ − nμ = 0
→ μ̂ = ∑xᵢ/n = X̄

d²(ln L)/dμ² = −n/σ² < 0 → Confirmed maximum ✅
```

**MLE for μ is X̄ (sample mean)**

### Properties of MLE:
| Property | Details |
|----------|---------|
| **Consistency** | θ̂_MLE → θ as n → ∞ |
| **Asymptotic efficiency** | Achieves CRLB for large samples |
| **Asymptotic normality** | θ̂ ~ N(θ, 1/I(θ)) for large n |
| **Invariance** | If θ̂ is MLE of θ, then g(θ̂) is MLE of g(θ) |
| **May be biased** | For small samples, MLE can be biased |
| **Not always easy** | May require numerical methods for complex distributions |

---

# MODULE 6: TESTS OF HYPOTHESES

---

## Q23. Explain Null and Alternative Hypotheses in detail. [5-10 Marks] — 2/5

### a) Core Concept
A **hypothesis** is a statement about a population parameter. **Null hypothesis (H₀)** asserts "no effect/difference" and is assumed true until evidence against it. **Alternative hypothesis (H₁)** is the claim the researcher wants to prove.

### f) Comparison Table

| Parameter | Null Hypothesis (H₀) | Alternative Hypothesis (H₁) |
|-----------|----------------------|----------------------------|
| **Statement** | No effect, no difference, status quo | Effect exists, difference is real |
| **Contains** | Equality: =, ≤, or ≥ | Inequality: ≠, <, or > |
| **Assumed** | True until evidence disproves it | Accepted only when H₀ is rejected |
| **Burden** | On the researcher to reject | Accepted passively when H₀ is rejected |
| **Example** | H₀: μ = 500 | H₁: μ ≠ 500 (two-tailed) |
| **Risk of wrong rejection** | Type I Error (α) | Type II Error (β) if H₀ falsely accepted |

### Types of Tests:
```
One-tailed (Right):  H₀: μ ≤ μ₀   vs   H₁: μ > μ₀
One-tailed (Left):   H₀: μ ≥ μ₀   vs   H₁: μ < μ₀
Two-tailed:          H₀: μ = μ₀    vs   H₁: μ ≠ μ₀
```

---

## Q24. Explain Type I and Type II Errors in detail. [5-10 Marks] — QB

### a) Core Concept
Statistical hypothesis testing can produce two types of errors: rejecting a true null hypothesis (**Type I**) or failing to reject a false null hypothesis (**Type II**).

### c) Decision Matrix Diagram
```
                    ┌─────────────────┬──────────────────┐
                    │  H₀ is TRUE     │  H₀ is FALSE     │
┌───────────────────┼─────────────────┼──────────────────┤
│ REJECT H₀         │ TYPE I ERROR    │ CORRECT DECISION │
│                   │ (α = False      │ (Power = 1 − β)  │
│                   │  Positive)      │                  │
├───────────────────┼─────────────────┼──────────────────┤
│ FAIL TO REJECT H₀ │ CORRECT         │ TYPE II ERROR    │
│                   │ DECISION        │ (β = False       │
│                   │ (Confidence     │  Negative)       │
│                   │  = 1 − α)       │                  │
└───────────────────┴─────────────────┴──────────────────┘
```

### d) Formulas
```
α = P(Type I Error) = P(Reject H₀ | H₀ is true)
β = P(Type II Error) = P(Fail to reject H₀ | H₀ is false)
Power = 1 − β = P(Reject H₀ | H₀ is false)
```

### Relationship:
- As α decreases → β increases (trade-off)
- Increasing **sample size n** → both α and β can be reduced simultaneously
- α is set by the researcher (typically 0.05 or 0.01)

### e) Real-World Examples:
| | Type I (False Positive) | Type II (False Negative) |
|---|---|---|
| **Medical** | Diagnosing disease when patient is healthy | Missing a disease when patient is actually sick |
| **Legal** | Convicting an innocent person | Acquitting a guilty person |
| **Quality** | Rejecting a good batch | Accepting a defective batch |

---

## Q25. Differentiate: Critical Region and Region of Acceptance. [5-10 Marks] — 2/5

### c) Diagram
```
Two-Tailed Test (α = 0.05):

         Rejection     Acceptance        Rejection
          Region         Region            Region
         (α/2)          (1−α)             (α/2)
         ┌──┐    ┌────────────────┐    ┌──┐
    ─────┘  └────┘                └────┘  └─────
        −Z_c                          +Z_c
       (−1.96)                       (+1.96)

One-Tailed Test (Right, α = 0.05):

         Acceptance Region              Rejection
              (1−α)                      (α)
    ┌──────────────────────────┐    ┌──┐
    └──────────────────────────└────┘  └─────
                                   Z_c
                                 (+1.645)
```

### f) Comparison Table

| Parameter | Critical Region | Region of Acceptance |
|-----------|----------------|---------------------|
| **Definition** | Values of test statistic leading to **rejection** of H₀ | Values where H₀ is **not rejected** |
| **Also called** | Rejection region | Non-rejection region |
| **Location** | Tail(s) of the distribution | Central area of the distribution |
| **Area** | = α (significance level) | = 1 − α (confidence level) |
| **Decision** | If test stat falls here → **Reject H₀** | If test stat falls here → **Fail to reject H₀** |
| **Boundary** | Defined by critical value(s) from statistical tables | Between the critical values |

---

## Q26. Explain the Neyman-Pearson Lemma in detail. [10 Marks] — 3/5

### a) Core Concept
The **Neyman-Pearson Lemma** provides the theoretical foundation for constructing the **most powerful (MP) test** of a simple null hypothesis against a simple alternative hypothesis at a given significance level α.

### b) Formal Statement

For testing **H₀: θ = θ₀** vs **H₁: θ = θ₁** (simple vs simple):

The **most powerful test** of size α is the **Likelihood Ratio Test** with critical region:

```
           L(θ₁ | x)
C = {x : ─────────── ≥ k}
           L(θ₀ | x)

Where:
L(θ₀ | x) = ∏ f(xᵢ | θ₀) = Likelihood under H₀
L(θ₁ | x) = ∏ f(xᵢ | θ₁) = Likelihood under H₁
k = constant determined such that P(X ∈ C | H₀) = α
```

### Interpretation:
- Reject H₀ when the **likelihood ratio** (data is more likely under H₁ than H₀) exceeds threshold k
- This test **maximizes power** (1−β) among all tests with the same significance level α
- No other test of the same size can have higher power against the specific H₁

### c) Flowchart
```
┌──────────────────────┐
│ Define H₀: θ = θ₀    │
│ Define H₁: θ = θ₁    │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Compute Likelihood    │
│ Ratio: Λ = L(θ₁)/L(θ₀)│
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Find critical value k │
│ such that             │
│ P(Λ ≥ k | H₀) = α    │
└──────────┬───────────┘
           ▼
    ┌──────┴──────┐
    │  Λ ≥ k?     │
    └──┬──────┬───┘
    Yes│      │No
       ▼      ▼
  Reject H₀  Fail to
  (H₁ true)  reject H₀
```

### Key Results:
1. The test is **most powerful** at level α for the given H₁
2. If this MP test also has the highest power for **all values** of θ in H₁ → it's a **UMP test**
3. Foundation of all modern hypothesis testing theory

---

## Q27. Explain MP and UMP Tests. [5-10 Marks] — Dec 2024

### a) Core Concept
**MP (Most Powerful)** test is the test with the highest probability of correctly rejecting H₀ (highest power) for a specific alternative. **UMP (Uniformly Most Powerful)** test maintains highest power across all possible alternative values.

### f) Comparison Table

| Parameter | MP Test | UMP Test |
|-----------|---------|----------|
| **Full Form** | Most Powerful Test | Uniformly Most Powerful Test |
| **Alternative** | Works for **specific** H₁: θ = θ₁ | Works for **all** values in H₁: θ > θ₀ or θ < θ₀ |
| **Derived via** | Neyman-Pearson Lemma | Extension of N-P Lemma |
| **Power** | Maximized for ONE specific θ₁ | Maximized for ALL θ₁ simultaneously |
| **Existence** | Always exists (by N-P Lemma) | May NOT exist (especially for two-tailed tests) |
| **Best for** | Simple vs Simple hypotheses | One-sided composite alternatives |
| **Condition** | N-P Lemma applies directly | Exists mainly for **Monotone Likelihood Ratio (MLR)** families |

### When UMP exists:
- **Exponential family** distributions (Normal, Exponential, Binomial, Poisson)
- **One-sided** alternatives only (H₁: θ > θ₀ or H₁: θ < θ₀)
- For **two-sided** alternatives (H₁: θ ≠ θ₀), UMP generally does NOT exist

---

## Q28. What is Hypothesis Testing? Explain Z-Test for Single Mean and Difference of Means. [10 Marks] — 2/5

### a) Core Concept
**Hypothesis testing** is a systematic statistical procedure to determine whether there is sufficient evidence in a sample to reject a claim (null hypothesis) about a population parameter.

### b) Steps of Hypothesis Testing
```
Step 1: State H₀ and H₁
Step 2: Choose significance level (α = 0.05 or 0.01)
Step 3: Select test statistic (Z, t, F, χ²)
Step 4: Calculate test statistic from sample data
Step 5: Determine critical value from table
Step 6: Decision — Compare and conclude
```

### Z-Test for Single Mean:
```
Used when: n ≥ 30 or σ is known

         x̄ − μ₀
Z = ─────────────
       σ / √n

x̄  = sample mean
μ₀ = hypothesized population mean
σ  = population standard deviation (or s for large n)
n  = sample size
```

### Z-Test for Difference of Two Means:
```
Used when: Comparing means of two independent populations

        (x̄₁ − x̄₂) − (μ₁ − μ₂)₀
Z = ─────────────────────────────────
       √(σ₁²/n₁ + σ₂²/n₂)

Under H₀: μ₁ = μ₂  (so (μ₁−μ₂)₀ = 0):

         x̄₁ − x̄₂
Z = ───────────────────
    √(σ₁²/n₁ + σ₂²/n₂)
```

### Critical Values Reference:
| α | One-tailed | Two-tailed |
|---|-----------|-----------|
| 0.10 | ±1.28 | ±1.645 |
| 0.05 | ±1.645 | ±1.96 |
| 0.01 | ±2.33 | ±2.576 |
