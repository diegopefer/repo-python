# Reto 25
# Nivel: Fácil
# Reto: CONVERSOR DE TEMPERATURA
# Enunciado: /*
#  * Crea una función que transforme grados Celsius en Fahrenheit
#  * y viceversa.
#  *
#  * - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
#  *   y su unidad ("C" o "F").
#  * - En caso contrario retornará un error.
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge42.kt
# --------------------------------------------------
import re

def conversor_temperatura(grados):
    resultado = re.match(r"^-?\d+(\.\d+)?º[CF]$",grados)
    if resultado:
        dato = resultado.group()
        if dato[-1] == "C":
            return round(float(dato[:-2]) * 9 / 5 +32,2), dato[-1]
        elif dato[-1] == "F":
            return round(float((dato[:-2]) - 32) * 5/9,2),dato[-1]
    else:
        print("El formato del dato de entrada no es correcto")

valor,tipo_grado = conversor_temperatura("25ºC")

if tipo_grado == "C":
    print(f"el resultado en grados Fahrenheit  es: {valor}ºF")
elif tipo_grado == "F":
    print(f"el resultado en grados Celsius es: {valor}ºC")