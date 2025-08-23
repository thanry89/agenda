import streamlit as st
#import pandas as pd
import pickle

st.set_page_config(page_title="Revisar", page_icon="🌍", layout='wide')

st.header("Revisar Registro")


with open('data/glendaDatabase.pkl', "rb") as file:
        data = pickle.load(file)

option = st.selectbox(
        'Seleccione el Dr:',
        data['Doctor'].sort_values(ascending=False).unique(),
        index=None,
        placeholder="Escoja el Dr..."
)

st.dataframe(data[data['Doctor'] == option], use_container_width=True)

option = st.selectbox(
        'Eliminar Registro',
        data.index,
        index=None,
        placeholder="Seleccionar Registro"
)