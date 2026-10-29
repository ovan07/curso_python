password="admin"
intentos=3
acertado=False

while intentos>0:
    contra=input("Introduce contraseña ")
    if contra==password:
        acertado=True
        break
    else:
        print("Vuelve a intentar!")
        intentos=intentos-1
        
if acertado!=True:
    print("Usuario no válido!")
