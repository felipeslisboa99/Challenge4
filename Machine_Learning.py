import streamlit as st
import pandas as pd
import xgboost as xgb
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Título da página
def app():
    st.title("🤖 Modelo de Machine Learning")

    # Carregar os dados
    @st.cache_data
    def load_data():
        return pd.read_excel("base_petroleo.xlsx")

    df = load_data()

    # Exibir os dados carregados
    st.write("### Dados Carregados")
    st.dataframe(df.head())

    # Conversão de Data para DateTime
    if 'data' in df.columns:
        df['data'] = pd.to_datetime(df['data'])
        df = df.drop(columns=['data'])  # Remover a coluna de data

    # Garantir que há colunas disponíveis
    if df.empty or len(df.columns) < 2:
        st.error("⚠ Erro: Não há colunas suficientes para modelagem!")
        return

    # Selecionar automaticamente a variável alvo (última coluna)
    variaveis = df.columns.tolist()
    target = variaveis[-1]  # Última coluna é a variável alvo
    features = variaveis[:-1]  # Todas as outras são preditoras

    # **Transformar valores categóricos em numéricos**
    df = pd.get_dummies(df, drop_first=True)

    # **Remover NaN**
    df = df.dropna()

    # Definir X e y
    X = df[features]
    y = df[target]

    # **Garantir que há dados válidos**
    if X.empty or y.empty:
        st.error("⚠ Erro: Não há dados suficientes para treinar o modelo!")
        return

    st.write(f"🔹 Tamanho de X: {X.shape}, Tamanho de y: {y.shape}")

    # **Divisão treino e teste**
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # **Treinamento do modelo XGBoost**
    try:
        model_xgb = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
        model_xgb.fit(X_train, y_train)
        pred_xgb = model_xgb.predict(X_test)
    except Exception as e:
        st.error(f"⚠ Erro no treinamento do XGBoost: {e}")
        return

    # **Treinamento do modelo Random Forest**
    model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
    model_rf.fit(X_train, y_train)
    pred_rf = model_rf.predict(X_test)

    # **Função para calcular métricas**
    def calcular_metricas(y_true, y_pred):
        return {
            "MAE": mean_absolute_error(y_true, y_pred),
            "MSE": mean_squared_error(y_true, y_pred),
            "R²": r2_score(y_true, y_pred)
        }

    # **Exibir métricas**
    st.write("### 🎯 Desempenho dos Modelos")
    st.write("**XGBoost:**", calcular_metricas(y_test, pred_xgb))
    st.write("**Random Forest:**", calcular_metricas(y_test, pred_rf))

    # **Previsão com Prophet**
    st.write("### 🔮 Previsão com Prophet")
    df_prophet = df[[target]].reset_index().rename(columns={'index': 'ds', target: 'y'})
    model_prophet = Prophet()
    model_prophet.fit(df_prophet)

    future = model_prophet.make_future_dataframe(periods=30)
    forecast = model_prophet.predict(future)

    st.write("### 🔍 Previsão para os próximos 30 dias")
    st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(30))
