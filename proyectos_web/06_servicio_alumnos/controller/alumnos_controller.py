from typing import List
from fastapi import HTTPException, APIRouter
from model.alumnos_model import Alumno
from service.alumnos_service import AlumnosService

router = APIRouter()
servicio = AlumnosService()

@router.post("/alumno", response_model=Alumno)
def guardar_libro(alumno: Alumno):
    alumno = servicio.alta_alumno(alumno)
    print(alumno)
    if alumno is None:
        raise HTTPException(status_code = 409, detail = "No admite email y curso repetido")
    return alumno

@router.get("/alumnos", response_model=List)
def buscar_alumnos():
    return servicio.buscar_alumnos()

@router.delete("/alumno/{email}")
def eliminar_libro(email: str):
    servicio.eliminar_alumno(email)

