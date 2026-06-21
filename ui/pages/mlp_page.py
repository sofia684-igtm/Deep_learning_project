"""MLP Page."""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

from ui.components.layout import render_page_header, render_section_title
from ui.components.cards import render_metric_card

def render() -> None:
    render_page_header(
        "Multi-Layer Perceptron",
        "Classification du cancer du sein à partir du dataset Breast Cancer Wisconsin."
    )

    # 1. Dataset Overview
    render_section_title("Dataset Overview")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(
            """
            <div class="saas-card" style="height: 100%;">
                <div style="font-weight: 600; font-size: 1.125rem; margin-bottom: 0.5rem;">Breast Cancer Wisconsin (Diagnostic)</div>
                <div style="color: var(--text-muted); line-height: 1.6;">
                    Ce dataset contient 569 échantillons de tumeurs, avec 30 caractéristiques numériques calculées à partir d'images numérisées d'aspirations à l'aiguille fine (FNA) de masses mammaires.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        # Dummy Pie Chart using Plotly with dark theme matching our UI
        fig = px.pie(
            values=[357, 212], 
            names=['Benign', 'Malignant'],
            color_discrete_sequence=['#06B6D4', '#8B5CF6'],
            hole=0.4
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#FFFFFF'),
            margin=dict(t=0, b=0, l=0, r=0),
            height=200
        )
        st.plotly_chart(fig, use_container_width=True)

    # 2. Network Architecture
    render_section_title("Network Architecture")
    st.markdown(
        """
        <div class="saas-card">
            <div style="display: flex; justify-content: center; gap: 2rem; align-items: center; padding: 2rem 0;">
                <div style="text-align: center;">
                    <div style="width: 60px; height: 60px; border-radius: 50%; background: var(--border-color); display: flex; align-items: center; justify-content: center; font-weight: bold;">30</div>
                    <div style="margin-top: 0.5rem; color: var(--text-muted); font-size: 0.875rem;">Input Layer</div>
                </div>
                <div style="color: var(--accent-cyan); font-weight: bold;">&xrarr;</div>
                <div style="text-align: center;">
                    <div style="width: 60px; height: 60px; border-radius: 50%; background: rgba(139, 92, 246, 0.2); border: 2px solid var(--accent-purple); display: flex; align-items: center; justify-content: center; font-weight: bold;">16</div>
                    <div style="margin-top: 0.5rem; color: var(--text-muted); font-size: 0.875rem;">Hidden 1 (ReLU)</div>
                </div>
                <div style="color: var(--accent-cyan); font-weight: bold;">&xrarr;</div>
                <div style="text-align: center;">
                    <div style="width: 60px; height: 60px; border-radius: 50%; background: rgba(139, 92, 246, 0.2); border: 2px solid var(--accent-purple); display: flex; align-items: center; justify-content: center; font-weight: bold;">8</div>
                    <div style="margin-top: 0.5rem; color: var(--text-muted); font-size: 0.875rem;">Hidden 2 (ReLU)</div>
                </div>
                <div style="color: var(--accent-cyan); font-weight: bold;">&xrarr;</div>
                <div style="text-align: center;">
                    <div style="width: 60px; height: 60px; border-radius: 50%; background: rgba(6, 182, 212, 0.2); border: 2px solid var(--accent-cyan); display: flex; align-items: center; justify-content: center; font-weight: bold;">1</div>
                    <div style="margin-top: 0.5rem; color: var(--text-muted); font-size: 0.875rem;">Output (Sigmoid)</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 3. Model Prediction
    render_section_title("Model Prediction")
    st.markdown('<div class="saas-card">', unsafe_allow_html=True)
    st.markdown('<div style="margin-bottom: 1rem; color: var(--text-muted);">Enter sample features to run the diagnosis:</div>', unsafe_allow_html=True)
    
    col_input1, col_input2, col_input3 = st.columns(3)
    with col_input1:
        radius = st.number_input("Mean Radius", value=14.0)
    with col_input2:
        texture = st.number_input("Mean Texture", value=19.0)
    with col_input3:
        perimeter = st.number_input("Mean Perimeter", value=90.0)
    
    if st.button("Run Diagnosis", type="primary", use_container_width=True):
        st.success("Analysis complete!")
        # Dummy Results
        rcol1, rcol2 = st.columns(2)
        with rcol1:
            render_metric_card("Predicted Class", "Benign", "Based on model output")
        with rcol2:
            render_metric_card("Probability", "98.4%", "Confidence score")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # 4. Performance Metrics
    render_section_title("Performance Metrics")
    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
    with mcol1:
        render_metric_card("Accuracy", "96.5%")
    with mcol2:
        render_metric_card("Precision", "97.1%")
    with mcol3:
        render_metric_card("Recall", "95.8%")
    with mcol4:
        render_metric_card("F1-Score", "96.4%")

    # Confusion Matrix
    col_cm, col_init = st.columns(2)
    with col_cm:
        st.markdown('<div style="font-weight:600; margin-bottom:1rem;">Confusion Matrix</div>', unsafe_allow_html=True)
        z = [[70, 2], [3, 39]]
        x = ['Benign (Pred)', 'Malignant (Pred)']
        y = ['Benign (True)', 'Malignant (True)']
        fig_cm = px.imshow(z, text_auto=True, x=x, y=y, color_continuous_scale=['#0F172A', '#8B5CF6', '#06B6D4'])
        fig_cm.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#FFFFFF'),
            margin=dict(t=0, b=0, l=0, r=0),
            height=300
        )
        st.plotly_chart(fig_cm, use_container_width=True)
        
    with col_init:
        st.markdown('<div style="font-weight:600; margin-bottom:1rem;">Initializations Comparison</div>', unsafe_allow_html=True)
        epochs = np.arange(1, 21)
        loss_he = np.exp(-epochs/4) + np.random.normal(0, 0.05, 20)
        loss_xavier = np.exp(-epochs/5) + np.random.normal(0, 0.05, 20)
        loss_random = np.exp(-epochs/8) + 0.2 + np.random.normal(0, 0.05, 20)
        
        fig_loss = go.Figure()
        fig_loss.add_trace(go.Scatter(x=epochs, y=loss_he, name='He', line=dict(color='#06B6D4')))
        fig_loss.add_trace(go.Scatter(x=epochs, y=loss_xavier, name='Xavier', line=dict(color='#8B5CF6')))
        fig_loss.add_trace(go.Scatter(x=epochs, y=loss_random, name='Random', line=dict(color='#94A3B8')))
        
        fig_loss.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#FFFFFF'),
            margin=dict(t=0, b=0, l=0, r=0),
            height=300,
            xaxis_title="Epochs",
            yaxis_title="Loss",
            legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99)
        )
        st.plotly_chart(fig_loss, use_container_width=True)
