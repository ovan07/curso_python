import json
import streamlit as st

dir_fichero = "countries.json"

# extraemos los datos del json
with open(dir_fichero,"r") as f:
    datos = json.load(f)

# funciones
def continentes():
    return list(set(map(lambda p:p["region"], datos)))

def paises_continente(continente):
    return list(filter(lambda p:p["region"] == continente, datos))
    
# definimos los nombres de las pestañas
tab_paises = st.tabs(["Seleccione continente:"]) 

with tab_paises[0]:
    regiones = set([p for p in [d["region"] for d in datos]])
    region = st.selectbox("Seleccione", regiones)
    
    paises_region = list(filter(lambda p:p["region"] == region, datos))
    
    col_pais,col_continente,col_poblacion,col_bandera = st.columns(4)
    
    col_pais.write("**País**")
    col_continente.write("**Continente**")
    col_poblacion.write("**Población**")
    col_bandera.write("**Bandera**")

    for paises in paises_region:
        col_pais,col_continente,col_poblacion,col_bandera = st.columns(4)
        col_pais.write(paises["name"])
        col_continente.write(paises["region"])
        col_poblacion.write(paises["population"])
        col_bandera.image(paises["flags"]["svg"], width = 50)