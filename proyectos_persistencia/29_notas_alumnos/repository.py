import polars as pl

#pl.Config.set_tbl_rows(-1)
#pl.Config.set_tbl_cols(-1)
#pl.Config.set_tbl_width_chars(-1)

df1 = pl.read_csv("alumnos.csv")
df2 = pl.read_csv("notas.csv")

def cursos():
    return tabla_completa()["curso"].unique().sort().to_list()

def asignaturas():
    return tabla_completa()["asignatura"].unique().sort().to_list()

def grupos():
    return tabla_completa()["grupo"].unique().sort().to_list()

def evaluaciones():
    return tabla_completa()["evaluacion"].unique().sort().to_list()

def tabla_completa():
    return df1.join(df2, on="id_alumno", how="inner")

def obtener_datos_filtrados(filtro):
    datos = tabla_completa()
    
    if filtro[0] != "Todos":
        datos = datos.filter(pl.col("curso") == filtro[0]) 
    if filtro[1] != "Todos":
        datos = datos.filter(pl.col("asignatura") == filtro[1])
    if filtro[2] != "Todos":
        datos = datos.filter(pl.col("grupo") == filtro[2])
    if filtro[3] != "Todos":
        datos = datos.filter(pl.col("evaluacion") == filtro[3])
    
    return datos

def tabla_estadistica_asignatura(filtro):
    datos_filtrados = obtener_datos_filtrados(filtro)
    
    return datos_filtrados.group_by("asignatura").agg(
        pl.col("nombre").unique().count().alias("alumnos_evaluados"),
        pl.col("nota").mean().alias("nota_media"),
        pl.col("nota").max().alias("nota_maxima"),
        ((pl.col("nota") >= 5).mean() * 100).round(2).alias("porcentaje_aprobados"),
    ).sort("asignatura").to_dicts()
    
def tabla_rendimiento_alumno(filtro):
    datos_filtrados = obtener_datos_filtrados(filtro)
    
    por_asignatura = datos_filtrados.group_by(["id_alumno", "nombre", "curso", "grupo", "asignatura"]).agg(
        pl.col("nota").mean().alias("media_asignatura")
    )
    
    return por_asignatura.group_by(["id_alumno","nombre","curso","grupo"]).agg(
        pl.col("media_asignatura").mean().round(2).alias("nota_media"),
        pl.col("media_asignatura").count().alias("asignaturas_evaluadas"),
        ((pl.col("media_asignatura") >= 5).sum()).alias("asignaturas_aprobadas")
    ).sort("id_alumno").to_dicts()

def metricas(filtro):
    datos_filtrados = obtener_datos_filtrados(filtro)
    
    return datos_filtrados.select(
        pl.col("nombre").unique().count().alias("alumnos_evaluados"),
        pl.col("nota").mean().round(2).alias("nota_media"),
        pl.col("nota").max().alias("nota_maxima"),
        pl.col("nota").min().alias("nota_minima"),
        ((pl.col("nota") >= 5).mean() * 100).round(2).alias("porcentaje_aprobados"),
        ).to_dict()

def evolucion_evaluaciones(filtro):
    datos_filtrados = obtener_datos_filtrados(filtro)
    
    return datos_filtrados.group_by("evaluacion").agg(
        pl.col("nota").mean().round(2).alias("nota_media"),
        ).to_dicts()