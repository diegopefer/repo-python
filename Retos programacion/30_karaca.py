# RETO 30
# Nivel: Fácil
# Reto: LA ENCRIPTACIÓN DE KARACA
# Enunciado: /*
#  * Crea una función que sea capaz de encriptar y desencriptar texto
#  * utilizando el algoritmo de encriptación de Karaca
#  * (debes buscar información sobre él).
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge50.kt
# --------------------------------------------------


def karaca(texto,modo):
    
    if modo.lower() == "encriptar":
        reverse_texto = texto.lower()[::-1]
        replace_texto = reverse_texto.replace("a","0").replace("e","1").replace("i","2").replace("o","3").replace("u","4")
        aca_texto = replace_texto + "aca"
        return aca_texto
        
    elif modo.lower() == "desencriptar":
        
        if texto[-3:] == "aca":
            quit_aca = texto.lower()[:-3]
            replace_texto = quit_aca.replace("0","a").replace("1","e").replace("2","i").replace("3","o").replace("4","u")
            reverse_texto = replace_texto[::-1]
            return reverse_texto
         
    else:
        print("No existe ese modo, intentalo con encriptar o desencriptar")
    
print(karaca("hola","encriptar"))