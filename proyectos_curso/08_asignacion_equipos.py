#teniendo en cuenta que alevin es 10 años y benjamin es 16.
#hacer un programa que solicte la edad y nos muestre a que grupo pertenece
#pertenece ( el mas cercano a su edad). la edad debe estar
#entre 9 y 18 años
limite_inf,limite_sup,benjamin,alevin=9,18,10,16
edad=int(input("Introduce tu edad:"))

if edad>=limite_inf and edad<=13:
    print("pertenece al grupo de alevin")
elif edad>13 and edad<=limite_sup:
    print("pertenece al grupo de benjamin")
else:
    print("la edad no pertence a ningun grupo")
    
    
distancia_benjamin=edad-benjamin
distancia_alevin=edad-alevin
if distancia_benjamin<distancia_alevin:
    print("eres de benjamin")
else:
    print("eres de alevin")