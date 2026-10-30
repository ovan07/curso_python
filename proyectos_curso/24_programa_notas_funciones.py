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

#variables
lista_notas=[]
opcion=0

#funciones propias
def menu():
    print("1.- Añadir nota")
    print("2.- Mostrar notas extremas")
    print("3.- Total de aprobados")
    print("4.- Nota media")
    print("5.- Mostrar todas")
    print("6.- Salir")

def aprobados():
    aprobados=0
    for n in lista_notas:
        if n>=5:
            aprobados+=1 
    return aprobados       

def promedio():
    sumatoria=0
    promedio=0
    for n in lista_notas:
        sumatoria+=n
    if len(lista_notas)>0:
        sumatoria/len(lista_notas)
    return promedio
 
#funciones principales
while opcion!=6:
    menu()
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
            print(f"La cantidad de alunnos aprobados son de: {aprobados(lista_notas)} \n")
        case 4:
            print(f"El promedio de las notas introducidas es: {promedio()} \n")
        case 5:
            print(f"Lista de notas: {lista_notas} \n")
        case 6:
            print(f"Fin del programa")
