# utilizando los archivos de funciones definidos, hará lo siguiente: 
# - borrará las tablas de base de datos 
# - recuperar continentes y paises del json 
# - prepará los datos obtenidos, para poder enviarlos a la funciones de la base de datos 
# - llamará a las funciones para guardar continentes y guardar paises
import operaciones_bd as op_bd
import operaciones_json as op_json

# funciones
def obtener_idcontinente(pais, continentes_bd):
    continente = [c["idContinente"] for c in continentes_bd if c["continente"] == pais["region"]]
    #continente = list(filter(lambda c:c["continente"] == pais["region"], continentes_bd))
    return continente[0]

# limpiamos el contenido de las tablas
op_bd.borrar_tablas()

# obtenemos los datos del json
lista_continentes = op_json.continentes()
lista_paises = op_json.paises()

# introducimos la lista de continenes en su respectiva tabla de bd
op_bd.crear_continentes(lista_continentes)

# obtenemos la lista de continente de la bd para usar su idContinente
continentes_bd = op_bd.devolver_continentes()

# actualizo el valor region (continente) por su idContinente correspondiente
for pais in lista_paises:    
    idContinente = obtener_idcontinente(pais, continentes_bd)
    pais["region"] = idContinente
    pais["flags"] = pais["flags"]["svg"]

"""
paises_para_bd = [
    {
        "flags" : p["flags"]["svg"],
        "region" : obtener_idcontinente(p["region"],continentes_bd)
    } for p in lista_paises
]
"""
# introducimos la lista de los paises y lo guardamos en la tabla bd
op_bd.crear_paises(lista_paises)

print("datos almacenados")