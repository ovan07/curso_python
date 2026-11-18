import streamlit as st 
import repository as repo
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Análisis académico",
    page_icon="📊",
    layout="wide",
)

def grafico_barras(x,y,title,xlabel,ylabel, lminite_y = 10):
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.axhline(y=lminite_y, linestyle='')
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)
    plt.close(fig)

def grafico_lineas(x2,y2,title,xlabel,ylabel):
    fig, ax = plt.subplots()
    ax.plot(x2, y2, marker="o")
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)
    plt.close(fig)
    
#------------------ Barra lateral ------------------#
with st.sidebar:
    st.title("**Filtros**")
    curso = st.selectbox("Curso", ["Todos"] + repo.cursos(), key="select1")
    asignatura = st.selectbox("Asignatura", ["Todos"] + repo.asignaturas(), key="select2")
    grupo = st.selectbox("Grupo", ["Todos"] + repo.grupos(), key="select3")
    evaluacion = st.selectbox("Evaluación", ["Todos"] + repo.evaluaciones(), key="select4")

st.title("**📊 Dashboard de rendimiento académico**")

#------------------ 1er segmento ------------------#
estadistica_asignatura = repo.tabla_estadistica_asignatura()
rendimiento_alumno = repo.tabla_rendimiento_alumno()
metricas = repo.metricas()

col_1,col_2,col_3,col_4,col_5 = st.columns(5)
col_1.metric("Alumnos evaluados", metricas["alumnos_evaluados"])
col_2.metric("Nota media", metricas["nota_media"])
col_3.metric("Nota máxima", metricas["nota_maxima"])
col_4.metric(" Nota mínima", metricas["nota_minima"])
col_5.metric("Aprobados", metricas["porcentaje_aprobados"])

#------------------ 2do segmento ------------------#
st.subheader("**Estadísticas por asignatura**")
st.dataframe(estadistica_asignatura)

#------------------ 3er segmento ------------------#
st.subheader("**Rendimiento por alumno**")
st.dataframe(rendimiento_alumno)

#------------------ 4to segmento ------------------#
# pestañas 
tab_op1, tab_op2, tab_op3 = st.tabs([
    "Notas por asignatura",
    "Evolución de evaluaciones",
    "Distribución de notas"
]) 

with tab_op1:
    estadistica_asignatura = repo.tabla_estadistica_asignatura()
    y = [d["nota_media"] for d in estadistica_asignatura]
    x = [d["asignatura"] for d in estadistica_asignatura]

    grafico_barras(
        x,
        y,
        "Nota media por asignatura",
        "Asignatura",
        "Nota media"
    )
    #st.pyplot(grafico)

with tab_op2:
    rendimiento_alumno = repo.evolucion_evaluaciones()
    y2 = [d["nota_media"] for d in rendimiento_alumno]
    x2 = [d["evaluacion"] for d in rendimiento_alumno]

    grafico_lineas(
        x2,
        y2,
        "Evolución de las notas",
        "Evaluación",
        "Nota media"
    )
    
