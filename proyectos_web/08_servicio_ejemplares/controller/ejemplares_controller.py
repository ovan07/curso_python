from typing import List
from fastapi import APIRouter, HTTPException, Response

from model.ejemplar_model import Ejemplar
from service.ejemplares_service import EjemplaresService

router = APIRouter()
service = EjemplaresService()

@router.get("/ejemplar/{isbn}", response_model=Ejemplar)
def buscar_ejemplar(isbn: int):
    return service.buscar_ejemplar(isbn)
