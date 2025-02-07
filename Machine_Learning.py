import streamlit as st
import itertools
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

    df_petroleo = data
    df_petroleo = df_petroleo.sort_values(by='data', ascending=True)

    # Dividir os dados em treino e teste
    train_size = len(data) - 253
    train, test = data[:train_size], data[train_size:]

    # Feature Engineering
    def create_features(df):
        df["Data"] = pd.to_datetime(df["data"])
        df['year'] = df['data'].dt.year
        df['month'] = df['data'].dt.month
        df['day'] = df['data'].dt.day
        df['dayofweek'] = df['data'].dt.dayofweek
        return df

    train = create_features(train.copy())
    test = create_features(test.copy())

    FEATURES = ['year', 'month', 'day', 'dayofweek', 'valor']
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
    MAPE_xgb = metrics_xgb["MAPE"]
    st.write("Métricas XGBoost:", metrics_xgb)
    st.write(f"Acurácia de {100 - (MAPE_xgb * 100) :.2f}%")

    # Gráfico XGBoost
    xgboost_results = pd.DataFrame({'Data': test['data'], 'Previsão': preds_xgb})

    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(test['data'], test['valor'], label='Real', color='black')
    ax.plot(xgboost_results['Data'], xgboost_results['Previsão'], label='XGBoost', color='orange')
    ax.set_title('Comparação de Previsão do Modelo XGBoost com os Dados Reais')
    ax.set_xlabel('Data')
    ax.set_ylabel('Petróleo')
    ax.legend()
    st.pyplot(fig)

    # Prophet
    st.markdown("### Modelo Prophet")
    st.write("O modelo Prophet é ajustado para capturar padrões sazonais e tendências nos dados. Abaixo estão as previsões e métricas.")
    train_prophet = train.rename(columns={"Data": "ds", "valor": "y"})
    train_prophet["valor"] = train["valor"]

    test_prophet = test.rename(columns={"Data": "ds", "valor": "y"})
    test_prophet["valor"] = test["valor"]

    model = Prophet(daily_seasonality=True)
    model.add_regressor("valor")
    model.fit(train_prophet)

    future = model.make_future_dataframe(periods=len(test))
    future["valor"] = pd.concat([train["valor"], test["valor"]], ignore_index=True)
    forecast = model.predict(future)

    preds_pr = forecast[["ds", "yhat"]].tail(len(test))
    preds_pr = preds_pr.set_index("ds")
    y_test = test_prophet.set_index("ds")["y"]
    metrics_pr = calculate_metrics(y_test, preds_pr["yhat"])

    MAPE_pr = metrics_pr["MAPE"]
    print("Prophet Metrics")
    print(metrics_pr)
    print(f"Acurácia de {100 - (MAPE_pr * 100): .2f}%")

    # Gráfico Prophet
    prophet_results = preds_pr.reset_index()

    plt.figure(figsize=(14, 7))

    plt.plot(test['Data'], test['valor'], label='Real', color='black')

    plt.plot(prophet_results['ds'], prophet_results['yhat'], label='Prophet', color='blue')

    plt.title('Comparação de Previsão do Modelo Prophet com os Dados Reais')
    plt.xlabel('Data')
    plt.ylabel('Petroleo')
    plt.legend()
    plt.show()

# SARIMAX
    st.markdown("### Modelo SARIMAX")
    st.write("O modelo SARIMAX é usado para capturar dependências temporais nos dados. Aqui estão as previsões e métricas.")

    # Definição do grid search para encontrar melhores parâmetros
    p = d = q = range(0, 3)  # Testando valores de 0 a 2
    P = D = Q = range(0, 2)  # Testando valores de 0 a 1
    m = [7, 12]  # Período sazonal: semanal (7) ou mensal (12)
    param_grid = list(itertools.product(p, d, q, P, D, Q, m))

    best_aic = float("inf")
    best_params = None
    if "valor" not in train.columns or "valor" not in test.columns:
        raise ValueError("A coluna 'valor' não foi encontrada no conjunto de dados.")
    exog_train = train[["valor"]].copy()
    exog_test = test[["valor"]].copy()

    for (p, d, q, P, D, Q, m) in param_grid:
        try:
            model = SARIMAX(train["valor"], order=(p, d, q), seasonal_order=(P, D, Q, m), exog=exog_train)
            result = model.fit()
            if result.aic < best_aic:
                best_aic = result.aic
                best_params = (p, d, q, P, D, Q, m)
        except:
            continue  # Pula combinações que falham

    st.write("Melhores parâmetros SARIMAX:", best_params)

    # Treinando o modelo com os melhores parâmetros encontrados
    p, d, q, P, D, Q, m = best_params
    model_sarimax = SARIMAX(train["valor"], exog=exog_train, order=(p, d, q), seasonal_order=(P, D, Q, m))
    result_sarimax = model_sarimax.fit()

    # Fazer previsões
    preds_sarimax = result_sarimax.get_forecast(steps=len(test), exog=exog_test).predicted_mean

    # Avaliação do modelo
    metrics_sarimax = calculate_metrics(test["valor"], preds_sarimax)
    MAPE_sarimax = metrics_sarimax["MAPE"]
    st.write("Métricas SARIMAX:", metrics_sarimax)
    st.write(f"Acurácia de {100 - (MAPE_sarimax * 100): .2f}%")

    # Gráfico SARIMAX
    st.write("O gráfico abaixo compara as previsões do SARIMAX com os valores reais.")
    sarimax_results = pd.DataFrame({
        'Data': pd.to_datetime(test['Data']),
        'Previsão': preds_sarimax.values
    })

    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(test['Data'], test['valor'], label='Real', color='black')
    ax.plot(sarimax_results['Data'], sarimax_results['Previsão'], label='SARIMAX', color='green', linestyle='dashed')
    ax.set_title('Comparação de Previsão do Modelo SARIMAX com os Dados Reais')
    ax.set_xlabel('Data')
    ax.set_ylabel('Petróleo')
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
