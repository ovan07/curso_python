import mysql.connector as con

def crear_conexion():
    return con.connect(
        host = "localhost",
        user = "root",
        password = "root",
        port = 3306,
        database = "universidad"
    )
    
def borrar_tabla():
    db = crear_conexion()
    cursor = db.cursor()
    cursor.execute("delete from alumnos")
    db.commit()
    db.close()
    
def crear_alumno(alumno):  #("dni","nombre","email","curso","nota")
    db = crear_conexion()
    cursor = db.cursor()
    sql = "insert into alumnos(dni,nombre,email,curso,nota) values(%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(alumno))
    db.commit()
    db.close()
    
def borrar_alumno(dni):
    db = crear_conexion()
    cursor = db.cursor() #DELETE FROM nombre_tabla WHERE columna = 'valor';
    sql = "delete from alumnos where dni = %s"
    cursor.execute(sql, dni)
    db.commit()
    db.close()

def obtener_alumno_curso(curso):
    db = crear_conexion()
    cursor = db.cursor(dictionary = True)
    sql = "select * from alumnos where curso = %s"
    cursor.execute(sql, curso)
    resultado = cursor.fetchall()
    db.close()
    return resultado

def obtener_alumno_dni(dni):
    db = crear_conexion()
    cursor = db.cursor(dictionary = True)
    sql = "select * from alumnos where dni = %s"
    cursor.execute(sql, dni)
    resultado = cursor.fetchall()
    db.close()
    return resultado
    
def obtener_alumnos():
    db = crear_conexion()
    cursor = db.cursor(dictionary = True)
    sql = "select * from alumnos"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    db.close()
    return resultado