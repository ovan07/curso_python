#Solicitar al usuario la introducción de unas coordenadas (x,y),
#cada pareja de coordenadas se guarda en una lista. (una lista de tuplas)
#Cada vez que solicitamos coordenadas
#preguntamos si quiere introducir nuevas coordenadas. 
#En caso afirmativo, se solicitan de nuevo
#si responde que no, finaliza el programa mostrando la lista 
#de coordenadas 

import math
import csv
#from math import hypot

dir_fichero="coordenadas.csv"

def distancia(punto1,punto2):
    #return math.dist(p1,p2)
    return math.hypot(punto1[0]-punto2[0],punto1[1]-punto2[1])

def leer_fichero():
    with open(dir_fichero,"r") as f:
        coordenadas=list(csv.DictReader(f))
    return coordenadas

#Se pide al usuario su posición, después el programa
#le mostrará las coordenadas del punto 
#más cercano a su posición 

actual_x=int(input("Introduce tu coordenada actual x:"))
actual_y=int(input("Introduce tu coordenada actual y:"))

mi_coordenada=(actual_x,actual_y)
tienda_cercana=coordenadas[0]
#establecemos la variable de cercanica con el calculo de la distancia del 1er elemento y mi coordenada
cercania=distancia(tienda_cercana,mi_coordenada)

for coordenada in coordenadas:
    dist=distancia(coordenada,mi_coordenada)
    if dist<cercania:
        cercania=dist
        tienda_cercana=coordenada

print(f"La tienda mas cercana es: {tienda_cercana}")