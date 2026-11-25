import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/saludo")
def saludar():
    return  {"saludo": "Hola FastAPI", "fecha": datetime.date.today()}

@app.get("/saludo/{nombre}")
def saludo_personal(nombre):
    return {"saludo": f"Hola {nombre}, bienvenido a FastAPI", "fecha": datetime.date.today()}

@app.get("/saludo_completo")
def saludo_completo(nombre, edad):
    return {"saludo": f"Hola {nombre}, tienes {edad} años bienvenido a FastAPI", "fecha": datetime.date.today()}