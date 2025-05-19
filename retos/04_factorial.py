"""
FACTORIAL
Crea una función que calcule
el factorial de un número.
"""


def factorial(numero):
    
    if numero < 0:
        raise ValueError("El numero debe ser entero positivo")
    
    if numero in [0,1]:
        return 1

    resultado = 1
    
    for i in range(numero,0,-1):
        resultado *= i
        print(i,end = "")
        if i != 1:
            print(" * ",end = "")
    
    return resultado

num = 7

resultado_factorial = factorial(num)

print(f"\nEl factorial de {num} es: {resultado_factorial}")