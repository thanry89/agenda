import streamlit as st

if "selection" not in st.session_state:
    st.session_state.selection = None

options = ["Ingresar Registro", "Revisar Registro"]

def inicio():
    st.header("Seleccionar")
    selection = st.selectbox("Seleccionar ", options)

    if st.button("OK"):
        st.session_state.selection = selection
        st.rerun()


def home():
    st.session_state.selection = None
    st.rerun()


selection = st.session_state.selection

home_page = st.Page(home, title="Inicio")

ingresar_page = st.Page(
    "Ingresar/Ingresar.py",
    title="Ingresar Registro",
    default=(selection == "Ingresar Registro"),
)

revisar_page = st.Page(
    "Revisar/revisar.py",
    title="Revisar Registro",
    default=(selection == "Revisar Registro"),
)

account_pages = [home_page]
request_pages = [ingresar_page, revisar_page]

page_dict = {}

if st.session_state.selection in ["Ingresar Registro"]:
    page_dict["Doctores"] = request_pages

if st.session_state.selection in ["Revisar Registro"]:
    page_dict["Doctores"] = request_pages


if len(page_dict) > 0:
    pg = st.navigation({"Inicio": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(inicio)])

pg.run()