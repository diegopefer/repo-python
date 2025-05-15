# --------------------------------------------------
# RETO 36
# Nivel: Fácil
# Reto: VIERNES 13
# Enunciado: /*
#  * Crea una función que sea capaz de detectar si existe un viernes 13
#  * en el mes y el año indicados.
#  * - La función recibirá el mes y el año y retornará verdadero o falso.
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2312%20-%20VIERNES%2013%20%5BF%C3%A1cil%5D/ejercicio.md
import datetime

def buscar_viernes_13(mes,anho):
    try:
        dia = datetime.date(anho,mes,13)
        if dia.weekday() == 4:
            return True
    except ValueError:
        return False
    

print(buscar_viernes_13(6,2025))