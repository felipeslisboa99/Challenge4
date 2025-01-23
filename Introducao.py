import streamlit as st
import matplotlib.pyplot as plt

# Funções para cada aba
def tab_introduction():
    st.markdown(
        """
        <div style="background-color:#007acc;padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">🔎 Introdução</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="text-align:justify; font-size:18px; line-height:1.6;">
        No coração da economia global, o <span style="color:#007acc;font-weight:bold;">petróleo</span> desempenha um papel vital como motor do progresso e da energia.
        Analisar e compreender as oscilações de preços não é apenas uma tarefa estratégica, mas um diferencial competitivo
        para negócios, governos e investidores.
        </p>
        <p style="text-align:justify; font-size:18px; line-height:1.6;">
        Combinando a força de <b>dados históricos</b> e <b>técnicas avançadas de análise</b>, este dashboard oferece uma abordagem dinâmica para explorar
        as variações do mercado de petróleo. Por meio de <b>visualizações interativas</b>, você poderá identificar padrões ocultos,
        prever tendências futuras e tomar decisões fundamentadas com base em insights claros e precisos.
        </p>
        """,
        unsafe_allow_html=True
    )

def tab_objectives():
    st.markdown(
        """
        <div style="background-color:#007acc;padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">🎯 Objetivos</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="text-align:justify; font-size:18px; line-height:1.6;">
        Este projeto tem como principais objetivos:
        </p>
        <ul style="font-size:18px;line-height:1.8;">
            <li><b>Analisar Padrões de Preço:</b> Identificar oscilações históricas no preço do petróleo e entender os fatores que influenciam essas variações.</li>
            <li><b>Desenvolver Modelos de Previsão:</b> Criar modelos robustos para prever tendências futuras utilizando técnicas de Machine Learning e estatística.</li>
            <li><b>Auxiliar na Tomada de Decisões:</b> Fornecer insights baseados em dados para apoiar empresas, governos e investidores em estratégias relacionadas ao mercado de petróleo.</li>
            <li><b>Explorar Fatores Econômicos e Geopolíticos:</b> Avaliar como eventos globais, como crises econômicas ou avanços tecnológicos, impactam os preços.</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

def tab_insights():
    st.markdown(
        """
        <div style="background-color:#007acc;padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">💡 Aprendizados</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="text-align:justify; font-size:18px; line-height:1.6;">
        Durante o desenvolvimento deste projeto, destacaram-se os seguintes aprendizados:
        </p>
        <ul style="font-size:18px;line-height:1.8;">
            <li><b>Compreensão da Dinâmica de Preços:</b> Eventos geopolíticos e econômicos têm impacto direto e significativo no mercado de petróleo.</li>
            <li><b>Utilização de Modelos Estatísticos e Machine Learning:</b> Abordagens combinadas geram melhores resultados na previsão de séries temporais.</li>
            <li><b>Importância de Dados Limpos:</b> A preparação e o tratamento de dados foram cruciais para garantir a qualidade das análises.</li>
            <li><b>Sazonalidade e Tendências:</b> Componentes sazonais e de tendência são indispensáveis para entender os ciclos de preço do petróleo.</li>
            <li><b>Visualizações Interativas:</b> Gráficos claros e interativos facilitam a interpretação dos resultados e a comunicação dos insights.</li>
        </ul>
        <p style="text-align:justify; font-size:18px; line-height:1.6;">
        Esses aprendizados reforçam a importância de uma análise multidimensional e baseada em dados para enfrentar os desafios do mercado global.
        </p>
        """,
        unsafe_allow_html=True
    )

def app():
    # Layout com abas
    st.title("Dashboard do Mercado de Petróleo")
    tabs = st.tabs(["Introdução", "Objetivos", "Aprendizados"])

    with tabs[0]:
        tab_introduction()
    with tabs[1]:
        tab_objectives()
    with tabs[2]:
        tab_insights()

if __name__ == "__main__":
    app()
