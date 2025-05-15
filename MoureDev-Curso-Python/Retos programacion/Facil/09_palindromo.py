#  * Reto #09
#  * ¿ES UN PALÍNDROMO?
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
#  * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
#  * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#  * Ejemplo: Ana lleva al oso la avellana.

import string

def es_palindromo(texto):
    texto_limpio = ''.join(char for char in texto.lower() if char.isalnum()) #solo letras y numeros
    
    
    if texto_limpio == texto_limpio[::-1]:
        return "es palindromo"
    else:
        return False
    

print(es_palindromo("Ana lleva al oso la avellana."))