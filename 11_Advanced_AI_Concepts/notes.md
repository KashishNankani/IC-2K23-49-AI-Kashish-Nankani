# Advanced AI Concepts – Theory Notes

## Overview

This lab covers three advanced topics in Artificial Intelligence:

1. **PCA** — Principal Component Analysis (Dimensionality Reduction)
2. **SVD** — Singular Value Decomposition (Matrix Factorization)
3. **Adversarial AI** — FGSM Attack (Fooling Neural Networks)

---

## PART 1 — PCA (Principal Component Analysis)

### What is PCA?

PCA is a dimensionality reduction technique that transforms a dataset
with many features into a smaller number of new features called
**Principal Components**, while retaining as much information
(variance) as possible.

It is used when datasets have too many features — which causes
slow training, overfitting, and difficulty in visualization.

### Why Do We Need It?

- Real datasets can have hundreds or thousands of features
- Many features are correlated and carry redundant information
- PCA compresses the data while keeping the most important patterns
- Allows us to visualize high-dimensional data in 2D or 3D

### How PCA Works

1. **Standardize** the data — subtract mean and divide by std
2. **Compute the Covariance Matrix** — shows how features vary together
3. **Find Eigenvectors and Eigenvalues** — eigenvectors are the
   principal components; eigenvalues tell us how much variance each
   component captures
4. **Sort by Eigenvalue** — highest eigenvalue = most important component
5. **Project the data** onto the top k principal components

### Explained Variance Ratio

This tells us what percentage of the original information is kept
after reduction. For example:

```
PC1 explains 72.96% of variance
PC2 explains 22.85% of variance
Total = 95.81% — most information is preserved
```

### Key Points

- Principal components are **orthogonal** (perpendicular to each other)
- The first component captures the most variance
- PCA is **unsupervised** — it does not use class labels
- Used as a preprocessing step before training ML models

---

## PART 2 — SVD (Singular Value Decomposition)

### What is SVD?

SVD is a fundamental matrix factorization technique from linear algebra.
It decomposes any matrix A into three matrices:

```
A = U × Σ × Vᵀ
```

Where:
- **U** — Left singular vectors (orthogonal matrix)
- **Σ (S)** — Diagonal matrix of singular values (non-negative)
- **Vᵀ** — Right singular vectors transposed (orthogonal matrix)

### What are Singular Values?

Singular values (the diagonal of Σ) represent the "importance" of
each component. Larger singular values carry more information.

By keeping only the top k singular values and setting the rest to
zero, we get a low-rank approximation of the original matrix —
this is exactly how image compression works.

### Relationship Between PCA and SVD

PCA is actually computed using SVD internally. The principal
components of PCA are the right singular vectors (V), and the
explained variance comes from the singular values squared.

### Applications of SVD

- **Image Compression** — approximate images with fewer components
- **Recommendation Systems** — Netflix uses SVD-based methods
- **Noise Reduction** — remove small singular values to clean data
- **Latent Semantic Analysis** — finding hidden topics in documents

---

## PART 3 — Adversarial AI (FGSM Attack)

### What is Adversarial AI?

Adversarial AI studies how machine learning models can be fooled by
carefully crafted inputs called **adversarial examples**. These are
inputs that look perfectly normal to humans but cause AI models to
make completely wrong predictions with high confidence.

For example: an image of a panda that looks normal to us but a
neural network classifies as a "gibbon" with 99% confidence — just
because tiny invisible noise was added.

### Why Does This Matter?

- Autonomous cars could misread a stop sign
- Face recognition systems could be fooled
- Medical AI could misdiagnose a patient
- Security systems could be bypassed

Understanding adversarial attacks is crucial for building safe and
robust AI systems.

### FGSM — Fast Gradient Sign Method

FGSM is one of the simplest and most well-known adversarial attacks,
proposed by Goodfellow et al. in 2014.

The idea is simple: instead of training the model to reduce the loss,
we take a small step **in the direction that increases the loss** —
making the model more wrong.

**Formula:**
```
x_adversarial = x + ε × sign(∇_x J(θ, x, y))
```

Where:
- **x** — original input image
- **ε (epsilon)** — small perturbation strength (e.g. 0.1)
- **∇_x J** — gradient of the loss with respect to the input
- **sign()** — just the direction (+1 or -1) of the gradient

### Step-by-Step

1. Take the original image x and its true label y
2. Do a forward pass to get the model's prediction and loss
3. Compute the gradient of the loss with respect to the input pixels
4. Take the sign of the gradient (direction of steepest increase)
5. Add a small scaled perturbation to the original image
6. Clip pixel values to stay in valid range [0, 1]

### Effect of Epsilon

| Epsilon | Effect |
|---------|--------|
| 0.01 | Almost invisible change, mild effect |
| 0.1 | Slight noise visible, strong effect on model |
| 0.3 | Noticeable noise, model almost always wrong |

### Defenses Against Adversarial Attacks

- **Adversarial Training** — train the model on adversarial examples
- **Input Preprocessing** — smooth or denoise inputs before classifying
- **Certified Defenses** — mathematically guaranteed robustness
- **Detection Methods** — detect adversarial inputs before classifying

---

## Summary Table

| Technique | Type | Purpose |
|-----------|------|---------|
| PCA | Unsupervised | Reduce dimensions, visualize data |
| SVD | Linear Algebra | Matrix factorization, compression |
| FGSM | Adversarial Attack | Fool neural networks with tiny noise |

---

## Real-World Applications

- **PCA** — face recognition (Eigenfaces), gene expression analysis
- **SVD** — Netflix recommendations, document topic modelling
- **Adversarial AI** — robustness testing of self-driving cars,
  medical imaging systems, security applications