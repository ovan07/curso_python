#pregunta al usuario que lenguaje quiere aprender, y el programa
#le indicara si existe un curso para ese lenguaje o no

cursos=["Java","Python","Typescript","C","Dart"]
existe=False

lenguaje=input("Que lenguaje quiere aprender?: ").capitalize()
"""
for curso in cursos:
    if curso==lenguaje:
        existe=True
        break

if existe:
    print(f"hay un curso para {lenguaje}")
else:
    print(f"No hay ningun curso para {lenguaje}")
"""

if lenguaje in cursos:
    print(f"hay un curso para {lenguaje}")
else:
    print(f"No hay ningun curso para {lenguaje}")