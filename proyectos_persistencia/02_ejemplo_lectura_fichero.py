#leer el contenido de un fichero
#op1
"""
f=open("dias.txt","r")
linea=f.readline()
while linea!="":
    print(linea)
    linea=f.readline()
f.close()
"""
#op2
"""
with open("dias.txt","r") as f:
    linea=f.readline()
    while linea!="":
        print(linea)
        linea=f.readline()
"""  
#op3
with open("dias.txt","r") as f:
    lista_dias=f.readlines()
print(lista_dias)
#lista_limpia=[ld.strip() for ld in lista_dias]
lista_limpia=list(map(lambda ld:ld.strip(),lista_dias))
print(lista_limpia)

#quitar los espacios y simbolos a la izquierda y derecha del texto
texto=" aaa   \n\t"
texto_limpio=texto.strip()
print(texto_limpio)