import datetime as dt

print(f"Fecha de hoy: {dt.date.today()}")
print(f"Hora actual: {dt.datetime.now()}")
f_posterior=dt.datetime.now()+dt.timedelta(days=20,hours=60)

print(f_posterior)

fechahora_actual=dt.datetime.now()
print(f"La fecha y hora actuales {dt.datetime.strftime(fechahora_actual,"%d/%m/%Y - %H:%M")}") 

fecha1="10/11/2003"
fecha2="25/04/2002"
fecha1=dt.datetime.strptime(fecha1,"%d/%m/%Y")
fecha2=dt.datetime.strptime(fecha2,"%d/%m/%Y")

if fecha1<fecha2:
    print(f"la mas antigua es {fecha1}")
else:
    print(f"la mas antigua es {fecha2}")
