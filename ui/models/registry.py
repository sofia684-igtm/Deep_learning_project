"""
Model registry and loader stubs.

When checkpoints become available, implement load_* methods here
without changing the page modules.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ui.config import MODEL_REGISTRY


def is_model_available(model_key: str) -> bool:
    """Check whether a checkpoint file exists on disk."""
    entry = MODEL_REGISTRY.get(model_key)
    if entry is None:
        return False
    checkpoint: Path = entry["checkpoint"]
    return checkpoint.exists()


class ModelLoader:
    """Centralized model loading — extend as checkpoints are trained."""

    @staticmethod
    def load_mlp() -> Any | None:
        """
        Load MonMLP from mlp_model.pth.
        Architecture: Linear(30→16) → ReLU → Linear(16→8) → ReLU → Linear(8→2)
        """
        if not is_model_available("mlp"):
            return None
        # Future: import torch, instantiate MonMLP, load_state_dict
        return None

    @staticmethod
    def predict_mlp(features) -> tuple[int, str] | None:
        """Run inference on breast cancer features. Returns (class_id, label)."""
        model = ModelLoader.load_mlp()
        if model is None:
            return None
        # Future: scaler transform → tensor → model → argmax
        return None

    @staticmethod
    def load_cnn() -> Any | None:
        """
        Load SimpleCNN from cnn_model.pth.
        Architecture: Conv2d(stride=2) → AvgPool → FC(16×7×7 → 128 → 10)
        """
        if not is_model_available("cnn"):
            return None
        return None

    @staticmethod
    def predict_cnn(image_array) -> int | None:
        """Run digit prediction on a 28×28 grayscale array."""
        model = ModelLoader.load_cnn()
        if model is None:
            return None
        return None

    @staticmethod
    def load_lstm() -> Any | None:
        """Load SimpleLSTM from lstm_model.pth."""
        if not is_model_available("lstm"):
            return None
        return None

    @staticmethod
    def predict_lstm(text: str) -> tuple[str, float] | None:
        """Run sentiment analysis. Returns (label, confidence)."""
        model = ModelLoader.load_lstm()
        if model is None:
            return None
        return None

    # ── Future models ────────────────────────────────────────────────────────
    @staticmethod
    def load_gru() -> Any | None:
        if not is_model_available("gru"):
            return None
        return None

    @staticmethod
    def load_rnn() -> Any | None:
        if not is_model_available("rnn"):
            return None
        return None

    @staticmethod
    def load_seq2seq() -> Any | None:
        if not is_model_available("seq2seq"):
            return None
        return None
