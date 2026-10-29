#Se solicita la inserción de un número y el programa nos dirá
#si es par o impar. Después, se pregunta si quiere introducir otro número
#Si dice que sí(S), se vuelve a pedir el número y a indicar si es par o impar. 
#A continuación se vuelve a preguntar si quiere introducir otro número, y así hasta
#que diga que no(N)

#se establece la variable
continuar="S"

while continuar=="S" or continuar=="s":
    num=int(input("introduce un numero: "))
    #verifico si es par o impar
    if num%2==0:
        print("par")
    else:
        print("impar")
    
    continuar=input("Desea continuar (S) o (N): ")
        