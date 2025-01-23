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
            <h3 style="color:#007acc;text-align:center;">🎯 Objetivo</h3>
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
            Este projeto foi idealizado para fornecer uma compreensão ampla e estratégica sobre as oscilações do mercado de petróleo,
            explorando dados históricos, tendências atuais e perspectivas futuras. Com isso, busca-se alcançar os seguintes objetivos:
            </p>
            <ul style="font-size:16px;line-height:1.8;">
               <li><b>Identificar Padrões Relevantes:</b> Realizar uma análise detalhada de séries temporais para identificar sazonalidades, ciclos econômicos e tendências de longo prazo no mercado de petróleo.</li>
               <li><b>Compreender Impactos Geopolíticos:</b> Explorar como eventos globais, como guerras, sanções e negociações internacionais, influenciam diretamente os preços.</li>
               <li><b>Previsão de Oscilações:</b> Desenvolver modelos de Machine Learning robustos para prever flutuações futuras no mercado de petróleo, com foco em acurácia e confiabilidade.</li>
               <li><b>Promover Sustentabilidade:</b> Avaliar como a transição para energias renováveis impacta o mercado tradicional e suas implicações econômicas.</li>
               <li><b>Auxiliar na Tomada de Decisões:</b> Fornecer insights claros e práticos para que investidores e gestores possam criar estratégias de mitigação de riscos em mercados voláteis.</li>
            </ul>
           <p style="text-align:justify; font-size:18px;">
           Este projeto não apenas aborda a análise histórica, mas também visa trazer inovações em previsões e ferramentas analíticas que possam ser aplicadas em diferentes setores econômicos e energéticos.
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
           Durante o desenvolvimento deste projeto, uma série de aprendizados importantes foram alcançados, abrangendo desde a análise de dados históricos até a aplicação de modelos preditivos e compreensão de fatores externos que moldam o mercado de petróleo.
           </p>
            <ul style="font-size:16px;line-height:1.8;">
               <li><b>Preparação de Dados:</b> A limpeza e organização de dados históricos provaram ser essenciais para garantir análises confiáveis e robustas.</li>
               <li><b>Impacto de Eventos Geopolíticos:</b> Conflitos internacionais e sanções econômicas desempenham um papel crucial na determinação das oscilações de preço.</li>
               <li><b>Sazonalidade e Tendências:</b> A identificação de padrões sazonais no mercado possibilitou uma melhor compreensão dos ciclos de oferta e demanda.</li>
               <li><b>Eficiência dos Modelos Preditivos:</b> Técnicas como Prophet e XGBoost demonstraram eficácia ao capturar variações complexas em séries temporais.</li>
               <li><b>Influência de Energias Renováveis:</b> A crescente adoção de fontes renováveis tem alterado a dinâmica do mercado, trazendo novas oportunidades e desafios.</li>
               <li><b>Importância de Visualizações:</b> Representações gráficas interativas tornaram os dados mais acessíveis, facilitando a comunicação de resultados para diferentes públicos.</li>
               <li><b>Abordagem Multidisciplinar:</b> Trabalhar com conhecimentos de economia, ciência de dados e política global resultou em análises mais completas e integradas.</li>
            </ul>
           <p style="text-align:justify; font-size:18px;">
           Esses aprendizados reforçam a necessidade de análises detalhadas e interdisciplinares para enfrentar os desafios de um mercado tão dinâmico e influenciado por múltiplos fatores.
           </p>
           </div>
           """,
           unsafe_allow_html=True
    )



if __name__ == "__main__":
    app()
