import streamlit as st
import pandas as pd
import statsmodels.api as sm
import xgboost as xgb
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Título da página
 
def app():
    st.title("🤖 Modelo de Machine Learning")

    # Carregar os dados do arquivo base_petroleo.xlsx
    @st.cache_data
    def load_data():
        return pd.read_excel("base_petroleo.xlsx")
    df = load_data()

# Exibir os dados carregados
    st.write("### Dados Carregados")
    st.dataframe(df.head())

# Conversão de Data para DateTime
    df['data'] = pd.to_datetime(df['data'])

# Seleção das colunas para modelagem
    variaveis = df.drop(columns=['data']).columns.tolist()
    target = st.selectbox("Selecione a variável alvo:", variaveis)

# Seleção das features
    features = st.multiselect("Selecione as variáveis preditoras:", variaveis, default=variaveis[:-1])

    if target and features:
        X = df[features]
        y = df[target]

    # Divisão em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinamento do modelo XGBoost
    model_xgb = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
    model_xgb.fit(X_train, y_train)
    pred_xgb = model_xgb.predict(X_test)

    # Treinamento do modelo Random Forest
    model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
    model_rf.fit(X_train, y_train)
    pred_rf = model_rf.predict(X_test)

    # Métricas dos modelos
    def calcular_metricas(y_true, y_pred):
        return {
            "MAE": mean_absolute_error(y_true, y_pred),
            "MSE": mean_squared_error(y_true, y_pred),
            "R²": r2_score(y_true, y_pred)
        }

    metricas_xgb = calcular_metricas(y_test, pred_xgb)
    metricas_rf = calcular_metricas(y_test, pred_rf)

    # Exibir as métricas
    st.write("### 🎯 Desempenho dos Modelos")
    st.write("**XGBoost:**", metricas_xgb)
    st.write("**Random Forest:**", metricas_rf)

    # Previsões futuras com Prophet (se houver uma variável de data)
    if 'data' in df.columns:
        st.write("### 🔮 Previsão com Prophet")

        df_prophet = df[['data', target]].rename(columns={'data': 'ds', target: 'y'})
        model_prophet = Prophet()
        model_prophet.fit(df_prophet)

        future = model_prophet.make_future_dataframe(periods=30)
        forecast = model_prophet.predict(future)

        st.write("### 🔍 Previsão para os próximos 30 dias")
        st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(30))
