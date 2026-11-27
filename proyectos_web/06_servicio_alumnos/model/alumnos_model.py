from pydantic import BaseModel

class Alumno(BaseModel):
    nombre: str
    curso: str
    email: str
    nota: float
