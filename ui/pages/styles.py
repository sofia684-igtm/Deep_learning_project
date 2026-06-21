import streamlit as st

def apply_custom_style():
    """Applique le thème CSS global Premium SaaS à l'application."""
    st.markdown(
        """
        <style>
        /* Importer une police professionnelle */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Inter', sans-serif;
            background-color: #0F172A;
            color: #E2E8F0;
        }
        
        /* Cacher les éléments natifs Streamlit inutiles */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {background: transparent !important;}
        
        /* Sidebar premium et fixe */
        [data-testid="stSidebar"] {
            background-color: #090D1A !important;
            border-right: 1px solid rgba(255, 255, 255, 0.05);
            min-width: 260px !important;
            max-width: 260px !important;
        }
        
        /* Conteneur principal */
        .main-container {
            padding: 2rem;
            animation: fadeIn 0.5s ease-in-out;
        }
        
        /* Cartes KPI Glassmorphism */
        .kpi-card {
            background: rgba(30, 41, 59, 0.4);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.3);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }
        .kpi-card:hover {
            transform: translateY(-2px);
            border-color: rgba(6, 182, 212, 0.3); /* Accent Cyan discret */
        }
        
        .kpi-val {
            font-size: 2.25rem;
            font-weight: 700;
            color: #FFFFFF;
            margin-bottom: 0.25rem;
        }
        .kpi-label {
            font-size: 0.85rem;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        /* Boutons personnalisés par page */
        .stButton>button {
            width: 100%;
            border-radius: 8px;
            padding: 0.6rem 1.5rem;
            font-weight: 500;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            border: none;
        }
        
        /* Bouton spécifique MLP (Accent Violet) */
        .btn-mlp button {
            background: linear-gradient(135deg, #7C3AED 0%, #4C1D95 100%) !important;
            color: white !important;
            box-shadow: 0 4px 12px rgba(124, 58, 237, 0.2);
        }
        .btn-mlp button:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 20px rgba(124, 58, 237, 0.4) !important;
        }
        
        /* Bouton spécifique CNN (Accent Cyan) */
        .btn-cnn button {
            background: linear-gradient(135deg, #06B6D4 0%, #0891B2 100%) !important;
            color: #0F172A !important;
            font-weight: 600 !important;
        }
        .btn-cnn button:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 20px rgba(6, 182, 212, 0.4) !important;
        }
        
        /* Boutons pour les pages récurrentes (Style épuré Tech) */
        .btn-tech button {
            background: rgba(255, 255, 255, 0.05) !important;
            color: white !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }
        .btn-tech button:hover {
            background: rgba(255, 255, 255, 0.1) !important;
            border-color: rgba(255, 255, 255, 0.2) !important;
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Tableaux académiques */
        .styled-table {
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 0.95rem;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        }
        .styled-table th {
            background-color: #1E293B;
            color: #ffffff;
            text-align: left;
            padding: 12px 15px;
            font-weight: 600;
        }
        .styled-table td {
            padding: 12px 15px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def card_kpi(value, label):
    """Générateur de carte KPI HTML."""
    return f"""
    <div class="kpi-card">
        <div class="kpi-val">{value}</div>
        <div class="kpi-label">{label}</div>
    </div>
    """