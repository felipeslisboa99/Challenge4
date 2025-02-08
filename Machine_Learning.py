import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose

def app():
    st.title("📊 Análise de Séries Temporais")

    # Carregar os dados
    df = pd.read_excel("base_petroleo.xlsx")
    df["data"] = pd.to_datetime(df["data"])

    # Exibir os primeiros dados
    st.write("### Dados Carregados")
    st.dataframe(df.head())

    # Criar Série Temporal
    st.write("### 📈 Série Temporal")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df["data"], df["preco_bruto_Brent_FOB"], linestyle="-")
    ax.set_title("Série Temporal", fontsize=14)
    ax.set_xlabel("Data", fontsize=12)
    ax.set_ylabel("Preço Bruto Brent FOB", fontsize=12)
    ax.grid(True, which="major", axis="x", linestyle="--", color="gray", alpha=0.7)
    st.pyplot(fig)  # <- ESSA LINHA FAZ O GRÁFICO APARECER NO STREAMLIT

    # Decomposição da Série Temporal
    st.write("### 🔍 Decomposição da Série Temporal")
    result = seasonal_decompose(df["preco_bruto_Brent_FOB"], model="additive", period=365)
    fig = result.plot()
    fig.set_size_inches(14, 7)
    st.pyplot(fig)  # <- ESSA LINHA FAZ O GRÁFICO APARECER NO STREAMLIT

    # Série Temporal Diferenciada
    df["Diferenciado"] = df["preco_bruto_Brent_FOB"].diff()
    st.write("### 📉 Série Temporal Diferenciada (Estacionarizada)")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df["data"], df["Diferenciado"])
    ax.set_title("Série Temporal Diferenciada", fontsize=14)
    ax.set_xlabel("Data", fontsize=12)
    ax.set_ylabel("Valores Diferenciados", fontsize=12)
    st.pyplot(fig)  # <- ESSA LINHA FAZ O GRÁFICO APARECER NO STREAMLIT
