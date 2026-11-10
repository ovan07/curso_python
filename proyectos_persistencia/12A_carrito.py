# tienda online
# products disponibles (producto, precio)
# mi carrito (producto, precio, unidad)(total, en otra linea)
import streamlit as st
import csv

dir_fichero = "productos.csv"
# leemos del fichero los productos
with open(dir_fichero, "r") as f:
    productos = list(csv.DictReader(f))  # lista de diccionarios (json)

# guardamos en sesion el carrito
if "carrito" not in st.session_state:
    st.session_state.carrito = []

carrito = st.session_state.carrito

st.title("Tienda online")
st.subheader("Productos disponibles")

col_producto, col_precio, col_accion = st.columns(3)
indice = 0
for p in productos:
    col_producto, col_precio, col_accion = st.columns(3)
    col_producto.write(p["nombre"])
    col_precio.write(f"{p['precio']} €")
    if col_accion.button("Añadir", key=f"añadir_{indice}"):
        producto_existente = []
        for c in carrito:
            if c["nombre"] == p["nombre"]:
                producto_existente = c
                break

        if producto_existente:
            producto_existente["unidades"] += 1
        else:
            nuevo_pruducto = {"nombre": p["nombre"],"precio": p["precio"],"unidades": 1}
            carrito.append(nuevo_pruducto)
    indice += 1

st.subheader("Mi carrito")

# si el carrito no esta vacio
if len(carrito) > 0:
    col_producto, col_precio, col_accion, col_unidades = st.columns(4)
    total = 0
    indice2 = 0
    for c in carrito:
        col_producto, col_precio, col_unidades, col_accion = st.columns(4)
        col_producto.write(c["nombre"])
        col_precio.write(f"{c["precio"]} €")
        col_unidades.write(f"Unidades: {c["unidades"]}")
        if col_accion.button("Eliminar", key=f"remover_{indice2}"):
            st.session_state.carrito.pop(indice2)
            st.rerun()
        indice2 += 1
        # vamos calculando el total sumando el precio por el numero de unidades
        total += int(c["precio"]) * c["unidades"]

    st.write(f"**Total:** {total} €")
    st.success("Producuto añadido")
else:
    st.info("El carrito está vacío")
