# app.py
import streamlit as st
import shortuuid
import webbrowser
from urllib.parse import urlparse
from db import init_db, salvar_link, buscar_link

# Inicializa o banco
init_db()

st.set_page_config(page_title="Encurtador de Links", layout="centered")
st.title("🔗 Encurtador de Links")

# Verifica se tem ?id= na URL para redirecionamento
query_params = st.experimental_get_query_params()
if "id" in query_params:
    codigo = query_params["id"][0]
    url = buscar_link(codigo)
    if url:
        st.success(f"Redirecionando para: {url}")
        st.markdown(f"<meta http-equiv='refresh' content='1;url={url}'>", unsafe_allow_html=True)
    else:
        st.error("Link não encontrado.")
    st.stop()

# Interface principal
with st.form("encurtar"):
    original_url = st.text_input("Cole seu link aqui:", placeholder="https://exemplo.com")
    submit = st.form_submit_button("Encurtar")

if submit and original_url:
    if not urlparse(original_url).scheme:
        original_url = "https://" + original_url

    codigo = shortuuid.ShortUUID().random(length=6)
    salvar_link(codigo, original_url)

    base_url = st.request.url.replace("?", "")
    short_link = f"{base_url}?id={codigo}"

    st.success("Link encurtado com sucesso!")
    st.write(f"🔗 [Clique aqui]({short_link}) ou copie abaixo:")
    st.code(short_link, language="text")