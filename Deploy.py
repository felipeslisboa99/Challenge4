import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def app():
    # Título principal
    st.markdown(
        """
        <div style="background-color:#007acc;padding:15px;border-radius:10px;text-align:center">
        <h1 style="color:white;">🚀 Deploy - Previsão do Preço do Petróleo</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="font-size:18px;text-align:justify;">
        Bem-vindo à seção de deploy! Aqui você pode explorar as previsões futuras do preço do petróleo bruto Brent, 
        utilizando modelos baseados em aprendizado de máquina. Ajuste os parâmetros para obter insights personalizados 
        sobre o mercado energético.
        </p>
        """,
        unsafe_allow_html=True
    )

   
    # Parâmetros interativos
    st.markdown("### 🔧 Parâmetros de Previsão")
    anos = st.slider("Escolha o período de previsão (anos):", 1, 10, 5)
    erro_max = st.slider("Defina a margem de erro (em %):", 5, 20, 10)

    # Gerar dados fictícios para previsão anual
    data_futura = pd.date_range(start='2025', periods=anos, freq='Y')
    previsao = np.random.uniform(70, 100, len(data_futura))
    erro_valor = previsao * (erro_max / 100)

    # Gráfico de previsão
    st.markdown("### 📈 Gráfico de Previsão")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data_futura, previsao, marker='o', linestyle='-', color='blue', label='Preço Estimado')
    ax.fill_between(data_futura, previsao - erro_valor, previsao + erro_valor, color='blue', alpha=0.2, label='Margem de Erro')
    ax.set_title("Previsão do Preço do Petróleo (Brent)", fontsize=16)
    ax.set_xlabel("Mês", fontsize=12)
    ax.set_ylabel("Preço Estimado (USD)", fontsize=12)
    ax.legend()
    st.pyplot(fig)

    # Tabela de valores previstos
    st.markdown("### 📋 Detalhes da Previsão")
    tabela_previsao = pd.DataFrame({
        "Data": data_futura.strftime('%Y'),
        "Preço Estimado (USD)": [f"${p:.2f}" for p in previsao],
        "Margem Inferior (USD)": [f"${(p - e):.2f}" for p, e in zip(previsao, erro_valor)],
        "Margem Superior (USD)": [f"${(p + e):.2f}" for p, e in zip(previsao, erro_valor)],
    })
    st.dataframe(tabela_previsao)

    # Conclusão
    st.markdown(
        """
        <div style="background-color:#f0f0f0;padding:15px;border-radius:10px;text-align:center;margin-top:20px;">
        <p style="font-size:16px;color:gray;">
        📊 As previsões fornecem uma visão aproximada baseada em dados históricos. Use-as como apoio estratégico 
        para decisões no mercado de petróleo.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )
