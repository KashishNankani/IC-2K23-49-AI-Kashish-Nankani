import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# ── 1. Load and Prepare Data ─────────────────────────────────────────────────
iris = load_iris()
X = iris.data
y = iris.target

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert to PyTorch tensors
X_train = torch.FloatTensor(X_train)
X_test  = torch.FloatTensor(X_test)
y_train = torch.LongTensor(y_train)
y_test  = torch.LongTensor(y_test)

train_dataset = TensorDataset(X_train, y_train)
train_loader  = DataLoader(train_dataset, batch_size=16, shuffle=True)

print("Dataset: Iris Flower Classification via Neural Network")
print(f"Training samples: {len(X_train)} | Test samples: {len(X_test)}\n")

# ── 2. Define the Neural Network ─────────────────────────────────────────────
class IrisNet(nn.Module):
    def __init__(self):
        super(IrisNet, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(4, 16),     # Input layer: 4 features → 16 neurons
            nn.ReLU(),
            nn.Linear(16, 12),    # Hidden layer: 16 → 12 neurons
            nn.ReLU(),
            nn.Linear(12, 3)      # Output layer: 12 → 3 classes
        )

    def forward(self, x):
        return self.network(x)

model = IrisNet()
print("Model Architecture:")
print(model)

# ── 3. Loss Function and Optimizer ───────────────────────────────────────────
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# ── 4. Training Loop ─────────────────────────────────────────────────────────
epochs = 100
train_losses = []

print("\nTraining...\n")
for epoch in range(epochs):
    model.train()
    epoch_loss = 0

    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        outputs = model(X_batch)
        loss = criterion(outputs, y_batch)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()

    avg_loss = epoch_loss / len(train_loader)
    train_losses.append(avg_loss)

    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch+1:3d}/{epochs}] | Loss: {avg_loss:.4f}")

# ── 5. Evaluation ────────────────────────────────────────────────────────────
model.eval()
with torch.no_grad():
    outputs = model(X_test)
    _, predicted = torch.max(outputs, 1)
    correct = (predicted == y_test).sum().item()
    accuracy = correct / len(y_test) * 100

print(f"\nTest Accuracy: {accuracy:.2f}%")
print(f"Correct: {correct}/{len(y_test)}")

# ── 6. Plot Training Loss ────────────────────────────────────────────────────
plt.figure(figsize=(8, 4))
plt.plot(range(1, epochs + 1), train_losses, color='steelblue', linewidth=2)
plt.title('Training Loss over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('training_loss.png')
plt.show()
print("\nPlot saved as training_loss.png")