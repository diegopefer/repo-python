# Reto 23
# Nivel: Fácil
# Reto: EL SEGUNDO
# Enunciado: /*
#  * Dado un listado de números, encuentra el SEGUNDO más grande
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge32.kt
# --------------------------------------------------

def segundo_numero(lista):
    if len(lista) >= 2:
        maximo = None
        segundo_maximo = None
        
        for i in lista:
            if i > maximo:
                temp = maximo
                maximo = i
                segundo_maximo = temp
                    
            elif i < maximo and i > segundo_maximo:
                segundo_maximo=i
            
        return f"maximo: {maximo} || segundo maximo: {segundo_maximo}"
    else:
       return "lista con minimo 2 valores"

    
print(segundo_numero([2,5,7,10]))