# reto 02
# Nivel: Medio
# Reto: EXPRESIONES EQUILIBRADAS
# Enunciado: /*
#  * Crea un programa que comprueba si los paréntesis, llaves y corchetes
#  * de una expresión están equilibrados.
#  * - Equilibrado significa que estos delimitadores se abren y cieran
#  *   en orden y de forma correcta.
#  * - Paréntesis, llaves y corchetes son igual de prioritarios.
#  *   No hay uno más importante que otro.
#  * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#  * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge10.kt
# --------------------------------------------------

def expresiones_equilibradas(expresion):
    lista_equilibrada = []  # Pila para almacenar los símbolos de apertura
    
    for caracter in expresion:
        if caracter in delimitadores_pares.values():
            lista_equilibrada.append(caracter)  # Añade apertura a la pila
        elif caracter in delimitadores_pares:
            # Si no hay apertura o no coincide con el cierre
            if not lista_equilibrada or lista_equilibrada[-1] != delimitadores_pares[caracter]:
                return False  # Expresión desequilibrada
            lista_equilibrada.pop()  # Elimina apertura emparejada
    
    return not lista_equilibrada  # Devuelve True si la pila está vacía (equilibrado)

delimitadores_pares = {')': '(', ']': '[', '}': '{'}

expresiones_equilibradas("{ [ a * ( c + d ) ] - 5 }")














   # for caracter in expresion:
    #     if caracter in delimitadores_pares.values():
    #         lista_equilibrada.append(caracter)
    #     elif caracter in delimitadores_pares:
    #         if not lista_equilibrada or lista_equilibrada[-1] != delimitadores_pares[caracter]:
    #             return False
    #         lista_equilibrada.pop()
            
    # return not lista_equilibrada
                