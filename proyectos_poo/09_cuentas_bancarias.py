class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo
        
    def ingresar(self, cantidad):
        self.saldo += cantidad
        
    def extraer(self, cantidad):
        self.saldo -= cantidad
        
# crear la clase CuentaLimitada, que sera una subclase de cuenta y tendra un atributo con la cantidad maxima a extraer. 
# si el valor del atributo es 0, no hay limite. 
# si es mayor de 0, ese sera el limite y no se epodra extrar mas dinero que el que marque el limite

class CuentaLimitada(Cuenta):
    def __init__(self, saldo, limite):
        super().__init__(saldo)
        self.limite = limite
        
    def extraer(self, cantidad):
        if self.limite > 0 and self.limite <= cantidad:
            cantidad = self.limite
        super().extraer(cantidad)

                
#cuenta = CuentaLimitada(100, 10)
#cuenta.extraer(15)
#print(cuenta.saldo)

# crear nueva clase que herede CuentaLimitada, llamada CuentaMovimientos. 
# cada vez que se ingrese o extraiga, se debera registrar dicho movimiento. 
# un movimiento tiene 2 propiedades: cantidad y tipo (ingreso o extraccion). 
# la nueva clase tendra un metodo que devuelva la lista de los 5 ultimos movimientos

class Movimientos:
    def __init__(self, cantidad, tipo):
        self.cantidad = cantidad
        self.tipo = tipo
        
    def __str__(self):
        return f"cantidad: {self.cantidad}, tipo: {self.tipo}"

class CuentaMovimientos(CuentaLimitada):
    def __init__(self, saldo, limite):
        super().__init__(saldo, limite)
        self.movimientos = []
     
    def ingresar(self, cantidad):
        super().ingresar(cantidad) 
        self.movimientos.append(Movimientos(cantidad, "ingreso"))
        
    def extraer(self, cantidad):
        super().extraer(cantidad)
        self.movimientos.append(Movimientos(cantidad, "extracción"))
     
    def ultimos_movimientos(self, valor = 5):
        return self.movimientos[-valor:]
    
cm = CuentaMovimientos(100, 20)

cm.extraer(15)
cm.ingresar(50)
cm.ingresar(150)
cm.extraer(5)
cm.extraer(25)
cm.ingresar(80)
cm.extraer(30)

for um in cm.ultimos_movimientos():
    print(um)
print(cm.saldo)