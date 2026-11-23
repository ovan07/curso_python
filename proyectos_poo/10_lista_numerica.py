# crear una subclase de list para el almacenamiento de numeros con las siguientes caracteristicas: 
# incluira los metodos: 
# sum(), devuelve la suma de los numeros almacenados 
# mean(), devuelve la media de los numeros almacenados 
# ademas de esos metodos, el construcctor recibira un parametro que en caso de ser true, impidira que se repita un numero

class ListaNumerica(list):
    def __init__(self, unicos = False):
        super().__init__()
        self.unicos = unicos

    def sum(self):            
        return sum(self)
    
    def mean(self):
        if not len(self):
            return 0
                    
        return sum(self) / len(self)
    
    def append(self, object):
        if (self.unicos and object in self) or isinstance(object, str):
            return None
        return super().append(object)


#---------------# caso de usos #---------------#
ln = ListaNumerica(True)
ln.append(5)
ln.append(5)
ln.append(10)
ln.append("hello")

print(f"sumatoria: {ln.sum()}")
print(f"media: {ln.mean()}")
print(ln)