import json

dir_fichero = "countries.json"

def continentes():
    with open(dir_fichero,"r") as f:
        return list(set(map(lambda p:p["region"], json.load(f))))
    
def paises():
    with open(dir_fichero,"r") as f:
        return json.load(f)
    
