#Al iniciar el programar se debe mostrar el siguiente menu:
#1.- Añadir nota
#2.- Mostrar notas extremas
#3.- Total de aprobados
#4.- Nota media
#5.- Mostrar todas
#6.- Salir

#El usuario elige una opcion (1 a 6) y el programa le muestra o le pide
#los datos necesarios para llevar a cabo esa accion. Despues, vuelve a salir el menu
#y asi hasta que elija la opcion salir
opcion=0
lista_notas=[]
nota=0
aprobados=0
sumatoria=0
menu=" 1.- Añadir nota \n 2.- Mostrar notas extremas \n 3.- Total de aprobados \n 4.- Nota media \n 5.- Mostrar todas \n 6.- Salir \n"

while opcion!=6:
    print(menu)
    opcion=int(input("- Opcion: "))
    
    match opcion:
        case 1:
            nota=int(input("-- Añada una nota: "))
            lista_notas.append(nota)
            sumatoria+=nota
        case 2:
            if lista_notas!=[]:
                print(f"La nota mas alta: {max(lista_notas)} y la nota mas baja: {min(lista_notas)} \n")
        case 3:
            for n in lista_notas:
                if n>=5:
                    aprobados+=1 
            print(f"La cantidad de alunnos aprobados son de: {aprobados} \n")
        case 4:
            if len(lista_notas)>0:
                print(f"El promedio de las notas introducidas es: {sumatoria/len(lista_notas)} \n")
        case 5:
            print(f"Lista de notas: {lista_notas} \n")
        case 6:
            print("Fin del programa")
