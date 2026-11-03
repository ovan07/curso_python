numeros=[4,3,7,8,7,9,2]

#dada esa lista de notas, crea otra lista
#que contenga solo los aprobados, ademas se añadira
#un punto extra a cada uno
#finalmente se imprime la lista

"""
aprobados=[]
for n in numeros:
    if n>=5:
        aprobados.append(n+1)
"""

#compresion de lista
aprobados=[nota+1 for nota in numeros if nota>=5]
print(f"{aprobados}")

#funcion que haga indicada arriba, pero devolviendo una tupla
def obtener_aprobados():
    return tuple(aprobados)

print(f"{obtener_aprobados()} \n")

#crea una lista a partir de la anterior que contenga
#solo los positivos
numeros=[3,-1,-9,4,2,11,-8,7,-5]

positivos=[n for n in numeros if n>=0]
print(positivos)