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

#print(cursos[0]["fecha_fin"])

def media(numeros):
    media=0
    suma=0
    for n in numeros:
        suma+=n
    if suma>0:
        media=suma/len(numeros)
    return media
    
def convertir_fecha(texto):
    return dt.datetime.strptime(texto,"%d/%m/%Y")

def curso_antes():
    curso_nombre=""
    fecha_menor=cursos[0]["fecha_fin"]
    for c in cursos:
        if convertir_fecha(c["fecha_fin"])<convertir_fecha(fecha_menor):
            fecha_menor=c["fecha_fin"]
            curso_nombre=c["denominacion"]
    return curso_nombre

def curso_media_alta():
    curso_nombre=""
    media_alta=cursos[0]["calificaciones"]
    for c in cursos:
        if media(c["calificaciones"])>media(media_alta):
            media_alta=c["calificaciones"]
            curso_nombre=c["denominacion"]
    return curso_nombre

print("")       
print(f"El curso '{curso_media_alta()}' obtuvo la nota media mas alta")
print(f"El curso '{curso_antes()}' termino antes")

# libreria de interfaz grafica: streamlit
st.write(f"El curso '{curso_media_alta()}' obtuvo la nota media mas alta")
st.write(f"El curso '{curso_antes()}' termino antes")