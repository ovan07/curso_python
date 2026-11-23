class Rectangulo:
    alto = 0
    ancho = 0
    
    def area(self):
        return self.alto * self.ancho
    
    def perimetro(self):
        return 2*(self.alto + self.ancho)
    
    def aumentar(self, valor):
        self.alto += valor
        self.ancho += valor
        
# ejemplo de uso
r1 = Rectangulo()
r2 = Rectangulo()

r1.alto = 5
r1.ancho = 10

r2.alto = 6
r2.ancho = 3

print(f"Area del 1er rectanglo: {r1.area()}")
print(f"Perimetro del 2er rectanglo: {r2.perimetro()}")