num1=input("Introduce 1er numero: ")
num2=input("Introduce 2do numero: ")

#convertir texto a numero con "int" y "float" para decimal
num1=int(num1)
num2=int(num2)

#operaciones
suma=num1+num2
resta=num2-num1
multi=num1*num2
divi=num2/num1
potencia=num1**num2

print(f"La suma de los numeros es: {suma}")
print(f"La resta de los numeros es: {resta}")
print(f"La multiplicacion de los numeros es: {multi}")
print(f"La division de los numeros es: {divi}")
print(f"La potencia de los numeros es: {potencia}")