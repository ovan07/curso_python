cursos=[
    {"denominacion":"Python y datos","horario":"mañana","fecha_fin":"10/03/2026"},
    {"denominacion":"Inglés científico","horario":"mañana","fecha_fin":"22/07/2026"},
    {"denominacion":"Spring e hibernate","horario":"tarde","fecha_fin":"04/12/2025"},
    {"denominacion":"Programador cerficado","horario":"festivos","fecha_fin":"30/09/2025"}  
]

# se pide al usuario que introduzca horario y le mostremos
# los nombre de los cursos con ese horario

horario=input(f"Introduzca un horario: ")

#horario_encontrado=list(filter(lambda c:c["horario"]==horario, cursos))
horario_encontrado=list(map(lambda l:l["denominacion"], filter(lambda c:c["horario"]==horario, cursos)))

print(horario_encontrado)