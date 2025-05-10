# *
#  * Reto #2
#  * ¿ES UN ANAGRAMA?
#  * Dificultad: MEDIA
#  * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
#  * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#  * NO hace falta comprobar que ambas palabras existan.
#  * Dos palabras exactamente iguales no son anagrama.




def es_anagrama(palabra1,palabra2):
    
    return sorted(palabra1.lower()) == sorted(palabra2.lower())
    
    
    
print(f"¿Es anagrama? {es_anagrama("monja","jamon")}")

