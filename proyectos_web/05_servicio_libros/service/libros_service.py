from repository.libros_repository import LibrosRepository
from model.libros_model import Libro

class LibrosService:
    repo = LibrosRepository()

    def alta_libro(self, libro: Libro):
        if self.repo.find_by_isbn(libro.isbn):
            return None                         # informamos al controlador de que no se ha podido dar de alta
        return self.repo.save(libro)

    def buscar_libro(self, isbn):
        libro = self.repo.find_by_isbn(isbn)
        if libro:
            return Libro(isbn= libro["isbn"],
                         titulo = libro["titulo"],
                         autor = libro["autor"],
                         precio = libro["precio"],
                         paginas = libro["paginas"],
                         idTema = libro["idTema"]
                         )
        return None

    def eliminar_libro(self, isbn):
        self.repo.delete_by_isbn(isbn)