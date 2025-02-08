import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        st.sidebar.title("Navegação")
        app = st.sidebar.radio(
            "Selecione a página:",
            self.apps,
            format_func=lambda app: app["title"]
        )

        # 🔥 IMPORTANTE: Chamar a função da página selecionada
        app["function"]()
