#solicitar la introduccion de un numero y despues muestra todos los pares entre el 1 y ese numero

num=int(input("Introduce un numero: "))
valor,resto=0,0

for n in range(1,num+1):
    # comprueba si es par
    if n%2==0:
        print(f"es par: {n}")