"""CNN Page."""

import streamlit as st
import numpy as np

from ui.components.layout import render_page_header, render_section_title
from ui.components.cards import render_metric_card

def render() -> None:
    render_page_header(
        "Convolutional Neural Network",
        "Reconnaissance de chiffres manuscrits MNIST."
    )

    # 1. Upload Image & 2. Prediction
    render_section_title("Upload & Prediction")
    st.markdown('<div class="saas-card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        uploaded_file = st.file_uploader("Drag & Drop your digit image here", type=["png", "jpg", "jpeg"])
        analyze_btn = st.button("Analyze Digit", type="primary", use_container_width=True)
        
    with col2:
        if uploaded_file and analyze_btn:
            st.image(uploaded_file, caption="Uploaded Image", width=150)
            rcol1, rcol2 = st.columns(2)
            with rcol1:
                render_metric_card("Predicted Digit", "7")
            with rcol2:
                render_metric_card("Confidence", "99.8%")
        else:
            st.info("Upload an image and click 'Analyze Digit' to see prediction.")
            
    st.markdown('</div>', unsafe_allow_html=True)

    # 3. Feature Extraction
    render_section_title("Feature Extraction")
    st.markdown(
        """
        <div class="saas-card">
            <div style="font-weight: 600; margin-bottom: 1rem; color: var(--text-main);">Feature Maps Gallery</div>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem;">
        """,
        unsafe_allow_html=True
    )
    # Generate dummy feature map placeholders
    for i in range(8):
        st.markdown(
            f"""
            <div style="aspect-ratio: 1; background: radial-gradient(circle at center, rgba(6, 182, 212, {np.random.uniform(0.1, 0.8)}), var(--bg-color)); border: 1px solid var(--border-color); border-radius: 0.5rem; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; color: var(--text-muted);">
                Map {i+1}
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown('</div></div>', unsafe_allow_html=True)

    # 4. CNN Architecture
    render_section_title("CNN Architecture")
    st.markdown(
        """
        <div class="saas-card">
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 0;">
                <div style="text-align: center; padding: 1rem; border: 1px solid var(--border-color); border-radius: 0.5rem; background: var(--bg-color);">
                    <div style="font-weight: bold; color: var(--text-main);">Input Image</div>
                    <div style="font-size: 0.875rem; color: var(--text-muted);">28x28x1</div>
                </div>
                <div style="color: var(--accent-cyan); font-weight: bold;">&xrarr;</div>
                <div style="text-align: center; padding: 1rem; border: 1px solid var(--accent-cyan); border-radius: 0.5rem; background: rgba(6, 182, 212, 0.1);">
                    <div style="font-weight: bold; color: var(--accent-cyan);">Conv2D</div>
                    <div style="font-size: 0.875rem; color: var(--text-muted);">3x3 filters</div>
                </div>
                <div style="color: var(--accent-cyan); font-weight: bold;">&xrarr;</div>
                <div style="text-align: center; padding: 1rem; border: 1px solid var(--accent-purple); border-radius: 0.5rem; background: rgba(139, 92, 246, 0.1);">
                    <div style="font-weight: bold; color: var(--accent-purple);">Max Pooling</div>
                    <div style="font-size: 0.875rem; color: var(--text-muted);">2x2 window</div>
                </div>
                <div style="color: var(--accent-cyan); font-weight: bold;">&xrarr;</div>
                <div style="text-align: center; padding: 1rem; border: 1px solid var(--accent-cyan); border-radius: 0.5rem; background: rgba(6, 182, 212, 0.1);">
                    <div style="font-weight: bold; color: var(--accent-cyan);">Conv2D</div>
                    <div style="font-size: 0.875rem; color: var(--text-muted);">3x3 filters</div>
                </div>
                <div style="color: var(--accent-cyan); font-weight: bold;">&xrarr;</div>
                <div style="text-align: center; padding: 1rem; border: 1px solid var(--accent-purple); border-radius: 0.5rem; background: rgba(139, 92, 246, 0.1);">
                    <div style="font-weight: bold; color: var(--accent-purple);">Avg Pooling</div>
                    <div style="font-size: 0.875rem; color: var(--text-muted);">2x2 window</div>
                </div>
                <div style="color: var(--accent-cyan); font-weight: bold;">&xrarr;</div>
                <div style="text-align: center; padding: 1rem; border: 1px solid var(--border-color); border-radius: 0.5rem; background: var(--bg-color);">
                    <div style="font-weight: bold; color: var(--text-main);">Fully Connected</div>
                    <div style="font-size: 0.875rem; color: var(--text-muted);">10 classes</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
