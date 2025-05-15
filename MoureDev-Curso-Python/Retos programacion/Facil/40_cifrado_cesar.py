# reto 40
# Nivel: Fácil
# Reto: CIFRADO CÉSAR
# Enunciado: /*
#  * Crea un programa que realize el cifrado César de un texto y lo imprima.
#  * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
#  *
#  * Te recomiendo que busques información para conocer en profundidad cómo
#  * realizar el cifrado. Esto también forma parte del reto.
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2324%20-%20CIFRADO%20C%C3%89SAR%20%5BF%C3%A1cil%5D/ejercicio.md
# --------------------------------------------------


def cifrado_cesar(texto, desplazamiento):

    # Convierte a minúsculas y elimina todo lo que no sea letra
    texto_simplificado = [letra for letra in texto.lower() if letra.isalpha()]
    
    texto_cesar = ""
    
    for l in texto_simplificado:
        # Calcula la posición de la letra en el alfabeto (0 a 25)
        nuevo_valor = ord(l) - ord('a')
        
        # Aplica el desplazamiento y asegura que siga entre 0 y 25
        nueva_posicion = (nuevo_valor + desplazamiento) % 26
        
        # Convierte de nuevo a letra
        nueva_letra = chr(nueva_posicion + ord('a'))
        
        # Añade la letra al resultado final
        texto_cesar += nueva_letra  # ← cambio aquí, antes estaba al revés

    print(f"Texto cifrado: {texto_cesar}")
    
    
    
def descifrado_cesar(texto, desplazamiento):
    texto_cesar = ""
    
    for l in texto:
        # Calcula la posición de la letra en el alfabeto (0 a 25)
        nuevo_valor = ord(l) - ord('a')
        
        # Aplica el desplazamiento y asegura que siga entre 0 y 25
        nueva_posicion = (nuevo_valor - desplazamiento) % 26
        
        # Convierte de nuevo a letra
        nueva_letra = chr(nueva_posicion + ord('a'))
        
        # Añade la letra al resultado final
        texto_cesar += nueva_letra  # ← cambio aquí, antes estaba al revés

    print(f"Texto descifrado: {texto_cesar}")

texto_cifrado = "Hola que tal"
texto_descifrado = "krodtxhwdo"
desplazamiento = 4

cifrado_cesar(texto_cifrado, desplazamiento)
descifrado_cesar(texto_descifrado, desplazamiento)
