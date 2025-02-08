import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import xgboost as xgb
from prophet import Prophet
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error

)
from statsmodels.tsa.seasonal import seasonal_decompose
def app():
    df = pd.read_excel("base_petroleo.xlsx")
    df.head()

    df = pd.DataFrame({
        "data": df['data'],
        "valor": df['preco_bruto_Brent_FOB']
})
    df_mensal = df.groupby(df["data"].dt.to_period("M")).agg({"valor": "mean"}).reset_index()
    df_mensal.rename(columns={"data": "mes", "valor": "mean_mensal"}, inplace=True)
    df_anual = df.groupby(df["data"].dt.to_period("Y")).agg({"valor": "mean"}).reset_index()
    df_anual.rename(columns={"data": "ano", "valor": "media_anual"}, inplace=True)
    df['data'] = pd.to_datetime(df["data"])
    df.dtypes
#Serie Temporal
    plt.figure(figsize=(10, 6))
    plt.plot(df['data'], df['valor'], linestyle='-')
    plt.title('Série Temporal', fontsize=14)
    plt.xlabel('Data', fontsize=12)
    plt.ylabel('Valor', fontsize=12)
    plt.grid(True, which='major', axis='x', linestyle='--', color='gray', alpha=0.7)
    plt.xticks(pd.date_range(start='2004-01-01', end='2024-12-31', freq='YS'), rotation=45)
    plt.tight_layout()
    plt.show()
    
    result = seasonal_decompose(df['valor'], model='additive', period=365)
    fig = result.plot()
    fig.set_size_inches(14,7)
#Serie Temporal Diferenciada
    df.loc[:, 'Diferenciado'] = df['valor'].diff()

    plt.figure(figsize=(12, 6))
    plt.plot(df['Diferenciado'])
    plt.title('Série Temporal Diferenciada (Estacionarizada)')
    plt.xlabel('Tempo')
    plt.ylabel('Valores Diferenciados')
    plt.show()