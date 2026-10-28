#hacer un programa que muestra la suma de los 10 primeros naturales (1 al 10)
num=0

for c in range(1,11):
    num+=c
    
print(f"la suma de los numeros: {num} \n")

#hacer un programa que muestra la suma de todos los numeros naturales 
#entre 1 y un numero leido por teclado

num1=0

valor=int(input("Introducde un numero: "))

for n in range(1,valor):
    num1+=n
    
print(f"la suma de los numeros hasta el introducido: {num1}")