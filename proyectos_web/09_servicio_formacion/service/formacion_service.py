import httpx as http
from typing import List
from fastapi import HTTPException

from model.estudiantes_model import Alumno, Estudiante

class FormacionService:
    url1 = "http://localhost:8000/alumno"
    url2 = "http://localhost:8000/alumnos"

    def alta_estudiante(self, estudiante: Estudiante):
        alumno:Alumno = Alumno(estudiante.nombre,estudiante.curso,estudiante.email,estudiante.calificacion)
        resp = http.post(self.url1, json=vars(alumno))
        #resp = http.post(self.url1, json=alumno.__dict__)
        return resp.json()

    def buscar_por_rango(self, nota_min: float, nota_max: float):
        resp = http.get(self.url2)
        alumnos = resp.json()
        alumnos_rango = [a for a in alumnos if float(nota_min) <= a['nota'] <= float(nota_max)]
        return list(map(lambda a: Estudiante(nombre=a['nombre'],curso=a["curso"],email=a["email"],calificacion=a["nota"]), alumnos_rango))