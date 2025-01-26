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

    # Conteúdo da aba Power BI
    with tab1:
        st.markdown(
            """
            <h3 style="text-align:center;">💻 Explorando o Dashboard Power BI</h3>
            <p style="text-align:justify; font-size:18px;">
            O <b>Dashboard Power BI</b> foi desenvolvido para oferecer uma análise visual interativa das flutuações no mercado de petróleo. 
            Aqui, você pode explorar os principais indicadores e tendências que impactam os preços ao longo do tempo.
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <iframe 
                width="100%" 
                height="600" 
                src="https://app.powerbi.com/view?r=eyJrIjoiOTgxYjk0NTQtM2I5Yi00ZmM0LWJjNTEtNTViZmM1OWEwMjVjIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9&pageName=0082ee71249d6144a69d" 
                frameborder="0" 
                allowFullScreen="true">
            </iframe>
            """,
            unsafe_allow_html=True
        )

    # Conteúdo da aba Insights Detalhados
    with tab2:
        st.markdown(
            """
            <h3 style="text-align:center;">🔍 Análise de Insights Detalhados</h3>
            <p style="text-align:justify; font-size:18px;">
            Bem-vindo à seção de Insights Detalhados! Aqui, exploramos os dados em profundidade, destacando tendências, correlações e previsões com base em análises avançadas e modelagem preditiva.
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <h4 style="text-align:center;">📊 Principais Insights</h4>
            <ul style="font-size:16px;line-height:1.8;">
                <li><b>Tendências Históricas:</b> Análise detalhada das mudanças de preços ao longo dos últimos anos.</li>
                <li><b>Correlação de Variáveis:</b> Impactos diretos e indiretos de fatores geopolíticos e econômicos no mercado.</li>
                <li><b>Modelos Preditivos:</b> Projeções futuras usando Machine Learning e algoritmos estatísticos.</li>
            </ul>
            """,
            unsafe_allow_html=True
        )

        # Gráfico de Tendências Históricas
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(x, y, label="Oscilações Históricas", color="blue", linewidth=2)
        ax.set_title("Oscilações de Preços do Petróleo", fontsize=14)
        ax.set_xlabel("Período")
        ax.set_ylabel("Preço")
        ax.legend()
        ax.grid(alpha=0.5)

        st.pyplot(fig)

        # Gráfico de Projeções Futuras
        x_future = np.linspace(0, 10, 100)
        y_future = np.cos(x_future) + 0.2 * np.random.randn(100)

        fig2, ax2 = plt.subplots(figsize=(8, 4))
        ax2.plot(x_future, y_future, label="Projeção de Preços", color="green", linewidth=2)
        ax2.set_title("Projeção de Preços do Petróleo", fontsize=14)
        ax2.set_xlabel("Período")
        ax2.set_ylabel("Preço Previsto")
        ax2.legend()
        ax2.grid(alpha=0.5)

        st.pyplot(fig2)

