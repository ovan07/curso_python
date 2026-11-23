import streamlit as st 
import empleados_service as ep

url = "empleados.csv"
e_gestor = ep.Gestor_Empleados(url)

tab_op1, tab_op2, tab_op3 = st.tabs([
    "Nuevo",
    "Buscar",
    "Buscar por departamento"
]) 

with tab_op1:
    nombre = st.text_input("Nombre", key="nom1")
    edad = st.number_input("Edad", value = 0, min_value = 0, max_value = 100)
    salario = st.number_input("Salario", value = 0)
    departamento = st.text_input("Departamento")
    
    existe_emp = e_gestor.buscar_empleado(nombre)
    boton = st.button("Guardar")
    if boton and nombre and not existe_emp:
        empleado = ep.Empleado(nombre,edad,salario,departamento)
        e_gestor.alta_empleado(empleado)
        st.success("Empleado guardado")
        st.rerun()
    elif boton and not nombre:
        st.warning("Debe introducir un Empleado")
    elif existe_emp:
        st.error("El Empleado ya existe")
    
with tab_op2:
    nombre = st.text_input("Nombre", key="nom2")
    
    empelado = e_gestor.buscar_empleado(nombre)
    boton = st.button("Buscar")
    if boton and empelado:
        st.write(f"Nombre: {empelado.nombre}")
        st.write(f"Edad: {empelado.edad}")
        st.write(f"Salario: {empelado.salario}")
        st.write(f"Departamento: {empelado.departamento}")
        
with tab_op3:
    departamento = st.selectbox("Departamento",e_gestor.departamentos(), index = None, placeholder = "Seleccione")
    if departamento:
        empleados = e_gestor.empleado_departamento(departamento)
        datos = [vars(e) for e in empleados]

        st.dataframe(datos)
