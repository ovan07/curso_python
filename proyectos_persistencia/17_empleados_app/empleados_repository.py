import pymongo as pm

def crear_conexion(): 
    url = "mongodb://localhost:27017"
    return pm.MongoClient(url)

def nuevo_empleado(json):
    serv = crear_conexion()
    col_empleados = serv.empresa.empleados
    col_empleados.insert_one(json)
    serv.close()
    
def departamentos():
    serv = crear_conexion()
    col_empleados = serv.empresa.empleados
    depart = col_empleados.find()
    departamentos = list(set([dp["departamento"] for dp in depart]))
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
