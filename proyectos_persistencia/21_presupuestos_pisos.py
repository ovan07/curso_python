import pandas as pd

df = pd.read_csv("houses.csv", encoding = "UTF-8")
#print(df)

presupuesto = int(input("introduce tu presupuesto: "))
filtro = df.query("price <= @presupuesto").sort_values(by = "price", ascending = False)
print(filtro)