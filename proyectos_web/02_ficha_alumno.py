from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel


# hacer una API REST con una función que reciba l dni del alumno
# y devuelva su ficha, formada por dni, nombre, edad y email
# class Alumno:
#     def __init__(self, dni, nombre, edad, email):
#         self.dni = dni
#         self.nombre = nombre
#         self.edad = edad
#         self.email = email

class Alumno(BaseModel):
    dni: str
    nombre: str
    edad: int
    email: str

app = FastAPI()

@app.get("/ficha/{dni}", response_model= Alumno)
def ficha(dni)-> Alumno:
    if dni is None:
        return None

    return Alumno(
        dni = dni,
        nombre = "prueba",
        edad = 80,
        email = "al@email.com"
    )

@app.post("/ficha", response_model = Alumno)
def nueva_ficha(ficha: Alumno)-> Alumno:
    if not ficha.dni:
        raise HTTPException(status_code=402, detail="No es posible dar un alta sin dni")
    print(ficha.nombre)
    return ficha

@app.delete("/ficha/{dni}")
def eliminar_ficha(dni, resp: Response):
    if dni == 0:
        resp.status_code= 409
        return
    print(f"Eliminado ficha: {dni}")