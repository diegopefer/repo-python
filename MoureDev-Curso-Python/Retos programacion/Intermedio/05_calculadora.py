# RETO 05
# 

# Nivel: Medio
# Reto: CALCULADORA .TXT
# Enunciado: /*
#  * Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
#  * resultado e imprímelo.
#  * - El .txt se corresponde con las entradas de una calculadora.
#  * - Cada línea tendrá un número o una operación representada por un
#  *   símbolo (alternando ambos).
#  * - Soporta números enteros y decimales.
#  * - Soporta las operaciones suma "+", resta "-", multiplicación "*"
#  *   y división "/".
#  * - El resultado se muestra al finalizar la lectura de la última
#  *   línea (si el .txt es correcto).
#  * - Si el formato del .txt no es correcto, se indicará que no se han
#  *   podido resolver las operaciones.
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge21.kt



with open(r"Retos programacion\Intermedio\Challenge21.txt","r") as file:
    lineas = [linea.strip() for linea in file.readlines()]
    
    try:
        resultado = float(lineas[0])
        
        for i in range(1,len(lineas),2):
            operacion = lineas[i]
            try:
                numero = float(lineas[i+1])
            except IndexError:
                raise ValueError("Falta un número después de una operación.")
            
            if operacion == "+":
                resultado += numero
            elif operacion == "-":
                resultado -= numero
            elif operacion == "*":
                resultado *= numero
            elif operacion == "/":
                resultado /= numero
            else:
                raise ValueError("Operación inválida")
            
        print(f"resultado final: {resultado}")
            
            
    except Exception as e:
        print("no se pudieron resolver las operaciones",e)

