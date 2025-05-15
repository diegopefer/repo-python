# RETO 08
# Nivel: Medio
# Reto: TOP ALGORITMOS | QUICK SORT
# Enunciado: /*
#  * Implementa uno de los algoritmos de ordenación más famosos:
#  * el "Quick Sort", creado por C.A.R. Hoare.
#  * - Entender el funcionamiento de los algoritmos más utilizados de la historia
#  *   Nos ayuda a mejorar nuestro conocimiento sobre ingeniería de software.
#  *   Dedícale tiempo a entenderlo, no únicamente a copiar su implementación.
#  * - Esta es una nueva serie de retos llamada "TOP ALGORITMOS",
#  *   donde trabajaremos y entenderemos los más famosos de la historia.
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge39.kt

def quicksort(lista_numeros):
    if len(lista_numeros) <= 1:
        return lista_numeros
    else:
        pivote = lista_numeros [0]
        menores = [menor for menor in lista_numeros[1:] if menor < pivote]
        mayores = [mayor for mayor in lista_numeros[1:] if mayor >= pivote]
        
        return quicksort(menores) + [pivote] + quicksort(mayores)


print(quicksort([7,8,4,1,2,3]))