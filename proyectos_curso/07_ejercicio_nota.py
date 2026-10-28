#lee la nota de un alumno y dependiendo del numero (0 - 10)
#le indca si es suspenso (menos de 5), aprobado (5 o 6)
#notable (7 o 8) o sobresaliente (9 o 10)

nota=int(input("Introduce la nota:"))

match nota:
    case 0 | 1 | 2 | 3 | 4:
        print("suspenso")
    case 5 | 6 | 7:
        print("aprobado")
    case 9 | 10:
        print("sobresaliente")
    case _:
        print("nota no valida")