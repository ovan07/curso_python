import polars as pl

df = pl.scan_csv("ventas_tiendas.csv")

tienda = input("Introduce el nombre de la tienda: ")
df_filter = df.filter(pl.col("nombre_tienda") == tienda)
# ventas totales de la tienda
ventas_totales = df_filter.select("facturacion").sum().collect().row(0)[0]
print(f"Tienda: {tienda}, Ventas total: {ventas_totales}")

# mes con mayor facturacion de la tienda (ordenado por 'facturacion', primer elemento, pasado a diccionario)
mes_mas_facturado = df_filter.sort(by="facturacion", descending=True).select("mes").collect().row(0)[0]
print(f"Tienda: {tienda}, El mes con mayor facturacion: {mes_mas_facturado}")

# el mayor gasto personal de empresas
gastos_empresas = df.group_by("nombre_tienda").agg(
    pl.col("gastos_personal")
    .sum()
    .alias("gastos personal")
).max().collect().row(0)
print(f"Mayor gasto personal: {gastos_empresas[0]} y cantidad: {gastos_empresas[1]}")

# tienda mas antigua
tienda_antigua = df.sort("año_apertura", descending=False).select("nombre_tienda").collect().row(0)[0]
print(f"La tienda más antigua:, {tienda_antigua}")
