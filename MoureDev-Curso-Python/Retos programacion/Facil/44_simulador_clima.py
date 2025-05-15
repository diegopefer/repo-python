# RETO 44
# --------------------------------------------------
# Nivel: Fácil
# Reto: SIMULADOR DE CLIMA
# Enunciado: /*
#  * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
#  * de un lugar ficticio al pasar un número concreto de días según estas reglas:
#  * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
#  * - Cada día que pasa:
#  *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
#  *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día
#  *     siguiente aumenta en un 20%.
#  *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día
#  *     siguiente disminuya en un 20%.
#  *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
#  * - La función recibe el número de días de la predicción y muestra la temperatura
#  *   y si llueve durante todos esos días.
#  * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2343%20-%20SIMULADOR%20DE%20CLIMA%20%5BF%C3%A1cil%5D/ejercicio.md
import random

def simulador_clima(temperatura, prob_lluvia, dias_prediccion):
    
    temperaturas = []  # Para almacenar las temperaturas de cada día
    cont_dias_lluvia = 0    # Contador de los días que llovió
    
    for dia in range(1, dias_prediccion + 1):
        print(f"\nDía: {dia}")
        
        if dia == 1:
            print(f"Temperatura: {temperatura}°C")
            print(f"Probabilidad de lluvia: {prob_lluvia}%")
            # Verificamos si llueve al 100% o si la probabilidad de lluvia es menor
            llueve = random.randint(1, 100) <= prob_lluvia
            print("¿Llueve?: Sí" if llueve else "¿Llueve?: No")
            temperaturas.append(temperatura)
            if llueve:
                cont_dias_lluvia += 1
            continue
        
        # Simulamos el cambio de temperatura con un 10% de probabilidad
        if random.randint(1, 10) == 1:
            if random.choice([True, False]):
                temperatura += 2
            else:
                temperatura -= 2
        
        # Regla para ajustar la probabilidad de lluvia según la temperatura
        if temperatura > 25:
            prob_lluvia = min(prob_lluvia + 20, 100)
        elif temperatura < 5:
            prob_lluvia = max(prob_lluvia - 20, 0)
        
        # Determinar si llueve basado en la probabilidad actual
        llueve = random.randint(1, 100) <= prob_lluvia
        
        # Si llueve (probabilidad 100%), disminuimos la temperatura en 1 grado
        if llueve and prob_lluvia == 100:
            temperatura -= 1
        
        # Imprimir el estado del clima
        print(f"Temperatura: {temperatura}°C")
        print(f"Probabilidad de lluvia: {prob_lluvia}%")
        print("¿Llueve?: Sí" if llueve else "¿Llueve?: No")
        
        temperaturas.append(temperatura)
        if llueve:
            cont_dias_lluvia += 1
                
    # Al final, mostrar las estadísticas finales
    print(f"\nEstadísticas finales:")
    print(f"Temperatura mínima: {min(temperaturas)}°C")
    print(f"Temperatura máxima: {max(temperaturas)}°C")
    print(f"Días con lluvia: {cont_dias_lluvia}")

# Entrada del usuario
temperatura = int(input("Introduce la temperatura inicial: "))
prob_lluvia = int(input("Introduce la probabilidad de lluvia inicial (0 a 100): "))
dias_prediccion = int(input("¿Cuántos días quieres simular?: "))

# Llamada a la función
simulador_clima(temperatura, prob_lluvia, dias_prediccion)