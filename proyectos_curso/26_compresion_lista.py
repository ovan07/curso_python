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

print(f"{obtener_aprobados()}")