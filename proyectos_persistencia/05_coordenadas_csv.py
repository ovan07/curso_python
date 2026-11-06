# Solicitar al usuario la introducción de unas coordenadas (x,y),
# cada pareja de coordenadas se guarda en una lista. (una lista de tuplas)
# Cada vez que solicitamos coordenadas
# preguntamos si quiere introducir nuevas coordenadas. 
# En caso afirmativo, se solicitan de nuevo
# si responde que no, finaliza el programa mostrando la lista de coordenadas 

import math
import csv
#from math import hypot     #otra forma de importarlo la funcion hypot del metodo math

dir_fichero = "coordenadas.csv"

def distancia(punto1, punto2):
    #return math.dist(punto1, punto2)
    return math.hypot(punto1["x"]-punto2["x"], punto1["y"]-punto2["y"])

def leer_fichero():
    with open(dir_fichero,"r") as f:
        coordenadas = list(csv.DictReader(f))  
    for c in coordenadas:
        c["x"] = int(c["x"])
        c["y"] = int(c["y"])
    return coordenadas

# Se pide al usuario su posición, después el programa
# le mostrará las coordenadas del punto 
# más cercano a su posición 

actual_x = int(input("Introduce tu coordenada actual x: "))
actual_y = int(input("Introduce tu coordenada actual y: "))
mi_coordenada = {"x":actual_x,"y":actual_y}

coordenadas = leer_fichero()
"""
#establecemos la variable de cercanica con el calculo de la distancia del 1er elemento y mi coordenada
tienda_cercana = coordenadas[0]     # 1er elemento de coordenadas
cercania = distancia(tienda_cercana,mi_coordenada)

for c in coordenadas:
    dist = distancia(c, mi_coordenada)
    if dist < cercania:
        cercania = dist
        tienda_cercana = c
"""
tienda_cercana = min(coordenadas, key = lambda c: distancia(c, mi_coordenada))

print(f"La tienda mas cercana es: {tienda_cercana}")