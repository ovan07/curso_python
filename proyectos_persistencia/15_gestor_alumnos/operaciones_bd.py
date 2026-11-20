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
    try:
        db = crear_conexion()
        cursor = db.cursor()
        cursor.execute("delete from alumnos")
        db.commit()
    except con.Error as err:
        print(err)
        return None
    finally:
        db.close()
    
def crear_alumno(alumno):  #("dni","nombre","email","curso","nota")
    try:
        db = crear_conexion()
        cursor = db.cursor()
        sql = "insert into alumnos(dni,nombre,email,curso,nota) values(%s,%s,%s,%s,%s)"
        cursor.execute(sql, alumno)
        db.commit()
    except con.Error as err:
        print(err)
        return None
    finally:
        db.close()
    
def actualizar_alumno(alumno):  #("nombre","email","curso","nota","dni")
    try:
        db = crear_conexion()
        cursor = db.cursor()
        sql = "update alumnos set nombre=%s,email=%s,curso=%s,nota=%s where dni=%s"
        cursor.execute(sql, alumno)
        db.commit()
    except con.Error as err:
        print(err)
        return None
    finally:
        db.close()
    
def borrar_alumno(dni):
    try:
        db = crear_conexion()
        cursor = db.cursor()    #DELETE FROM nombre_tabla WHERE columna = 'valor';
        sql = "delete from alumnos where dni = %s"
        cursor.execute(sql, [dni])
        db.commit()
    except con.Error as err:
        print(err)
        return None
    finally:
        db.close()

def buscar_alumno_curso(curso):
    try:
        db = crear_conexion()
        cursor = db.cursor(dictionary = True)
        sql = "select * from alumnos where curso = %s"
        cursor.execute(sql, [curso])
        resultado = cursor.fetchall()
        db.close()
        return resultado
    except con.Error as err:
        print(err)
        return None
    finally:
        db.close()

def buscar_alumno_dni(dni):
    try:
        db = crear_conexion()
        cursor = db.cursor(dictionary = True)
        sql = "select * from alumnos where dni = %s"
        cursor.execute(sql, [dni])
        resultado = cursor.fetchone()
        return resultado
    except con.Error as err:
        print(err)
        return None
    finally:
        db.close()
    
def buscar_alumnos():
    try:
        db = crear_conexion()
        cursor = db.cursor(dictionary = True)
        sql = "select * from alumnos"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        return resultado
    except con.Error as err:
        print(err)
        return None
    finally:
        db.close()

def buscar_cursos():
    try:
        db = crear_conexion()
        cursor = db.cursor(dictionary = True)
        sql = "select distinct(curso) from alumnos"
        cursor.execute(sql)
        resultado = cursor.fetchall() 
        return resultado
    except con.Error as err:
        print(err)
        return None
    finally:
        db.close()