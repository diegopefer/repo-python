# RETO 33
# Nivel: Fácil
# Reto: EL "LENGUAJE HACKER"
# Enunciado: /*
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet)
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%231%20-%20EL%20LENGUAJE%20HACKER%20%5BF%C3%A1cil%5D/ejercicio.md
# --------------------------------------------------

def lenguaje_hacker(texto,diccionario_hacker):
    
    texto_minusculas = texto.lower()
    hacker_string = ""
    for char in texto_minusculas:
        if char in diccionario_hacker:
            hacker_string += leet_dict[char]
        else:
            hacker_string+= char   
    print(hacker_string)
    


leet_dict = {
    'a': '4',
    'b': '8',
    'c': '<',
    'd': '|)',
    'e': '3',
    'f': '|=',
    'g': '6',
    'h': '#',
    'i': '1',
    'j': '_|',
    'k': '|<',
    'l': '1',
    'm': r'|\/|',
    'n': r'|\|',
    'o': '0',
    'p': '|>',
    'q': '9',
    'r': '2',
    's': '5',
    't': '7',
    'u': '(_)',
    'v': r'\/',
    'w': r'\/\/',
    'x': '><',
    'y': '`/',
    'z': '2',
    '0': 'o',
    '1': 'l',
    '2': 'z',
    '3': 'e',
    '4': 'A',
    '5': 's',
    '6': 'G',
    '7': 'T',
    '8': 'B',
    '9': 'g'
}

lenguaje_hacker("hola que tal estas bro",leet_dict)
