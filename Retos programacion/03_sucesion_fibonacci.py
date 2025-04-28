#  * Reto #3
#  * LA SUCESIÓN DE FIBONACCI
#  * Dificultad: DIFÍCIL
#  *
#  * Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
#  * La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
#  * 0, 1, 1, 2, 3, 5, 8, 13...


def fibonacci():
    lista_fibonacci = [0,1]
    previo = 1
    anterior_previo = 0
    
    for i in range(1,49):
        suma_fibonacci = anterior_previo + previo
        anterior_previo = previo
        previo = suma_fibonacci
        lista_fibonacci.append(suma_fibonacci)
        
        
        
    print(lista_fibonacci)
        

fibonacci()