# RETO 01
# Nivel: Medio
# Reto: CÓDIGO MORSE
# Enunciado: /*
#  * Crea un programa que sea capaz de transformar texto natural a código
#  * morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar
#  *   la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#  *   o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en
#  *   https://es.wikipedia.org/wiki/Código_morse.
#  */
# Enlace: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge9.kt
# --------------------------------------------------

def es_morse(texto):

    for char in texto:
        if char not in  [".", "-", " ", "/"]:
            return False
        
    return True


def convertir_a_morse(texto):
    morse_texto = ""
    # Convierte un texto a Morse
    morse_texto = " ".join(morse_dict[char] for char in texto.lower() if char in morse_dict)
    
    return morse_texto

def convertir_a_texto(texto):
    texto_normal = []
    palabras = texto.split("  ")  # doble espacio separa palabras
    
    for palabra in palabras:
        letras = palabra.split()   # espacio simple separa letras
        for letra in letras:
            if letra in morse_to_text_dict:
                texto_normal += morse_to_text_dict[letra]
        texto_normal += " "  # añadimos espacio al final de cada palabra

    return texto_normal.strip()

texto_entrada = input ("Introduce el texto en Morse o en texto normal: ")    


morse_dict = {
    "a": ".-",     "b": "-...",   "c": "-.-.",   "d": "-..",    "e": ".",      "f": "..-.",
    "g": "--.",    "h": "....",   "i": "..",     "j": ".---",   "k": "-.-",    "l": ".-..",
    "m": "--",     "n": "-.",     "o": "---",    "p": ".--.",   "q": "--.-",   "r": ".-.",
    "s": "...",    "t": "-",      "u": "..-",     "v": "...-",   "w": ".--",    "x": "-..-",
    "y": "-.--",   "z": "--..",   "1": ".----",  "2": "..---",  "3": "...--",  "4": "....-",
    "5": ".....",  "6": "-....",  "7": "--...",  "8": "---..",  "9": "----.",  "0": "-----",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.",
    "(": "-.--.",  ")": "-.--.-", "&": ".-...",  ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.",  "-": "-....-", "_": "..--.-", "$": "...-..-", "@": ".--.-."
}

# diccionario de morse a texto 
morse_to_text_dict = {v:k for k,v in morse_dict.items()}

if es_morse(texto_entrada):
    print(f"el texto en lenguaje normal es: {convertir_a_texto(texto_entrada)}")
else:
    print(f"El texto en morse es : {convertir_a_morse(texto_entrada)}")
