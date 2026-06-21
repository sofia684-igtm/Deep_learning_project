"""Central configuration, benchmark data, and model registry."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ── Benchmark results ────────────────────────────────────────────────────────
BENCHMARK_DATA = [
    {"Model": "MLP", "Dataset": "Breast Cancer", "Accuracy": 96.49},
    {"Model": "MLP", "Dataset": "MNIST", "Accuracy": 97.01},
    {"Model": "CNN", "Dataset": "MNIST", "Accuracy": 98.27},
    {"Model": "CNN Stride=2", "Dataset": "MNIST", "Accuracy": 97.67},
    {"Model": "CNN Avg Pooling", "Dataset": "MNIST", "Accuracy": 97.06},
    {"Model": "LSTM", "Dataset": "IMDb", "Accuracy": 99.50},
]

CNN_COMPARISON_DATA = [
    {"Variant": "CNN", "Accuracy (%)": 98.27},
    {"Variant": "CNN stride=2", "Accuracy (%)": 97.67},
    {"Variant": "CNN Average Pooling", "Accuracy (%)": 97.06},
]

# ── Dataset metadata ─────────────────────────────────────────────────────────
BREAST_CANCER_INFO = {
    "name": "Breast Cancer Wisconsin (Diagnostic)",
    "samples": 569,
    "features": 30,
    "classes": 2,
    "class_names": ["Malignant", "Benign"],
    "description": (
        "The Breast Cancer Wisconsin dataset contains features computed from "
        "digitized fine needle aspirate (FNA) images of breast mass cell nuclei. "
        "The task is binary classification: malignant vs. benign."
    ),
}

MNIST_INFO = {
    "name": "MNIST Handwritten Digits",
    "train_samples": 60_000,
    "test_samples": 10_000,
    "image_size": "28×28 grayscale",
    "classes": 10,
    "description": (
        "MNIST is a classic benchmark of 70,000 grayscale images of handwritten "
        "digits (0–9). Convolutional Neural Networks excel at capturing spatial "
        "patterns in these images."
    ),
}

IMDB_INFO = {
    "name": "IMDb Movie Reviews",
    "samples": "50,000 reviews",
    "classes": 2,
    "class_names": ["Negative", "Positive"],
    "description": (
        "The IMDb dataset consists of 50,000 movie reviews labeled as positive "
        "or negative. Long Short-Term Memory networks capture sequential "
        "dependencies in text for sentiment classification."
    ),
}

# ── Model registry (extensible for GRU, RNN, Seq2Seq) ────────────────────────
MODEL_REGISTRY = {
    "mlp": {
        "display_name": "MLP (Multi-Layer Perceptron)",
        "checkpoint": PROJECT_ROOT / "mlp_model.pth",
        "connected": False,
        "dataset": "Breast Cancer",
        "accuracy": 96.49,
    },
    "cnn": {
        "display_name": "CNN (Convolutional Neural Network)",
        "checkpoint": PROJECT_ROOT / "cnn_model.pth",
        "connected": False,
        "dataset": "MNIST",
        "accuracy": 98.27,
    },
    "lstm": {
        "display_name": "LSTM (Long Short-Term Memory)",
        "checkpoint": PROJECT_ROOT / "lstm_model.pth",
        "connected": False,
        "dataset": "IMDb",
        "accuracy": 99.50,
    },
    # Future integrations
    "gru": {
        "display_name": "GRU (Gated Recurrent Unit)",
        "checkpoint": PROJECT_ROOT / "gru_model.pth",
        "connected": False,
        "coming_soon": True,
        "dataset": "IMDb",
        "accuracy": None,
    },
    "rnn": {
        "display_name": "RNN (Recurrent Neural Network)",
        "checkpoint": PROJECT_ROOT / "rnn_model.pth",
        "connected": False,
        "coming_soon": True,
        "dataset": "IMDb",
        "accuracy": None,
    },
    "seq2seq": {
        "display_name": "Seq2Seq (Sequence-to-Sequence)",
        "checkpoint": PROJECT_ROOT / "seq2seq_model.pth",
        "connected": False,
        "coming_soon": True,
        "dataset": "Custom",
        "accuracy": None,
    },
}

# ── Navigation ───────────────────────────────────────────────────────────────
NAV_PAGES = [
    {"key": "home", "label": "Home"},
    {"key": "mlp", "label": "MLP"},
    {"key": "cnn", "label": "CNN"},
    {"key": "rnn", "label": "RNN"},
    {"key": "lstm", "label": "LSTM"},
    {"key": "gru", "label": "GRU"},
    {"key": "seq2seq", "label": "Seq2Seq"},
    {"key": "benchmark", "label": "Benchmark"},
    {"key": "about", "label": "About Project"},
]
