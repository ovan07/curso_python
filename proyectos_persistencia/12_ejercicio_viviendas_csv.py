#dado un presupuesto, muestras las viviendas menores o igual de ese presupuesto
import csv
import streamlit as st

dir_fichero = "houses.csv"

with open(dir_fichero, "r") as f:
    datos = list(csv.DictReader(f))  # lista de diccionarios (json)

def posibles(presupuesto):
    #return [d for d in datos if int(d["price"]) <= presupuesto]            # solucion alternativa 1
    #return list(filter(lambda p:int(p["price"]) <= presupuesto, datos))    # solucion alternativa 2
    return sorted(filter(lambda p: int(p["price"]) <= presupuesto, datos), key = lambda p: int(p["price"]))
     
presupuesto = st.number_input("Ingrese el presupuesto:", value = 0)

tab_op1, tab_op2 = st.tabs(["Opción 1","Opción 2"]) 

resultado = posibles(presupuesto)

with tab_op1:
    st.table(resultado)            # solucion alternativa 1

with tab_op2:
    # solucion alternativa 2
    col_size,col_rooms,col_age,col_location,col_price = st.columns(5)
        
    col_size.write("**Tamaño**")
    col_rooms.write("**Habitaciones**")
    col_age.write("**Año**")
    col_location.write("**Localidad**")
    col_price.write("**Precio**")

    for r in resultado:
        col_size,col_rooms,col_age,col_location,col_price = st.columns(5)
        col_size.write(r["size"])
        col_rooms.write(r["rooms"])
        col_age.write(r["age"])
        col_location.write(r["location"])
        col_price.write(r["price"])
