import polars as pl

# ¿porque polars? 
# 1.- estilos y metodos mas modernos 
# 2.- mas eficiente 

datos = [ 
    {"nombre": "Ana", "edad": 25, "salario": 25000, "departamento": "ventas"}, 
    {"nombre": "Luis", "edad": 32, "salario": 32000, "departamento": "informatica"}, 
    {"nombre": "Marta", "edad": 28, "salario": 28000, "departamento": "informatica"}, 
    {"nombre": "Pedro", "edad": 41, "salario": 41000, "departamento": "ventas"} 
] 
df = pl.DataFrame(datos) 
print(df)

# acceso a filas y columnas
print(df["edad"].to_list())     # columna en lista de valores
print(df.row(0,named=True))     # diccionario con los datos de la fila
print(df.to_dicts())            # convierte todo el dataframe en una lista de diccionarios

# filtrado
print(df.filter(pl.col("salario")>30000))
print(df.filter((pl.col("salario")>30000) & (pl.col("edad")<50)))

# ordenacion
print(df.sort(by="edad", descending=False))
print(df.sort("salario", descending=True).row(0)[0])    # imprime la 1ra fila y la 1ra columna

# funciones para calculos: min(), max(), mean(), count(), unique()
print("salario mas alto ", df["salario"].max())
print("salario mas bajo ", df["salario"].min())

# seleccion
result = df.select(
    pl.col("salario").mean().alias("salario medio"),
    pl.col("edad").mean().alias("edad medio")
)
print(result)

# muestra la lista sin duplicados
departamentos = df["departamento"].unique().to_list()
print(departamentos)

# agrupacion
print(df.group_by("departamento").agg(
    pl.col("salario").mean().alias("salario medio"),
    pl.col("nombre").count().alias("total empleados")
))

# recorrido de un dataframe
for element in df.iter_rows():  # como tuplas
    print(element)
    
for element in df.iter_rows(named=True):    # como diccionario
    print(element)
    
