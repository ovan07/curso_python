import polars as pl

pl.Config.set_tbl_rows(-1)
pl.Config.set_tbl_cols(-1)
pl.Config.set_tbl_width_chars(-1)

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

def tabla_estadistica_asignatura(filtro = True):
    return tabla_completa().filter(filtro).group_by("asignatura").agg(
        pl.col("nombre").unique().count().alias("alumnos_evaluados"),
        pl.col("nota").mean().alias("nota_media"),
        pl.col("nota").max().alias("nota_maxima"),
        ((pl.col("nota") >= 5).mean() * 100).round(2).alias("porcentaje_aprobados"),
    ).sort("asignatura").to_dicts()
    
def tabla_rendimiento_alumno(filtro = True):
    return tabla_completa().filter(filtro).group_by("id_alumno").agg(
        pl.col("nombre").first(),
        pl.col("curso").first(),
        pl.col("grupo").first(),
        pl.col("nota").mean().round(2).alias("nota_media"),
        pl.col("asignatura").unique().count().alias("asignaturas_evaluadas"),
    ).sort("id_alumno").to_dicts()

def alunnos_evaluados(filtro = True):
    return tabla_completa().filter(filtro).select("nombre").unique().count().row(0)[0]
    
def nota_media(filtro = True):
    return tabla_completa().filter(filtro).select("nota").mean().row(0)[0]

def nota_maxima(filtro = True):
    return tabla_completa().filter(filtro).select("nota").max().row(0)[0]

def nota_minima(filtro = True):
    return tabla_completa().filter(filtro).select("nota").min().row(0)[0]

def metricas(filtro = True):
    return tabla_completa().filter(filtro).select(
        pl.col("nombre").unique().count().alias("alumnos_evaluados"),
        pl.col("nota").mean().round(2).alias("nota_media"),
        pl.col("nota").max().alias("nota_maxima"),
        pl.col("nota").min().alias("nota_minima"),
        ((pl.col("nota") >= 5).mean() * 100).round(2).alias("porcentaje_aprobados"),
        ).to_dict()

def evolucion_evaluaciones(filtro = True):
    return tabla_completa().filter(filtro).group_by("evaluacion").agg(
        pl.col("nota").mean().round(2).alias("nota_media"),
        ).to_dicts()
    

print(evolucion_evaluaciones())
