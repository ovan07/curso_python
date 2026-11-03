dias={"lunes","martes","miercoles"}
#dias.add("jueves")
#dias.add("lunes") #elemento duplicado,no se añade

dia=input("dime un dia de la semana: ")

if dia in dias:
    print("ese dia ya existe")
else:
    dias.add(dia)

print(dias)

lista_dias=list(dias)
print(lista_dias)

lista_numeros=[4,7,11,3,2,11,9,4,7]
conjunto_numeros=set(lista_numeros)
print(conjunto_numeros)