try:
    numero = int(input("Introduce un numero: "))
    resultado = 10 / numero
    print(resultado)
    
except ValueError, KeyError:
    print(KeyError)
    print("Debes introducir un numero")
    
except ZeroDivisionError:
    print("No se puede dividir entre cero")
    
finally:
    print("Siempre se ejecuta")