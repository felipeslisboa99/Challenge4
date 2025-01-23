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

    # Criando as abas
    tab3, tab4, tab5 = st.tabs(["📘 Introdução", "🎯 Objetivo", "💡 Aprendizado"])

    # Aba Introdução
    with tab3:
        st.markdown(
            """
            <div style="background-color:#f4f4f9;padding:15px;border-radius:10px;">
            <h3 style="color:#007acc;text-align:center;">📘 Introdução</h3>
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
                <li><b>Geopolítica e Fatores Geoeconômicos:</b> Como conflitos, sanções e acordos internacionais moldam o preço do petróleo.</li>
                <li><b>Crises Econômicas:</b> O impacto de eventos macroeconômicos globais, como recessões e mudanças na política monetária.</li>
                <li><b>Demanda Energética:</b> A influência das mudanças na demanda por energia, especialmente em momentos de transição energética.</li>
                <li><b>Avanços Tecnológicos:</b> O papel de inovações no setor energético, como energias renováveis e novas técnicas de extração.</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
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
            Este projeto visa demonstrar por meio da analise de dados a oscilações do preço do petróleo e sua relevância no cenário global. Os principais objetivos incluem:
            </p>
            <ul style="font-size:16px;line-height:1.8;">
                <li><b>Explorar Dados Históricos:</b> Utilizar séries temporais para identificar padrões recorrentes no preço do petróleo.</li>
                <li><b>Previsão de Preços:</b> Aplicar técnicas avançadas de Machine Learning e análise estatística para projetar tendências futuras.</li>
                <li><b>Avaliar Impactos Geopolíticos:</b> Compreender como eventos globais afetam diretamente o mercado de petróleo.</li>
                <li><b>Auxiliar na Tomada de Decisões:</b> Fornecer insights que possibilitem decisões estratégicas em um mercado volátil.</li>
                <li><b>Ensinamento Basico de Analise de Dados e Estatistica:</b> Por meio de nosso streamlit tentamos demonstrar um pouco do dia a dia de um Analista de Dados.</li>
            </ul>
            <p style="text-align:justify; font-size:18px;">
            Com estes objetivos, este projeto busca fortalecer a compreensão do mercado de petróleo, oferecendo uma base sólida para estratégias econômicas e sustentáveis.
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
            O desenvolvimento deste projeto proporcionou uma ampla gama de aprendizados, destacando a complexidade e a dinâmica do mercado de petróleo. Os principais aprendizados incluem:
            </p>
            <ul style="font-size:16px;line-height:1.8;">
                <li><b>Importância da Análise de Dados:</b> Dados históricos são fundamentais para compreender as oscilações de preços e prever tendências futuras.</li>
                <li><b>Relevância da Geopolítica:</b> Eventos globais, como conflitos e acordos internacionais, têm um impacto significativo no mercado de petróleo.</li>
                <li><b>Avanços Tecnológicos:</b> O uso de Machine Learning e modelos estatísticos proporcionou maior precisão nas análises preditivas.</li>
                <li><b>Sazonalidade e Ciclos Econômicos:</b> Identificar padrões sazonais ajuda a antecipar movimentos no mercado.</li>
                <li><b>Impacto da Sustentabilidade:</b> A crescente adoção de energias renováveis está remodelando o mercado tradicional de petróleo.</li>
                <li><b>Colaboração Multidisciplinar:</b> Trabalhar com equipes diversificadas foi essencial para unir conhecimentos econômicos, tecnológicos e estratégicos.</li>
            </ul>
            <p style="text-align:justify; font-size:18px;">
            Estes aprendizados reforçam a importância de uma abordagem estratégica e baseada em dados para lidar com os desafios e oportunidades do mercado energético global.
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )


if __name__ == "__main__":
    app()
