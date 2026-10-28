#1+2+3+4+..... ¿hasta que numero tedremos que llegar
#para que la suma alcance o supere el valor 1000?

num,sumatoria,total=0,0,1000

while sumatoria<total:
    num+=1
    sumatoria+=num
    print(f"sumatoria: {sumatoria}")
    
print(f"el numero que supero la sumatoria {sumatoria} y el numero fue {num}")