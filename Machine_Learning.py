# import streamlit as st
# import time
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# import statsmodels.api as sm
# import xgboost as xgb
# import pmdarima as pm
# from prophet import Prophet
# from sklearn.metrics import (
#     mean_absolute_error,
#     mean_squared_error,
#     mean_absolute_percentage_error
# )
# from statsmodels.tsa.seasonal import seasonal_decompose
# from statsmodels.tsa.stattools import adfuller
# from statsmodels.graphics.tsaplots import plot_acf as _plot_acf, plot_pacf as _plot_pacf

# def app():
#     st.title("Tech Petróleo - Análise de Dados")
    
# with st.spinner("Carregando... Isso pode levar alguns segundos"):
#     time.sleep(1)  # Simula um tempo de carregamento
#     st.write("Pronto! 🎉")

#     st.markdown("### 📂  Carregar o arquivo diretamente")
#     file_path = r"C:\Users\felip\OneDrive\Documentos\GitHub\Challenge4\base_petroleo.xlsx"

#     try:
#         # 📂 Carregar o arquivo diretamente 
#         df = pd.read_excel(file_path)
#         st.write("Dados carregados com sucesso!")
#         st.dataframe(df.head())

#         df['data'] = pd.to_datetime(df['data'])

#         # 🔹 Gráfico de Série Temporal st.markdown("###  🔹 Gráfico de Série Temporal ") 
#         fig, ax = plt.subplots(figsize=(10, 6))
#         ax.plot(df['data'], df['preco_bruto_Brent_FOB'], linestyle='-')
#         ax.set_title('Série Temporal')
#         ax.set_xlabel('Data')
#         ax.set_ylabel('Valor')
#         ax.grid(True)
#         st.pyplot(fig)

#         st.markdown("###  🔹 Teste de estacionaridade (Dickey-Fuller) ") 
#         adf_result = adfuller(df['preco_bruto_Brent_FOB'].dropna())
#         st.write(f"ADF Statistic: {adf_result[0]}")
#         st.write(f"p-value: {adf_result[1]}")
#         st.write(f"Critical Values: {adf_result[4]}")

#         if adf_result[1] < 0.03:
#             st.success("A série temporal é estacionária")
#         else:
#             st.warning("A série temporal não é estacionária")

#         st.markdown("###  🔹 Diferenciação da Série Temporal ") 
#         df['Diferenciado'] = df['preco_bruto_Brent_FOB'].diff()
#         fig, ax = plt.subplots(figsize=(12, 6))
#         ax.plot(df['Diferenciado'])
#         ax.set_title('Série Temporal Diferenciada (Estacionarizada)')
#         ax.set_xlabel('Tempo')
#         ax.set_ylabel('Valores Diferenciados')
#         st.pyplot(fig)

#         st.markdown("### 🔹 ACF e PACF ") 
#         fig, ax = plt.subplots(figsize=(12, 6))
#         _plot_acf(df['Diferenciado'].dropna(), lags=30, ax=ax)
#         ax.set_title('ACF da Série Diferenciada')
#         st.pyplot(fig)

#         fig, ax = plt.subplots(figsize=(12, 6))
#         _plot_pacf(df['Diferenciado'].dropna(), lags=30, ax=ax)
#         ax.set_title('PACF da Série Diferenciada')
#         st.pyplot(fig)

#         # Criando features
#         df["year"] = df["data"].dt.year
#         df["month"] = df["data"].dt.month
#         df["day"] = df["data"].dt.day
#         df["dayofweek"] = df["data"].dt.dayofweek

#         st.markdown("###  📊 Divisão de treino e teste ") 
#         train_size = len(df) - 253
#         train, test = df[:train_size], df[train_size:]

#         FEATURES = ["year", "month", "day", "dayofweek", "preco_bruto_Brent_FOB"]
#         TARGET = "preco_bruto_Brent_FOB"

#         x_train, y_train = train[FEATURES], train[TARGET]
#         x_test, y_test = test[FEATURES], test[TARGET]

#         st.markdown("### 🚀 Modelo XGBoost ") 
#         reg = xgb.XGBRegressor(objective="reg:squarederror")
#         reg.fit(x_train, y_train)

#         preds_xgb = reg.predict(x_test)

#         st.markdown("### 🔹 Métricas XGBoost ") 
#         metrics_xgb = {
#             "MSE": mean_squared_error(y_test, preds_xgb),
#             "MAE": mean_absolute_error(y_test, preds_xgb),
#             "MAPE": mean_absolute_percentage_error(y_test, preds_xgb),
#         }
#         st.write("Métricas do Modelo XGBoost:")
#         st.json(metrics_xgb)

#         st.markdown("### 🚀   Prophet")  
#         train_prophet = train.rename(columns={"data": "ds", "preco_bruto_Brent_FOB": "y"})
#         model = Prophet(daily_seasonality=True)
#         model.fit(train_prophet)

#         future = model.make_future_dataframe(periods=len(test))
#         forecast = model.predict(future)

#         preds_pr = forecast[["ds", "yhat"]].tail(len(test))
#         preds_pr.set_index("ds", inplace=True)

#         st.markdown("### 🔹  Métricas Prophet") 
#         metrics_pr = {
#             "MSE": mean_squared_error(y_test, preds_pr["yhat"]),
#             "MAE": mean_absolute_error(y_test, preds_pr["yhat"]),
#             "MAPE": mean_absolute_percentage_error(y_test, preds_pr["yhat"]),
#         }
#         st.write("Métricas do Modelo Prophet:")
#         st.json(metrics_pr)

#         st.markdown("### 🔹 Comparação visual dos modelos")
#         fig, ax = plt.subplots(figsize=(14, 7))
#         ax.plot(test['data'], test['preco_bruto_Brent_FOB'], label='Real', color='black')
#         ax.plot(test['data'], preds_xgb, label='XGBoost', color='orange')
#         ax.plot(preds_pr.index, preds_pr["yhat"], label='Prophet', color='blue')
#         ax.set_title('Comparação de Modelos')
#         ax.set_xlabel('Data')
#         ax.set_ylabel('Preço do Petróleo')
#         ax.legend()
#         st.pyplot(fig)

#     except FileNotFoundError:
#         st.error("Erro: O arquivo não foi encontrado. Verifique o caminho e tente novamente.")
#     except Exception as e:
#         st.error(f"Erro ao carregar os dados: {e}")
