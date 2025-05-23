

from datetime import datetime

mes=9
dia = 10

hoy = datetime.today()
fecha_cumpleaños= datetime(hoy.year,mes,dia)

if fecha_cumpleaños < hoy:
    fecha_cumpleaños = fecha_cumpleaños.replace(year=hoy.year+1)

dias_restantes = (fecha_cumpleaños-hoy).days

print(f"Para mi cumpleaños faltan: {dias_restantes} días")