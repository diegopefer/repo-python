#  * Reto #15
#  * EN MAYÚSCULA
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
#  * poner en mayúscula la primera letra de cada palabra.
#  * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

def en_mayuscula(texto):
    lista_palabras = texto.split(" ")
    palabras_mayuscula = []
    for palabra in lista_palabras:
        palabras_mayuscula.append(palabra[0].upper()+palabra[1::].lower())
                
    
    print(' '.join(palabras_mayuscula))
    
    
en_mayuscula("Hola soy patxi feliz navidad, te deseo lo mejor")