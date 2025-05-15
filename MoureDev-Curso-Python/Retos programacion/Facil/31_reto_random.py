
# RETO31
# Nivel: Fácil
# Reto: EL RETO RANDOM
# Enunciado: /*
#  * Crea tu propio enunciado para que forme parte de los retos de 2023.
#  * - Ten en cuenta que su dificultad debe ser asumible por la comunidad y seguir
#  * un estilosemejante a los que hemos realizado durante el año.
#  * - Si quieres también puedes proponer tu propia solución al reto
#  *   (en el lenguaje que quieras).
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge51.kt
# --------------------------------------------------
# Reto: Cadena Palíndroma
# Crea una función que reciba una cadena de texto y determine si es un palíndromo.
# Un palíndromo es una palabra o secuencia que se lee igual hacia adelante y hacia atrás,
# ignorando mayúsculas, minúsculas, espacios y signos de puntuación.
# La función debe devolver si la cadena es un palíndromo o no.
# Ejemplos:
# Entrada: "A man, a plan, a canal, Panama" -> Salida: "Es un palíndromo"
# Entrada: "Hello, World!" -> Salida: "No es un palíndromo"



def cadena_palindroma(texto):
    
    if len(texto) > 0:
    
        texto_limpio = "".join(char for char in texto.lower() if char.isalnum())
        print(texto_limpio)
        
        palindromo = texto_limpio == texto_limpio[::-1]
        return palindromo
    else:
        return False
    

print(cadena_palindroma("A man, a plan, a canal, Panama"))