import streamlit as st
import matplotlib.pyplot as plt
from multiapp import MultiApp
from Home import app as home_app
from Insights import app as insights_app
from Machine_Learning import app as machine_learning_app
from Deploy import app as deploy_app
from Analise_Dados import app as analise_dados_app

# Configuração inicial do Streamlit
st.set_page_config(
    page_title="Tech Challenge: Fase 4",
    page_icon="📊",
    layout="wide",
)

# Criar instância do MultiApp
app = MultiApp()

# Adicionar a navegação no topo da barra lateral
st.sidebar.title("📌 Navegação")
app.add_app("🏠 Home", home_app)
app.add_app("📊 Insights", insights_app)
app.add_app("🤖 Modelo de Machine Learning", machine_learning_app)
app.add_app("🚀 Deploy", deploy_app)
app.add_app("📈 Análise de Dados", analise_dados_app)

# Rodar o MultiApp (controla a navegação entre as páginas)
if __name__ == "__main__":
    app.run()

# Adicionar os integrantes abaixo da navegação
st.sidebar.markdown("### 👥 Integrantes do Projeto")
st.sidebar.markdown("""
- **Felipe Saraiva Lisboa**
- **Renato Batista dos Santos**
- **Jéssyca Dias Matos Lima**
- **Everton Ferreira Alves**
""")

#Adicionar informações sobre a turma e a instituição no final
st.sidebar.markdown("### 🏫 Informações")
st.sidebar.markdown("""
- **Turma:** 6DTAT  
- **Instituição:** FIAP - Pós em Data Analytics  
""")
