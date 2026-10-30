#cual es la temperatura mas baja
temperaturas="12.4,23.6,17.8,3.5,29.0,11.6"
lista_temp=temperaturas.split(",")
temp_baja=min([float(t) for t in lista_temp])

#for indice,valor in enumerate(lista):
#    lista[indice]=float(valor)

print(lista_temp)
print(temp_baja)