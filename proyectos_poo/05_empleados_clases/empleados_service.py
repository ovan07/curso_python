import csv

# Clase Empleado
class Empleado:
    def __init__(self,nombre,edad,salario,departamento):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.departamento = departamento

# Clase Gestor de Empleados        
class Gestor_Empleados:
    def __init__(self, dir):
        self.dir = dir
        
    def alta_empleado(self, empleado):
        with open(self.dir, "a", newline = "") as f:
            csv.writer(f).writerow([empleado.nombre, empleado.edad, empleado.salario, empleado.departamento])
    
    def buscar_empleado(self, nombre):
        with open(self.dir, "r") as f:
            datos = list(csv.DictReader(f))
            resultado = [d for d in datos if d["empleado"] == nombre]
            if resultado:
                r = resultado[0]
                return Empleado(r["empleado"], int(r["edad"]), float(r["salario"]), r["departamento"])
            else:
                return []
            
    def empleado_departamento(self, departamento):
        with open(self.dir, "r") as f:
            datos = list(csv.DictReader(f))
            return [Empleado(d["empleado"], int(d["edad"]), float(d["salario"]), d["departamento"]) for d in datos if d["departamento"] == departamento]

            
    def departamentos(self):
        with open(self.dir, "r") as f:
            datos = list(csv.DictReader(f))
            return list(set([d["departamento"] for d in datos]))
        
        
print(Gestor_Empleados("empleados.csv").departamentos())