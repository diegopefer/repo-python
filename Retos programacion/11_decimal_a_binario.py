#  * Reto #11
#  * DECIMAL A BINARIO
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.


def decimal_a_binario(num):
    bits = ""
    
    while num  > 0:
        resto = num % 2
        bits = str(resto) + bits 
        
        num = num // 2
        
    print(bits)
    
decimal_a_binario(13)