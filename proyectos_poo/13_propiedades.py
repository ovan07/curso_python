class Empleado:
    def __init__(self, nombre, edad, salario_base):
        self.nombre = nombre
        self._edad = edad
        self.salario_base = salario_base

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Salario base: {self.salario_base} €")

    def calcular_salario(self):
        return self.salario_base

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        #if valor < 0:
        #    raise ValueError("La edad no puede ser negativa")
        if valor > 0:
            self._edad = valor

emp = Empleado("Juan", 30, 1500)
emp.edad = -10
print(emp.edad)