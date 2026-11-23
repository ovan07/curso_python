import _03_calculadora as cal

class Cientifica(cal.Caculadora):
    
    def sumatorio(self):
        suma = 0
        for n in range(self.num1, self.num2 + 1):
            suma += n
        return suma
    