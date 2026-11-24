class Empleado:
    def __init__(self, nombre, edad, salario_base):
        self.nombre = nombre
        self.edad = edad
        self.salario_base = salario_base

    def mostrar_informacion(self):
        return self.nombre, self.edad, self.salario_base

    def calcular_salario(self):
        return self.salario_base

class Desarrollador(Empleado):
    def __init__(self, nombre, edad, salario_base, lenguaje, horas_extras):
        super().__init__(nombre, edad, salario_base)
        self.lenguaje = lenguaje
        self.horas_extras = horas_extras

    def mostrar_informacion(self):
        return super().mostrar_informacion() + (self.lenguaje, self.horas_extras)

    def calcular_salario(self):
        return super().calcular_salario() + (self.horas_extras * 25)

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario_base, departamento, bonus):
        super().__init__(nombre, edad, salario_base)
        self.departamento = departamento
        self.bonus = bonus

    def mostrar_informacion(self):
        return super().mostrar_informacion() + (self.departamento, self.bonus)
    
    def calcular_salario(self):
        return super().calcular_salario() + self.bonus
    
    
#=================# Programa principal #=================#
empleados = [
    Desarrollador("Juan", 30, 1500, "Java", 20),
    Desarrollador("Ana", 28, 1200, "Python", 5),
    Gerente("Marcos", 42, 2100, "Informatica", 200),
    Gerente("María", 35, 2500, "Ventas", 150)
]
Empleado()
importe_total = 0
for e in empleados:
    print(f"Información: {e.mostrar_informacion()}")
    print(f"Salario calculado: {e.calcular_salario()}")
    importe_total += e.calcular_salario()

print(f"Importe total de las nominas: {importe_total}")