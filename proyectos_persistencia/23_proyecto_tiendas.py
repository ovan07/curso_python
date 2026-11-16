import pandas as pd

df = pd.read_csv("ventas_tiendas.csv", encoding = "UTF-8")

# tienda mas antigua
tienda_antigua = df.sort_values(by="año_apertura", ascending=True).iloc[0].to_dict()
print(f"La tienda más antigua: {tienda_antigua["nombre_tienda"]}")

# el mayor gasto personal de empresas
df_grupo = df.groupby("nombre_tienda").agg(gastos_personal=("gastos_personal", "sum"))
print(f"Mayor gasto personal: {df_grupo["gastos_personal"].max()}")

tienda = input("Introduce el nombre de la tienda: ")
dfquery = df.query("nombre_tienda == @tienda")
# ventas totales de la tienda
print(f"Ventas total: {dfquery["facturacion"].sum()}")

# mes con mayor facturacion de la tienda (ordenado por 'facturacion', primer elemento, pasado a diccionario)
mes_mas_facturado = dfquery.sort_values(by="facturacion", ascending=False).iloc[0].to_dict()
print(f"El mes con mayor facturacion: {mes_mas_facturado["mes"]}")