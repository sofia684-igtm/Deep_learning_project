# ==============================
# 1. IMPORTS
# ==============================
import torch
import torch.nn as nn

from torchvision import datasets, transforms
from torch.utils.data import DataLoader

import matplotlib.pyplot as plt

# ==============================
# 2. DEVICE
# ==============================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Device :", device)

# ==============================
# 3. DATASET MNIST
# ==============================
transform = transforms.ToTensor()

test_dataset = datasets.MNIST(
    root='./data',
    train=False,
    download=True,
    transform=transform
)

test_loader = DataLoader(
    test_dataset,
    batch_size=1,
    shuffle=True
)

# ==============================
# 4. CNN SIMPLE
# ==============================
class SimpleCNN(nn.Module):

    def __init__(self):
        super(SimpleCNN, self).__init__()

        self.conv1 = nn.Conv2d(
            in_channels=1,
            out_channels=16,
            kernel_size=3,
            padding=1
        )

        self.relu = nn.ReLU()

    def forward(self, x):

        x = self.conv1(x)

        x = self.relu(x)

        return x

# ==============================
# 5. MODÈLE
# ==============================
model = SimpleCNN().to(device)

# ==============================
# 6. IMAGE TEST
# ==============================
images, labels = next(iter(test_loader))

images = images.to(device)

# ==============================
# 7. FEATURE MAPS
# ==============================
with torch.no_grad():

    feature_maps = model(images)

print("Feature maps shape :", feature_maps.shape)

# ==============================
# 8. IMAGE ORIGINALE
# ==============================
plt.figure(figsize=(3,3))

plt.imshow(
    images[0][0].cpu(),
    cmap='gray'
)

plt.title("Image originale")

plt.axis('off')

plt.show()

# ==============================
# 9. FEATURE MAPS
# ==============================
fig, axes = plt.subplots(
    4,
    4,
    figsize=(8,8)
)

for i, ax in enumerate(axes.flat):

    ax.imshow(
        feature_maps[0][i].cpu(),
        cmap='viridis'
    )

    ax.axis('off')

plt.suptitle("Feature Maps CNN")

plt.show()