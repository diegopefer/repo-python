# RETO 26
# Nivel: Fácil
# Reto: BUMERANES
# Enunciado: /*
#  * Crea una función que retorne el número total de bumeranes de
#  * un array de números enteros e imprima cada uno de ellos.
#  * - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números
#  *   seguidos, en el que el primero y el último son iguales, y el segundo
#  *   es diferente. Por ejemplo [2, 1, 2].
#  * - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2]
#  *   y [4, 2, 4]).
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge44.kt
# --------------------------------------------------


def bumeranes(lista_numeros):
    
    lista_bumeranes = []
    
    for i in range(len(lista_numeros)-2):
        if lista_numeros[i] == lista_numeros[i+2] and  lista_numeros[i] != lista_numeros[i+1]:
            lista_bumeranes.append([lista_numeros[i],lista_numeros[i+1],lista_numeros[i+2]])
        
    if len(lista_bumeranes) == 0:
        print("No hay bumeranes en la lista")
    else:
        print("numero de bumeranes: " + str(len(lista_bumeranes)))
        print(lista_bumeranes)
    
bumeranes([2, 1, 2, 3, 3, 4, 2, 4])