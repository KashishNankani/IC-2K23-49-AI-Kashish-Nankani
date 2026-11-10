import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# ════════════════════════════════════════════════════════════════════════════
# PART 1 — PCA (Principal Component Analysis)
# ════════════════════════════════════════════════════════════════════════════

print("=" * 50)
print("PART 1 — PCA (Dimensionality Reduction)")
print("=" * 50)

iris = load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA — reduce from 4 dimensions to 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"Original shape : {X.shape}")
print(f"Reduced shape  : {X_pca.shape}")
print(f"Explained Variance Ratio: {pca.explained_variance_ratio_}")
print(f"Total Variance Explained: {sum(pca.explained_variance_ratio_)*100:.2f}%")

# Plot PCA result
plt.figure(figsize=(7, 5))
colors = ['red', 'green', 'blue']
for i, (color, label) in enumerate(zip(colors, class_names)):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1],
                color=color, label=label, alpha=0.7, edgecolors='k', s=60)
plt.title("PCA — Iris Dataset (4D → 2D)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.tight_layout()
plt.savefig("pca_output.png")
plt.show()
print("PCA plot saved as pca_output.png\n")


# ════════════════════════════════════════════════════════════════════════════
# PART 2 — SVD (Singular Value Decomposition)
# ════════════════════════════════════════════════════════════════════════════

print("=" * 50)
print("PART 2 — SVD (Matrix Decomposition)")
print("=" * 50)

# Create a simple matrix
A = np.array([
    [3, 1, 1],
    [-1, 3, 1]
], dtype=float)

print(f"Original Matrix A:\n{A}\n")

# Perform SVD
U, S, Vt = np.linalg.svd(A)

print(f"U (Left Singular Vectors):\n{U}\n")
print(f"S (Singular Values): {S}\n")
print(f"Vt (Right Singular Vectors Transposed):\n{Vt}\n")

# Reconstruct A from U, S, Vt
S_matrix = np.zeros(A.shape)
for i in range(len(S)):
    S_matrix[i, i] = S[i]

A_reconstructed = U @ S_matrix @ Vt
print(f"Reconstructed Matrix:\n{np.round(A_reconstructed, 4)}")
print(f"Reconstruction successful: {np.allclose(A, A_reconstructed)}\n")


# ════════════════════════════════════════════════════════════════════════════
# PART 3 — Adversarial Example (FGSM — Fast Gradient Sign Method)
# ════════════════════════════════════════════════════════════════════════════

print("=" * 50)
print("PART 3 — Adversarial AI (FGSM)")
print("=" * 50)

def fgsm_attack(image, epsilon, gradient):
    """Add adversarial perturbation to an image using FGSM."""
    perturbation = epsilon * np.sign(gradient)
    adversarial_image = image + perturbation
    adversarial_image = np.clip(adversarial_image, 0, 1)
    return adversarial_image, perturbation

# Simulate a simple grayscale image (8x8) and a fake gradient
np.random.seed(42)
original_image = np.random.rand(8, 8)
fake_gradient   = np.random.randn(8, 8)
epsilon         = 0.1

adversarial_image, perturbation = fgsm_attack(original_image, epsilon, fake_gradient)

print(f"Epsilon (perturbation strength): {epsilon}")
print(f"Max pixel change: {np.max(np.abs(perturbation)):.4f}")
print(f"Mean pixel difference: {np.mean(np.abs(adversarial_image - original_image)):.4f}\n")

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].imshow(original_image,    cmap='gray', vmin=0, vmax=1)
axes[0].set_title("Original Image")
axes[0].axis('off')

axes[1].imshow(perturbation,      cmap='RdBu', vmin=-epsilon, vmax=epsilon)
axes[1].set_title(f"Perturbation (ε={epsilon})")
axes[1].axis('off')

axes[2].imshow(adversarial_image, cmap='gray', vmin=0, vmax=1)
axes[2].set_title("Adversarial Image")
axes[2].axis('off')

plt.suptitle("FGSM Adversarial Attack", fontsize=13)
plt.tight_layout()
plt.savefig("adversarial_output.png")
plt.show()
print("Adversarial plot saved as adversarial_output.png")