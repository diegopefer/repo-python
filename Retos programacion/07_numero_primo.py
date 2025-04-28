#  * Reto #7
#  * ¿ES UN NÚMERO PRIMO?
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.

def es_primo(numero):
    
    if numero < 2:
        return False
    else:
        for i in range(2,numero,1):
            if numero % i == 0:
                return False
        
        return True