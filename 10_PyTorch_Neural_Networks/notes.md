# Neural Networks with PyTorch – Theory Notes

## What is a Neural Network?

A Neural Network is a machine learning model inspired by the structure
of the human brain. It consists of layers of interconnected nodes called
**neurons**. Each neuron receives inputs, applies a mathematical
transformation, and passes the result to the next layer.

Neural networks are especially powerful for complex tasks like image
recognition, language processing, and pattern detection where traditional
algorithms struggle.

---

## Why PyTorch?

PyTorch is an open-source deep learning framework developed by Facebook AI.
It is widely used in research and industry because:

- It uses **dynamic computation graphs** — the graph is built on the fly
- Very Pythonic and easy to debug
- Excellent support for GPU acceleration
- Industry standard alongside TensorFlow

---

## Key Concepts

### Neuron
A single unit that takes inputs, multiplies each by a **weight**, adds
a **bias**, and passes the result through an **activation function**.

```
output = activation(w1*x1 + w2*x2 + ... + wn*xn + bias)
```

### Layers

| Layer | Role |
|-------|------|
| Input Layer | Receives raw features (4 for Iris dataset) |
| Hidden Layers | Learn patterns from data |
| Output Layer | Produces final predictions (3 classes) |

### Activation Functions
Activation functions add non-linearity to the network, allowing it
to learn complex patterns.

**ReLU (Rectified Linear Unit)** — used in hidden layers:
```
ReLU(x) = max(0, x)
```
It outputs 0 for negative values and x for positive. Simple and effective.

**Softmax** — used implicitly in CrossEntropyLoss for the output layer:
Converts raw scores into probabilities that sum to 1.

### Weights and Biases
These are the learnable parameters of the network. Training adjusts
them to minimize the error (loss).

---

## Architecture Used in This Lab

```
Input (4) → Linear(4→16) → ReLU → Linear(16→12) → ReLU → Linear(12→3)
```

- **Input**: 4 features (sepal/petal length and width)
- **Hidden Layer 1**: 16 neurons + ReLU
- **Hidden Layer 2**: 12 neurons + ReLU
- **Output**: 3 neurons (one per Iris class)

---

## Training Process

### 1. Forward Pass
Input data is passed through all layers from left to right to get a
prediction (output).

### 2. Loss Calculation
The loss function measures how wrong the prediction is compared to
the actual label.

**Cross-Entropy Loss** (used here) — standard for classification:
```
Loss = -Σ y_true × log(y_predicted)
```
Higher loss = worse prediction. We want to minimize this.

### 3. Backward Pass (Backpropagation)
The gradient of the loss with respect to each weight is calculated
using the chain rule. This tells us how much each weight contributed
to the error.

### 4. Weight Update (Gradient Descent)
The optimizer adjusts the weights to reduce the loss:
```
weight = weight - learning_rate × gradient
```

**Adam Optimizer** (used here) — an advanced optimizer that adapts
the learning rate for each parameter automatically. Better than
basic gradient descent.

### 5. Repeat
Steps 1–4 are repeated for every **epoch** (one full pass through
the training data) until the loss is sufficiently low.

---

## Important Terms

| Term | Meaning |
|------|---------|
| Epoch | One complete pass through the entire training dataset |
| Batch Size | Number of samples processed before updating weights |
| Learning Rate | How big a step to take when updating weights |
| Loss | Measure of how wrong the model's predictions are |
| Gradient | Direction and rate of steepest increase in loss |
| Backpropagation | Algorithm to calculate gradients layer by layer |

---

## Data Preprocessing for Neural Networks

Neural networks are sensitive to the scale of input features. We use
**StandardScaler** to normalize features to mean=0 and std=1:

```
x_scaled = (x - mean) / std_deviation
```

This ensures no single feature dominates training due to its scale.

---

## PyTorch Workflow Summary

```python
# 1. Define model
model = MyNet()

# 2. Define loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 3. Training loop
for epoch in range(epochs):
    optimizer.zero_grad()   # clear old gradients
    output = model(X)       # forward pass
    loss = criterion(output, y)  # compute loss
    loss.backward()         # backpropagation
    optimizer.step()        # update weights

# 4. Evaluation
model.eval()
with torch.no_grad():
    predictions = model(X_test)
```

---

## Advantages and Disadvantages

| Advantages | Disadvantages |
|------------|---------------|
| Learns complex non-linear patterns | Requires large amounts of data |
| Very flexible architecture | Hard to interpret (black box) |
| State of the art for many tasks | Computationally expensive |
| Automatically learns features | Many hyperparameters to tune |

---

## Real-World Applications

- **Image Recognition** — identifying objects in photos
- **Natural Language Processing** — translation, chatbots, summarization
- **Medical Imaging** — detecting tumours in X-rays and MRI scans
- **Speech Recognition** — converting speech to text
- **Recommendation Systems** — Netflix, YouTube suggestions