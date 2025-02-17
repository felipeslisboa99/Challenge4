import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import xgboost as xgb
from prophet import Prophet
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error
)
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf as _plot_acf
from statsmodels.graphics.tsaplots import plot_pacf as _plot_pacf

def app():
    st.title("📊 Modelo de Machine Learning - Análise de Séries Temporais")

    # Carregar os dados
    df = pd.read_excel("base_petroleo.xlsx")
    df["data"] = pd.to_datetime(df["data"])

    df = df.rename(columns={"preco_bruto_Brent_FOB": "valor"})

    # Exibir os dados carregados
    st.write("### 📂 Dados Carregados")
    st.dataframe(df.head())

    # Gráfico de Série Temporal
    st.write("### 📈 Série Temporal")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['data'], df['valor'], linestyle='-')
    ax.set_title('Série Temporal')
    ax.set_xlabel('Data')
    ax.set_ylabel('Valor')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Decomposição Sazonal
    st.write("### 🔍 Decomposição Sazonal")
    result = seasonal_decompose(df['valor'], model='additive', period=365)
    fig = result.plot()
    fig.set_size_inches(14, 7)
    st.pyplot(fig)

    # Série Temporal Diferenciada
    df['Diferenciado'] = df['valor'].diff()

    st.write("### 📊 Série Temporal Diferenciada")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df['Diferenciado'].dropna())
    ax.set_title('Série Temporal Diferenciada (Estacionarizada)')
    ax.set_xlabel('Tempo')
    ax.set_ylabel('Valores Diferenciados')
    st.pyplot(fig)

    # Autocorrelação (ACF)
    #st.write("### 🔄 Função de Autocorrelação (ACF)")
    #fig, ax = plt.subplots(figsize=(12, 6))
    #_plot_acf(df['Diferenciado'].dropna(), lags=30, ax=ax)
    #ax.set_title('ACF da Série Diferenciada')
    #st.pyplot(fig)

    # Autocorrelação Parcial (PACF)
    #st.write("### 🔄 Função de Autocorrelação Parcial (PACF)")
    #fig, ax = plt.subplots(figsize=(12, 6))
    #_plot_pacf(df['Diferenciado'].dropna(), lags=30, ax=ax)
    #ax.set_title('PACF da Série Diferenciada')
    #st.pyplot(fig)

    # Preparação dos dados para o modelo
    df_petroleo = df
    df_petroleo = df.sort_values(by='data', ascending=True)

    train_size = len(df_petroleo) - 253
    train, test = df_petroleo[:train_size].copy(), df_petroleo[train_size:].copy()

    def create_features(df_f):
        df_f["Data"] = pd.to_datetime(df_f["data"])
        df_f["year"] = df_f["data"].dt.year
        df_f["month"] = df_f["data"].dt.month
        df_f["day"] = df_f["data"].dt.day
        df_f["dayofweek"] = df_f["data"].dt.dayofweek
        return df_f

    train = create_features(train)
    test = create_features(test)

    FEATURES = ["year", "month", "day", "dayofweek", "valor"]
    TARGET = "valor"

    x_train, y_train = train[FEATURES], train[TARGET]
    x_test, y_test = test[FEATURES], test[TARGET]

    reg = xgb.XGBRegressor(objective="reg:squarederror")
    reg.fit(x_train, y_train)

    preds_xgb = reg.predict(x_test)

    def calculate_metrics(y_true, y_pred):
        mse = mean_squared_error(y_true, y_pred)
        mae = mean_absolute_error(y_true, y_pred)
        mape = mean_absolute_percentage_error(y_true, y_pred)
        return {"MSE": mse, "MAE": mae, "MAPE": mape}

    metrics_xgb = calculate_metrics(y_test, preds_xgb)
    MAPE_xgb = metrics_xgb["MAPE"]

    st.write("### 📊 Resultados do Modelo XGBoost")
    st.write(f"**MSE:** {metrics_xgb['MSE']:.2f}")
    st.write(f"**MAE:** {metrics_xgb['MAE']:.2f}")
    st.write(f"**MAPE:** {metrics_xgb['MAPE']:.4f}")
    st.write(f"✅ **Acurácia do modelo:** {100 - (MAPE_xgb * 100):.2f}%")

    # Gráfico de Comparação entre Real e Previsão
    xgboost_results = pd.DataFrame({'Data': test['data'], 'Previsão': preds_xgb})

    st.write("### 📉 Comparação entre Previsões e Valores Reais")
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(test['data'], test['valor'], label='Real', color='black')
    ax.plot(xgboost_results['Data'], xgboost_results['Previsão'], label='XGBoost', color='orange')
    ax.set_title('Comparação de Previsão do Modelo XGBoost com os Dados Reais')
    ax.set_xlabel('Data')
    ax.set_ylabel('Preço do Petróleo')
    ax.legend()
    st.pyplot(fig)

    # Modelo Prophet
    st.write("### 🔮 Modelo Prophet")
    
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
    st.write("### 📊 Métricas do Modelo Prophet")
    st.write(metrics_pr)
    st.write(f"✅ **Acurácia do modelo:** {100 - (MAPE_pr * 100):.2f}%")

    # Gráfico Prophet
    st.write("### 📊 Comparação de Previsão do Modelo Prophet com os Dados Reais")

    prophet_results = preds_pr.reset_index()

    fig, ax = plt.subplots(figsize=(14, 7))

    ax.plot(test['Data'], test['valor'], label='Real', color='black')
    
    ax.plot(prophet_results['ds'], prophet_results['yhat'], label='Prophet', color='blue')

    ax.set_title('Comparação de Previsão do Modelo Prophet com os Dados Reais')
    ax.set_xlabel('Data')
    ax.set_ylabel('Petróleo')
    ax.legend()

    df_modelos = pd.DataFrame(
    [metrics_xgb, metrics_pr],
    columns=["MAE", "MSE", "MAPE"],
    index=["XGBoost", "Prophet"],
)
    
    # Supondo que df_modelos já esteja carregado
    # df_modelos = pd.read_csv('seu_arquivo.csv') ou já tenha sido definido no código

    # Criando a coluna de Acurácia no DataFrame
    df_modelos["Acurácia%"] = (100 - (df_modelos["MAPE"] * 100))
    df_modelos["Acurácia%"] = df_modelos["Acurácia%"].map('{:,.2f}'.format)

    # Ordenando os modelos por acurácia
    df_modelos = df_modelos.sort_values(by="Acurácia%", ascending=False)

    # Exibindo a tabela no Streamlit
    st.write("### Comparação de Modelos")
    st.dataframe(df_modelos)

    # Criando a figura com design aprimorado
    fig, ax = plt.subplots(figsize=(14, 7))

    # Plotando os dados reais
    test = pd.DataFrame({'Data': test['Data'], 'valor': test['valor']})  # Garantindo que 'test' está em formato correto
    ax.plot(test['Data'], test['valor'], label='Real', color='black', linewidth=2)

    # Plotando previsões dos modelos
    ax.plot(prophet_results['ds'], prophet_results['yhat'], label='Prophet', color='blue', linewidth=2, linestyle='dashed')
    ax.plot(xgboost_results['Data'], xgboost_results['Previsão'], label='XGBoost', color='orange', linewidth=2, linestyle='dotted')
    # Configurações do gráfico
    ax.set_title('Comparação de Previsões dos Modelos com os Dados Reais', fontsize=14, fontweight='bold')
    ax.set_xlabel('Data', fontsize=12)
    ax.set_ylabel('Petróleo', fontsize=12)
    ax.legend(frameon=True, loc='best', fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.6)

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)

