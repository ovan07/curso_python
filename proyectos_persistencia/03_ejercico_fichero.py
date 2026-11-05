#Al iniciar el programar se debe mostrar el siguiente menu:
#1.- Añadir nota
#2.- Mostrar notas extremas
#3.- Total de aprobados
#4.- Nota media
#5.- Mostrar todas
#6.- Salir

# El usuario elige una opcion (1 a 6) y el programa le muestra o le pide
# los datos necesarios para llevar a cabo esa accion. Despues, vuelve a salir el menu
# y asi hasta que elija la opcion salir. 
# las notas se guardan en un fichero
opcion=0
dir_fichero="notas.txt"

#funciones propias
def menu():
    print("1.- Añadir nota")
    print("2.- Mostrar notas extremas")
    print("3.- Total de aprobados")
    print("4.- Nota media")
    print("5.- Mostrar todas")
    print("6.- Salir")

def leer_fichero():
    try:
        with open(dir_fichero,"r") as f:
            notas=f.readlines()
    except FileNotFoundError:
        print("El fichero no existe")
    return list(map(lambda n:int(n.strip()),notas))

def escribir_fichero(nota):
    with open(dir_fichero,"a") as f:
        f.write(nota+"\n")
        
def aprobados(lista_notas):
    return list(filter(lambda n:n>=5, lista_notas))      

def promedio(lista_notas):
    if not lista_notas:
        return 0
    return sum(lista_notas)/len(lista_notas)
 
def mostrar_notas(lista_notas):
    if not lista_notas:
        return "no hay notas"
    for n in lista_notas:
        print(n)
     
#funciones principales
while opcion!=6:
    menu()
    try:
        opcion=int(input("- Opcion: "))
    except ValueError:
        break
    
    match opcion:
        case 1:
            nota=input("-- Añada una nota: ")
            escribir_fichero(nota)
        case 2:
            lista_notas=leer_fichero()
            if lista_notas!=[]:
                print(f"La nota mas alta: {max(lista_notas)} y la nota mas baja: {min(lista_notas)} \n")
        case 3:
            lista_notas=leer_fichero()
            print(f"La cantidad de alunnos aprobados son de: {len(aprobados(lista_notas))} \n")
        case 4:
            lista_notas=leer_fichero()
            print(f"El promedio de las notas introducidas es: {promedio(lista_notas)} \n")
        case 5:
            lista_notas=leer_fichero()
            mostrar_notas(lista_notas)
            #print(f"Lista de notas: {lista_notas} \n")
        case 6:
            print(f"Fin del programa")