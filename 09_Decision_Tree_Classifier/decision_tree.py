from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
from sklearn import tree

# ── 1. Load Dataset ──────────────────────────────────────────────────────────
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
class_names = iris.target_names

print("Dataset: Iris Flower Classification")
print(f"Features: {feature_names}")
print(f"Classes: {class_names}")
print(f"Total Samples: {len(X)}\n")

# ── 2. Split into Train and Test ─────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Training samples: {len(X_train)}")
print(f"Testing samples:  {len(X_test)}\n")

# ── 3. Train the Decision Tree ───────────────────────────────────────────────
clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# ── 4. Evaluate ──────────────────────────────────────────────────────────────
y_pred = clf.predict(X_test)

print("=" * 50)
print("MODEL EVALUATION")
print("=" * 50)
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=class_names))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ── 5. Print the Tree Rules ──────────────────────────────────────────────────
print("\n" + "=" * 50)
print("DECISION TREE RULES")
print("=" * 50)
print(export_text(clf, feature_names=feature_names))

# ── 6. Predict a New Sample ──────────────────────────────────────────────────
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = clf.predict(sample)
print(f"Prediction for sample {sample[0]}: {class_names[prediction[0]]}")

# ── 7. Visualize the Tree ────────────────────────────────────────────────────
plt.figure(figsize=(14, 6))
tree.plot_tree(clf,
               feature_names=feature_names,
               class_names=class_names,
               filled=True,
               rounded=True,
               fontsize=10)
plt.title("Decision Tree — Iris Dataset")
plt.tight_layout()
plt.savefig("decision_tree.png")
plt.show()
print("\nTree saved as decision_tree.png")