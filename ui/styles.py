"""CSS injection for SaaS styling."""

import streamlit as st

def inject_styles() -> None:
    css = """
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* CSS Variables */
    :root {
        --bg-color: #0F172A;
        --sidebar-bg: #1E293B;
        --card-bg: rgba(30, 41, 59, 0.7);
        --text-main: #FFFFFF;
        --text-muted: #94A3B8;
        --accent-cyan: #06B6D4;
        --accent-purple: #8B5CF6;
        --border-color: #334155;
        --font-family: 'Inter', sans-serif;
    }

    /* Global reset and typography */
    html, body, [class*="css"]  {
        font-family: var(--font-family) !important;
        background-color: var(--bg-color) !important;
        color: var(--text-main) !important;
    }

    /* Hide Streamlit Header & Footer */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    footer {
        display: none !important;
    }
    
    /* Main Content Area */
    .stApp {
        background-color: var(--bg-color) !important;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: var(--sidebar-bg) !important;
        border-right: 1px solid var(--border-color);
        padding-top: 2rem;
    }
    .sidebar-brand {
        padding: 1.5rem;
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text-main);
        text-align: center;
        border-bottom: 1px solid var(--border-color);
        margin-bottom: 2rem;
        background: linear-gradient(90deg, var(--accent-cyan), var(--accent-purple));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Sidebar Navigation Radio Buttons */
    div[data-testid="stRadio"] > div {
        gap: 0.5rem;
    }
    div[data-testid="stRadio"] label {
        padding: 0.75rem 1rem;
        border-radius: 0.5rem;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
        background: transparent;
        color: var(--text-muted);
    }
    div[data-testid="stRadio"] label:hover {
        background-color: rgba(255, 255, 255, 0.05);
        color: var(--text-main);
    }
    /* Hide the actual radio circle */
    div[data-testid="stRadio"] input {
        display: none;
    }
    div[data-testid="stRadio"] div[data-testid="stMarkdownContainer"] {
        font-weight: 500;
        font-size: 1rem;
    }
    
    /* Buttons */
    button[kind="primary"], button[kind="secondary"] {
        background: linear-gradient(135deg, var(--accent-cyan), var(--accent-purple)) !important;
        color: white !important;
        border: none !important;
        border-radius: 0.5rem !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.025em !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06) !important;
    }
    button[kind="primary"]:hover, button[kind="secondary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05) !important;
    }

    /* Input Fields */
    input, textarea, select {
        background-color: var(--card-bg) !important;
        border: 1px solid var(--border-color) !important;
        color: var(--text-main) !important;
        border-radius: 0.5rem !important;
        padding: 0.75rem !important;
    }
    input:focus, textarea:focus, select:focus {
        border-color: var(--accent-cyan) !important;
        box-shadow: 0 0 0 1px var(--accent-cyan) !important;
    }

    /* Cards */
    .saas-card {
        background-color: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 1rem;
        padding: 1.5rem;
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .saas-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
    }
    
    .card-title {
        color: var(--text-muted);
        font-size: 0.875rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
    }
    
    .card-value {
        color: var(--text-main);
        font-size: 1.875rem;
        font-weight: 700;
    }

    /* Page Headers */
    .pg-header {
        margin-bottom: 2rem;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 1.5rem;
    }
    .pg-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        background: linear-gradient(to right, #FFFFFF, var(--text-muted));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .pg-sub {
        color: var(--text-muted);
        font-size: 1.125rem;
        margin-top: 0.5rem;
    }

    /* Section Titles */
    .sec-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--text-main);
        margin-top: 2rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .sec-title::before {
        content: '';
        display: block;
        width: 4px;
        height: 24px;
        background: var(--accent-cyan);
        border-radius: 2px;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
