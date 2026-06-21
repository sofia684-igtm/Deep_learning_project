"""Model loading layer — connect PyTorch checkpoints here when ready."""

from ui.models.registry import ModelLoader, is_model_available

__all__ = ["ModelLoader", "is_model_available"]
