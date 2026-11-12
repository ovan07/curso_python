import streamlit as st 
import empleados_repository as repo

# imprime y rellena la tabla con los datos
def generar_tabla(lista, accion = False):
    col_empleado,col_edad,col_salario,col_departamento = st.columns(4) 
    col_empleado.write("**Empleado**")
    col_edad.write("**Edad**")
    col_salario.write("**Salario**")
    col_departamento.write("**Departamento**")
    for l in lista:
        col_empleado.write(l["empleado"])
        col_edad.write(l["edad"])
        col_salario.write(l["salario"])
        col_departamento.write(l["departamento"])
# tabla simple
def generar_tabla2(lista):
    st.table(lista)
# tabla con bootstrap y filtros por columnas    
def generar_tabla3(lista):
    st.dataframe(lista)

st.header("Gestión de empleados")

# pestañas 
tab_op1, tab_op2 = st.tabs([
    "Alta de empleados",
    "Filtrar empleados"
]) 
# contenido de las pestañas
with tab_op1:
    empleado = st.text_input("Empleado").capitalize()
    edad = st.number_input("Edad", value = 0)
    salario = st.number_input("Salario", value = 0)
    departamento = st.text_input("Departamento")
    boton = st.button("Guardar")
    if boton and empleado:
        existe_empleado = repo.buscar_empleado(empleado)
        if repo.buscar_empleado(empleado):
            st.toast("El empleado ya existe",  icon = "❌")
        else:  
            repo.nuevo_empleado({'empleado': empleado, 'edad': edad, 'salario': salario, 'departamento': departamento})
            st.toast("Empleado guardado", icon = "✅")
    elif boton and not empleado:
        st.toast("Debe introducir un Empleado", icon = "⚠️")

with tab_op2:
    filtro = st.radio("**Filtro por:**", ["Departamento","Rango salarial"], index = None, horizontal = True)
    if filtro == "Departamento":
        departamento = st.selectbox("**Departamento:**", repo.departamentos(), index = None, placeholder = "Seleccione")
        if departamento:
            empleados = repo.empleados_por_departamento(departamento)
            generar_tabla3(empleados)
    elif filtro == "Rango salarial":
        salario_min = st.number_input("Salario mínimo", value = 0)
        salario_max = st.number_input("Salario máximo", value = 0)
        if st.button("Buscar") and salario_min and salario_max:
            empleados = repo.empleados_por_rango(salario_min, salario_max)
            generar_tabla3(empleados)