lista=[5,2,11,6,44,20,1]
lista_ordenada=sorted(lista,reverse=True)
print(lista_ordenada)

nombres=["bicicleta","oro","casa","martillo"]
print(sorted(nombres))

#ordenacion personalizada, por ejemplo por numero de caracteres
print(sorted(nombres, key=lambda c:len(c)))

#dde la lista de numeros, imprime el mayor
print(max(lista))

#imprime el menor de la lista de nombres
print(min(nombres))

#imprime el que tiene menos caracteres
print(min(nombres, key=lambda c:len(c)))