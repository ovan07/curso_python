from typing import List
from fastapi import HTTPException, APIRouter
from model.libros_model import Libro
from service.libros_service import LibrosService

router = APIRouter()
servicio = LibrosService()

@router.post("/libro", response_model=Libro)
def guardar_libro(libro: Libro):
    libro = servicio.alta_libro(libro)
    if libro is None:
        raise HTTPException(status_code = 409, detail = "No admite isbn repetido")
    return libro

@router.get("/libro/{isbn}", response_model=Libro)
def buscar_libro(isbn: int):
    return servicio.buscar_libro(isbn)

@router.delete("/libro/{isbn}")
def eliminar_libro(isbn: int):
    servicio.eliminar_libro(isbn)

