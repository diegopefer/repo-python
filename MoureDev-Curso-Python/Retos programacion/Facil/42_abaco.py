# RETO 42
# Nivel: Fácil
# Reto: EL ÁBACO
# Enunciado: /*
#  * Crea una función que sea capaz de leer el número representado por el ábaco.
#  * - El ábaco se representa por un array con 7 elementos.
#  * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar
#  *   operaciones) para las cuentas y una secuencia de "---" para el alambre.
#  * - El primer elemento del array representa los millones, y el último las unidades.
#  * - El número en cada elemento se representa por las cuentas que están a
#  *   la izquierda del alambre.
#  *
#  * Ejemplo de array y resultado:
#  * ["O---OOOOOOOO",
#  *  "OOO---OOOOOO",
#  *  "---OOOOOOOOO",
#  *  "OO---OOOOOOO",
#  *  "OOOOOOO---OO",
#  *  "OOOOOOOOO---",
#  *  "---OOOOOOOOO"]
#  *
#  *  Resultado: 1.302.790
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2331%20-%20EL%20%C3%81BACO%20%5BF%C3%A1cil%5D/ejercicio.md
# --------------------------------------------------



def abaco(array_abaco):
    resultado_numero = ""
    
    for i in array_abaco:
        # Se divide en la parte antes y después del alambre
        division_elemento = i.split("---")
        
        # Añadimos el número de "O"s antes del "---"
        resultado_numero += str(len(division_elemento[0]))
        
    # Al final, imprimimos el número como un valor entero
    print(f"Resultado: {int(resultado_numero)}")

abaco([
    "O---OOOOOOOO",  # 1 millón
    "OOO---OOOOOO",  # 3 centenas de mil
    "---OOOOOOOOO",  # 0 decenas de mil
    "OO---OOOOOOO",  # 2 mil
    "OOOOOOO---OO",  # 7 cientos
    "OOOOOOOOO---",  # 9 decenas
    "---OOOOOOOOO"   # 0 unidades
])
