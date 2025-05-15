# reto 06
# Nivel: Medio
# Reto: LA CARRERA DE OBSTÁCULOS
# Enunciado: /*
#  * Crea una función que evalúe si un/a atleta ha superado correctamente una
#  * carrera de obstáculos.
#  * - La función recibirá dos parámetros:
#  *      - Un array que sólo puede contener String con las palabras
#  *        "run" o "jump"
#  *      - Un String que represente la pista y sólo puede contener "_" (suelo)
#  *        o "|" (valla)
#  * - La función imprimirá cómo ha finalizado la carrera:
#  *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
#  *        será correcto y no variará el símbolo de esa parte de la pista.
#  *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#  *      - Si hace "run" en "|" (valla), se variará la pista por "/".
#  * - La función retornará un Boolean que indique si ha superado la carrera.
#  * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge17.kt
# --------------------------------------------------

def carrera_obstaculos(lista_movimientos,pista):
    
    resultado = list(pista) #convierte a lista con cada elemento como string
    prueba_superada = True
    
    if len(pista) != len(lista_movimientos):
        raise ValueError("No se puede realizar la comparación por diferente tamaño")
    
    print(f"Prueba a superar: {''.join(resultado)}")
    for i,(mov,obstaculo) in enumerate(zip(lista_movimientos,pista)):
        if mov == "run" and obstaculo =="_":
            continue
        elif mov == "jump" and obstaculo =="|":
            continue
        else:
            prueba_superada = False
            if mov == "jump" and obstaculo =="_":
                resultado[i] = "x"
            elif mov == "run" and obstaculo == "|":
                resultado[i] = "/"
            
    return "".join(resultado), prueba_superada

    
pista = "|||_|_|_____"
lista_movimientos = ["jump","jump","jump","run","jump","run","jump","run","jump","run","run","run"]


resultado , prueba_superada = carrera_obstaculos(lista_movimientos,pista)

if prueba_superada:
    print("PRUEBA SUPERADA!!")
else:
    print(f"La prueba no ha sido superada: {resultado}")
    
    
    
