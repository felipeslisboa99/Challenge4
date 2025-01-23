import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def app():
    # Título da página com estilo
    st.markdown(
        """
        <div style="background-color:#007acc;padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">🔎 Analisando e Compreendendo as Variações do Mercado de Petróleo</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Criando as abas
    tab3, tab4, tab5 = st.tabs(["📘 Introdução", "🎯 Objetivo", "💡 Aprendizado"])

    # Aba Introdução
    with tab3:
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
        st.markdown(
            """
            <div style="background-color:#f4f4f9;padding:15px;border-radius:10px;margin:20px 0;">
            <h3 style="color:#007acc;text-align:center;">🔍 Insights Fundamentais</h3>
            <ul style="font-size:18px;line-height:1.8;">
                <li><b>Geopolítica e Fatores Geoeconômicos</b>: Como conflitos, sanções e acordos internacionais moldam o preço do petróleo.</li>
                <li><b>Crises Econômicas</b>: O impacto de eventos macroeconômicos globais, como recessões e mudanças na política monetária.</li>
                <li><b>Demanda Energética</b>: A influência das mudanças na demanda por energia, especialmente em momentos de transição energética.</li>
                <li><b>Avanços Tecnológicos</b>: O papel de inovações no setor energético, como energias renováveis e novas técnicas de extração.</li>
            </ul>
            </div>
            """
        )
        st.markdown(
            """
            ### 🕒 Linha do Tempo do Mercado de Petróleo:
            - **1973:** Crise do Petróleo - Primeiro choque no preço global.
            - **1986:** Queda drástica nos preços devido ao aumento da produção.
            - **2008:** Crise financeira global - Impacto significativo na demanda de petróleo.
            - **2020:** Pandemia de COVID-19 - Demanda reduzida drasticamente.
            """
        )

    # Aba Objetivo
    with tab4:
        st.markdown(
            """
            <div style="background-color:#f4f4f9;padding:15px;border-radius:10px;">
            <h3 style="color:#007acc;text-align:center;">🎯 Objetivo</h3>
            <p style="text-align:justify; font-size:18px;">
            Este projeto tem como objetivo principal explorar, analisar e prever as oscilações no preço do petróleo bruto Brent.
            Através do uso de técnicas avançadas de análise de dados e Machine Learning, busca-se:
            </p>
            <ul style="font-size:16px;line-height:1.8;">
                <li><b>Analisar Tendências Históricas:</b> Entender padrões recorrentes e seus impactos no mercado.</li>
                <li><b>Prever Movimentos Futuros:</b> Desenvolver modelos que auxiliem na projeção de preços futuros com base em dados históricos.</li>
                <li><b>Identificar Fatores Chave:</b> Compreender como eventos geopolíticos, avanços tecnológicos e mudanças na demanda influenciam os preços.</li>
            </ul>
            <p style="text-align:justify; font-size:18px;">
            Com isso, esperamos fornecer uma base sólida para a tomada de decisões estratégicas em um mercado tão volátil.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Aba Aprendizado
    with tab5:
        st.markdown(
            """
            <div style="background-color:#f4f4f9;padding:15px;border-radius:10px;">
            <h3 style="color:#007acc;text-align:center;">💡 Aprendizado</h3>
            <p style="text-align:justify; font-size:18px;">
            Durante o desenvolvimento deste projeto, vários aprendizados foram adquiridos, como:
            </p>
            <ul style="font-size:16px;line-height:1.8;">
                <li><b>Importância da Preparação de Dados:</b> Dados limpos e bem estruturados são essenciais para análises confiáveis.</li>
                <li><b>Modelos de Machine Learning:</b> Abordagens como XGBoost e Prophet mostraram-se eficazes para a previsão de séries temporais.</li>
                <li><b>Impacto de Eventos Globais:</b> Fatores como crises econômicas e pandemias podem causar oscilações significativas no mercado.</li>
                <li><b>Visualizações Interativas:</b> Representações gráficas ajudam na comunicação clara dos resultados e insights.</li>
            </ul>
            <p style="text-align:justify; font-size:18px;">
            Este aprendizado reforça a importância de uma abordagem interdisciplinar para enfrentar desafios em mercados complexos.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    app()
