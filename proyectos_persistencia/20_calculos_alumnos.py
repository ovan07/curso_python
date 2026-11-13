import pandas as pd

df = pd.read_json("alumnos.json", encoding = "UTF-8")
#print(df)

# nota media global
print(f"nota media global: {df["nota"].mean():.2f}")

# notas mas alta y total de alumnos de cada curso
grupo_cursos = df.groupby("curso").agg(nota_alta=("nota","max"), total_alumno=("nombre","count"))
print(grupo_cursos)
