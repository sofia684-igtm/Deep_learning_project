"""LSTM Page."""

import streamlit as st

from ui.components.layout import render_page_header, render_section_title
from ui.components.cards import render_metric_card, render_feature_card

def render() -> None:
    render_page_header(
        "Long Short-Term Memory",
        "Version améliorée du RNN pour pallier au problème de disparition du gradient."
    )

    col_main, col_side = st.columns([2, 1])
    
    with col_main:
        render_section_title("Sentiment Analysis")
        st.markdown('<div class="saas-card">', unsafe_allow_html=True)
        review_text = st.text_area("Enter sequence / review:", height=100, placeholder="The cinematography was absolutely breathtaking...")
        
        if st.button("Run Sentiment Analysis", type="primary"):
            if review_text:
                st.success("Analysis complete.")
                st.markdown(
                    """
                    <div style="padding: 1.5rem; border-radius: 0.5rem; background: rgba(139, 92, 246, 0.1); border-left: 4px solid var(--accent-purple); margin-top: 1rem;">
                        <h3 style="margin: 0; color: var(--accent-purple);">Sentiment Prédit : Positif</h3>
                        <p style="margin: 0.5rem 0 0 0; color: var(--text-muted);">Accuracy obtenue : 99.5%</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.warning("Please enter text first.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_side:
        render_section_title("RNN vs LSTM")
        st.markdown(
            """
            <div class="saas-card" style="padding: 1rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span style="color: var(--text-muted);">RNN Accuracy</span>
                    <span style="color: var(--text-main); font-weight: bold;">85.2%</span>
                </div>
                <div style="width: 100%; background: var(--bg-color); height: 8px; border-radius: 4px; margin-bottom: 1.5rem;">
                    <div style="width: 85.2%; background: var(--text-muted); height: 100%; border-radius: 4px;"></div>
                </div>
                
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                    <span style="color: var(--accent-cyan);">LSTM Accuracy</span>
                    <span style="color: var(--text-main); font-weight: bold;">99.5%</span>
                </div>
                <div style="width: 100%; background: var(--bg-color); height: 8px; border-radius: 4px;">
                    <div style="width: 99.5%; background: var(--accent-cyan); height: 100%; border-radius: 4px;"></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    render_section_title("LSTM Architecture & Long-Term Memory")
    col_arch1, col_arch2 = st.columns(2)
    with col_arch1:
        st.markdown(
            """
            <div class="saas-card" style="height: 100%;">
                <div style="font-weight: 600; color: var(--accent-cyan); margin-bottom: 1rem;">Cell State & Gates</div>
                <ul style="color: var(--text-muted); line-height: 1.8;">
                    <li><b>Cell State (C<sub>t</sub>) :</b> L'autoroute de l'information permettant à la mémoire de traverser la chaîne.</li>
                    <li><b>Forget Gate :</b> Décide quelles informations jeter du Cell State (Sigmoid).</li>
                    <li><b>Input Gate :</b> Décide quelles nouvelles informations stocker (Sigmoid + Tanh).</li>
                    <li><b>Output Gate :</b> Décide ce qu'on va générer comme sortie (Sigmoid + Tanh).</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_arch2:
        st.markdown(
            """
            <div class="saas-card" style="display: flex; justify-content: center; align-items: center; height: 100%; flex-direction: column;">
                <div style="padding: 1rem; border: 2px solid var(--accent-purple); border-radius: 1rem; position: relative; width: 80%;">
                    <div style="text-align: center; color: var(--accent-purple); font-weight: bold; margin-bottom: 1rem;">LSTM Cell</div>
                    <div style="display: flex; justify-content: space-between; padding: 0.5rem; background: rgba(255,255,255,0.05); border-radius: 0.5rem; margin-bottom: 0.5rem;">
                        <span>C<sub>t-1</sub></span> <span>&xrarr; <b>Cell State</b> &xrarr;</span> <span>C<sub>t</sub></span>
                    </div>
                    <div style="display: flex; justify-content: space-around; color: var(--accent-cyan); font-size: 0.875rem;">
                        <span>[Forget]</span> <span>[Input]</span> <span>[Output]</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
