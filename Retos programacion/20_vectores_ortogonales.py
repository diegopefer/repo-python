#  * Reto #20
#  * VECTORES ORTOGONALES
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea un programa que determine si dos vectores son ortogonales.
#  * - Los dos array deben tener la misma longitud.
#  * - Cada vector se podría representar como un array. Ejemplo: [1, -2]

def vectores_ortogonales(lista1,lista2):
    
    if len(lista1) == len(lista2):
        producto_punto = 0
        for a,b in zip(lista1,lista2): #recorrer 2 listas a la vez, devuelve una tupla, no un indice
            producto_punto += a * b
            
        print(producto_punto)
    
vectores_ortogonales([1,2,3],[3,4,6])