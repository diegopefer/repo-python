# --------------------------------------------------
# RETO 37
# Nivel: Fácil
# Reto: ADIVINA LA PALABRA
# Enunciado: /*
#  * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
#  * - El juego comienza proponiendo una palabra aleatoria incompleta
#  *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
#  * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
#  *   la palabra a adivinar)
#  *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
#  *     uno al número de intentos
#  *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
#  *     al número de intentos
#  *   - Si el contador de intentos llega a 0, el jugador pierde
#  * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
#  *   ocultando más del 60%
#  * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2313%20-%20ADIVINA%20LA%20PALABRA%20%5BMedia%5D/ejercicio.md
import random

palabras = [
    "murcielago",
    "programacion",
    "desarrollo",
    "python",
    "computadora",
    "algoritmo",
    "variable",
    "internet",
    "funcion",
    "teclado",
    "pantalla",
    "robot",
    "matematicas",
    "astronomia",
    "galaxia"
]

random_palabra = random.choice(palabras)

# Paso 1: Ocultar letras
num_ocultas = int(len(random_palabra) * 0.6)
indices = random.sample(range(len(random_palabra)), num_ocultas)
palabra_oculta = ["_" if i in indices else letra for i, letra in enumerate(random_palabra)]

# Paso 2: Inicializar intentos
num_intentos = 3
print("Palabra a adivinar:", "".join(palabra_oculta))
print(f"Tienes {num_intentos} intentos para resolverla correctamente. ¡A por ello!")

# Paso 3: Bucle del juego
while num_intentos > 0:
    entrada = input("Introduce una letra o la palabra completa: ").lower()

    # Validación de entrada
    if len(entrada) == 1:
        # Verifica si ya estaba visible
        if entrada in random_palabra:
            encontrada = False
            for i, letra in enumerate(random_palabra):
                if letra == entrada and palabra_oculta[i] == "_":
                    palabra_oculta[i] = entrada
                    encontrada = True
            if encontrada:
                print(f"¡Letra acertada! [{entrada}]")
            else:
                print(f"¡La letra [{entrada}] ya está descubierta en todas sus posiciones!")
                num_intentos -= 1
        else:
            print("¡Fallo!")
            num_intentos -= 1

    elif len(entrada) == len(random_palabra):
        if entrada == random_palabra:
            print("¡Has acertado la palabra!", random_palabra)
            break
        else:
            print("¡Fallo!")
            num_intentos -= 1

    else:
        print("Entrada inválida.")
        num_intentos -= 1

    # Mostrar estado y comprobar si se ha ganado
    print("\nPalabra:", "".join(palabra_oculta))
    print(f"Intentos restantes: {num_intentos}")
    if "_" not in palabra_oculta:
        print("¡Has completado la palabra! Ganaste.")
        break

# Fin del juego
if "_" in palabra_oculta:
    print("Se acabaron los intentos. La palabra era:", random_palabra)