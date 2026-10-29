lista=[4,1,8,2,11]
#muestra cada numero de la lista
for valor in lista:
    print(f"{valor}")
    
#muestra los pares de la lista
for valor in lista:
    if valor%2==0:
        print(f"este numero es par: {valor}")  

#sustituye cada elemento de lista por su cuadrado
#y luego imprimes la lista entera y suma de todo
#su contenido
"""
indice=0
for valor in lista:
    valor**=2
    lista[indice]=valor
    indice+=1
"""
#solucion alternativa
for indice,valor in enumerate(lista):
    lista[indice]=valor**2
    
print(f"la nueva lista es: {lista}")  

sumatoria=0
for valor in lista:
    sumatoria+=valor
    
print(f"la sumatoria del contenido de la lista: {sumatoria}") 