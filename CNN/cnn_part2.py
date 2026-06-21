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
# 3. TRANSFORMATIONS
# ==============================
transform = transforms.ToTensor()

# ==============================
# 4. DATASETS MNIST
# ==============================
train_dataset = datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

test_dataset = datasets.MNIST(
    root="./data",
    train=False,
    download=True,
    transform=transform
)

# ==============================
# 5. DATALOADERS
# ==============================
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
# 6. VÉRIFICATION
# ==============================
print("Train size :", len(train_dataset))
print("Test size  :", len(test_dataset))

images, labels = next(iter(train_loader))

print("Image batch shape :", images.shape)
print("Label batch shape :", labels.shape)

# ==============================
# 7. MODÈLE CNN
# ==============================
class SimpleCNN(nn.Module):

    def __init__(self):
        super(SimpleCNN, self).__init__()

        # ==============================
        # TEST STRIDE = 2
        # ==============================
        self.conv1 = nn.Conv2d(
            in_channels=1,
            out_channels=16,
            kernel_size=3,
            stride=2,
            padding=1
        )

        # ==============================
        # AVERAGE POOLING
        # ==============================
        self.pool = nn.AvgPool2d(
            kernel_size=2,
            stride=2
        )

        # ==============================
        # DIMENSIONS :
        # 28x28
        # -> conv stride=2 => 14x14
        # -> pooling => 7x7
        # ==============================
        self.fc1 = nn.Linear(16 * 7 * 7, 128)

        self.fc2 = nn.Linear(128, 10)

        self.relu = nn.ReLU()

    def forward(self, x):

        # Convolution + ReLU
        x = self.relu(self.conv1(x))

        # Pooling
        x = self.pool(x)

        # Flatten
        x = x.view(x.size(0), -1)

        # Fully connected
        x = self.relu(self.fc1(x))

        x = self.fc2(x)

        return x


model = SimpleCNN().to(device)

print("\n===== ARCHITECTURE CNN =====")
print(model)

# ==============================
# 8. LOSS + OPTIMIZER
# ==============================
criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

# ==============================
# 9. ENTRAÎNEMENT
# ==============================
print("\n===== ENTRAÎNEMENT CNN =====")

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

    print(f"Epoch {epoch + 1}, Loss: {running_loss:.4f}")

# ==============================
# 10. TEST
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

# ==============================
# 11. RÉSULTATS
# ==============================
print("\n===== RÉSULTATS =====")

print(f"Accuracy CNN avec Average Pooling : {accuracy:.2f}%")
