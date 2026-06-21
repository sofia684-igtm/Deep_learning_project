"""Shared layout components — sidebar, headers, sections."""

from __future__ import annotations

import streamlit as st

from ui.config import NAV_PAGES


def render_sidebar() -> None:
    page_map = {p["key"]: p for p in NAV_PAGES}
    keys = [p["key"] for p in NAV_PAGES]
    labels = [p["label"] for p in NAV_PAGES]

    current = st.session_state.get("nav_page", "home")
    index = keys.index(current) if current in keys else 0

    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-brand">
                <span class="brand-text">DL Explorer</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        selected = st.radio(
            "Navigation",
            labels,
            index=index,
            label_visibility="collapsed",
            key="sidebar_nav_radio",
        )
        st.session_state.nav_page = keys[labels.index(selected)]


def render_page_header(title: str, subtitle: str, badge: str = None) -> None:
    badge_html = f'<span class="pg-badge" style="font-size:0.8rem; background:var(--accent-purple); color:white; padding:0.2rem 0.5rem; border-radius:0.5rem; margin-left:1rem; vertical-align:middle;">{badge}</span>' if badge else ''
    st.markdown(
        f"""
        <div class="pg-header">
            <h2 class="pg-title">{title}{badge_html}</h2>
            <p class="pg-sub">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_title(title: str) -> None:
    st.markdown(f'<p class="sec-title">{title}</p>', unsafe_allow_html=True)


def render_section(title: str) -> None:
    render_section_title(title)


def render_pipeline_compact() -> None:
    st.markdown(
        """
        <div class="saas-card" style="display: flex; justify-content: space-between; align-items: center; color: var(--text-main); font-size: 0.9rem;">
            <div style="padding: 0.5rem; border: 1px solid var(--border-color); border-radius: 0.5rem;">Datasets</div>
            <div style="color: var(--accent-cyan); font-weight: bold;">&rarr;</div>
            <div style="padding: 0.5rem; border: 1px solid var(--border-color); border-radius: 0.5rem;">Preprocess</div>
            <div style="color: var(--accent-cyan); font-weight: bold;">&rarr;</div>
            <div style="padding: 0.5rem; border: 1px solid var(--accent-purple); border-radius: 0.5rem; background: rgba(139, 92, 246, 0.1);">Models</div>
            <div style="color: var(--accent-cyan); font-weight: bold;">&rarr;</div>
            <div style="padding: 0.5rem; border: 1px solid var(--border-color); border-radius: 0.5rem;">Evaluate</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
