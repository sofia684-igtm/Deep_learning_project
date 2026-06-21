"""Benchmark Page."""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from ui.components.layout import render_page_header, render_section_title

def render() -> None:
    render_page_header(
        "Benchmark and Model Comparison",
        "Analyse comparative des performances et caractéristiques de chaque architecture."
    )

    # Data
    data = [
        {"Architecture": "MLP", "Dataset": "Breast Cancer", "Accuracy": 96.5, "Advantages": "Simple, fast training", "Limitations": "No spatial/sequential awareness"},
        {"Architecture": "CNN", "Dataset": "MNIST", "Accuracy": 99.2, "Advantages": "Spatial hierarchies, translation invariance", "Limitations": "Requires grid-like data (images)"},
        {"Architecture": "RNN", "Dataset": "IMDb", "Accuracy": 85.2, "Advantages": "Processes sequences of any length", "Limitations": "Vanishing gradient, short-term memory"},
        {"Architecture": "LSTM", "Dataset": "IMDb", "Accuracy": 99.5, "Advantages": "Long-term dependencies, handles vanishing grad", "Limitations": "Computationally expensive, complex"},
        {"Architecture": "GRU", "Dataset": "IMDb", "Accuracy": 98.8, "Advantages": "Faster than LSTM, similar performance", "Limitations": "Less powerful than LSTM for very long seqs"},
        {"Architecture": "Seq2Seq", "Dataset": "Translation", "Accuracy": 94.0, "Advantages": "Variable length input to variable length output", "Limitations": "Information bottleneck at context vector"}
    ]
    df = pd.DataFrame(data)

    # 1. Comparison Table
    render_section_title("Model Comparison")
    st.markdown('<div class="saas-card">', unsafe_allow_html=True)
    # Style dataframe for a modern look
    st.dataframe(
        df,
        column_config={
            "Accuracy": st.column_config.ProgressColumn(
                "Accuracy (%)",
                help="Model Accuracy",
                format="%f%%",
                min_value=0,
                max_value=100,
            ),
        },
        hide_index=True,
        use_container_width=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        render_section_title("Accuracy Bar Chart")
        st.markdown('<div class="saas-card">', unsafe_allow_html=True)
        # Sort by accuracy for better visualization
        df_sorted = df.sort_values(by="Accuracy", ascending=True)
        fig_bar = px.bar(
            df_sorted, 
            x="Accuracy", 
            y="Architecture", 
            orientation='h',
            color="Architecture",
            color_discrete_sequence=['#334155', '#475569', '#06B6D4', '#6366F1', '#8B5CF6', '#A855F7']
        )
        fig_bar.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#FFFFFF'),
            margin=dict(t=10, b=0, l=0, r=0),
            height=350,
            showlegend=False,
            xaxis=dict(range=[80, 100])
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        render_section_title("Capabilities Radar Chart")
        st.markdown('<div class="saas-card">', unsafe_allow_html=True)
        
        categories = ['Images', 'Sequences', 'Speed', 'Memory', 'Complexity']
        
        fig_radar = go.Figure()
        
        fig_radar.add_trace(go.Scatterpolar(
            r=[1, 1, 5, 2, 1],
            theta=categories,
            fill='toself',
            name='MLP',
            line_color='#334155'
        ))
        fig_radar.add_trace(go.Scatterpolar(
            r=[5, 1, 3, 3, 3],
            theta=categories,
            fill='toself',
            name='CNN',
            line_color='#06B6D4'
        ))
        fig_radar.add_trace(go.Scatterpolar(
            r=[1, 5, 2, 5, 4],
            theta=categories,
            fill='toself',
            name='LSTM',
            line_color='#8B5CF6'
        ))

        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=False, range=[0, 5]),
                bgcolor='rgba(0,0,0,0)'
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#FFFFFF'),
            margin=dict(t=10, b=0, l=0, r=0),
            height=350,
            legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
        )
        st.plotly_chart(fig_radar, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Automatic Conclusions
    render_section_title("Automatic Conclusions")
    st.markdown(
        """
        <div class="saas-card" style="display: flex; gap: 1.5rem; justify-content: space-between;">
            <div style="flex: 1; padding: 1.5rem; background: rgba(6, 182, 212, 0.1); border-left: 4px solid var(--accent-cyan); border-radius: 0.5rem;">
                <h4 style="margin-top: 0; color: var(--accent-cyan);">Best for Image Classification</h4>
                <div style="font-size: 1.5rem; font-weight: bold; color: var(--text-main);">CNN</div>
                <p style="color: var(--text-muted); font-size: 0.875rem; margin-bottom: 0;">Achieves 99.2% accuracy on MNIST, leveraging spatial hierarchies.</p>
            </div>
            
            <div style="flex: 1; padding: 1.5rem; background: rgba(139, 92, 246, 0.1); border-left: 4px solid var(--accent-purple); border-radius: 0.5rem;">
                <h4 style="margin-top: 0; color: var(--accent-purple);">Best for Sentiment Analysis</h4>
                <div style="font-size: 1.5rem; font-weight: bold; color: var(--text-main);">LSTM</div>
                <p style="color: var(--text-muted); font-size: 0.875rem; margin-bottom: 0;">Captures long-term context with 99.5% accuracy on IMDb.</p>
            </div>
            
            <div style="flex: 1; padding: 1.5rem; background: rgba(255, 255, 255, 0.05); border-left: 4px solid var(--text-muted); border-radius: 0.5rem;">
                <h4 style="margin-top: 0; color: var(--text-main);">Best for General Sequence Modeling</h4>
                <div style="font-size: 1.5rem; font-weight: bold; color: var(--text-main);">Seq2Seq</div>
                <p style="color: var(--text-muted); font-size: 0.875rem; margin-bottom: 0;">Handles variable length inputs/outputs effectively (e.g., Translation).</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
