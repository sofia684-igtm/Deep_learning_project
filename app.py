"""
Deep Learning Project Dashboard
Run with: streamlit run app.py
"""

import streamlit as st

from ui.components.layout import render_sidebar
from ui.pages import PAGE_RENDERERS
from ui.styles import inject_styles

st.set_page_config(
    page_title="Deep Learning Architectures Explorer",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_styles()

if "nav_page" not in st.session_state:
    st.session_state.nav_page = "home"

render_sidebar()

renderer = PAGE_RENDERERS.get(st.session_state.nav_page)
if renderer:
    renderer()
else:
    st.error("Page not found.")
