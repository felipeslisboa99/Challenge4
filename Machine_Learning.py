import streamlit as st
def app():
    st.title("Tech Petróleo - Análise de Dados")
import pandas as pd
import numpy as np

file_path = "base_petroleo.xlsx"

uploaded_file = st.file_uploader("C:\Users\felip\OneDrive\Documentos\GitHub\Challenge4\base_petroleo.xlsx", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df.head())

df = pd.DataFrame({
    "data": df['data'],
    "valor": df['preco_bruto_Brent_FOB']
})

df_mensal = df.groupby(df["data"].dt.to_period("M")).agg({"valor": "mean"}).reset_index()
df_mensal.rename(columns={"data": "mes", "valor": "mean_mensal"}, inplace=True)

df_mensal.head()

df_anual = df.groupby(df["data"].dt.to_period("Y")).agg({"valor": "mean"}).reset_index()
df_anual.rename(columns={"data": "ano", "valor": "media_anual"}, inplace=True)

df_anual.head()

df['data'] = pd.to_datetime(df["data"])
df.dtypes

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import xgboost as xgb
import pmdarima as pm
from prophet import Prophet
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error

)
from statsmodels.tsa.seasonal import seasonal_decompose

plt.figure(figsize=(10, 6))
plt.plot(df['data'], df['valor'], linestyle='-')
plt.title('Série Temporal', fontsize=14)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Valor', fontsize=12)
plt.grid(True, which='major', axis='x', linestyle='--', color='gray', alpha=0.7)
plt.xticks(pd.date_range(start='2004-01-01', end='2024-12-31', freq='YS'), rotation=45)
plt.tight_layout()
plt.show()

result = seasonal_decompose(df['valor'], model='multiplicative', period=365)

result.seasonal.iloc[:500].plot(figsize=(14,7))

result = seasonal_decompose(df['valor'], model='additive', period=365)
fig = result.plot()
fig.set_size_inches(14,7)

adf_result = sm.tsa.adfuller(df['valor'])
print(f"ADF Statistic: {adf_result[0]}")
print(f"p-value: {adf_result[1]}")
print(f"Critical Values: {adf_result[4]}")

if adf_result[1] < 0.03:
  print("A série temporal é estacionária")
else:
  print("A série temporal não é estacionária")

df.loc[:, 'Diferenciado'] = df['valor'].diff()

plt.figure(figsize=(12, 6))
plt.plot(df['Diferenciado'])
plt.title('Série Temporal Diferenciada (Estacionarizada)')
plt.xlabel('Tempo')
plt.ylabel('Valores Diferenciados')
plt.show()

from statsmodels.tsa.stattools import adfuller

result = adfuller(df['Diferenciado'].dropna())

print(f"Valor-p: {result[1]}")

if result[1] < 0.05:
    print("A série diferenciada é estacionária (Rejeitamos H0).")
else:
    print("A série diferenciada ainda não é estacionária (Não rejeitamos H0).")

from statsmodels.graphics.tsaplots import plot_acf as _plot_acf

plt.figure(figsize=(12, 6))
_plot_acf(df['Diferenciado'].dropna(), lags=30)
plt.title('ACF da Série Diferenciada')
plt.show()

from statsmodels.graphics.tsaplots import plot_pacf as _plot_pacf

plt.figure(figsize=(12, 6))
_plot_pacf(df['Diferenciado'].dropna(), lags=30)
plt.title('PACF da Série Diferenciada')
plt.show()

df_petroleo = df
df_petroleo = df_petroleo.sort_values(by='data', ascending=True)

train_size = len(df_petroleo) - 253
train, test = df_petroleo[:train_size], df_petroleo[train_size:]


def create_features(df_f):
  df_f["Data"] = pd.to_datetime(df_f["data"])
  df_f["year"] = df_f["data"].dt.year
  df_f['month'] = df_f["data"].dt.month
  df_f["day"] = df_f["data"].dt.day
  df_f["dayofweek"] = df_f["data"].dt.dayofweek
  return df_f

train = create_features(train)
test = create_features(test)

FEATURES =["year", "month", "day", "dayofweek", "valor"]
TARGET = "valor"

x_train, y_train = train[FEATURES], train[TARGET]
x_test, y_test = test[FEATURES], test[TARGET]

reg = xgb.XGBRegressor(objective = "reg:squarederror")
reg.fit(x_train, y_train)

preds_xgb = reg.predict(x_test)

def calculate_metrics(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mape = mean_absolute_percentage_error(y_true, y_pred)
    return {"MSE": mse, "MAE": mae, "MAPE": mape}

metrics_xgb = calculate_metrics(y_test, preds_xgb)
MAPE_xgb = metrics_xgb["MAPE"]
print("XGBoost Metrics:")
print(metrics_xgb)
print(f"Acurácia de {100 - (MAPE_xgb * 100): .2f}%")

xgboost_results = pd.DataFrame({'Data': test['Data'], 'Previsão': preds_xgb})

plt.figure(figsize=(14, 7))

plt.plot(test['Data'], test['valor'], label='Real', color='black')

plt.plot(xgboost_results['Data'], xgboost_results['Previsão'], label='XGBoost', color='orange')

plt.title('Comparação de Previsão do Modelo XGBoost com os Dados Reais')
plt.xlabel('Data')
plt.ylabel('Petroleo')
plt.legend()
plt.show()

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

prophet_results = preds_pr.reset_index()

plt.figure(figsize=(14, 7))

plt.plot(test['Data'], test['valor'], label='Real', color='black')

plt.plot(prophet_results['ds'], prophet_results['yhat'], label='Prophet', color='blue')

plt.title('Comparação de Previsão do Modelo Prophet com os Dados Reais')
plt.xlabel('Data')
plt.ylabel('Petroleo')
plt.legend()
plt.show()

model = pm.auto_arima(
    df['valor'].dropna(),
    seasonal=True,
    m=12,
    stepwise=True,
    suppress_warnings=True
)

print(model.summary())

seasonal_order = model.seasonal_order
print(f"Detected Seasonal Order: {seasonal_order}")

exog_train = train[["valor"]]
exog_test = test[["valor"]]

model = sm.tsa.statespace.SARIMAX(
    train["valor"],
    exog=exog_train,
    order=(
        5,
        1,
        1,
    ),
    seasonal_order=(0, 0, 0, 12),
)
result = model.fit()

preds_sarimax = result.get_forecast(steps=len(test), exog=exog_test).predicted_mean

metrics_sarimax = calculate_metrics(test["valor"], preds_sarimax)
MAPE_sarimax = metrics_sarimax["MAPE"]
print("SARIMAX Metrics")
print(metrics_sarimax)
print(f"Acurácia de {100 - (MAPE_sarimax * 100): .2f}%")

sarimax_results = pd.DataFrame({
    'Data': pd.to_datetime(test['Data']),
    'Previsão': preds_sarimax.values
})

plt.figure(figsize=(14, 7))

plt.plot(test['Data'], test['valor'], label='Real', color='black')

plt.plot(sarimax_results['Data'], sarimax_results['Previsão'], label='SARIMAX', color='green')

plt.title('Comparação de Previsão do Modelo SARIMAX com os Dados Reais')
plt.xlabel('Data')
plt.ylabel('Petroleo')
plt.legend()
plt.show()

df_modelos = pd.DataFrame(
    [metrics_xgb, metrics_pr, metrics_sarimax],
    columns=["MAE", "MSE", "MAPE"],
    index=["XGBoost", "Prophet", "SARIMAX"],
)

df_modelos["Acurácia%"] = (100 - (df_modelos["MAPE"] * 100)).map('{:,.2f}'.format)

df_modelos.sort_values(by="Acurácia%", ascending=False)

plt.figure(figsize=(14, 7))

plt.plot(test['Data'], test['valor'], label='Real', color='black')

plt.plot(prophet_results['ds'], prophet_results['yhat'], label='Prophet', color='blue')

plt.plot(xgboost_results['Data'], xgboost_results['Previsão'], label='XGBoost', color='orange')

plt.plot(sarimax_results['Data'], sarimax_results['Previsão'], label='SARIMAX', color='green')

plt.title('Comparação de Previsões dos Modelos com os Dados Reais')
plt.xlabel('Data')
plt.ylabel('Petroleo')
plt.legend()
plt.show()
