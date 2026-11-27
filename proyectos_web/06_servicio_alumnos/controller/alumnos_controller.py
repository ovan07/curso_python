from typing import List
from fastapi import HTTPException, APIRouter
from model.alumnos_model import Alumno
from service.alumnos_service import AlumnosService

router = APIRouter()
servicio = AlumnosService()

@router.post("/alumno", response_model=Alumno)
def guardar_libro(alumno: Alumno):
    alumno = servicio.alta_alumno(alumno)
    if alumno is None:
        raise HTTPException(status_code = 409, detail = "No admite email y curso repetido")
    return alumno

@router.get("/alumnos", response_model=List[Alumno])
def buscar_alumnos():
    return servicio.buscar_alumnos()

@router.get("/alumnos/{curso}", response_model=List[Alumno])
def buscar_alumnos_curso(curso: str):
    return servicio.buscar_alumnos_curso(curso)

# @router.get("/alumno/{curso}&{email}")
# def buscar_alumno_curso_email(curso, email):
#     return servicio.buscar_alumno_curso_email(curso, email)

@router.delete("/alumno/{email}")
def eliminar_libro(email: str):
    servicio.eliminar_alumno(email)

