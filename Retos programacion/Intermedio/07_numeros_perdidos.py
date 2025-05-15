# reto 07
# Nivel: Medio
# Reto: LOS NÚMEROS PERDIDOS
# Enunciado: /*
#  * Dado un array de enteros ordenado y sin repetidos,
#  * crea una función que calcule y retorne todos los que faltan entre
#  * el mayor y el menor.
#  * - Lanza un error si el array de entrada no es correcto.
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge34.kt
# --------------------------------------------------



def numeros_perdidos(lista_numeros):
    if lista_numeros != sorted(lista_numeros) or len(lista_numeros) != len(set(lista_numeros)):
        print("La lista es erronea, introduce la correcta")
    else:
        inicio = min(lista_numeros)
        fin = max (lista_numeros)
        
        numeros_faltantes = [num_faltante for num_faltante in range(inicio,fin+1) if num_faltante not in lista_numeros]
        
        return numeros_faltantes
        
        
    
    
print(f"Los numeros faltantes son: {numeros_perdidos([1,2,3,7])}")