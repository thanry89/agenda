import streamlit as st

st.set_page_config(
    page_title="Agenda",
    page_icon="👋",
)

st.write("# Hola Glendita! 👋")

st.title('Seleccionar Opción:')

if st.button("Ingresar Registro"):
        st.switch_page('pages/1_Ingresar.py')
if st.button("Revisar Registro"):
        st.switch_page('pages/2_Revisar.py')
if st.button("Editar Registro"):
        st.switch_page('pages/3_Editar.py')

#st.sidebar.success("Select a demo above.")
