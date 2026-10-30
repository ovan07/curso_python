"""
def sumatoria(x,y,z=0,w=0):
    return x+y+z+w

print(sumatoria(6,5))
print(sumatoria(6,5,4))
print(sumatoria(6,5,4,9))
"""

def sumatoria(*args):
    suma=0
    for n in args:
        suma+=n
    return suma

print(sumatoria(4,1))
print(sumatoria(4,1,9,10,3,8))
