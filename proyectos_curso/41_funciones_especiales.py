#from functools import reduce
import functools as ft
numeros=[1,8,3,-4,9,-2,-11,16]

positivos=list(filter(lambda n:n>0, numeros))
#positivos=[n for n in numeros if n>0]
print(positivos)
#calcula la suma de los cuadrados de todos los numeros
print(ft.reduce(lambda a,b:a+b, map(lambda n:n**2, positivos)))