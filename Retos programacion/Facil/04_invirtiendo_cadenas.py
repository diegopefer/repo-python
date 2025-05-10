#  * Reto #4
#  * INVIRTIENDO CADENAS
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"


def invertir_cadena(texto_a_invertir):
    texto_invertido= ""
    for i in range(len(texto_a_invertir)-1,-1,-1):
        texto_invertido += texto_a_invertir[i]
    
    return texto_invertido
        
        

print(invertir_cadena("Hola mundo"))


# Alternativa usando slicing:
def invertir_cadena(texto_a_invertir):
    return texto_a_invertir[::-1]

print(invertir_cadena("Hola mundo"))

# Explicación del slicing:
# texto_a_invertir[::-1] invierte la cadena sin necesidad de usar un bucle. El -1 indica que se tomará la cadena en orden inverso.

