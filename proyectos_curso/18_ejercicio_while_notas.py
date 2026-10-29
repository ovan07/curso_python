#solicite una nota, despues otra, y asi sucesiamnete hasta introducir un cero
#en es momento, no pedirá mas notas y mostrara la nota media de las introducidas
#hasta el momento

parar=False
contador=0
sumatoria=0
promedio=0

while parar!=True:
    nota=int(input("introduce una nota: "))
    sumatoria+=nota
    
    if nota==0:
        parar=True
    else:
        contador+=1
    
if contador!=0:
    promedio=sumatoria/contador
    print(f"El promedio de {contador} notas introducidas es: {promedio}")
