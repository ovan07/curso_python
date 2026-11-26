from pydantic import BaseModel

class Libro(BaseModel):
    isbn: int
    titulo: str
    autor: str
    precio: float
    paginas: int
    idTema: int
