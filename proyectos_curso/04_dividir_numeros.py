#pide dos numeros y muestra del resultado de dividir el mayor entre el menor
num1=int(input("Introduce el 1er numero: "))
num2=int(input("Introduce el 2do numero: "))

if num1>num2:
    print(f"{num1} entre {num2} es {num1/num2}")
else:
    print(f"{num2} entre {num1} es {num2/num1}")