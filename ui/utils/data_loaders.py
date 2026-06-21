"""Data loading helpers for dashboard visualizations."""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer


def get_breast_cancer_class_distribution() -> pd.DataFrame:
    """Return class counts for the Breast Cancer dataset."""
    data = load_breast_cancer()
    counts = pd.Series(data.target).value_counts().sort_index()
    return pd.DataFrame(
        {
            "Class": ["Malignant (0)", "Benign (1)"],
            "Count": [counts.get(0, 0), counts.get(1, 0)],
        }
    )


def get_mnist_sample_image():
    """
    Load a sample MNIST digit image as a numpy array (28×28, float 0–1).
    Downloads MNIST on first use if not cached.
    """
    from torchvision import datasets, transforms

    transform = transforms.ToTensor()
    dataset = datasets.MNIST(
        root="./data",
        train=True,
        download=True,
        transform=transform,
    )
    image, label = dataset[0]
    return image.squeeze().numpy(), int(label)


def preprocess_uploaded_image(uploaded_file) -> np.ndarray | None:
    """Convert an uploaded image file to a 28×28 grayscale numpy array."""
    from PIL import Image

    try:
        img = Image.open(uploaded_file).convert("L")
        img = img.resize((28, 28), Image.Resampling.LANCZOS)
        arr = np.array(img, dtype=np.float32) / 255.0
        return arr
    except Exception:
        return None
