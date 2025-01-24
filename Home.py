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
           <div style="background-color:#f4f4f9;padding:15px;border-radius:10px;">
           <h3 style="color:#007acc;text-align:center;">📘 Tipos de Introdução</h3>
           <ul style="font-size:16px;line-height:1.8;">
              <li><b>Introdução Histórica:</b> Explorar como o mercado de petróleo evoluiu ao longo das décadas, destacando eventos marcantes que moldaram seus preços e importância.</li>
              <li><b>Introdução Geopolítica:</b> Destacar o impacto de conflitos, sanções e acordos internacionais na dinâmica do mercado global de petróleo.</li>
              <li><b>Introdução Tecnológica:</b> Analisar como avanços em Machine Learning e tecnologias de previsão revolucionaram a compreensão e análise do mercado de petróleo.</li>
              <li><b>Introdução Sustentável:</b> Enfatizar a transição global para fontes de energia renováveis e como isso desafia e transforma o setor de petróleo.</li>
              <li><b>Introdução Estratégica:</b> Apresentar o mercado de petróleo como um elemento essencial para decisões econômicas, políticas e de negócios em escala global.</li>
           </ul>
           <p style="text-align:justify; font-size:18px;">
           Este projeto permite abordar o tema de maneira diversificada, unindo análises históricas, impactos globais e inovações tecnológicas para oferecer uma visão holística do mercado de petróleo.
           </p>
           </div>
           """,
    unsafe_allow_html=True


        )
        st.markdown(
            """
            <div style="background-color:#f4f4f9;padding:15px;border-radius:10px;">
            <h3 style="color:#007acc;text-align:center;">🕒 Linha do Tempo do Mercado de Petróleo</h3>
            - **1973:** Crise do Petróleo - Primeiro choque no preço global.
            - **1986:** Queda drástica nos preços devido ao aumento da produção.
            - **1990**  Guerra do Golfo - A invasão do Kuwait pelo Iraque gerou uma nova crise no fornecimento.
            - **2008:** Crise financeira global - Impacto significativo na demanda de petróleo.
            - **2020:** Pandemia de COVID-19 - Demanda reduzida drasticamente.
            - **2022**  Guerra na Ucrânia - A invasão pela Rússia gerou sanções econômicas e aumentou os preços devido a incertezas no fornecimento.
            """
        )

    # Aba Objetivo
    with tab4:
        st.markdown(
            """
            <div style="background-color:#f4f4f9;padding:15px;border-radius:10px;">
            <h3 style="color:#007acc;text-align:center;">🎯 Objetivo</h3>
            <p style="text-align:justify; font-size:18px;">
            O objetivo deste projeto é analisar e compreender as oscilações do mercado de petróleo por meio de dados históricos e técnicas avançadas de Machine Learning. Busca-se identificar padrões sazonais, avaliar o impacto de eventos geopolíticos e prever tendências futuras com alta precisão. Além disso, o projeto visa explorar como a transição para energias renováveis influencia o mercado tradicional. Combinando análises estatísticas e visuais, pretende-se fornecer insights práticos que auxiliem na tomada de decisões estratégicas em um mercado altamente volátil. Assim, o projeto contribui para uma compreensão aprofundada e embasada do setor energético global.
            </p>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div style="background-color:#f4f4f9;padding:15px;border-radius:10px;margin:20px 0;">
            <h3 style="color:#007acc;text-align:center;">📜 Tipos de Objetivos</h3>
            <ul style="font-size:16px;line-height:1.8;">
               <li><b>Identificar Padrões Relevantes:</b> Realizar uma análise detalhada de séries temporais para identificar sazonalidades, ciclos econômicos e tendências de longo prazo no mercado de petróleo.</li>
               <li><b>Compreender Impactos Geopolíticos:</b> Explorar como eventos globais, como guerras, sanções e negociações internacionais, influenciam diretamente os preços.</li>
               <li><b>Previsão de Oscilações:</b> Desenvolver modelos de Machine Learning robustos para prever flutuações futuras no mercado de petróleo, com foco em acurácia e confiabilidade.</li>
               <li><b>Passar Ensinamento:</b> Ensinar um pouco do dia a dia de um Analista de Dados.</li>
               <li><b>Auxiliar na Tomada de Decisões:</b> Fornecer insights claros e práticos para que investidores e gestores possam criar estratégias de mitigação de riscos em mercados voláteis.</li>
           </ul>
           <p style="text-align:justify; font-size:18px;">
           Este projeto não apenas aborda a análise histórica, mas também visa trazer inovações em previsões e ferramentas analíticas que possam ser aplicadas em diferentes setores .
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
           Com este projeto, aprendemos a importância da análise de dados históricos para identificar padrões sazonais e tendências no mercado de petróleo. Descobrimos como eventos geopolíticos, como conflitos e sanções, influenciam diretamente os preços, reforçando a necessidade de análises estratégicas. O uso de técnicas de Machine Learning destacou a eficácia de modelos preditivos, como Prophet e XGBoost, para capturar oscilações complexas. Também compreendemos o impacto crescente das energias renováveis na dinâmica do mercado tradicional. Por fim, o trabalho evidenciou a relevância de abordagens interdisciplinares, unindo economia, ciência de dados e política global, para resultados mais completos e precisos.
           </p>
           """,
           unsafe_allow_html=True
        )
        st.markdown(
            """
            <div style="background-color:#f4f4f9;padding:15px;border-radius:10px;margin:20px 0;">
            <h3 style="color:#007acc;text-align:center;"> 🧠 Tipos de Aprendizados</h3>
            <ul style="font-size:16px;line-height:1.8;">
               <li><b>Preparação de Dados:</b> A limpeza e organização de dados históricos provaram ser essenciais para garantir análises confiáveis e robustas.</li>
               <li><b>Impacto de Eventos Geopolíticos:</b> Conflitos internacionais e sanções econômicas desempenham um papel crucial na determinação das oscilações de preço.</li>
               <li><b>Sazonalidade e Tendências:</b> A identificação de padrões sazonais no mercado possibilitou uma melhor compreensão dos ciclos de oferta e demanda.</li>
               <li><b>Eficiência dos Modelos Preditivos:</b> Técnicas como Prophet e XGBoost demonstraram eficácia ao capturar variações complexas em séries temporais.</li>
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
