def caracter_infiltrado(cadena1, cadena2):
    # Comprobamos que las cadenas tengan el mismo tamaño
    if len(cadena1) != len(cadena2):
        print("Cadenas de tamaño distinto")
        return  # Terminamos la ejecución si las cadenas no son del mismo tamaño
    
    # Lista para almacenar los caracteres que son diferentes
    char_distintos = []
    
    # Versión 1: Usando zip() para recorrer ambas cadenas al mismo tiempo
    # zip(cadena1, cadena2) combina ambas cadenas en pares de caracteres
    # y recorre esas parejas al mismo tiempo
    # for c1, c2 in zip(cadena1, cadena2):
    #     if c1 != c2:  # Si los caracteres en la misma posición son diferentes
    #         char_distintos.append(c2)  # Agregamos el carácter de la segunda cadena
    # print(f"Diferencias usando zip(): {char_distintos}")
    
    # Versión 2: Usando índices para recorrer las cadenas
    # Usamos range(len(cadena1)) para iterar por las posiciones de las cadenas
    for i in range(len(cadena1)):
        if cadena1[i] != cadena2[i]:  # Si los caracteres en la misma posición son diferentes
            char_distintos.append(cadena2[i])  # Agregamos el carácter de la segunda cadena
    
    # Devolver la lista de caracteres diferentes
    print(f"Diferencias usando índices: {char_distintos}")
    return char_distintos

# Ejemplo de uso
cadena1 = "Me llamo mouredev"
cadena2 = "Me llemo mouredov"

caracter_infiltrado(cadena1, cadena2)