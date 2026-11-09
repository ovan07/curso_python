"""
Realiza un progrma para la organizacion de una libreria
un libro tiene tres propiedades: titulo, autor y precio.

Cuando se inicie el programa, se va a mostrar un menu:
1-Nuevo libro
2-Mostrar todos
3-Buscar por titulo
4-Libros por precio maximo
5-Salir

1-Se piden los datos del nuevo libro y se guardan
2-Se muestran los titulos de todos los libros
3-Se le pide el titulo y se muestran todos sus datos
4-Se le pide el precio maximo y se muestran los titulos de los libros cuyo precio sea igual o inferior al introducido
Despues de ejecutar cualquiera de las anteriores opciones, se muestra de nuevo el menu.
Asi hasta que elija la opcion 5 que sale del programa
"""
import streamlit as st

# Se define la variable que contiene los libros con un par de ellos como ejemplos
lista_libros = [
    {"titulo":"Autos","autor":"Carlos P","precio":9.99},
    {"titulo":"Monumentos","autor":"Fran M","precio":15.45}
]

# Guardamos en sesion
if "libros" not in st.session_state:
    st.session_state.libros = lista_libros
else:
    lista_libros = st.session_state.libros

# Definir los nombres de las pestañas
tab_todos, tab_nuevo,tab_buscar,tab_precios,tab_tienda = st.tabs(["Mostrar todos","Nuevo libro","Buscar por título","Libros por precio máximo","Tiendas"])

# Contenido de las pestañas 
with tab_todos:
    st.title("Listado de libros")
    st.table(lista_libros)
    
with tab_nuevo:
    titulo = st.text_input("Introduce título").capitalize()
    autor = st.text_input("Introduce autor")
    precio = st.number_input("Introduce pecio")
    existe = list(filter(lambda lib:lib["titulo"] == titulo, lista_libros))
    if st.button("Guardar") and titulo and not existe:
        lista_libros.append({"titulo": titulo, "autor": autor, "precio": precio})
        st.success("Libro guardado")

with tab_buscar:
    titulo = st.text_input("Introduce el título del libro a buscar: ").capitalize()
    libs = list(filter(lambda lib:lib["titulo"] == titulo, lista_libros))
    if st.button("Buscar", key = "boton1") and libs:
        st.success(f"Titulo: {libs[0]["titulo"]}, Autor: {libs[0]["autor"]}, Precio: {libs[0]["precio"]}")
    
with tab_precios:
    precio = st.number_input("Introduce un precio")
    libs = list(filter(lambda lib:lib["precio"] <= precio, lista_libros))
    if st.button("Buscar", key = "boton2") and libs:
        st.success(f"Los libros encontrados en el rango de precio")
        st.table(libs)
        
with tab_tienda:
    col_tienda,col_direccion,col_imagen = st.columns(3)
    col_tienda.write("**Nombre tienda**")
    col_direccion.write("**direccion tienda**")
    col_imagen.write("**Foto**")
    tiendas = [
        {"nombre":"tienda 1","direccion":"dir1","foto":"tienda.jpg"},
        {"nombre":"tienda 2","direccion":"dir2","foto":"tienda.jpg"},
        {"nombre":"tienda 3","direccion":"dir3","foto":"tienda.jpg"},
        ]
    for tienda in tiendas:
        col_tienda,col_direccion,col_imagen = st.columns(3)
        col_tienda.write(tienda["nombre"])
        col_direccion.write(tienda["direccion"])
        col_imagen.image(tienda["foto"], width = 70)