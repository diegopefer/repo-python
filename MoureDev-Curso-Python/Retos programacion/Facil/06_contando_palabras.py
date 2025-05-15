#  * Reto #6
#  * CONTANDO PALABRAS
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
import re

def contar_palabras(texto):
    
    diccionario_palabras = {}
    texto_sin_puntuacion =re.sub(r'[^\w\s]','',texto)
    
    lista_palabras= texto_sin_puntuacion.lower().split(' ')
    
    for palabra in lista_palabras:
        if palabra in diccionario_palabras:
            diccionario_palabras[palabra] +=1
        else:
            diccionario_palabras[palabra] = 1
    
    print(diccionario_palabras)
    

contar_palabras("hola, soy diego, feliz navidul Diego!!")