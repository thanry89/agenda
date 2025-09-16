import streamlit as st
#import pandas as pd
import pickle

st.set_page_config(page_title="Editar", layout='wide')

st.header("Editar Registro")


with open('data/glendaDatabase.pkl', "rb") as file:
        data = pickle.load(file)

option = st.selectbox(
        'Seleccione el Dr:',
        data['Doctor'].sort_values(ascending=False).unique(),
        index=None,
        placeholder="Escoja el Dr..."
)

filtered_df = data[data['Doctor']==option]

edited_df = st.data_editor(filtered_df, num_rows="dynamic")

if st.button("Guardar"):
        print(filtered_df.compare(edited_df).index)
        st.switch_page('pages/2_Revisar.py')

option = st.selectbox(
        'Eliminar Registro',
        data.index,
        index=None,
        placeholder="Seleccionar Registro"
)