class Color:
    r=0;g=0;b=0
    
    def colorear(self):
        self.r=100;self.g=120;self.b=200

class Rectangulo:
    alto=0
    ancho=0
    col=Color()
    
    def __init__(self, a, b):
        self.alto = a
        self.ancho = b
    
    def area(self):
        return self.alto*self.ancho
    
    def perimetro(self):
        return 2*(self.alto+self.ancho)
    
    def aumentar(self,valor):
        self.alto+=valor
        self.ancho+=valor
        
    def dibujar(self):
        for a in range(0,self.alto):
            for b in range(0,self.ancho):
                print("[]",end="")
            print()
            
r1 = Rectangulo(3,9)
r2 = Rectangulo(7,2)

r1.dibujar()
r2.dibujar()