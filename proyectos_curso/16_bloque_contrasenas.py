#solicita la introduccion de una contraseña,
#si es correcta le dice que es un  usuario valido, 
#se le vuelve a pedir asi hasta 3 intentos, 
#Si despues del 3er intento la contraseña es incorrecta le dice que no es un usuario valido

password="admin"
intentos=3
acertado=False

while intentos>0 and acertado==False:
    contra=input("Introduce contraseña ")
    if contra==password:
        acertado=True
    else:
        print("Vuelve a intentar!")
        intentos=intentos-1
if acertado==True:
    print("Usuario válido!")
else:
    print("Usuario no válido!")

"""
clave=123
cont=0
acertado=False
intentos=3
valor=int(input("Introduce la contraseña: "))
while valor!=clave:
    cont+=1
    if cont==3:
        print("No es usuario valido \n")
    else:
        print("Contraseña incorrecta \n")
    valor=int(input("Vuelve a introduir la contrasela: "))

print("Usuario valido \n")
"""