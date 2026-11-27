from typing import List
from fastapi import APIRouter, HTTPException, Response

from model.estudiantes_model import Alumno, Estudiante
from service.formacion_service import FormacionService

router = APIRouter()
service = FormacionService()

@router.post("/estudiante", response_model=Estudiante)
def alta_estudiante(estudiante: Estudiante):
    return service.alta_estudiante(estudiante)

@router.get("/estudiantes/{nota_min}/{nota_max}", response_model=List[Estudiante])
def buscar_estudiantes(nota_min, nota_max):
    return service.buscar_por_rango(nota_min, nota_max)