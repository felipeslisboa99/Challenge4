import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xgboost as xgb
from prophet import Prophet
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error

# Função para carregar os dados
def load_data():
    try:
        data = pd.read_excel("base_petroleo.xlsx")
        data = pd.DataFrame({
            "data": pd.to_datetime(data['data']),
            "valor": data['preco_bruto_Brent_FOB']
        })
        return data
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None

# Função para calcular métricas
def calculate_metrics(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mape = mean_absolute_percentage_error(y_true, y_pred)
    return {"MSE": mse, "MAE": mae, "MAPE": mape}

def app():
        # Título da página com estilo
    st.markdown(
        """
        <div style="background-color:#007acc;padding:10px;border-radius:10px">
        <h1 style="color:white;text-align:center;">🤖 Machine Learning</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Carregar dados
    data = load_data()
    if data is None:
        return

    # Visualização inicial dos dados
    st.markdown("### Visualização Inicial dos Dados")
    st.dataframe(data.head())

    # Série Temporal Original
    st.markdown("### Série Temporal Original")
    st.write("Este gráfico mostra a evolução histórica do preço do petróleo ao longo do tempo.")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data['data'], data['valor'], color='blue', label='Preço do Petróleo')
    ax.set_title('Série Temporal do Preço do Petróleo')
    ax.set_xlabel('Data')
    ax.set_ylabel('Preço')
    ax.legend()
    st.pyplot(fig)

    # Decomposição da Série Temporal
    st.markdown("### Decomposição da Série Temporal")
    st.write("Este gráfico decompõe a série temporal em seus componentes principais: tendência, sazonalidade e resíduo.")
    result = seasonal_decompose(data['valor'], model='multiplicative', period=365)
    fig = result.plot()
    fig.set_size_inches(14, 7)
    st.pyplot(fig)

    # Dividir os dados em treino e teste
    train_size = len(data) - 253
    train, test = data[:train_size], data[train_size:]

    # Feature Engineering
    def create_features(df):
        df['year'] = df['data'].dt.year
        df['month'] = df['data'].dt.month
        df['day'] = df['data'].dt.day
        df['dayofweek'] = df['data'].dt.dayofweek
        return df

    train = create_features(train.copy())
    test = create_features(test.copy())

    FEATURES = ['year', 'month', 'day', 'dayofweek']
    TARGET = 'valor'

    # XGBoost
    st.markdown("### Modelo XGBoost")
    st.write("O modelo XGBoost é usado para prever os preços do petróleo com base em variáveis derivadas de datas. Aqui estão as previsões e as métricas de desempenho.")
    x_train, y_train = train[FEATURES], train[TARGET]
    x_test, y_test = test[FEATURES], test[TARGET]

    reg = xgb.XGBRegressor(objective="reg:squarederror")
    reg.fit(x_train, y_train)
    preds_xgb = reg.predict(x_test)

    metrics_xgb = calculate_metrics(y_test, preds_xgb)
    st.write("Métricas XGBoost:", metrics_xgb)

    # Gráfico XGBoost
    st.write("O gráfico abaixo compara as previsões do XGBoost com os valores reais.")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(test['data'], y_test, label='Real', color='black')
    ax.plot(test['data'], preds_xgb, label='XGBoost', color='orange')
    ax.set_title('Previsão XGBoost vs Real')
    ax.set_xlabel('Data')
    ax.set_ylabel('Preço')
    ax.legend()
    st.pyplot(fig)

    # Prophet
    st.markdown("### Modelo Prophet")
    st.write("O modelo Prophet é ajustado para capturar padrões sazonais e tendências nos dados. Abaixo estão as previsões e métricas.")
    train_prophet = train.rename(columns={"data": "ds", "valor": "y"})
    model = Prophet(daily_seasonality=True)
    model.fit(train_prophet)

    future = model.make_future_dataframe(periods=len(test))
    forecast = model.predict(future)

    preds_pr = forecast[['ds', 'yhat']].tail(len(test))
    metrics_pr = calculate_metrics(y_test, preds_pr['yhat'])
    st.write("Métricas Prophet:", metrics_pr)

    # Gráfico Prophet
    st.write("O gráfico abaixo mostra as previsões do Prophet em comparação com os valores reais.")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(test['data'], y_test, label='Real', color='black')
    ax.plot(test['data'], preds_pr['yhat'], label='Prophet', color='blue')
    ax.set_title('Previsão Prophet vs Real')
    ax.set_xlabel('Data')
    ax.set_ylabel('Preço')
    ax.legend()
    st.pyplot(fig)

    # SARIMAX
    st.markdown("### Modelo SARIMAX")
    st.write("O modelo SARIMAX é usado para capturar dependências temporais nos dados. Aqui estão as previsões e métricas.")
    model_sarimax = SARIMAX(train['valor'], order=(5, 1, 1), seasonal_order=(0, 0, 0, 12))
    result_sarimax = model_sarimax.fit()
    preds_sarimax = result_sarimax.get_forecast(steps=len(test)).predicted_mean

    metrics_sarimax = calculate_metrics(y_test, preds_sarimax)
    st.write("Métricas SARIMAX:", metrics_sarimax)

    # Gráfico SARIMAX
    st.write("O gráfico abaixo compara as previsões do SARIMAX com os valores reais.")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(test['data'], y_test, label='Real', color='black')
    ax.plot(test['data'], preds_sarimax, label='SARIMAX', color='green')
    ax.set_title('Previsão SARIMAX vs Real')
    ax.set_xlabel('Data')
    ax.set_ylabel('Preço')
    ax.legend()
    st.pyplot(fig)

    # Comparação entre Modelos
    st.markdown("### Comparação entre Modelos")
    st.write("A tabela abaixo apresenta uma comparação das métricas de desempenho entre os diferentes modelos usados.")
    comparison = pd.DataFrame({
        'Modelo': ['XGBoost', 'Prophet', 'SARIMAX'],
        'MAE': [metrics_xgb['MAE'], metrics_pr['MAE'], metrics_sarimax['MAE']],
        'MSE': [metrics_xgb['MSE'], metrics_pr['MSE'], metrics_sarimax['MSE']],
        'MAPE': [metrics_xgb['MAPE'], metrics_pr['MAPE'], metrics_sarimax['MAPE']]
    })
    st.dataframe(comparison)

if __name__ == "__main__":
    app()
