# RETO 27
# Nivel: Fácil
# Reto: VOCAL MÁS COMÚN
# Enunciado: /*
#  * Crea un función que reciba un texto y retorne la vocal que
#  * más veces se repita.
#  * - Ten cuidado con algunos casos especiales.
#  * - Si no hay vocales podrá devolver vacío.
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge47.kt
# --------------------------------------------------


def vocal_mas_comun(texto):
    if len(texto) > 0:
        texto_min_no_tildes = texto.lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
        dict_vocales = {}
        print(texto_min_no_tildes)
        for char in texto_min_no_tildes:
            if char in ['a','e','i','o','u']:
                if char in dict_vocales:
                    dict_vocales[char] += 1
                else:
                    dict_vocales[char] = 1
                
        clave_max = max(dict_vocales,key=dict_vocales.get)
        valor_max = dict_vocales[clave_max]
                    
        return clave_max,valor_max
    else:
        return "no hay vocales"
        
        

print(vocal_mas_comun("Este es un texto con muchas vocales."))
