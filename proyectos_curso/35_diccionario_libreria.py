"""
Realiza un progrma para la organizacion de una libreria
un libro tiene tres propiedades: titulo, autor y precio.

Cuando se inicie el programa, se va a mostrar un menu:
1-Nuevo libro
2-Mostrar todos
3-Buscar por titulo
4-Libros por precio maximo
5-Salir

1-Se piden los datos del nuevo libro y se guardan
2-Se muestran los titulos de todos los libros
3-Se le pide el titulo y se muestran todos sus datos
4-Se le pide el precio maximo y se muestran los titulos de los libros cuyo precio sea igual o inferior al introducido
Despues de ejecutar cualquiera de las anteriores opciones, se muestra de nuevo el menu.
Asi hasta que elija la opcion 5 que sale del programa
"""
lista_libros=[
    {"titulo":"Autos","autor":"Carlos P","precio":9.99},
    {"titulo":"Monumentos","autor":"Fran M","precio":15.45}
]

def menu():
    print("\n------ Menu ------")
    print("1-Nuevo libro")
    print("2-Mostrar todos")
    print("3-Buscar por titulo")
    print("4-Libros por precio maximo")
    print("5-Salir")

def existe(titulo):
    return titulo in titulos()

def titulos():
    return [lib["titulo"] for lib in lista_libros]

def buscar_por_titulo(titulo):
    libro=[lib for lib in lista_libros if lib["titulo"]==titulo]
    if not libro:
        print("No se encontro el libro")
    return libro
    
def buscar_por_precio(precio):
    encontrados=[]
    for lib in lista_libros:
        if precio>=lib["precio"]:
            encontrados.append(lib)
    if not encontrados:
        print("No se encontraron libros")
    return encontrados
    
opcion=0
while opcion!=5:
    libro={}
    
    menu()
    opcion=int(input("- Opcion: "))
    
    match opcion:
        case 1:
            libro["titulo"]=input("Introduce el titulo: ")
            libro["autor"]=input("Introduce el autor: ")
            libro["precio"]=float(input("Introduce el precio: "))
            if not existe(libro["titulo"]):
                lista_libros.append(libro)
            else:
                print("El libro ya existe")
        case 2:
            print(titulos())
        case 3:
            libro=buscar_por_titulo(input("Introduce el titulo a buscar: ").capitalize())
            if libro:
                print(libro)
        case 4:
            libros=buscar_por_precio(float(input("Introduce el precio maximo: ")))
            if libros:
                print(libros)
        case 5:
            print("Fin del programa")
        case _:
            print("Opcion no valida")