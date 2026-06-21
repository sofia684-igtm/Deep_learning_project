"""Chart builders — dark Plotly theme."""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

GRADIENT_COLORS = ["#6366f1", "#818cf8", "#8b5cf6"]
MODEL_COLORS = {
    "MLP": "#6366f1",
    "CNN": "#3b82f6",
    "LSTM": "#8b5cf6",
    "CNN Stride=2": "#818cf8",
    "CNN Avg Pooling": "#a5b4fc",
}

DARK_LAYOUT = dict(
    plot_bgcolor="#111827",
    paper_bgcolor="#111827",
    font=dict(family="Inter, sans-serif", color="#94a3b8", size=10),
    margin=dict(l=30, r=15, t=35, b=25),
)


def _dark_layout(fig: go.Figure, title: str, height: int) -> go.Figure:
    fig.update_layout(
        **DARK_LAYOUT,
        title=dict(text=title, font=dict(size=12, color="#e2e8f0")),
        height=height,
    )
    fig.update_xaxes(showgrid=False, linecolor="#243044", tickfont=dict(size=9))
    fig.update_yaxes(gridcolor="#1e293b", linecolor="#243044", zeroline=False, tickfont=dict(size=9))
    return fig


def plot_class_distribution_bar(df: pd.DataFrame):
    fig = go.Figure(
        data=[
            go.Bar(
                x=df["Class"],
                y=df["Count"],
                marker=dict(color=["#ef4444", "#10b981"], line=dict(width=0)),
                text=df["Count"],
                textposition="outside",
                textfont=dict(color="#94a3b8", size=10),
            )
        ]
    )
    _dark_layout(fig, "Class Distribution", 300)
    st.plotly_chart(fig, use_container_width=True)


def plot_benchmark_bar(df: pd.DataFrame):
    df = df.copy()
    df["Label"] = df["Model"] + "<br>(" + df["Dataset"] + ")"
    colors = [MODEL_COLORS.get(m, "#6366f1") for m in df["Model"]]

    fig = go.Figure(
        data=[
            go.Bar(
                x=df["Label"],
                y=df["Accuracy"],
                marker=dict(color=colors),
                text=[f"{v:.2f}%" for v in df["Accuracy"]],
                textposition="outside",
                textfont=dict(size=9, color="#94a3b8"),
            )
        ]
    )
    _dark_layout(fig, "Model Accuracy Comparison", 380)
    fig.update_yaxes(range=[90, 100.8], title="Accuracy (%)")
    st.plotly_chart(fig, use_container_width=True)


def plot_cnn_variants_bar(df: pd.DataFrame):
    fig = go.Figure(
        data=[
            go.Bar(
                x=df["Variant"],
                y=df["Accuracy (%)"],
                marker=dict(color=GRADIENT_COLORS),
                text=[f"{v:.2f}%" for v in df["Accuracy (%)"]],
                textposition="outside",
                textfont=dict(size=9, color="#94a3b8"),
            )
        ]
    )
    _dark_layout(fig, "CNN Variants — MNIST", 320)
    fig.update_yaxes(range=[96, 99.8], title="Accuracy (%)")
    st.plotly_chart(fig, use_container_width=True)


def plot_home_accuracy_chart(df: pd.DataFrame):
    summary = df.groupby("Model", as_index=False)["Accuracy"].max().sort_values("Accuracy", ascending=True)
    colors = [MODEL_COLORS.get(m, "#6366f1") for m in summary["Model"]]

    fig = go.Figure(
        data=[
            go.Bar(
                y=summary["Model"],
                x=summary["Accuracy"],
                orientation="h",
                marker=dict(color=colors),
                text=[f"{v:.2f}%" for v in summary["Accuracy"]],
                textposition="outside",
                textfont=dict(size=9, color="#94a3b8"),
            )
        ]
    )
    _dark_layout(fig, "", 180)
    fig.update_layout(title=None, margin=dict(l=10, r=10, t=5, b=5))
    fig.update_xaxes(range=[94, 101])
    st.plotly_chart(fig, use_container_width=True)
