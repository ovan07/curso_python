class Caculadora:
    
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
        
    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        if self.num1 > self.num2:
            return self.num1 - self.num2
        else:
            return self.num2 - self.num1
    
    def multiplicar(self):
        return self.num1 * self.num2
    
    def dividir(self):
        if self.num1 > self.num2:
            return self.num1 / self.num2
        else:
            return self.num2 / self.num1
    
# caso de uso:
"""
num1 = int(input("Introducir el 1er numero: "))
num2 = int(input("Introducir el 1er numero: "))
c = Caculadora(num1, num2)

print("Resultado de la suma ", c.sumar())
print("Resultado de la resta ", c.restar())
print("Resultado de la multiplicación ", c.multiplicar())
print("Resultado de la divición ", c.dividir())
"""