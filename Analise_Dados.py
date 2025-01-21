import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    try:
        # Substitua pelo caminho correto do seu arquivo
        data = pd.read_excel("base_petroleo.xlsx")
        return data
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None

def app():
    st.markdown(
        """
        <div style="background-color:#007acc;padding:10px;border-radius:10px;text-align:center">
        <h1 style="color:white;">📈 Análise de Dados do Petróleo</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Carregar dados
    data = load_data()
    if data is None:
        return

    # Renomear e processar dados
    data.rename(columns={'data': 'Data', 'preco_bruto_Brent_FOB': 'Preço Bruto Brent'}, inplace=True)
    data['Data'] = pd.to_datetime(data['Data'], errors='coerce').dt.date  # Remove as horas
    data.dropna(subset=['Data', 'Preço Bruto Brent'], inplace=True)

    # Layout em colunas
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 🔍 Visualização dos Dados")
        st.dataframe(data)

    with col2:
        st.markdown("### 📊 Informações Gerais")
        st.metric(label="Total de Registros", value=data.shape[0])
        st.metric(label="Preço Máximo", value=f"${data['Preço Bruto Brent'].max():.2f}")
        st.metric(label="Preço Médio (Todo Período)", value=f"${data['Preço Bruto Brent'].mean():.2f}")
        st.metric(label="Preço Mínimo", value=f"${data['Preço Bruto Brent'].min():.2f}")


    # Gráfico 1: Evolução Temporal
    st.markdown("### 📈 Evolução Temporal do Preço do Petróleo")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['Data'], data['Preço Bruto Brent'], label='Preço Bruto Brent', color='blue', linewidth=2)
    ax.set_title("Evolução Temporal do Preço do Petróleo (Brent)", fontsize=16)
    ax.set_xlabel("Data", fontsize=12)
    ax.set_ylabel("Preço (USD)", fontsize=12)
    ax.legend()
    st.pyplot(fig)

    # Gráfico 2: Preço Médio Mensal
    st.markdown("### 💵 Preço Médio Mensal do Petróleo")
    data['Mês'] = pd.to_datetime(data['Data'], errors='coerce').dt.month
    media_mensal = data.groupby('Mês')['Preço Bruto Brent'].mean().reset_index()
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(media_mensal['Mês'], media_mensal['Preço Bruto Brent'], color='green', alpha=0.7)
    ax.set_xticks(media_mensal['Mês'])
    ax.set_xticklabels(meses)
    ax.set_title("Variação Mensal Média do Preço do Petróleo (Brent)", fontsize=16)
    ax.set_xlabel("Mês", fontsize=12)
    ax.set_ylabel("Preço Médio (USD)", fontsize=12)
    st.pyplot(fig)

    # Gráfico 3: Preço Médio Anual
    st.markdown("### 📅  Média Anual do Preço do Petróleo")
    data['Ano'] = pd.to_datetime(data['Data'], errors='coerce').dt.year
    media_anual = data.groupby('Ano')['Preço Bruto Brent'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(media_anual['Ano'], media_anual['Preço Bruto Brent'], color='orange', alpha=0.8)
    ax.set_title("Média Anual do Preço do Petróleo (Brent)", fontsize=16)
    ax.set_xlabel("Ano", fontsize=12)
    ax.set_ylabel("Preço Médio (USD)", fontsize=12)
    st.pyplot(fig)

    st.markdown(
        """
        <div style="background-color:#f0f8ff;padding:10px;border-radius:10px;">
        <p style="text-align:center;font-size:16px;">
        Esta análise fornece uma visão detalhada das tendências e oscilações do mercado de petróleo ao longo do tempo. Explore os dados para entender as dinâmicas do mercado!
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Executar a aplicação
if __name__ == "__main__":
    app()
