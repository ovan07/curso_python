ciudades={}

ciudades["Madrid"]=3200000
ciudades["Getafe"]=100000
ciudades["Alcorcon"]=120000
ciudades["Avila"]=130000

del(ciudades["Avila"])

for k,v in ciudades.items():
    print(f"La ciudad {k} tiene {v} habitantes")
