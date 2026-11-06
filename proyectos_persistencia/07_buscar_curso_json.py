# realizar una nueva version del ejecicio 38 lo mas reducida posible
import datetime as dt
import streamlit as st
import json

dir_fichero = "cursos.json"
# extraemos los datos del json
with open(dir_fichero,"r") as f:
    datos = json.load(f)

cursos = datos["cursos"]

# nombre del curso con la media mas alta
# nombre del curso que finalizo antes
def media(numeros):
    if not numeros:
        return 0
    return sum(numeros)/len(numeros)
    
def convertir_fecha(texto):
    return dt.datetime.strptime(texto,"%d/%m/%Y")

def curso_antes():
    curso_antiguo = min(cursos, key=lambda c: convertir_fecha(c["fecha_fin"]))
    return curso_antiguo["denominacion"]

def curso_media_alta():
    curso_destacado = max(cursos, key=lambda c: media(c["calificaciones"]))
    return curso_destacado["denominacion"]

print(f"El curso '{curso_media_alta()}' obtuvo la nota media mas alta")
print(f"El curso '{curso_antes()}' termino antes")

# libreria de interfaz grafica: streamlit
st.write(f"El curso '{curso_media_alta()}' obtuvo la nota media mas alta")
st.write(f"El curso '{curso_antes()}' termino antes")
