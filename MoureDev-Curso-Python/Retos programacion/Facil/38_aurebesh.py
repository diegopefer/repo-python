# RETO 38
# Nivel: Fácil
# Reto: AUREBESH
# Enunciado: /*
#  * Crea una función que sea capaz de transformar Español al lenguaje básico
#  * del universo Star Wars: el "Aurebesh".
#  * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
#  * - También tiene que ser capaz de traducir en sentido contrario.
#  *
#  * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
#  *
#  * ¡Que la fuerza os acompañe!
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2315%20-%20AUREBESH%20%5BF%C3%A1cil%5D/ejercicio.md
# --------------------------------------------------

aurebesh_dict = {
    'a': 'Aurek',
    'b': 'Besh',
    'c': 'Cresh',
    'd': 'Dorn',
    'e': 'Enth',
    'f': 'Forn',
    'g': 'Grek',
    'h': 'Herf',
    'i': 'Isk',
    'j': 'Jenth',
    'k': 'Krill',
    'l': 'Leth',
    'm': 'Mern',
    'n': 'Nern',
    'o': 'Osk',
    'p': 'Peth',
    'q': 'Qek',
    'r': 'Resh',
    's': 'Senth',
    't': 'Trill',
    'u': 'Usk',
    'v': 'Vev',
    'w': 'Wesk',
    'x': 'Xesh',
    'y': 'Yirt',
    'z': 'Zerek',
    'ñ': 'Ñaer'  # inventado, ya que ñ no tiene equivalente oficial
}

aurebesh_reverse_dict = {v:k for k,v in aurebesh_dict.items()}


def convertir_a_aurebesh(aurebesh_dict,frase):
    aurebesh_frase = ""
    for char in frase.lower():
        if char in aurebesh_dict:
            aurebesh_frase += aurebesh_dict[char] + " "
        else:
            aurebesh_frase += char + " "
    
    print(aurebesh_frase)
    
def convertir_a_espanhol(aurebesh_reverse_dict, frase_aurebesh):
    espanhol_frase = ""
    for palabra in frase_aurebesh.split(" "):
        if palabra == "":
            espanhol_frase += " "  # si había dos espacios seguidos en la original
        elif palabra in aurebesh_reverse_dict:
            espanhol_frase += aurebesh_reverse_dict[palabra]
        else:
            espanhol_frase += palabra  # por si hay algo raro

    print(espanhol_frase)
    



frase_espanhol = "que la fuerza te acompañe"
frase_aurebesh = "Qek Usk Enth   Leth Aurek   Forn Usk Enth Resh Zerek Aurek   Trill Enth   Aurek Cresh Osk Mern Peth Aurek Ñaer Enth"

# convertir_a_aurebesh(aurebesh_dict,frase_espanhol)
convertir_a_espanhol(aurebesh_reverse_dict,frase_aurebesh)


