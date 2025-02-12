import streamlit as st
import matplotlib.pyplot as plt

def app():
    # Configurando responsividade e fundo neutro
    st.markdown(
        """
        <style>
            body {
                background-color: white !important;
                color: black !important;
            }
            .stTabs {
                background-color: white !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Título da página
    st.markdown(
        """
        <h1 style="text-align:center; color:#007acc;">🔎 Analisando e Compreendendo as Variações do Mercado de Petróleo</h1>
        """,
        unsafe_allow_html=True
    )

    # Criando as abas
    tab3, tab4, tab5 = st.tabs(["📘 Introdução", "🎯 Objetivo", "💡 Aprendizado"])

    # Aba Introdução
    with tab3:
        st.markdown(
            """
            <h3 style="color:#007acc;text-align:center;">📘 Introdução</h3>
            <p style="text-align:justify; font-size:18px; line-height:1.6; color:black;">
            No coração da economia global, o <b style="color:#007acc;">petróleo</b> desempenha um papel vital como motor do progresso e da energia.
            Analisar e compreender as oscilações de preços não é apenas uma tarefa estratégica, mas um diferencial competitivo
            para negócios, governos e investidores.
            </p>
            <p style="text-align:justify; font-size:18px; line-height:1.6; color:black;">
            Combinando a força de <b>dados históricos</b> e <b>técnicas avançadas de análise</b>, este dashboard oferece uma abordagem dinâmica para explorar
            as variações do mercado de petróleo. Por meio de <b>visualizações interativas</b>, você poderá identificar padrões ocultos,
            prever tendências futuras e tomar decisões fundamentadas com base em insights claros e precisos.
            </p>
            """,
            unsafe_allow_html=True
        )

    # Aba Objetivo
    with tab4:
        st.markdown(
            """
            <h3 style="color:#007acc;text-align:center;">🎯 Objetivo</h3>
            <p style="text-align:justify; font-size:18px; color:black;">
            O objetivo deste projeto é analisar e compreender as oscilações do mercado de petróleo por meio de dados históricos e técnicas avançadas de Machine Learning. Busca-se identificar padrões sazonais, avaliar o impacto de eventos geopolíticos e prever tendências futuras com alta precisão. Além disso, o projeto visa explorar como a transição para energias renováveis influencia o mercado tradicional. Combinando análises estatísticas e visuais, pretende-se fornecer insights práticos que auxiliem na tomada de decisões estratégicas em um mercado altamente volátil. Assim, o projeto contribui para uma compreensão aprofundada e embasada do setor energético global.
            </p>
            """,
            unsafe_allow_html=True
        )

    # Aba Aprendizado
    with tab5:
        st.markdown(
            """
            <h3 style="color:#007acc;text-align:center;">💡 Aprendizado</h3>
            <p style="text-align:justify; font-size:18px; color:black;">
            Com este projeto, aprendemos a importância da análise de dados históricos para identificar padrões sazonais e tendências no mercado de petróleo. Descobrimos como eventos geopolíticos, como conflitos e sanções, influenciam diretamente os preços, reforçando a necessidade de análises estratégicas. O uso de técnicas de Machine Learning destacou a eficácia de modelos preditivos, como Prophet e XGBoost, para capturar oscilações complexas. Também compreendemos o impacto crescente das energias renováveis na dinâmica do mercado tradicional. Por fim, o trabalho evidenciou a relevância de abordagens interdisciplinares, unindo economia, ciência de dados e política global, para resultados mais completos e precisos.
            </p>
            """,
            unsafe_allow_html=True
        )
