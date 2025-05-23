# Numeros de vocales para cada palabra



def contar_vocales(lista_palabras):
    contador_vocales = 0
    
    return [sum(1 for char in palabra if char in "aeiouAEIOU") for palabra in lista_palabras]


print(contar_vocales(lista_palabras=["entrevista","python","juego","gamer"]))