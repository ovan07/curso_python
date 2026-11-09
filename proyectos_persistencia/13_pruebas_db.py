import mysql.connector as con

# se establece la conexión a la base de datos
db = con.connect(
    host = "localhost",
    user = "root",
    password = "root",
    port = 3306,
    database = "universidad"
)

cursordb = db.cursor(dictionary = True)

cursordb.execute("select * from alumnos")

#se imprimen los datos de cada fila en forma de tupla
for row in cursordb:
    print(row)

db.close()