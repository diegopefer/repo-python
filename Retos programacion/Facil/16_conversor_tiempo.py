#  * Reto #16
#  * CONVERSOR TIEMPO
#  * Dificultad: FACIL
#  *
#  * Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.

def conversor_tiempo(dias,horas,minutos,segundos):
    
    return (dias*24*60*60*1000) + (horas*60*60*1000) + (minutos*60*1000) +(segundos*1000)


print(f"{conversor_tiempo(3,15,10,59)} milisegundos")