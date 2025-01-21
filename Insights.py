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

        # Como usar o dashboard
        st.markdown(
            """
            <h4>🛠 Como usar este dashboard:</h4>
            <ul style="font-size:16px;line-height:1.8;">
                <li><b>Indicadores-Chave:</b> Veja métricas como o preço máximo, mínimo e médio em diferentes períodos.</li>
                <li><b>Filtros Interativos:</b> Personalize sua análise ajustando os filtros no painel.</li>
                <li><b>Comparação de Períodos:</b> Compare diferentes anos ou meses para avaliar tendências.</li>
            </ul>
            """,
            unsafe_allow_html=True
        )

        # Link de incorporação do Power BI
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

        # Benefícios do dashboard
        st.markdown(
            """
            <div style="background-color:#f4f4f9;padding:15px;border-radius:10px;margin-top:20px;">
            <h4 style="text-align:center;">✨ Benefícios do Dashboard</h4>
            <p style="text-align:justify; font-size:16px;">
            Este dashboard é ideal para:
            </p>
            <ul style="font-size:16px;line-height:1.8;">
                <li><b>Tomada de Decisões:</b> Compreenda o impacto de eventos históricos e geopolíticos nos preços.</li>
                <li><b>Análise Intuitiva:</b> Gráficos interativos para facilitar a compreensão de tendências.</li>
                <li><b>Planejamento Estratégico:</b> Use insights para fundamentar estratégias no mercado de petróleo.</li>
                <li><b>Monitoramento de Tendências:</b> Identifique rapidamente os movimentos do mercado para tomar decisões em tempo real.</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Conteúdo da aba Insights Detalhados
    with tab2:
        st.markdown(
            """
            <h3 style="text-align:center;">🔍 Análise de Insights</h3>
            <p style="text-align:justify; font-size:18px;">
            Nesta seção, apresentamos os insights gerados a partir dos dados, abordando fatores como:
            </p>
            <ul style="font-size:16px;line-height:1.8;">
                <li><b>Tendências Históricas:</b> Análise dos padrões de preços ao longo dos anos.</li>
                <li><b>Correlação de Variáveis:</b> Impactos de fatores geopolíticos e econômicos no mercado de petróleo.</li>
                <li><b>Previsões:</b> Insights futuros com base em modelos de Machine Learning.</li>
            </ul>
            <hr style="border:1px solid #007acc;">
            """,
            unsafe_allow_html=True
        )

        # Exemplo de gráfico detalhado
        st.markdown(
            """
            <h4 style="text-align:center; margin-top:20px;">📈 Exemplo de Gráfico de Insights</h4>
            """,
            unsafe_allow_html=True
        )

        # Criar um gráfico de exemplo
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

        st.markdown(
            """
            <div style="background-color:#f0f8ff;padding:15px;border-radius:10px;margin-top:20px;">
            <p style="text-align:justify;font-size:16px;">
            A visualização acima demonstra padrões de oscilação de preços ao longo do tempo. Esses insights ajudam a compreender a dinâmica do mercado e identificar tendências importantes para estratégias futuras.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

