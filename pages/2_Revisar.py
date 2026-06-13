import streamlit as st
import pickle

st.set_page_config(page_title="Revisar", layout='wide')

st.header("Revisar Registro")

with open('data/glendaDatabase.pkl', "rb") as file:
        data,_ = pickle.load(file)

option = st.selectbox(
        'Seleccione el Dr:',
        data['Doctor'].sort_values(ascending=False).unique(),
        index=None,
        placeholder="Escoja el Dr..."
)

filtered_df = data[data['Doctor']==option]

if option:
        filtered_df.drop('Doctor', axis=1, inplace=True)
        st.dataframe(filtered_df,width='content', hide_index=True)

if st.button("Editar"):
        st.switch_page('pages/3_Editar.py')