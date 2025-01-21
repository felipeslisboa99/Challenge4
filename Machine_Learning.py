import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def app():
    # Título principal
    st.markdown(
        """
        <div style="background-color:#007acc;padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">📊 Insights e Power BI</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Criando as abas
    tab1, tab2 = st.tabs(["💻 Power BI", "🔍 Insights Detalhados"])
