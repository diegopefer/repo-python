# * Reto #21
#  * ORDENA LA LISTA
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que ordene y retorne una matriz de números.
#  * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro adicional
#  *   "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor o de mayor a menor.
#  * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.


def ordena_lista(lista, tipo_orden):
    
    if len(lista) > 0:
        cambios = True
    
        while cambios == True:
            cambios = False
            for i in range(len(lista)-1):
                if tipo_orden.lower() == "asc":
                    if lista[i] > lista[i+1]:
                        temp = lista[i]
                        lista[i]= lista[i+1]
                        lista[i+1] = temp
                        cambios = True
                elif tipo_orden.lower() == "desc":
                    if lista[i] < lista[i+1]:
                        temp = lista[i]
                        lista[i]= lista[i+1]
                        lista[i+1] = temp
                        cambios = True
        
        return lista
    
            
    

print(ordena_lista([2,6,5,8,9],"Asc"))