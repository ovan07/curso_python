#solicitar la inroduccion de dos numeros y calcula la suma de todos los numeros
#comprendidos entre el menor y el mayor

num1=int(input("Introduce el 1er numero: "))
num2=int(input("Introduce el 2do numero: "))
result,sumatoria=0,0

#solucion 1
if num1<num2:
    for n in range(num1,num2+1):
        sumatoria=num1+n
        result+=sumatoria
else:
    for n in range(num2,num1+1):
        sumatoria=num2+n
        result+=sumatoria
        
#solucion 2
"""
if num1<num2:
    menor,mayor=num1,num2
else:
    menor,mayor=num2,num1
    
sumatoria=menor
for n in range(menor,mayor+1):
    sumatoria+=n
"""
#solucion 3
"""
if num1>num2:
    num1,num2=num2,num1

for n in range(num1,num2+1):
    num1+=n
"""

print(f"la suma de los numeros comprendidos entre {num1} y {num2} es {result} ")