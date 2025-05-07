# RETO 29
# Nivel: Fácil
# Reto: EL DETECTOR DE HANDLES
# Enunciado: /*
#  * Crea una función que sea capaz de detectar y retornar todos los
#  * handles de un texto usando solamente Expresiones Regulares.
#  * Debes crear una expresión regular para cada caso:
#  * - Handle usuario: Los que comienzan por "@"
#  * - Handle hashtag: Los que comienzan por "#"
#  * - Handle web: Los que comienzan por "www.", "http://", "https://"
#  *   y finalizan con un dominio (.com, .es...)
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge49.kt
# --------------------------------------------------
import re

def detector_handles(texto):
    
    patron_usuario =  r"@\w+"
    patron_hashtag = r"#\w+"
    patron_web = r"(?:https?://|www\.)[\w.-]+\.[a-zA-Z]{2,}"
    
    coincidencias_usuario =re.findall(patron_usuario,texto)
    coincidencias_hashtag=re.findall(patron_hashtag,texto)
    coincidencias_web =re.findall(patron_web,texto)
    
    return coincidencias_usuario,coincidencias_hashtag,coincidencias_web

texto = "Síguenos en @usuariooo, participa con #Reto29 #Reto28 y visita nuestra web https://ejemplo.com/evento para más info."

print(detector_handles(texto))