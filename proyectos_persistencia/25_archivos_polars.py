import polars as pl

df = pl.scan_csv("houses.csv")  # mas eficiente
#print(df)
df_json = pl.scan_ndjson("academia.json")

filtro = df.filter(pl.col("rooms") > 2)
print(filtro.select(pl.col("price").mean()).collect())
    