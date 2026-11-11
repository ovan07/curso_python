import streamlit as st
import operaciones_bd as op


# imprime y rellena la tabla con los datos de los alumnos
def generar_tabla(lista, accion = False):
    col_dni,col_nombre,col_email,col_curso,col_nota,col_accion = st.columns([2,2,3,2,1,2]) 
    col_dni.write("**DNI**")
    col_nombre.write("**Nombre**")
    col_email.write("**Email**")
    col_curso.write("**Curso**")
    col_nota.write("**Nota**")
    if accion:
        col_accion.write("**Acción**")
    for a in lista:
        col_dni.write(a["dni"])
        col_nombre.write(a["nombre"])
        col_email.write(a["email"])
        col_curso.write(a["curso"])
        col_nota.write(a["nota"])
        if accion and col_accion.button("Eliminar", key=f"remover_{a["dni"]}"):
            op.borrar_alumno(a["dni"])
            st.rerun()

st.subheader("Gestión de alumnos")

# pestañas 
tab_op1, tab_op2, tab_op3, tab_op4 = st.tabs([
    "Alumnos",
    "Alta de alumno",
    "Busqueda por curso",
    "Busqueda por DNI"
]) 

#["dni","nombre","email","curso","nota"]
# todo los alumnos
with tab_op1:
    alumnos = op.buscar_alumnos()
    generar_tabla(alumnos)

# alta de alumno
with tab_op2:
    dni = st.text_input("DNI")
    nombre = st.text_input("Nombre")
    email = st.text_input("Email")
    curso = st.text_input("Curso")
    nota = st.number_input("Nota", value = 0, max_value = 10, min_value = 0)
    existe_alumno = op.buscar_alumno_dni(dni)
    boton = st.button("Guardar")
    if boton and dni and not existe_alumno:
        op.crear_alumno((dni,nombre,email,curso,nota))
        st.success("Alumno guardado")
        st.rerun()
    elif boton and not dni:
        st.warning("Debe introducir un DNI")
    elif existe_alumno:
        st.error("DNI ya existe")
        
# busqueda por curso
with tab_op3:
    lista_cursos = [c["curso"] for c in op.buscar_cursos()]
    curso = st.selectbox("**Curso**", lista_cursos, index = None, placeholder = "Seleccione")
    alumnos = op.buscar_alumno_curso(curso)
    if alumnos:
        generar_tabla(alumnos, True)
        st.success(f"Encontrados: {len(alumnos)}")
    elif curso:
        st.warning(f"No se ha encontrado alumnos del curso '{curso}'")
    
# busqueda por dni
with tab_op4:
    dni = st.text_input("**DNI**", key = "dni_b")
    alumno = op.buscar_alumno_dni(dni)
    boton_busca = st.button("Buscar", key=f"buscar_dni")
    if boton_busca or alumno:
        #generar_tabla(alumno)
        nombre = st.text_input("Nombre", value = alumno["nombre"])
        email = st.text_input("Email", value = alumno["email"])
        curso = st.text_input("Curso", value = alumno["curso"])
        nota = st.number_input("Nota", value = alumno["nota"], max_value = 10, min_value = 0)
        boton_actualizar = st.button("Actualizar", key=f"actualizar_dni")
        if boton_actualizar:
            op.actualizar_alumno((nombre,email,curso,nota,dni))
            st.success(f"Datos actualizados")
    elif dni:
        st.warning(f"No se ha encontrado alumno con DNI: {dni}")
        