"""Automatic benchmark analysis generation."""

from __future__ import annotations

import pandas as pd


def generate_benchmark_analysis(df: pd.DataFrame) -> str:
    """Produce a human-readable analysis from benchmark results."""
    best_row = df.loc[df["Accuracy"].idxmax()]
    worst_row = df.loc[df["Accuracy"].idxmin()]

    mnist_rows = df[df["Dataset"] == "MNIST"].sort_values("Accuracy", ascending=False)
    best_mnist = mnist_rows.iloc[0]

    cnn_std = mnist_rows[mnist_rows["Model"] == "CNN"]["Accuracy"].values
    cnn_stride = mnist_rows[mnist_rows["Model"] == "CNN Stride=2"]["Accuracy"].values
    cnn_pool = mnist_rows[mnist_rows["Model"] == "CNN Avg Pooling"]["Accuracy"].values

    gap_best_worst = best_row["Accuracy"] - worst_row["Accuracy"]

    lines = [
        f"**Best overall performance:** {best_row['Model']} on {best_row['Dataset']} "
        f"with **{best_row['Accuracy']:.2f}%** accuracy.",
        "",
        f"**Lowest recorded accuracy:** {worst_row['Model']} on {worst_row['Dataset']} "
        f"at **{worst_row['Accuracy']:.2f}%** — a gap of **{gap_best_worst:.2f} percentage points** "
        f"from the top result.",
        "",
        "**MNIST comparison:** Among models trained on handwritten digits, "
        f"the standard **{best_mnist['Model']}** achieves the highest accuracy "
        f"(**{best_mnist['Accuracy']:.2f}%**).",
    ]

    if len(cnn_std) and len(cnn_stride) and len(cnn_pool):
        lines.extend(
            [
                "",
                "**CNN architecture insights:**",
                f"- Standard CNN: **{cnn_std[0]:.2f}%**",
                f"- CNN with stride=2: **{cnn_stride[0]:.2f}%** "
                f"({'↓' if cnn_stride[0] < cnn_std[0] else '↑'} "
                f"{abs(cnn_std[0] - cnn_stride[0]):.2f} pp vs standard)",
                f"- CNN with Average Pooling: **{cnn_pool[0]:.2f}%** "
                f"({'↓' if cnn_pool[0] < cnn_std[0] else '↑'} "
                f"{abs(cnn_std[0] - cnn_pool[0]):.2f} pp vs standard)",
                "",
                "The standard convolution + pooling pipeline offers the best trade-off "
                "between spatial feature extraction and classification accuracy on MNIST.",
            ]
        )

    mlp_bc = df[(df["Model"] == "MLP") & (df["Dataset"] == "Breast Cancer")]["Accuracy"]
    mlp_mnist = df[(df["Model"] == "MLP") & (df["Dataset"] == "MNIST")]["Accuracy"]
    if len(mlp_bc) and len(mlp_mnist):
        lines.extend(
            [
                "",
                f"**MLP generalization:** The same MLP architecture reaches "
                f"**{mlp_bc.iloc[0]:.2f}%** on tabular Breast Cancer data and "
                f"**{mlp_mnist.iloc[0]:.2f}%** on image-based MNIST, illustrating "
                "how dataset complexity affects fully-connected network performance.",
            ]
        )

    lstm_row = df[df["Model"] == "LSTM"]
    if not lstm_row.empty:
        lines.extend(
            [
                "",
                f"**Sequence modeling:** The LSTM achieves **{lstm_row.iloc[0]['Accuracy']:.2f}%** "
                "on IMDb sentiment analysis, demonstrating the strength of recurrent "
                "architectures for sequential text data.",
            ]
        )

    return "\n".join(lines)
