from abc import ABC, abstractmethod

class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self._stock = stock

    def __str__(self):
        return f"{self.nombre} - {self.precio} € (Stock: {self.stock})"

    @property
    def stock(self):
        return self._stock

    def reducir_stock(self, cantidad):
        if cantidad > self._stock:
            raise ValueError("Stock insuficiente")
        self._stock -= cantidad

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"{self.nombre} ({self.email})"

class LineaPedido:
    def __init__(self, producto, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.producto = producto
        self.cantidad = cantidad

    def __str__(self):
        return (
            f"{self.producto.nombre} x {self.cantidad} "
            f"= {self.subtotal():.2f} €"
        )

    def subtotal(self):
        return self.producto.precio * self.cantidad

# Descuento
class Descuento(ABC):
    @abstractmethod
    def aplicar(self, importe):
        pass

class DescuentoPorcentaje(Descuento):
    def __init__(self, porcentaje):
        if not 0 <= porcentaje <= 100:
            raise ValueError("Porcentaje incorrecto")
        self.porcentaje = porcentaje

    def aplicar(self, importe):
        return importe * (1 - self.porcentaje / 100)

class DescuentoFijo(Descuento):
    def __init__(self, cantidad):
        if cantidad < 0:
            raise ValueError("Descuento incorrecto")
        self.cantidad = cantidad

    def aplicar(self, importe):
        return max(0, importe - self.cantidad)

class SinDescuento(Descuento):
    def aplicar(self, importe):
        return importe

# Forma de pago
class FormaPago(ABC):
    @abstractmethod
    def calcular(self, importe):
        pass

class PagoTarjeta(FormaPago):
    def calcular(self, importe):
        return importe * 1.01

class PagoPayPal(FormaPago):
    def calcular(self, importe):
        return importe *1.02

class PagoTransferencia(FormaPago):
    def calcular(self, importe):
        return importe

# Pedido
class Pedido:
    def __init__(self, numero_pedido, cliente):
        self.numero_pedido = numero_pedido
        self.cliente = cliente
        self.lineas = []
        self.descuento = SinDescuento
        self.estado = "Pendiente"

    def agregar_producto(self, producto, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")

        # Comprobar si el producto ya está en el pedido
        for linea in self.lineas:
            if linea.producto.codigo == producto.codigo:
                nueva_cantidad = linea.cantidad + cantidad
                if nueva_cantidad > producto.stock:
                    raise ValueError("Stock insuficiente")
                linea.cantidad = nueva_cantidad
                return

        #si es una línea de pedido nuevo
        if cantidad > producto.stock:
            raise ValueError("Stock insuficiente")

        self.lineas.append(LineaPedido(producto, cantidad))

    def eliminar_producto(self, codigo):
        self.lineas = [
            linea for linea in self.lineas
            if linea.producto.codigo != codigo
        ]

    def aplicar_descuento(self, descuento):
        if not isinstance(descuento, Descuento):
            raise TypeError("Descuento no válido")
        self.descuento = descuento

    def calcular_base(self):
        return sum(
            [linea.subtotal() for linea in self.lineas]
        )

    def calcular_total(self):
        return self.descuento.aplicar(self.calcular_base())
    
    def pagar(self, forma_pago):
        # Comprobar nuevamente el stock antes de cobrar
        for linea in self.lineas:
            if linea.cantidad > linea.producto.stock:
                raise ValueError(
                    f"Stock insuficiente de {linea.producto.nombre}"
                )

        self.estado = "PAGADO"
        return forma_pago.calcular(self.calcular_total())

#=================# Caso de Uso #=================#

