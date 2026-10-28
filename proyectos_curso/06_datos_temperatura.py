num=int(input("Introduce un numero"))

if num<0:
    print("Mucho frio")
elif num>=0 and num<= 10:
    print("Dia fresco")
elif num>10 and num<40:
    print("Calor")
else:
    print("Indeterminado")