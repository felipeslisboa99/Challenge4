import streamlit as st
import requests

# Substitua pela URL do Ngrok gerada no Colab
COLAB_API_URL = "http://127.0.0.1:5000"

def predict_from_colab(value):
    response = requests.post(COLAB_API_URL, json={"value": value})
    if response.status_code == 200:
        return response.json()["prediction"]
    else:
        return "Erro ao obter previsão"

def app():
    st.markdown(
        "<h1 style='text-align: center;'>🔗 Integração Google Colab + Streamlit</h1>",
        unsafe_allow_html=True
    )

    valor = st.number_input("Digite um valor para previsão:", value=1)

    if st.button("Enviar para Colab"):
        resultado = predict_from_colab(valor)
        st.write(f"Resultado da API do Colab: {resultado}")

if __name__ == "__main__":
    app()
