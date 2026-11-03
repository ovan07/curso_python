#lista de reproducción
lista_reproduccion=[
    {"titulo":"canción inventada","duracion":3.20,"valoracion":4},
    {"titulo":"Bohemian Rapsody","duracion":5.40,"valoracion":10},
    {"titulo":"Green summer","duracion":4.10,"valoracion":7}
]
"""
def repetido(titulo):
    rep=False
    for c in lista_reproduccion:
        if titulo==c["titulo"]:
            rep=True
            break
    return rep
"""
def repetido(titulo):
    return titulo in [can["titulo"] for can in lista_reproduccion]

#Se solicita la introducción de los datos de una nueva canción.
#si la cancion no existe se agrega a la lista, si ya existe no hace nada
#y se agrega a la lista
#Después, el programa muestra todos los titulos almacenados
#y la valoración media de toda la lista de reproducción 
cancion={}
cancion["titulo"]=input("Titulo de la canción: ")
cancion["duracion"]=float(input("Duracion de la canción: "))
cancion["valoracion"]=int(input("Valoracion de la canción: "))

if not repetido(cancion["titulo"]):
    lista_reproduccion.append(cancion)
else:
    print("la cancion no fue añadida")

sum=0
for music in lista_reproduccion:
    print(music["titulo"])
    sum+=music["valoracion"]
    
print(f"la media de valoracion de la lista es: {sum/len(lista_reproduccion)}")