"""Home page."""

import streamlit as st
from ui.components.layout import render_page_header, render_section_title
from ui.components.cards import render_kpi_card, render_feature_card

def render() -> None:
    render_page_header(
        "Deep Learning Architectures Explorer",
        "Comparative study of MLP, CNN, RNN, LSTM, GRU and Seq2Seq architectures"
    )

    # Statistical Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Models Implemented", "6")
    with col2:
        render_kpi_card("Datasets Used", "3")
    with col3:
        render_kpi_card("Figures", "12+")
    with col4:
        render_kpi_card("Technologies", "4")

    # Technologies
    render_section_title("Technologies Used")
    tcol1, tcol2, tcol3, tcol4 = st.columns(4)
    with tcol1:
        render_feature_card("PyTorch", "Deep Learning Framework")
    with tcol2:
        render_feature_card("Scikit-Learn", "Machine Learning tools")
    with tcol3:
        render_feature_card("Streamlit", "Web Interface")
    with tcol4:
        render_feature_card("Plotly", "Interactive Visualizations")

    # Global Scheme
    render_section_title("Global Architecture Diagram")
    
    # We will use mermaid for a sleek modern global diagram.
    mermaid_diagram = """
    graph LR
        A[Dataset] --> B[Preprocessing]
        B --> C[MLP]
        B --> D[CNN]
        B --> E[RNN]
        B --> F[LSTM]
        B --> G[GRU]
        B --> H[Seq2Seq]
        C --> I[Evaluation]
        D --> I
        E --> I
        F --> I
        G --> I
        H --> I
        I --> J[Benchmark & Comparison]
        
        classDef default fill:#1E293B,stroke:#334155,stroke-width:2px,color:#FFFFFF;
        classDef final fill:#06B6D4,stroke:#0F172A,stroke-width:2px,color:#0F172A;
        class J final;
    """
    
    st.markdown(
        f"""
        <div class="saas-card" style="display: flex; justify-content: center; padding: 2rem;">
            <!-- Using an image or html component for mermaid would be ideal, but Streamlit has st.components or native mermaid now -->
        </div>
        """,
        unsafe_allow_html=True
    )
    # Streamlit natively supports markdown mermaid, but only with `st.markdown("```mermaid\n...\n```")`?
    # Actually wait, we can just use graphviz or write html.
    # Let's use standard st.write with mermaid block.
    # Wait, Streamlit doesn't render mermaid by default without a third-party plugin or specific markdown hack. 
    # Actually, as of Streamlit 1.32.0, wait, it might? No, standard is `st.graphviz_chart`.
    # Let's do a pure CSS or simple markdown representation to avoid dependencies.
    
    st.markdown(
        """
        <div class="saas-card">
            <div style="display: flex; justify-content: space-between; align-items: center; color: var(--text-main); font-weight: 500;">
                <div style="padding: 1rem; border: 1px solid var(--border-color); border-radius: 0.5rem; background: var(--bg-color);">Datasets<br><span style="font-size:0.8rem; color:var(--text-muted);">Cancer, MNIST, IMDb</span></div>
                <div style="color: var(--accent-cyan); font-weight: 700;">&xrarr;</div>
                <div style="padding: 1rem; border: 1px solid var(--border-color); border-radius: 0.5rem; background: var(--bg-color);">Preprocessing</div>
                <div style="color: var(--accent-cyan); font-weight: 700;">&xrarr;</div>
                <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                    <div style="padding: 0.5rem 1rem; border: 1px solid var(--accent-purple); border-radius: 0.5rem; background: rgba(139, 92, 246, 0.1);">MLP</div>
                    <div style="padding: 0.5rem 1rem; border: 1px solid var(--accent-cyan); border-radius: 0.5rem; background: rgba(6, 182, 212, 0.1);">CNN</div>
                    <div style="padding: 0.5rem 1rem; border: 1px solid var(--accent-purple); border-radius: 0.5rem; background: rgba(139, 92, 246, 0.1);">RNN & LSTM & GRU</div>
                    <div style="padding: 0.5rem 1rem; border: 1px solid var(--accent-cyan); border-radius: 0.5rem; background: rgba(6, 182, 212, 0.1);">Seq2Seq</div>
                </div>
                <div style="color: var(--accent-cyan); font-weight: 700;">&xrarr;</div>
                <div style="padding: 1rem; border: 1px solid var(--border-color); border-radius: 0.5rem; background: var(--bg-color);">Evaluation</div>
                <div style="color: var(--accent-cyan); font-weight: 700;">&xrarr;</div>
                <div style="padding: 1rem; border: 1px solid var(--accent-cyan); border-radius: 0.5rem; background: var(--accent-cyan); color: white; font-weight: 600;">Benchmark Dashboard</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
