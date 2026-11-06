#dado un presupuesto, muestras las viviendas menores o igual de ese presupuesto
import csv

dir_fichero = "houses.csv"
presupuesto = int(input("Ingrese el presupuesto: "))

with open(dir_fichero, "r") as f:
    datos=list(csv.DictReader(f))  # lista de diccionarios (json)

resultado=[d for d in datos if int(d["price"]) <= presupuesto]

for r in resultado:
    print(r)
