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

df = pd.read_excel('/content/drive/MyDrive/PosTech/Fase4/Tech Cha/base_petroleo.xlsx')
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

