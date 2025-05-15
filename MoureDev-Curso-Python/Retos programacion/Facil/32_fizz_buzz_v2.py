# RETO 32
# Nivel: Fácil
# Reto: EL FAMOSO "FIZZ BUZZ" (v2)
# Enunciado: /*
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/tree/main/Retos/Reto%20%230%20-%20EL%20FAMOSO%20FIZZ%20BUZZ%20%5BF%C3%A1cil%5D
# --------------------------------------------------

def fizzbuzz_v2():
    
    for i in range(1,101):
        if i%5 == 0 and i%3 ==0:
            print(f"{i} : fizzbuzz")
        elif i%5 == 0:
            print(f"{i} : buzz")
        elif i%3 == 0:
            print(f"{i} : fizz")
        else:
            print(i)
            
fizzbuzz_v2()