"""About page — project information."""

import streamlit as st

from ui.components.layout import render_page_header, render_pipeline_compact, render_section
from ui.config import MODEL_REGISTRY


def render() -> None:
    render_page_header(
        title="About This Project",
        subtitle="Deep Learning architectures with PyTorch — EMSI",
        badge="About",
    )

    st.markdown(
        """
        <div class="content-container">
        Custom PyTorch models trained on Breast Cancer, MNIST and IMDb datasets.
        Evaluated with standard metrics and benchmarked across architectural variants.
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_section("Technologies")
    t1, t2, t3, t4 = st.columns(4)
    for col, (icon, name) in zip(
        [t1, t2, t3, t4],
        [("🐍", "Python"), ("🔥", "PyTorch"), ("📐", "Scikit-Learn"), ("🎈", "Streamlit")],
    ):
        with col:
            st.markdown(
                f'<div class="kpi"><span class="kpi-icon">{icon}</span>'
                f'<span class="kpi-val" style="font-size:0.85rem;">{name}</span></div>',
                unsafe_allow_html=True,
            )

    render_section("Pipeline")
    render_pipeline_compact()

    render_section("Model Registry")
    a1, a2 = st.columns(2)
    with a1:
        st.markdown("**Active:**")
        for key, cfg in MODEL_REGISTRY.items():
            if not cfg.get("coming_soon"):
                st.markdown(f"- {cfg['display_name']} · `{cfg['checkpoint'].name}`")
    with a2:
        st.markdown("**Planned:**")
        for key, cfg in MODEL_REGISTRY.items():
            if cfg.get("coming_soon"):
                st.markdown(f"- {cfg['display_name']} · `{cfg['checkpoint'].name}`")
