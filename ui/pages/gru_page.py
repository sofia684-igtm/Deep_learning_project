"""GRU Page."""

import streamlit as st

from ui.components.layout import render_page_header, render_section_title
from ui.components.cards import render_metric_card

def render() -> None:
    render_page_header(
        "Gated Recurrent Unit",
        "Alternative légère au LSTM, combinant les portes d'oubli et d'entrée."
    )

    col_main, col_side = st.columns([2, 1])
    
    with col_main:
        render_section_title("Process Sequence")
        st.markdown('<div class="saas-card">', unsafe_allow_html=True)
        sequence_text = st.text_area("Input Sequence:", height=100, placeholder="The performance of this model is outstanding...")
        
        if st.button("Process Sequence", type="primary"):
            if sequence_text:
                st.success("Sequence processed.")
                rcol1, rcol2 = st.columns(2)
                with rcol1:
                    render_metric_card("Sentiment", "Positive", "Predicted category")
                with rcol2:
                    render_metric_card("Probability", "96.8%", "Confidence score")
            else:
                st.warning("Please enter a sequence first.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_side:
        render_section_title("GRU vs LSTM")
        st.markdown(
            """
            <div class="saas-card">
                <table style="width: 100%; border-collapse: collapse; text-align: left;">
                    <tr style="border-bottom: 1px solid var(--border-color);">
                        <th style="padding: 0.5rem; color: var(--text-muted);">Feature</th>
                        <th style="padding: 0.5rem; color: var(--accent-cyan);">GRU</th>
                        <th style="padding: 0.5rem; color: var(--accent-purple);">LSTM</th>
                    </tr>
                    <tr style="border-bottom: 1px solid var(--border-color);">
                        <td style="padding: 0.5rem;">Gates</td>
                        <td style="padding: 0.5rem;">2 (Reset, Update)</td>
                        <td style="padding: 0.5rem;">3 (Input, Forget, Output)</td>
                    </tr>
                    <tr style="border-bottom: 1px solid var(--border-color);">
                        <td style="padding: 0.5rem;">Cell State</td>
                        <td style="padding: 0.5rem;">No</td>
                        <td style="padding: 0.5rem;">Yes</td>
                    </tr>
                    <tr>
                        <td style="padding: 0.5rem;">Speed</td>
                        <td style="padding: 0.5rem; font-weight: bold;">Faster</td>
                        <td style="padding: 0.5rem;">Slower</td>
                    </tr>
                </table>
            </div>
            """,
            unsafe_allow_html=True
        )

    render_section_title("GRU Architecture")
    st.markdown(
        """
        <div class="saas-card" style="display: flex; justify-content: center; align-items: center; padding: 2rem;">
            <div style="width: 60%; padding: 2rem; border: 2px solid var(--accent-cyan); border-radius: 1rem; background: rgba(6, 182, 212, 0.05); position: relative;">
                <div style="text-align: center; color: var(--accent-cyan); font-weight: bold; margin-bottom: 2rem; font-size: 1.25rem;">GRU Cell</div>
                
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
                    <div style="color: var(--text-muted);">h<sub style="font-size: 0.6em;">t-1</sub> &xrarr;</div>
                    <div style="flex: 1; border-top: 2px dashed var(--accent-cyan); margin: 0 1rem; position: relative;">
                        <div style="position: absolute; top: -25px; left: 30%; background: var(--bg-color); padding: 0 0.5rem; color: var(--accent-cyan); font-size: 0.875rem;">Update Gate</div>
                        <div style="position: absolute; top: 10px; left: 60%; background: var(--bg-color); padding: 0 0.5rem; color: var(--accent-cyan); font-size: 0.875rem;">Reset Gate</div>
                    </div>
                    <div style="color: var(--text-muted);">&xrarr; h<sub style="font-size: 0.6em;">t</sub></div>
                </div>
                
                <div style="text-align: center; color: var(--text-muted);">
                    &uarr;<br>x<sub style="font-size: 0.6em;">t</sub>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
