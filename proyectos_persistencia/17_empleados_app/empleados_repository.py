import pymongo as pm
from bson import ObjectId

def crear_conexion(): 
    url = "mongodb://localhost:27017"
    return pm.MongoClient(url)

def nuevo_empleado(datos):
    serv = crear_conexion()
    col_empleados = serv.empresa.empleados
    col_empleados.insert_one(datos)
    serv.close()
    
def departamentos():
    serv = crear_conexion()
    col_empleados = serv.empresa.empleados
    datos = col_empleados.find()
    departamentos = list(set([dp["departamento"] for dp in datos]))
    serv.close()
    return departamentos

def empleados_por_departamento(departamento):
    serv = crear_conexion()
    col_empleados = serv.empresa.empleados
    empleados = list(col_empleados.find({"departamento":departamento}))
    serv.close()
    return empleados    # lista de diccionarios [{"":"","":""},...]

def empleados_por_rango(salario_min, salario_max):
    serv = crear_conexion()
    col_empleados = serv.empresa.empleados
    empleados = list(col_empleados.find({"salario":{"$lte":salario_max,"$gte":salario_min}}))
    serv.close()
    return empleados
    
def buscar_empleado(nombre):
    serv = crear_conexion()
    col_empleados = serv.empresa.empleados
    empleado = col_empleados.find_one({"empleado":nombre})
    serv.close()
    return empleado

def empleados():
    serv = crear_conexion()
    col_empleados = serv.empresa.empleados
    datos = list(col_empleados.find())
    serv.close()
    return datos

def actualizar_empleados(datos):
    serv = crear_conexion()
    col_empleados = serv.empresa.empleados
    for d in datos:
        col_empleados.update_one(
            {"_id":ObjectId(d["_id"])},
            {"$set":{"empleado":d["empleado"],"edad":d["edad"],"salario":d["salario"],"departamento":d["departamento"]}}
        )
    serv.close()
