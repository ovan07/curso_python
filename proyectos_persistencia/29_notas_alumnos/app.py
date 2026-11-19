import streamlit as st 
import repository as repo
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Análisis académico",
    page_icon="📊",
    layout="wide",
)

def grafico_barras(x, y, title, xlabel, ylabel):
    fig, ax = plt.subplots()
    ax.bar(x, y)
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_ylim(0, 10)
    ax.grid(axis = "y")
    
    st.pyplot(fig)
    plt.close(fig)

def grafico_lineas(x, y, title, xlabel, ylabel):
    fig, ax = plt.subplots()
    ax.plot(x, y, marker="o", linewidth = 2.0)
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_ylim(0, 10)
    ax.grid()
    
    st.pyplot(fig)
    plt.close(fig)
 
def grafico_histograma(nota, title, xlabel, ylabel):
    fig, ax = plt.subplots()
    ax.hist(nota, bins = 10, range = (0, 10), edgecolor = "black")
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(range(0, 11))
    
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
estadistica_asignatura = repo.tabla_estadistica_asignatura([curso,asignatura,grupo,evaluacion])
rendimiento_alumno = repo.tabla_rendimiento_alumno([curso,asignatura,grupo,evaluacion])
metricas = repo.metricas([curso,asignatura,grupo,evaluacion])

col_1,col_2,col_3,col_4,col_5 = st.columns(5)
col_1.metric("Alumnos evaluados", metricas["alumnos_evaluados"])
col_2.metric("Nota media", metricas["nota_media"])
col_3.metric("Nota máxima", metricas["nota_maxima"])
col_4.metric("Nota mínima", metricas["nota_minima"])
col_5.metric("Aprobados", f"{metricas["porcentaje_aprobados"][0]} %")

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
    estadistica_asignatura = repo.tabla_estadistica_asignatura([curso,asignatura,grupo,evaluacion])
    y = [d["nota_media"] for d in estadistica_asignatura]
    x = [d["asignatura"] for d in estadistica_asignatura]

    grafico_barras(
        x,
        y,
        "Nota media por asignatura",
        "Asignatura",
        "Nota media"
    )

with tab_op2:
    rendimiento_alumno = repo.evolucion_evaluaciones([curso,asignatura,grupo,evaluacion])
    y2 = [d["nota_media"] for d in rendimiento_alumno]
    x2 = [d["evaluacion"] for d in rendimiento_alumno]

    grafico_lineas(
        x2,
        y2,
        "Evolución de las notas",
        "Evaluación",
        "Nota media"
    )
    
with tab_op3:
    datos_filtrados = repo.obtener_datos_filtrados([curso,asignatura,grupo,evaluacion]).to_dicts()
    nota = [d["nota"] for d in datos_filtrados]
    
    grafico_histograma(
        nota,
        "Distribución de calificaciones",
        "Nota",
        "Número de calificaciones"
    )