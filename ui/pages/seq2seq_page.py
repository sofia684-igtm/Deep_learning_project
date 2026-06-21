"""Seq2Seq Page."""

import streamlit as st

from ui.components.layout import render_page_header, render_section_title
from ui.components.cards import render_metric_card

def render() -> None:
    render_page_header(
        "Sequence-to-Sequence Model",
        "Architecture Encoder–Decoder."
    )

    # Input and Generation
    st.markdown('<div class="saas-card">', unsafe_allow_html=True)
    input_seq = st.text_input("Input Sequence", placeholder="Type a sentence in English to translate...")
    
    if st.button("Generate Sequence", type="primary"):
        if input_seq:
            st.markdown(
                f"""
                <div style="margin-top: 1.5rem; display: flex; flex-direction: column; gap: 1rem;">
                    <div style="padding: 1rem; border-left: 4px solid var(--text-muted); background: rgba(255,255,255,0.05); border-radius: 0.5rem;">
                        <span style="font-size: 0.875rem; color: var(--text-muted); text-transform: uppercase;">Séquence d'entrée</span><br>
                        <span style="font-size: 1.125rem; color: var(--text-main);">{input_seq}</span>
                    </div>
                    <div style="padding: 1rem; border-left: 4px solid var(--accent-cyan); background: rgba(6, 182, 212, 0.1); border-radius: 0.5rem;">
                        <span style="font-size: 0.875rem; color: var(--accent-cyan); text-transform: uppercase;">Séquence générée</span><br>
                        <span style="font-size: 1.125rem; color: var(--text-main); font-weight: 500;">Ceci est une traduction simulée (dummy output).</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.warning("Please provide an input sequence.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Encoder / Decoder Architecture Visualization
    render_section_title("Architecture Seq2Seq")
    st.markdown(
        """
        <div class="saas-card" style="display: flex; justify-content: space-between; align-items: center; padding: 2rem;">
            <div style="flex: 1; text-align: center; padding: 1.5rem; background: rgba(139, 92, 246, 0.1); border: 1px solid var(--accent-purple); border-radius: 1rem;">
                <h3 style="color: var(--accent-purple); margin-top: 0;">1. Encoder</h3>
                <p style="color: var(--text-muted); font-size: 0.875rem;">Processes the input sequence and compresses information into a context vector.</p>
                <div style="font-weight: bold; color: var(--text-main); margin-top: 1rem;">[ RNN / LSTM / GRU ]</div>
            </div>
            
            <div style="padding: 0 2rem; color: var(--accent-cyan); font-weight: bold; display: flex; flex-direction: column; align-items: center;">
                <div>Context Vector</div>
                <div style="font-size: 2rem;">&xrarr;</div>
            </div>
            
            <div style="flex: 1; text-align: center; padding: 1.5rem; background: rgba(6, 182, 212, 0.1); border: 1px solid var(--accent-cyan); border-radius: 1rem;">
                <h3 style="color: var(--accent-cyan); margin-top: 0;">2. Decoder</h3>
                <p style="color: var(--text-muted); font-size: 0.875rem;">Generates the output sequence step-by-step from the context vector.</p>
                <div style="font-weight: bold; color: var(--text-main); margin-top: 1rem;">[ RNN / LSTM / GRU ]</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Decoding Strategies
    col1, col2 = st.columns(2)
    with col1:
        render_section_title("3. Greedy Decoding")
        st.markdown(
            """
            <div class="saas-card" style="height: 150px;">
                <p style="color: var(--text-muted);">
                    Selects the token with the highest probability at each step. Fast but can lead to suboptimal global sequences as it cannot look ahead.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        render_section_title("4. Beam Search")
        st.markdown(
            """
            <div class="saas-card" style="height: 150px; position: relative;">
                <p style="color: var(--text-muted); margin-bottom: 0.5rem;">
                    Maintains Top-K (beam width) partial sequences. Explores multiple paths to find a better global optimum.
                </p>
                <div style="display: flex; gap: 0.5rem; justify-content: center; margin-top: 1rem;">
                    <span style="padding: 0.2rem 0.5rem; background: rgba(255,255,255,0.1); border-radius: 0.25rem; font-size: 0.75rem;">Path A (0.4)</span>
                    <span style="padding: 0.2rem 0.5rem; background: rgba(6,182,212,0.2); border: 1px solid var(--accent-cyan); border-radius: 0.25rem; font-size: 0.75rem;">Path B (0.7)</span>
                    <span style="padding: 0.2rem 0.5rem; background: rgba(255,255,255,0.1); border-radius: 0.25rem; font-size: 0.75rem;">Path C (0.2)</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Metrics
    render_section_title("Training Metrics")
    mcol1, mcol2 = st.columns(2)
    with mcol1:
        render_metric_card("5. Perplexity", "12.4", "Lower is better. Exp(CrossEntropyLoss).")
    with mcol2:
        render_metric_card("6. Gradient Clipping", "Max Norm: 1.0", "Prevents exploding gradients in deep RNNs.")
