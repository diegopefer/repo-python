# reto 04

# Nivel: Medio
# Reto: PARANDO EL TIEMPO
# Enunciado: /*
#  * Crea una función que sume 2 números y retorne su resultado pasados
#  * unos segundos.
#  * - Recibirá por parámetros los 2 números a sumar y los segundos que
#  *   debe tardar en finalizar su ejecución.
#  * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
#  *   asíncrona, es decir, sin detener la ejecución del programa principal.
#  *   Se podría ejecutar varias veces al mismo tiempo.
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge20.kt
# --------------------------------------------------

import asyncio
import threading
import time

async def suma_numeros_asincrono(num1,num2,segundos):
    
    print(f"Suma los numeros {num1} y {num2} con una espera de {segundos} segundos")
    await asyncio.sleep(segundos)
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
    return resultado

print(asyncio.run(suma_numeros_asincrono(2,3,5)))


def suma_numeros_threads(num1,num2,segundos):
    print(f"Suma los numeros {num1} y {num2} con una espera de {segundos} segundos")
    time.sleep(segundos)
    
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
    return resultado

hilo = threading.Thread(target=suma_numeros_threads,args=(2,3,5))
hilo.start()
    