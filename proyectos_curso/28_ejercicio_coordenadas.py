#Solicitar al usuario la introducción de unas coordenadas (x,y),
#cada pareja de coordenadas se guarda en una lista. (una lista de tuplas)
#Cada vez que solicitamos coordenadas
#preguntamos si quiere introducir nuevas coordenadas. 
#En caso afirmativo, se solicitan de nuevo
#si responde que no, finaliza el programa mostrando la lista 
#de coordenadas 

import math
#from math import hypot

resp="si"
coordenadas=[]
#cercania=9999

def distancia(punto1,punto2):
    math.hypot(punto1[0]-punto2[0],punto1[1]-punto2[1])

while resp=="si" or resp=="Si":
    x=int(input("Introduce la coordenada de la tienda x: "))
    y=int(input("Introduce la coordenada de la tienda y: "))
    
    coordenadas.append((x,y))
    resp=input("¿Desea introducir nuevas coordenadas? (si/no): ")
    
print(f"Las coordenadas introducidas son: {coordenadas}")

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