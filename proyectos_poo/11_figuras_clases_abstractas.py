import abc, math 

class Figura(abc.ABC):
    def __init__(self, color):
        self.color = color
    
    @abc.abstractmethod    
    def superficie():
        pass

class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio
    
    def superficie(self):
        return math.pi * (self.radio * self.radio)
    
class Triangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura
    
    def superficie(self):
        return (self.base * self.altura) / 2