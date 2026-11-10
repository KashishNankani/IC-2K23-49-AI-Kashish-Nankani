# Decision Tree Classifier – Theory Notes

## What is a Decision Tree?

A Decision Tree is a supervised machine learning algorithm that makes
decisions by splitting data into branches based on feature values. It
looks like a flowchart — starting from a root node, it asks questions
at each internal node, follows the appropriate branch, and reaches a
leaf node that gives the final prediction.

It can be used for both **classification** (predicting a category) and
**regression** (predicting a number). In this lab we use it for
classification.

---

## How Does a Decision Tree Work?

The tree is built by recursively splitting the dataset into smaller
subsets based on the feature that best separates the classes. The goal
at each split is to make the resulting groups as **pure** as possible
— meaning each group ideally contains only one class.

### Key Terms

**Root Node** — the topmost node, represents the entire dataset and
the first (best) split.

**Internal Node** — a node that represents a question/condition on a
feature. Example: "Is petal length ≤ 2.45?"

**Branch** — the outcome of a condition (Yes/No, True/False).

**Leaf Node** — the final node with no more splits, gives the
predicted class.

**Depth** — the number of levels in the tree. Deeper trees can
overfit the training data.

---

## Splitting Criteria

The algorithm chooses which feature to split on based on a measure
of impurity. Two common measures are:

### Gini Impurity (used in this lab)
Measures how often a randomly chosen element would be incorrectly
classified. Lower Gini = purer node.

```
Gini = 1 - Σ(p_i)²
```

Where p_i is the proportion of class i in the node.

- Gini = 0 → perfectly pure (all one class)
- Gini = 0.5 → maximally impure (equal mix of classes)

### Information Gain (Entropy)
Measures the reduction in uncertainty after a split.

```
Entropy = -Σ p_i × log2(p_i)
```

The feature with the highest information gain is chosen for the split.

---

## Algorithm Steps

1. Start with the full dataset at the root
2. For each feature, calculate Gini impurity or Information Gain
3. Choose the feature with the best split (lowest Gini or highest IG)
4. Split the data into subsets based on that feature
5. Recursively repeat for each subset
6. Stop when:
   - All samples in a node belong to one class (pure node)
   - Maximum depth is reached
   - Minimum samples threshold is reached

---

## Dataset Used — Iris Flower Classification

The Iris dataset is one of the most famous datasets in machine learning.

| Feature | Description |
|---------|-------------|
| Sepal Length | Length of the sepal (cm) |
| Sepal Width | Width of the sepal (cm) |
| Petal Length | Length of the petal (cm) |
| Petal Width | Width of the petal (cm) |

**Classes (3):** Setosa, Versicolor, Virginica
**Samples:** 150 total (50 per class)

---

## Model Evaluation Metrics

### Accuracy
Percentage of correct predictions out of total predictions.
```
Accuracy = Correct Predictions / Total Predictions × 100
```

### Confusion Matrix
A table showing actual vs predicted values for each class.

|              | Predicted A | Predicted B |
|--------------|-------------|-------------|
| **Actual A** | TP          | FN          |
| **Actual B** | FP          | TN          |

### Classification Report
Gives precision, recall, and F1-score per class.

- **Precision** — of all predicted positives, how many were correct
- **Recall** — of all actual positives, how many were found
- **F1-Score** — harmonic mean of precision and recall

---

## Overfitting and Max Depth

A deep tree memorizes training data but performs poorly on new data.
This is called **overfitting**. We control it using `max_depth`.

| max_depth | Effect |
|-----------|--------|
| Too small | Underfitting — model too simple |
| Just right | Good generalization |
| Too large | Overfitting — memorizes training data |

---

## Advantages and Disadvantages

| Advantages | Disadvantages |
|------------|---------------|
| Easy to understand and visualize | Can overfit without pruning |
| No need for feature scaling | Sensitive to small data changes |
| Works with numerical and categorical data | Biased with imbalanced datasets |
| Fast to train and predict | Not the best for complex relationships |

---

## Real-World Applications

- **Medical Diagnosis** — classifying diseases based on symptoms
- **Credit Scoring** — approving or rejecting loan applications
- **Email Spam Detection** — classifying emails as spam or not
- **Customer Segmentation** — grouping customers by behaviour
- **Fault Detection** — identifying errors in systems