import streamlit as st
import datetime
import pickle
import os
import pandas as pd

st.set_page_config(page_title="Ingresar", page_icon="📈")


def write_register(row_data):
        with open('data/glendaDatabase.pkl', "rb") as file:
                data,_ = pickle.load(file)
        #Add Row
        new_row = pd.DataFrame([row_data], columns=data.columns)
        df = pd.concat([new_row, data], ignore_index=True)
        with open('data/glendaDatabase.pkl', "wb") as file:
                pickle.dump([df,_], file)
        return

with st.form('Ingresar_Paciente', clear_on_submit=True):
        st.write("Ingresar Registro")

        opt_dr = ["Dra. A", "Dr. B"]
        opt_pieza = ['Pulpar', 'Anterior']
        opt_num_pieza = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        opt_diagPul = ['PULPA SANA', 'PULPITIS IRREVERSIBLE', 'PULPITIS REVERSIBLE', 'NECROSIS PULPAR', 'RETRATAMIENTO']
        opt_diagPer = ['PERIAPICE SANO', 'PERIODIONTITIAS APICAL SINTOMATICA', 'PERIODIONTITIAS APICAL ASINTOMATICA', 'ABSESO ALVEOLAR AGUDO',
                       'ABSESO ALVEOLAR CRONICO', 'PROCESO']
        opt_tratamiento = ['CITAS SIN TERMINO DE TRATAMIENTO', 'RECUBRIMIENTO PULPAR DIRECTO CON MATERIAL', 'RECUBRIMIENTO PULPAR DIRECTO SIN MATERIAL', 
                           'RECUBRIMIENTO PULPAR INDIRECTO CON MATERIAL', 'RECUBRIMIENTO PULPAR INDIRECTO SIN MATERIAL', 'APICOFORMACIÓN C/CITA', 'REVASCULARIZACIÓN'
                           'RETROBTURACIÓN CON MATERIAL', 'RETROBTURACIÓN SIN MATERIAL', 'SELLADO DE PERFORACIÓN CON MATERIAL', 'SELLADO DE PERFORACIÓN SIN MATERIAL',
                           'RETIRO DE INSTRUMENTO']

        dr = st.selectbox("Seleccionar Doctor", opt_dr)

        historia = st.text_input('Ingresar Historia Clínica')

        paciente = st.text_input('Nombre del Paciente')

        inicio = st.date_input("Fecha de Inicio", datetime.date.today(), format = 'DD/MM/YYYY')

        fin = st.date_input("Fecha de Fin", format = 'DD/MM/YYYY', value = None)

        pieza = st.selectbox(label='Ingresar Tipo de Pieza', options=opt_pieza, index = None, accept_new_options=True, placeholder=None)

        num_pieza = st.selectbox('Ingresar Numero de Pieza', opt_num_pieza, index = None, accept_new_options=True, placeholder=None)

        diag_pulpar = st.selectbox('Ingresar Diagnostico Pulpar', opt_diagPul, index = None, accept_new_options=True, placeholder=None)

        diag_peria = st.selectbox('Ingresar Diagnostico Periapical', opt_diagPer, index = None, accept_new_options=True, placeholder=None)

        tratamiento = st.selectbox('Ingresar Tratamiento', opt_tratamiento, index = None, accept_new_options=True, placeholder=None)

        otros = st.text_input('Ingresar Otros Comentarios')

        precio = st.number_input('Precio')
        
        submitted = st.form_submit_button("Ingresar Registro")
        
        if submitted:
                row_data = [dr, historia, paciente, inicio, fin, pieza, num_pieza, diag_pulpar, diag_peria, otros, precio]
                write_register(row_data)
                st.write(row_data)
