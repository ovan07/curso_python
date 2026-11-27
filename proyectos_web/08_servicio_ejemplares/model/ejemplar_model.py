from pydantic import BaseModel

class Libro:
    def __init__(self, isbn, titulo, autor, precio, paginas, idTema):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.paginas = paginas
        self.idTema = idTema

class Ejemplar(BaseModel):
    isbn:  int
    titulo: str
    dificultad: str

