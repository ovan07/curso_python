import streamlit as st 
import tiendas_repository as repo
import matplotlib.pyplot as plt

tienda, mes = "", ""
imprime_cuadro1,imprime_cuadro2,imprime_grafico = False, False, False
    
def generar_grafico():
    resumen = repo.resumen_facturacion()
    tiendas = resumen["nombre_tienda"]
    facturaciones = resumen["facturacion_total"]
    plt.pie(
        facturaciones,
        labels = tiendas,
        autopct = "%1.1f%%"     # muestra los porcentajes dentro del grafico
    )
    plt.title("Resumen de la facturación")
    return plt
    
with st.sidebar:
    st.subheader("Menú navegación")
    tienda = st.selectbox("**Tiendas**", repo.tiendas(), index = None, placeholder = "Seleccione", key="select1")
    if st.button("Mostrar",key="boton1"):
        imprime_cuadro1 = True
        
    mes = st.selectbox("**Meses**", repo.meses(), index = None, placeholder = "Seleccione", key="select2")
    if st.button("Mostrar",key="boton2"):
        imprime_cuadro2 = True
    
    st.subheader("Gráfico del resumen de la facturación")    
    if st.button("Generar",key="boton3"):
        imprime_grafico = True

if imprime_cuadro1 and tienda:
    st.subheader(f"Datos de la {tienda}")
    st.dataframe(repo.datos_tabla_tienda(tienda))
    
    col_1,col_2,col_3 = st.columns(3)
    col_1.metric("**Total facturación:**", repo.datos_tienda(tienda)["facturacion_total"])
    col_2.metric("**Total de gasto de personal:**", repo.datos_tienda(tienda)["gastos_totales"])
    col_3.metric("**Mes con mayor facturación:**", repo.mes_mayor_facturacion(tienda)[1])
    
if imprime_cuadro2 and mes:
    st.subheader(f"Datos del mes {mes}")
    st.dataframe(repo.datos_tabla_mes(mes))
    
    col_a,col_b,col_c = st.columns(3)
    mayor_gasto_personal = repo.mayor_gasto_personal(mes)
    col_a.metric("**Media de facturación:**", repo.datos_tiendas(mes)["media_facturacion"])
    col_b.metric("**Tienda con mayor gasto personal:**", mayor_gasto_personal[0])
    col_c.metric("**Mayor gasto personal:**", mayor_gasto_personal[1])

if imprime_grafico:
    grafico = generar_grafico()
    st.pyplot(grafico)
