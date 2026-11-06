import csv
"""
with open("empleados.csv","r") as f:
    next(f)                         #se salta la 1ra linea
    datos=csv.reader(f,delimiter=",")
    for row in datos:
        print(row)

with open("empleados.csv","r") as f:
    datos=csv.DictReader(f)
    for row in datos:
        print(row)
        
with open("empleados.csv","r") as f:
    datos=list(csv.reader(f))       #lista de listas
    print(datos)
    
with open("empleados.csv","r") as f:
    datos=list(csv.DictReader(f))   #lista de diccionarios (json)
    print(datos)
"""
# solicita la introduccion de un departamento y muestra
# los nombres de las personas de ese departamento
with open("empleados.csv","r") as f:
    datos=list(csv.DictReader(f))   #lista de diccionarios (json)
"""
departamento=input("Introduce un departamento: ")

empleados=[d["empleado"] for d in datos if d["departamento"]==departamento]
print(empleados)
"""
#nombre del empleado con mayor salario
mayor_salario = max(datos, key=lambda d: int(d["salario"]))
print(f"el empleado '{mayor_salario["empleado"]}' tiene el mayor salario con {mayor_salario["salario"]}")