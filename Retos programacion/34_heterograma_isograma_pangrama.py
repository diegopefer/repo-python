# RETO 34
# Nivel: Fácil
# Reto: HETEROGRAMA, ISOGRAMA Y PANGRAMA
# Enunciado: /*
#  * Crea 3 funciones, cada una encargada de detectar si una cadena de
#  * texto es un heterograma, un isograma o un pangrama.
#  * - Debes buscar la definición de cada uno de estos términos.
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%239%20-%20HETEROGRAMA%2C%20ISOGRAMA%20Y%20PANGRAMA%20%5BF%C3%A1cil%5D/ejercicio.md
# --------------------------------------------------

# 🔹 Heterograma
# Pista: Un heterograma es una palabra o frase que no repite ninguna letra.
# 👉 Convierte el texto a minúsculas, elimina espacios y signos, y revisa si todas las letras son únicas.
# 🔍 Puedes usar un set y comparar su longitud con la del texto filtrado.

# 🔹 Isograma
# Pista: Un isograma es una palabra o frase donde cada letra aparece el mismo número de veces.
# 👉 Cuenta las apariciones de cada letra (ignorando espacios y signos), y comprueba si todos los valores del contador son iguales.
# 📊 Usa collections.Counter.

# 🔹 Pangrama
# Pista: Un pangrama es una frase que contiene todas las letras del alfabeto al menos una vez.
# 👉 Convierte a minúsculas y verifica si el conjunto de letras contiene las 26 letras del abecedario.
# 📘 Puedes usar set(texto) y compararlo con set("abcdefghijklmnopqrstuvwxyz").

from collections import Counter

def heterograma(texto):
    texto_filtrado = "".join(char for char in texto.lower() if char.isalpha())
    texto_set = set(texto_filtrado)
    es_heterograma = len(texto_filtrado) == len(texto_set)
    print(f"¿Es heterograma?: {es_heterograma}")
    return es_heterograma

def isograma(texto):
    texto_filtrado= "".join(char for char in texto.lower() if char.isalpha())
    contador_dict = Counter(texto_filtrado)
    
    
    # Obtenemos las frecuencias de cada letra
    values_char = list(contador_dict.values())
    
    # Verificamos si todos los valores son iguales
    es_isograma = all(f == values_char[0] for f in values_char)
    
    print(f"¿Es isograma?: {es_isograma}")
    return es_isograma

def pangrama(texto):

   set_abecedario  = set("abcdefghijklmnopqrstuvwxyz")
   texto_filtrado = "".join(char for char in texto.lower() if char.isalpha())
   set_filtrado = set(texto_filtrado)
   
   es_pangrama = set_abecedario <= set_filtrado
   
   print(f"¿Es pangrama?: {es_pangrama}")
   return es_pangrama
   
   print(set_abecedario)
   

    
# heterograma("con sed vulpixi")
# isograma("con sed vulpixi")
pangrama("acb")
    