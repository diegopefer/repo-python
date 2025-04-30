# * Reto #22
# Nivel: Fácil
# Reto: MARCO DE PALABRAS
# Enunciado: /*
#  * Crea una función que reciba un texto y muestre cada palabra en una línea,
#  * formando un marco rectangular de asteriscos.
#  * - ¿Qué te parece el reto? Se vería así:
#  *   **********
#  *   * ¿Qué   *
#  *   * te     *
#  *   * parece *
#  *   * el     *
#  *   * reto?  *
#  *   **********
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge30.kt


def marco_palabras(texto):
    
    texto_dividido = texto.split(" ")
    tamanho_maximo = 0
    
    for i in texto_dividido:
        if len(i) > tamanho_maximo:
            tamanho_maximo = len(i)
        
    print("*" * (tamanho_maximo +4))
    
    for i in texto_dividido:
        print("* "+ i + " "* (tamanho_maximo - len(i)) +" *")
        
    print("*" * (tamanho_maximo +4))

    
    return texto_dividido
    
    
print(marco_palabras("Hola mi nombre es Diego"))