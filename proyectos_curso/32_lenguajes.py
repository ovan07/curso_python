cursos="Java basico, Python principiantes, C, Java avanzado, Java enterprise, Python web, Cobol"

# solicitamos al usuario que introduzca un lenguaje y le mostramos
# todo los cursos relacionados con ese lenguaje

cursos_lista=cursos.split(",")
cursos_encontrados=[]

lenguaje=input("Introduzca tu lenguaje: ").capitalize()

for curso in cursos_lista:
    if lenguaje in curso.split():
        cursos_encontrados.append(curso)

if cursos_encontrados!=[]:
    print(f"los cursos relacionados a {lenguaje} son {cursos_encontrados}")
else:
    print(f"no tenemos cursos relacionados a {lenguaje}")