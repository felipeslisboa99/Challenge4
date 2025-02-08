import streamlit as st
import pandas as pd
import xgboost as xgb
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# 🎯 Definir função principal do app
def app():
    st.title("🤖 Modelo de Machine Learning")

    # 📂 Carregar os dados do arquivo base_petroleo.xlsx
    @st.cache_data
    def load_data():
        return pd.read_excel("base_petroleo.xlsx")

    df = load_data()

    # 📊 Exibir os dados carregados
    st.write("### 📊 Dados Carregados")
    st.dataframe(df.head())

    # 🗓️ Conversão de Data para DateTime
    if 'data' in df.columns:
        df['data'] = pd.to_datetime(df['data'])

    # 🎯 Seleção da variável alvo (target)
    variaveis = [col for col in df.columns if col != 'data']
    target = st.selectbox("🎯 Selecione a variável alvo:", variaveis, index=len(variaveis)-1)

    # 📌 Seleção automática de todas as variáveis preditoras
    features = [col for col in variaveis if col != target]

    # 🔍 Garantir que temos features e target selecionados corretamente
    if not target:
        st.warning("⚠️ Por favor, selecione uma variável alvo.")
        return

    if not features:
        st.warning("⚠️ Não há variáveis preditoras disponíveis.")
        return

    # 📌 Definir X (features) e y (target)
    X = df[features]
    y = df[target]

    # 📊 Divisão dos dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 🚀 Treinamento do modelo XGBoost
    model_xgb = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
    model_xgb.fit(X_train, y_train)
    pred_xgb = model_xgb.predict(X_test)

    # 🌲 Treinamento do modelo Random Forest
    model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
    model_rf.fit(X_train, y_train)
    pred_rf = model_rf.predict(X_test)

    # 📈 Função para calcular métricas
    def calcular_metricas(y_true, y_pred):
        return {
            "MAE": mean_absolute_error(y_true, y_pred),
            "MSE": mean_squared_error(y_true, y_pred),
            "R²": r2_score(y_true, y_pred)
        }

    # 🎯 Exibir métricas dos modelos
    st.write("### 🎯 Desempenho dos Modelos")
    st.write("📌 **XGBoost:**", calcular_metricas(y_test, pred_xgb))
    st.write("📌 **Random Forest:**", calcular_metricas(y_test, pred_rf))

    # 📊 Gráficos comparando Previsões x Valores Reais
    st.write("### 📉 Comparação entre Previsões e Valores Reais")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(y_test.values, label="Valores Reais", color="black", linestyle="dotted")
    ax.plot(pred_xgb, label="XGBoost - Previsão", color="blue")
    ax.plot(pred_rf, label="Random Forest - Previsão", color="green")
    ax.set_title("Comparação de Previsões")
    ax.set_xlabel("Amostras")
    ax.set_ylabel("Valor")
    ax.legend()
    st.pyplot(fig)

    # 🔮 Previsões futuras com Prophet
    if 'data' in df.columns:
        st.write("### 🔮 Previsão com Prophet")

        df_prophet = df[['data', target]].rename(columns={'data': 'ds', target: 'y'})
        model_prophet = Prophet()
        model_prophet.fit(df_prophet)

        future = model_prophet.make_future_dataframe(periods=30)
        forecast = model_prophet.predict(future)

        # 📈 Gráfico de previsão
        st.write("### 📈 Previsão para os próximos 30 dias")
        fig_forecast, ax_forecast = plt.subplots(figsize=(10, 5))
        ax_forecast.plot(forecast['ds'], forecast['yhat'], label="Previsão", color="red")
        ax_forecast.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='pink', alpha=0.3)
        ax_forecast.set_title("Previsão com Prophet")
        ax_forecast.set_xlabel("Data")
        ax_forecast.set_ylabel("Valor")
        ax_forecast.legend()
        st.pyplot(fig_forecast)

        # 📋 Exibir previsão em formato de tabela
        st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(30))

