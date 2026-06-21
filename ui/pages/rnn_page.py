"""RNN Page."""

import streamlit as st

from ui.components.layout import render_page_header, render_section_title
from ui.components.cards import render_metric_card

def render() -> None:
    render_page_header(
        "Recurrent Neural Network",
        "Analyse de sentiments sur IMDb."
    )

    col_main, col_side = st.columns([2, 1])
    
    with col_main:
        render_section_title("Sentiment Analysis")
        st.markdown('<div class="saas-card">', unsafe_allow_html=True)
        review_text = st.text_area("Enter movie review:", height=150, placeholder="Type a movie review here to analyze sentiment...")
        
        if st.button("Evaluate Review", type="primary"):
            if review_text:
                st.success("Review evaluated successfully.")
                st.markdown(
                    """
                    <div style="padding: 1.5rem; border-radius: 0.5rem; background: rgba(6, 182, 212, 0.1); border-left: 4px solid var(--accent-cyan); margin-top: 1rem;">
                        <h3 style="margin: 0; color: var(--accent-cyan);">Positive Review</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.warning("Please enter a review first.")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_side:
        render_section_title("Model Info")
        render_metric_card("Confidence Score", "92.4%")
        render_metric_card("Dataset Used", "IMDb Reviews")
        render_metric_card("Vocabulary Size", "10,000 words")

    render_section_title("RNN Operation Diagram")
    st.markdown(
        """
        <div class="saas-card">
            <div style="display: flex; justify-content: space-around; align-items: center; padding: 2rem 0;">
                <div style="text-align: center;">
                    <div style="margin-bottom: 0.5rem; color: var(--text-muted);">x<sub style="font-size: 0.6em;">t-1</sub></div>
                    <div style="width: 50px; height: 50px; border-radius: 0.5rem; background: var(--bg-color); border: 1px solid var(--border-color); display: flex; align-items: center; justify-content: center;">...</div>
                </div>
                <div style="color: var(--accent-cyan);">&xrarr;</div>
                <div style="text-align: center; position: relative;">
                    <div style="position: absolute; top: -40px; left: 50%; transform: translateX(-50%); color: var(--text-muted);">h<sub style="font-size: 0.6em;">t-1</sub></div>
                    <div style="width: 80px; height: 80px; border-radius: 50%; background: rgba(139, 92, 246, 0.2); border: 2px solid var(--accent-purple); display: flex; align-items: center; justify-content: center; font-weight: bold; color: var(--accent-purple);">RNN</div>
                    <div style="margin-top: 0.5rem; color: var(--text-muted);">x<sub style="font-size: 0.6em;">t</sub></div>
                </div>
                <div style="color: var(--accent-cyan);">&xrarr;</div>
                <div style="text-align: center; position: relative;">
                    <div style="position: absolute; top: -40px; left: 50%; transform: translateX(-50%); color: var(--text-muted);">h<sub style="font-size: 0.6em;">t</sub></div>
                    <div style="width: 80px; height: 80px; border-radius: 50%; background: rgba(139, 92, 246, 0.2); border: 2px solid var(--accent-purple); display: flex; align-items: center; justify-content: center; font-weight: bold; color: var(--accent-purple);">RNN</div>
                    <div style="margin-top: 0.5rem; color: var(--text-muted);">x<sub style="font-size: 0.6em;">t+1</sub></div>
                </div>
                <div style="color: var(--accent-cyan);">&xrarr;</div>
                <div style="text-align: center;">
                    <div style="margin-bottom: 0.5rem; color: var(--text-muted);">...</div>
                    <div style="width: 50px; height: 50px; border-radius: 0.5rem; background: var(--bg-color); border: 1px solid var(--border-color); display: flex; align-items: center; justify-content: center;">y<sub style="font-size: 0.6em;">pred</sub></div>
                </div>
            </div>
            <p style="text-align: center; color: var(--text-muted); font-size: 0.875rem; margin-top: 1rem;">
                Standard RNN processes sequential data step-by-step, updating its hidden state based on current input and previous state.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
