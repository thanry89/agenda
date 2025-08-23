import streamlit as st
import datetime
import pickle
import os
import pandas as pd

st.set_page_config(page_title="Ingresar", page_icon="📈")


def write_register(row_data):
        with open('data/glendaDatabase.pkl', "rb") as file:
                data = pickle.load(file)
        #Add Row
        new_row = pd.DataFrame([row_data], columns=data.columns)
        df = pd.concat([new_row, data], ignore_index=True)
        with open('data/glendaDatabase.pkl', "wb") as file:
                pickle.dump(df, file)
        return


def generate_pkl():
        data = pd.read_excel('data/glendaDatabase.xlsx')
        with open('data/glendaDatabase.pkl', "wb") as file:
                pickle.dump(data, file)
        return

with st.form('Ingresar_Paciente', clear_on_submit=True):
        st.write("Ingresar Registro")

        opt_dr = ["Dra. A", "Dr. B"]
        opt_pieza = [1, 2]
        opt_diagPul = ["Opc 1", "Opc 2"]
        opt_diagPer = ["Opc 1", "Opc 2"]

        dr = st.selectbox("Seleccionar Doctor", opt_dr)

        inicio = st.date_input("Fecha de Inicio", datetime.date.today(), format = 'DD/MM/YYYY')

        fin = st.date_input("Fecha de Fin", format = 'DD/MM/YYYY', value = None)

        paciente = st.text_input('Nombre del Paciente')

        pieza = st.selectbox('Ingresar Numero de Pieza', opt_pieza)

        diag_pulpar = st.selectbox('Ingresar Diagnostico Pulpar', opt_diagPul)

        diag_peria = st.selectbox('Ingresar Diagnostico Periapical', opt_diagPer)

        otros = st.text_input('Ingresar Otros Comentarios')

        precio = st.number_input('Precio')
        
        submitted = st.form_submit_button("Ingresar Registro")
        
        if submitted:
                row_data = [dr, inicio, fin, paciente, pieza, diag_pulpar, diag_peria, otros, precio]
                #if not os.path.exists('data/glenda.pkl'):
                #        generate_pkl()
                write_register(row_data)
                st.write(row_data)
