"""CNN feature map generation for the dashboard (mirrors feature_maps.py logic)."""

from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import torch
import torch.nn as nn
from torchvision import datasets, transforms


class FeatureMapCNN(nn.Module):
    """Same architecture as feature_maps.py — conv1 + ReLU."""

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1)
        self.relu = nn.ReLU()

    def forward(self, x):
        return self.relu(self.conv1(x))


@torch.no_grad()
def compute_feature_maps():
    """Load a MNIST test image and compute 16 feature maps."""
    transform = transforms.ToTensor()
    test_dataset = datasets.MNIST(root="./data", train=False, download=True, transform=transform)
    image, label = test_dataset[0]

    model = FeatureMapCNN()
    model.eval()
    maps = model(image.unsqueeze(0))

    return image.squeeze().numpy(), int(label), maps.squeeze(0).numpy()


def build_feature_maps_grid(maps: np.ndarray) -> go.Figure:
    """4×4 grid of CNN feature maps (dark theme)."""
    fig = make_subplots(
        rows=4,
        cols=4,
        subplot_titles=[f"Filter {i + 1}" for i in range(16)],
        horizontal_spacing=0.03,
        vertical_spacing=0.05,
    )

    for i in range(16):
        r, c = divmod(i, 4)
        fig.add_trace(
            go.Heatmap(
                z=maps[i],
                colorscale="Viridis",
                showscale=False,
                hovertemplate=f"Filter {i + 1}: %{{z:.3f}}<extra></extra>",
            ),
            row=r + 1,
            col=c + 1,
        )

    fig.update_layout(
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        height=460,
        margin=dict(l=10, r=10, t=30, b=10),
        font=dict(family="Inter, sans-serif", color="#64748b", size=8),
        showlegend=False,
    )
    for ann in fig.layout.annotations:
        ann.font.size = 8
        ann.font.color = "#64748b"

    fig.update_xaxes(showticklabels=False, showgrid=False)
    fig.update_yaxes(showticklabels=False, showgrid=False, scaleanchor="x")
    return fig
