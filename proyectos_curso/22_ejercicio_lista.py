#solicita la introduccion de numeros, uno a uno
#y los guardamos en una lista. Despues de pedir un numero,
#pregunta si quiere introducir otro, si dice que si (S), pide uno nuevo
#y asi, sucesivamente hasta que diga que no (N)
#al final, muestra la lista completa

continuar="S"
num=0
lista=[]

while continuar=="S" or continuar=="s":
    try:
        num=int(input("Introduce un numero: "))
        lista.append(num)
        continuar=input("Desea continuar? (S/N): ")
    except ValueError:
        print("Valor no valido, vuelva a intentarlo")
        
print(f"La lista creada es: {lista}")