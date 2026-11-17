import streamlit as st 

saludo = ""
with st.sidebar:
    st.write("Menú navegación")
    st.text_input("Dato:")
    if st.button("Pulsar"):
        saludo = "Estoy en el navegador"

st.write(saludo)