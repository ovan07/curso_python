from typing import List
from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel

class Curso(BaseModel):
    codigo: int
    nombre: str
    tematica: str
    precio: float

app = FastAPI()
lista_cursos = []

@app.post("/curso", response_model=Curso)
def alta_curso(curso: Curso):
    lista_cursos.append(curso)
    return curso

@app.get("/cursos", response_model= List[Curso])
def cursos_tematica(tematica: str):
    return [c for c in lista_cursos if c.tematica == tematica]

@app.delete("/cursos/{codigo}")
def eliminar_curso(codigo: int):
    if codigo < 0:
        raise HTTPException(status_code=409, detail="Codigo no valido")
    lista_cursos = [c for c in lista_cursos if c.codigo != codigo]