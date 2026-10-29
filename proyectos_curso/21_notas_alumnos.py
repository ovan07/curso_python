notas_alumnos=[6.4,2.9,5.5,8.0,3.1,7.2]

#indica cuantos alumnos han aprobado
contador=0
for nota in notas_alumnos:
    if nota>=5:
        #print(f"Nota aprobada: {nota}")
        contador+=1
        
print(f"La cantidad de alunnos aprobados son de: {contador}")

#indica la nota mas alta
nota_alta=0
for nota in notas_alumnos:
    if nota>nota_alta:
        nota_alta=nota
        
print(f"La nota mas alta es: {nota_alta}")

#Alternativa con funcion max(lista)
#print(f"La nota mas alta es: {max(notas_alumnos)}")

#ordenar lista sorted() 
print(f"Lista ordenada: {sorted(notas_alumnos,reverse=True)}")
