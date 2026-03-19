cant_segundos = int(input("Ingrese una cantidad de segundos:"))

horas = cant_segundos // 3600
resto = cant_segundos % 3600
minutos = resto // 60
segundos = resto % 60

print (f"{cant_segundos} segundos son: {horas}h, {minutos}', {segundos}'' ")
