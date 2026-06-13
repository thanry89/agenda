import streamlit as st
#import pandas as pd
import pickle

st.set_page_config(page_title="Editar", layout='wide')

def del_register(row_index):
        with open('data/glendaDatabase.pkl', "rb") as file:
                data,_ = pickle.load(file)
        #Add Row
        df = data.drop(row_index)
        df.reset_index(inplace=True, drop=True)
        with open('data/glendaDatabase.pkl', "wb") as file:
                pickle.dump([df,_], file)
        return

st.header("Editar Registro")


with open('data/glendaDatabase.pkl', "rb") as file:
        [data,_] = pickle.load(file)

option = st.selectbox(
        'Seleccione el Dr:',
        data['Doctor'].sort_values(ascending=False).unique(),
        index=None,
        placeholder="Escoja el Dr..."
)

filtered_df = data[data['Doctor']==option]

edited_df = st.data_editor(filtered_df, num_rows="dynamic")

if st.button("Guardar"):
        #print(filtered_df.compare(edited_df).index)
        st.switch_page('pages/2_Revisar.py')

del_row = st.selectbox(
        'Eliminar Registro',
        data.index,
        index=None,
        placeholder="Seleccionar Registro"
)

if st.button("Eliminar"):
        del_register(del_row)
        st.switch_page('pages/2_Revisar.py')