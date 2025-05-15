# reto 39
# Nivel: Fácil
# Reto: OCTAL Y HEXADECIMAL
# Enunciado: /*
#  * Crea una función que reciba un número decimal y lo trasforme a Octal
#  * y Hexadecimal.
#  * - No está permitido usar funciones propias del lenguaje de programación que
#  * realicen esas operaciones directamente.
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2314%20-%20OCTAL%20Y%20HEXADECIMAL%20%5BF%C3%A1cil%5D/ejercicio.md
# --------------------------------------------------

def convertir_a_octal(numero_decimal):
    original = numero_decimal
    resto = 0
    cociente = 1
    octal_numero = ""
    
    if numero_decimal == 0:  # Caso especial para 0
        print(f"El número decimal 0 en octal es: 0")
        return
    
    while cociente != 0:
        resto = numero_decimal % 8
        cociente = numero_decimal // 8
        octal_numero = str(resto) + octal_numero
        
        numero_decimal = cociente
    print(f"numero decimal {original} en octal es: {octal_numero}")
    
def convertir_a_hexadecimal(numero_decimal):
    digitos_hex = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
    }
    
    
    if numero_decimal == 0:  # Caso especial para 0
        print(f"El número decimal 0 en hexadecimal es: 0")
        return
    
    original = numero_decimal
    resto = 0
    cociente = 1
    hexadecimal_numero = ""
    
    while cociente != 0:
        resto = numero_decimal % 16
        cociente = numero_decimal // 16
        
        if resto >= 10:
            resto = digitos_hex[resto]
        
        hexadecimal_numero = str(resto) + hexadecimal_numero
        
        numero_decimal = cociente
        
    print(f"numero decimal {original} en hexadecimal es: {hexadecimal_numero}")
    

numero_decimal = 128

convertir_a_octal(numero_decimal)
convertir_a_hexadecimal(numero_decimal)