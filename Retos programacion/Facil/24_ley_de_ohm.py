# RETO 24
# Nivel: Fácil
# Reto: LA LEY DE OHM
# Enunciado: /*
#  * Crea una función que calcule el valor del parámetro perdido
#  * correspondiente a la ley de Ohm.
#  * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
#  *   el valor del tercero (redondeado a 2 decimales).
#  * - Si los parámetros son incorrectos o insuficientes, la función retornará
#  *   la cadena de texto "Invalid values".
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge41.kt
# --------------------------------------------------

def ley_ohm(v=None,r=None, i=None):
    
    if (v is None and r is None) or (r is None and i is None) or (v is None and i is None) : 
        return "Invalid values", None
    else:
        if v is None:
            v = r*i
            return "v",round(v,2)
        elif r is None:
            r= v/i
            return "r",round(r,2)
        elif i is None:
            i = v/r
            return "i" , round(i,2)
    

parametro,resultado = ley_ohm(r=2,i=3)

if resultado is not None:
    
    print(f"el resultado de [{parametro}] es {resultado}")
else:
    print(parametro)