import httpx as http
import streamlit as st

url = "http://localhost:8000/libro"
isbn = st.text_input("Ingrese el ISBN")

if st.button("Buscar"):
    resp = http.get(url+"/"+isbn)
    libro= resp.json()
    st.write(f"ISBN: {libro['isbn']}")
    st.write(f"Titulo: {libro['titulo']}")
    st.write(f"Precio: {libro['precio']}")
