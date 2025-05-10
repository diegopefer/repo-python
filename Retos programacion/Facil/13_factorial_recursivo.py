#  * Reto #13
#  * FACTORIAL RECURSIVO
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.

def factorial_recursivo(num):
    if num <=1:
        return 1
    else:
        return num * factorial_recursivo(num-1)
    
    
print(factorial_recursivo(4))