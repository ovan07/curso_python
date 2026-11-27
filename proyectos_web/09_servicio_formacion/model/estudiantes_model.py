from pydantic import BaseModel

class Alumno:
    def __init__(self, nombre, curso, email, nota):
        self.nombre = nombre
        self.curso = curso
        self.email = email
        self.nota = nota

class Estudiante(BaseModel):
    nombre:str
    curso:str
    email:str
    calificacion:float