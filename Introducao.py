import streamlit as st
import matplotlib.pyplot as plt

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

    # Introdução com destaque
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
        </div>
        """,
        unsafe_allow_html=True
    )

    # Objetivo do Streamlit
    st.markdown(
        """
        <p style="font-size:18px;line-height:1.6;text-align:justify;">
        Este <b>Streamlit</b> foi desenvolvido com o objetivo de explorar, analisar e prever as oscilações no preço do petróleo bruto Brent, utilizando dados históricos, técnicas de <b>Machine Learning</b> e uma abordagem prática e acessível.
        </p>
        """,
        unsafe_allow_html=True
    )

    # Insights fundamentais com estilo
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
        """,
        unsafe_allow_html=True
    )

    # Linha do Tempo
    st.markdown("### 🕒 Linha do Tempo do Mercado de Petróleo:")
    st.markdown(
        """
        - **1973:** Crise do Petróleo - Primeiro choque no preço global.
        - **1986:** Queda drástica nos preços devido ao aumento da produção.
        - **2008:** Crise financeira global - Impacto significativo na demanda de petróleo.
        - **2020:** Pandemia de COVID-19 - Demanda reduzida drasticamente.
        """
    )

    # Conclusão com destaque
    st.markdown(
        """
        <div style="font-size:18px;line-height:1.6;text-align:justify;margin-top:20px;">
        Por meio do <b>Streamlit</b>, você encontrará visualizações interativas, análises detalhadas e previsões que buscam desvendar os fatores que impulsionam as flutuações do preço do petróleo, auxiliando na tomada de decisões estratégicas.
        </div>
        """,
        unsafe_allow_html=True
    )

