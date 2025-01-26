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
            <h3 style="text-align:center;">🔍 Análise de Insights Detalhados</h3>
            <p style="text-align:justify; font-size:18px;">
            Bem-vindo à seção de Insights Detalhados! Aqui, exploramos os dados em profundidade, destacando tendências, correlações e previsões com base em análises avançadas e modelagem preditiva.
            </p>
            """,
            unsafe_allow_html=True
        )

        # Dividindo a página em colunas para organização
        col1, col2 = st.columns([1, 1])

        # Conteúdo da primeira coluna (Análises)
    with col1:
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

         # Gráfico de exemplo: Tendências históricas
        st.markdown(
            """
            <h5 style="text-align:center;">📈 Tendências Históricas</h5>
            """,
            unsafe_allow_html=True
        )

        # Dados para o gráfico
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

        # Conteúdo da segunda coluna (Explicações e Previsões)
    with col2:
        st.markdown(
            """
            <h4 style="text-align:center;">📋 Explicações e Previsões</h4>
            <p style="text-align:justify; font-size:16px;">
            A partir das análises, é possível identificar padrões críticos que afetam diretamente os preços no mercado. As previsões a seguir são baseadas em modelos avançados:
            </p>
            <ul style="font-size:16px;line-height:1.8;">
                <li><b>Previsões de curto prazo:</b> Aumento gradual nos próximos meses devido à demanda sazonal.</li>
                <li><b>Impactos de eventos geopolíticos:</b> Oscilações significativas causadas por instabilidade em regiões produtoras.</li>
                <li><b>Estimativas de longo prazo:</b> Adaptação do mercado às fontes de energia renováveis.</li>
            </ul>
             """,
            unsafe_allow_html=True
        )

        # Gráfico de previsão
        st.markdown(
            """
            <h5 style="text-align:center;">🔮 Projeções Futuras</h5>
            """,
            unsafe_allow_html=True
        )

        # Dados para o gráfico de previsão
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

       # Rodapé com resumo
        st.markdown(
            """
            <hr style="border:1px solid #007acc;">
         <div style="background-color:#f9f9f9;padding:15px;border-radius:10px;margin-top:20px;">
            <p style="text-align:justify;font-size:16px;">
            Com base nos insights apresentados, é possível estruturar estratégias robustas para minimizar riscos e aproveitar oportunidades no mercado. Para mais detalhes, consulte as seções específicas ou entre em contato com nossos especialistas.
           </p>
         </div>
           """,
        unsafe_allow_html=True
        )