from model.alumnos_model import Alumno
from config.app_config import connection_pool

class AlumnosRepository:
    def save(self, alumno: Alumno):
        sql = "insert into alumnos (nombre, curso, email, nota) values(%s, %s, %s, %s)"
        con = connection_pool.get_connection()
        cursor = con.cursor()
        cursor.execute(sql, (alumno.nombre,alumno.curso,alumno.email,alumno.nota))
        con.commit()
        con.close()
        return alumno

    def find_all(self):
        sql = "select * from alumnos"
        con = connection_pool.get_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute(sql)
        alumnos = cursor.fetchall()
        con.close()
        return alumnos

    def find_by_curso_email(self, curso: str, email: str):
        sql = "select * from alumnos where email=%s and curso=%s"
        con = connection_pool.get_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute(sql, (email, curso))
        alumno = cursor.fetchone()
        con.close()
        return alumno

    def find_by_curso(self, curso: str):
        sql = "select * from alumnos where curso=%s"
        con = connection_pool.get_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute(sql, (curso,))
        alumnos = cursor.fetchall()
        con.close()
        return alumnos

    def delete_by_email(self, email: str):
        sql = "delete from alumnos where email=%s"
        con = connection_pool.get_connection()
        cursor = con.cursor()
        cursor.execute(sql, (email,))
        con.commit()
        con.close()
