from typing import List
from fastapi import FastAPI, HTTPException
from cursos_service import Curso, CursosService

app = FastAPI()
service = CursosService()

@app.post("/curso", response_model=Curso)
def alta_curso(curso: Curso):
    return service.alta_curso(curso)

@app.get("/cursos", response_model= List[Curso])
def cursos_tematica(tematica: str):
    return service.buscar_curso(tematica)

@app.delete("/curso")
def eliminar_curso(codigo: int):
    if codigo <= 0:
        raise HTTPException(status_code = 409, detail = "Codigo no valido")
    service.eliminar_curso(codigo)