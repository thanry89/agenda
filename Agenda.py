import streamlit as st

st.set_page_config(
    page_title="Agenda",
    page_icon="👋",
)

st.write("# Hola Glendita! 👋")

st.title('Selecciona una Opción:')

if st.button("Ingresar Registro"):
        st.switch_page('pages/1_Ingresar.py')
if st.button("Revisar Registro"):
        st.switch_page('pages/2_Revisar.py')
if st.button("Editar Registro"):
        st.switch_page('pages/3_Editar.py')
if st.button("Historial"):
        st.switch_page('pages/4_Historial.py')