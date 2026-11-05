#realizar una nueva version del ejecicio 38 lo mas reducida posible
import datetime as dt
import streamlit as st

cursos=[
    {"denominacion":"Python y datos","calificaciones":[5.6,7.8,3.3,7.2],"fecha_fin":"10/03/2026"},
    {"denominacion":"Inglés científico","calificaciones":[8.2,7.8,6.3,4.2,9.0],"fecha_fin":"22/07/2026"},
    {"denominacion":"Spring e hibernate","calificaciones":[5.8,4.3,7.5],"fecha_fin":"04/12/2025"},
    {"denominacion":"Programador cerficado","calificaciones":[7.8,6.6,4.8,5.3,7.7],"fecha_fin":"30/09/2025"}  
]
#nombre del curso con la media mas alta
#nombre del curso que finalizo antes
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
#st.write(f"El curso '{curso_media_alta()}' obtuvo la nota media mas alta")
#st.write(f"El curso '{curso_antes()}' termino antes")