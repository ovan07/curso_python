import numpy as np
import pymongo as pm

def crear_conexion(): 
    url = "mongodb://localhost:27017"
    return pm.MongoClient(url)

def empleados():
    serv = crear_conexion()
    col_empleados = serv.empresa.empleados
    datos = list(col_empleados.find())
    serv.close()
    return datos

datos = empleados()
salarios = [d["salario"] for d in datos]
edades = [d["edad"] for d in datos]
departamentos = [d["departamento"] for d in datos]

salario_medio = np.average(salarios)
print(salario_medio)

edad_mayor = np.amax(edades)
print(edad_mayor)

print(np.sort(departamentos))