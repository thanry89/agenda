import streamlit as st
import pickle

st.set_page_config(page_title="Historial", layout='wide')


st.header("Historial")

with open('data/glendaDatabase.pkl', "rb") as file:
        [_,historial] = pickle.load(file)

option = st.selectbox(
        'Seleccione el Dr:',
        historial['Doctor'].sort_values(ascending=False).unique(),
        index=None,
        placeholder="Escoja el Dr..."
)