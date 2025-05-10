# RETO 28
# Nivel: Fácil
# Reto: EL CALENDARIO DE ADEVIENTO 2022
# Enunciado: /*
#  * ¿Conoces el calendario de adviento de la comunidad (https://adviento.dev)?
#  * 24 días, 24 regalos sorpresa relacionados con desarrollo de software,
#  * ciencia y tecnología desde el 1 de diciembre.
#  *
#  * Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne
#  * lo siguiente:
#  * - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo
#  *   de ese día (a tu elección) y cuánto queda para que finalice el sorteo de ese día.
#  * - Si la fecha es anterior: Cuánto queda para que comience el calendario.
#  * - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.
#  *
#  * Notas:
#  * - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00
#  *   y finaliza a las 23:59:59.
#  * - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos
#  *   y segundos.
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge48.kt
# --------------------------------------------------

from datetime import datetime,timedelta

def calendario_adviento(fecha):
    fecha_inicio = datetime(2022,12,1,00,00,00)
    fecha_fin = datetime(2022,12,24,23,59,59)
    
    if fecha < fecha_inicio:
        tiempo_restante = fecha_inicio - fecha
        print(f"Queda {tiempo_restante.days} días para el comienzo del calendario")
    elif fecha > fecha_fin:
        tiempo_pasado = fecha - fecha_fin
        print(f"Ha pasado {tiempo_pasado.days} días desde el fin del calendario")
    
    else:
        tiempo_finalizacion = fecha_fin - fecha
        dia = fecha.day
        
        horas_restantes = tiempo_finalizacion.seconds // 3600
        minutos_restantes = (tiempo_finalizacion.seconds % 3600) // 60
        print(f"Hoy es día {dia}. Tu regalo sorpresa del dia  {fecha}.")
        print(f"Falta {tiempo_finalizacion.days} dias {horas_restantes} horas {minutos_restantes} minutos para finalizar el sorteo")
        


fecha = datetime(2022,11,2,11,15,22)
calendario_adviento(fecha)