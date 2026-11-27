import httpx as http
from model.ejemplar_model import Libro, Ejemplar


class EjemplaresService:
    url = "http://localhost:8000/libro"

    def buscar_ejemplar(self, isbn: int):
        resp = http.get(self.url + "/" + str(isbn))
        libro = Libro(**resp.json())

        if libro.paginas > 400:
            dificultad = "alta"
        elif 400 >= libro.paginas > 250:
            dificultad = "media"
        else:
            dificultad = "baja"

        return Ejemplar(isbn=libro.isbn, titulo=libro.titulo, dificultad=dificultad)
