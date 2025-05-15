#  * Reto #17
#  * CONJUNTOS
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
#  * - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
#  * - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
#  * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.



def conjuntos(lista1,lista2,es_comun):
    
    lista_resultado = []
    if es_comun:
        for i in lista1:
            if i in lista2 and i not in lista_resultado:
                lista_resultado.append(i)

        return lista_resultado
    else:
        for i in lista1:
            if i not in lista2 and i not in lista_resultado:
                lista_resultado.append(i)
        
        for j in lista2:
            if j not in lista1 and j not in lista_resultado:
                lista_resultado.append(j)
        
        return lista_resultado
    
    
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
    
print(conjuntos(lista1,lista2,False))