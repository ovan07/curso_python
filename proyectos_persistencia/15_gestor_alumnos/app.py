import streamlit as st
import operaciones_bd as op

tab_op1, tab_op2, tab_op3, tab_op4 = st.tabs(["Alumnos","Alta de alumno","Busqueda por curso","Busqueda por DNI"]) 

#["dni","nombre","email","curso","nota"]
# todo los alumnos
with tab_op1:
    col_dni,col_nombre,col_email,col_curso,col_nota = st.columns(5)
    
    col_dni.write("**DNI**")
    col_nombre.write("**Nombre**")
    col_email.write("**Email**")
    col_curso.write("**Curso**")
    col_nota.write("**Nota**")

    for a in op.obtener_alumnos():
        col_dni,col_nombre,col_email,col_curso,col_nota = st.columns(5)
        
        col_dni.write(a["dni"])
        col_nombre.write(a["nombre"])
        col_email.write(a["email"])
        col_curso.write(a["curso"])
        col_nota.write(a["nota"])

# alta de alumno
with tab_op2:
    dni = st.text_input("DNI")
    nombre = st.text_input("Nombre")
    email = st.text_input("Email")
    curso = st.text_input("Curso")
    nota = st.number_input("Nota",value = 0)
    existe = list(filter(lambda a:a["dni"] == dni, op.obtener_alumnos()))
    if st.button("Guardar") and dni and not existe:
        op.crear_alumno((dni,nombre,email,curso,nota))
        st.success("Libro guardado")
    elif existe:
        st.error("DNI ya existe")
        
# busqueda por curso
with tab_op3:
    curso = st.text_input("Curso", key = "curso_b")
    alumno = list(filter(lambda a:a["curso"] == curso, op.obtener_alumnos()))
    if st.button("Buscar", key = "boton2") and alumno:
        st.success(f"Titulo: {alumno}")