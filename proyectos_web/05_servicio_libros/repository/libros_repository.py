from model.libro_model import Libro
from config.app_config import connection_pool

class LibrosRepository:
    def save(self, libro: Libro):
        sql = "insert into libros values(%s, %s, %s, %s, %s, %s)"
        con = connection_pool.get_connection()
        cursor = con.cursor()
        cursor.execute(sql, (libro.isbn,libro.titulo,libro.autor,libro.precio,libro.paginas,libro.idTema))
        con.commit()
        con.close()
        return libro

    def find_by_isbn(self, isbn: int):
        sql = "select * from libros where isbn=%s"
        con = connection_pool.get_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute(sql, (isbn,))
        libro = cursor.fetchone()
        con.close()
        return libro

    def delete_by_isbn(self, isbn: int):
        sql = "delete from libros where isbn=%s"
        con = connection_pool.get_connection()
        cursor = con.cursor()
        cursor.execute(sql, (isbn,))
        con.commit()
        con.close()


