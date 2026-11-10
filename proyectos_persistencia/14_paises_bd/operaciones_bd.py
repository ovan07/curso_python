import mysql.connector as con

def crear_conexion():
    return con.connect(
        host = "localhost",
        user = "root",
        password = "root",
        port = 3306,
        database = "mundo"
    )

def borrar_tablas():
    db = crear_conexion()
    cursor = db.cursor()
    cursor.execute("delete from continentes")
    cursor.execute("delete from paises")
    db.commit()
    db.close()
    
def crear_continentes(continentes):  #["Asia","America",...]
    db = crear_conexion()
    cursor = db.cursor()
    sql = "insert into continentes(continente) values(%s)"
    lista_tuplas = [(c,) for c in continentes]    #lista de tuplas
    cursor.executemany(sql, lista_tuplas)
    #for c in continentes:               #alternativa
    #    cursor.execute(sql_insert, c)
    db.commit()
    db.close()
    
def devolver_continentes():
    db = crear_conexion()
    cursor = db.cursor(dictionary = True)
    sql = "select * from continentes"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    db.close()
    return resultado

def crear_paises(paises):   #[{"name":"España","population":1345,"flags":"https","region":idContinente},....]
    db = crear_conexion()
    cursor = db.cursor()
    sql = "insert into paises(pais, poblacion, bandera, idContinente) values(%s, %s, %s, %s)"
    lista_tuplas = [(p["name"], p["population"], p["flags"], p["region"]) for p in paises]    #lista de tuplas
    #lista_tuplas = [tuple(p.values()) for p in paises]    #lista de tuplas
    cursor.executemany(sql, lista_tuplas)
    db.commit()
    db.close()
    
def paises_por_continente(idContinente):
    db = crear_conexion()
    cursor = db.cursor(dictionary = True)
    sql = "select * from paises where idContinente = %s"
    cursor.execute(sql, idContinente)
    resultado = cursor.fetchall()
    db.close()
    return resultado