# reto 45
# Nivel: Fácil
# Reto: LA PALABRA DE 100 PUNTOS
# Enunciado: /*
#  * La última semana de 2021 comenzamos la actividad de retos de programación,
#  * con la intención de resolver un ejercicio cada semana para mejorar
#  * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
#  *
#  * Crea un programa que calcule los puntos de una palabra.
#  * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
#  *   español de 27 letras, la A vale 1 y la Z 27.
#  * - El programa muestra el valor de los puntos de cada palabra introducida.
#  * - El programa finaliza si logras introducir una palabra de 100 puntos.
#  * - Puedes usar la terminal para interactuar con el usuario y solicitarle
#  *   cada palabra.
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2347%20-%20LA%20PALABRA%20DE%20100%20PUNTOS%20%5BF%C3%A1cil%5D/ejercicio.md
# --------------------------------------------------

def palabra_100_puntos(puntos_letras):
    
    while True:
        num_puntos = 0

        palabra = input("Intenta introducir una palabra de 100 puntos: ")
        print(f"La palabra elegida es: [{palabra}]")
        for letra in palabra:
            if letra in puntos_letras:
                num_puntos += puntos_letras[letra]
                
        
        if(num_puntos !=100):
            print(f"\tTu puntuación es: {num_puntos}. Vuelve a intentarlo con otra palabra.")
        else:
            print(f"HAS GANADO CON LA PALABRA [{palabra}]. FELICIDADES!!")
            break



# Diccionario de puntos por cada letra
puntos_letras = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, 
    "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "ñ": 15, "o": 16, "p": 17, 
    "q": 18, "r": 19, "s": 20, "t": 21, "u": 22, "v": 23, "w": 24, "x": 25, 
    "y": 26, "z": 27
}

palabra_100_puntos(puntos_letras)