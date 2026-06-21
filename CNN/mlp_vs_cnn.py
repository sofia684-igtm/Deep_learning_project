# ==============================
# 1. IMPORTS
# ==============================
import torch
import torch.nn as nn
import torch.optim as optim

from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# ==============================
# 2. DEVICE
# ==============================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Device utilisé :", device)

# ==============================
# 3. DATASET MNIST
# ==============================
transform = transforms.ToTensor()

train_dataset = datasets.MNIST(
    root='./data',
    train=True,
    download=True,
    transform=transform
)

test_dataset = datasets.MNIST(
    root='./data',
    train=False,
    download=True,
    transform=transform
)

train_loader = DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=64,
    shuffle=False
)

# ==============================
# 4. MODÈLE MLP
# ==============================
class SimpleMLP(nn.Module):

    def __init__(self):
        super(SimpleMLP, self).__init__()

        self.fc1 = nn.Linear(28 * 28, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)

        self.relu = nn.ReLU()

    def forward(self, x):

        # Flatten image
        x = x.view(x.size(0), -1)

        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)

        return x

model = SimpleMLP().to(device)

# ==============================
# 5. LOSS + OPTIMIZER
# ==============================
criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

# ==============================
# 6. ENTRAÎNEMENT
# ==============================
print("\n===== ENTRAÎNEMENT MLP =====")

for epoch in range(3):

    running_loss = 0.0

    for images, labels in train_loader:

        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)

        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    print(f"Epoch {epoch+1}, Loss: {running_loss:.4f}")

# ==============================
# 7. TEST
# ==============================
correct = 0
total = 0

with torch.no_grad():

    for images, labels in test_loader:

        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)

        correct += (predicted == labels).sum().item()

accuracy = 100 * correct / total

print(f"\nAccuracy MLP : {accuracy:.2f}%")