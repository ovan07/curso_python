#realizar un programa que solicite la introduccion de un numero
#y calcule su factorial 7! 7*6*5*4*3*2*1

resul=1
num=int(input("Introducde un numero: "))

for c in range(1,num+1):
    resul*=c
    
print(f"el factorial del numero: {resul} \n")