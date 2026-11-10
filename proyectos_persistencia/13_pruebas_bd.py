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

sql_insert = "insert into alumnos values(%s,%s,%s,%s,%s)"
values = [("7777k","alumno7","al7@email.com","python",9)]
#cursordb.execute(sql_insert, values)
#db.commit()
cursordb.execute("select * from alumnos where nota > %s", [(5)])

#se imprimen los datos de cada fila en forma de tupla
for row in cursordb:
    print(row)

db.close()