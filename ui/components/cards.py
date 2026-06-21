"""Reusable card components."""

import streamlit as st

def render_kpi_card(title: str, value: str) -> None:
    """Render a modern SaaS KPI card."""
    st.markdown(
        f"""
        <div class="saas-card">
            <div class="card-title">{title}</div>
            <div class="card-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_metric_card(title: str, value: str, subtitle: str = "") -> None:
    """Render a metric card with optional subtitle."""
    sub_html = f'<div style="color: var(--text-muted); font-size: 0.875rem; margin-top: 0.5rem;">{subtitle}</div>' if subtitle else ""
    st.markdown(
        f"""
        <div class="saas-card" style="border-left: 4px solid var(--accent-cyan);">
            <div class="card-title">{title}</div>
            <div class="card-value">{value}</div>
            {sub_html}
        </div>
        """,
        unsafe_allow_html=True
    )

def render_feature_card(title: str, description: str) -> None:
    """Render a feature/info card."""
    st.markdown(
        f"""
        <div class="saas-card">
            <div style="font-weight: 600; font-size: 1.125rem; color: var(--accent-purple); margin-bottom: 0.5rem;">{title}</div>
            <div style="color: var(--text-muted); line-height: 1.5;">{description}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
