# reto 10
# Nivel: Medio
# Reto: CONTENEDOR DE AGUA
# Enunciado: /*
#  * Dado un array de números enteros positivos, donde cada uno
#  * representa unidades de bloques apilados, debemos calcular cuantas unidades
#  * de agua quedarán atrapadas entre ellos.
#  *
#  * - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
#  *
#  *        ⏹
#  *        ⏹
#  *   ⏹💧💧⏹
#  *   ⏹💧⏹⏹💧⏹
#  *   ⏹💧⏹⏹💧⏹
#  *   ⏹💧⏹⏹⏹⏹
#  *
#  *   Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades
#  *   de agua. Suponemos que existe un suelo impermeable en la parte inferior
#  *   que retiene el agua.
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge45.kt
# --------------------------------------------------


def contenedor_de_agua(bloques):
    
    
    max_izquierda = []
    max_actual = 0
    
    # Recorremos de izquierda a derecha, guardando el mayor visto hasta ahora
    
    for b in bloques:
        max_actual = max(max_actual,b)
        max_izquierda.append(max_actual)
        
    
    max_derecha = []
    max_actual = 0
    
     # Máximos hacia la derecha (recorremos al revés)
    for b in reversed(bloques):
        max_actual = max(max_actual,b)
        max_derecha.append(max_actual)
    
    # inversion para alinear indices y bloques
    max_derecha.reverse()
    
    agua_en_i = 0
    agua_total = 0
    
    # por cada posicion se calcula el agua que se puede almacenar
    for i in range(len(bloques)):
        # agua en la posicion depende del minimo entre maxderecha y maxizquuieda menos el bloque
        agua_en_i = min(max_izquierda[i],max_derecha[i]) - bloques[i]
        agua_total+= agua_en_i
        
    print(f"Bloques: {bloques}")
    print(f"Max izquierda: {max_izquierda}")
    print(f"Max derecha: {max_derecha}")
    print(f"Agua total: {agua_total}")
        
    
    
contenedor_de_agua([4, 0, 3, 6, 1, 3])
    
    

