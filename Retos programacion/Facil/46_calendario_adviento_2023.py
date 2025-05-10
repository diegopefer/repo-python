# RETO 46
# --------------------------------------------------
# Nivel: Fácil
# Reto: EL CALENDARIO DE ADEVIENTO 2023
# Enunciado: /*
#  * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
#  * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
#  * Desde el 1 al 24 de diciembre.
#  *
#  * Crea un programa que simule el mecanismo de participación:
#  * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
#  *   participantes, mostrarlos, lanzar el sorteo o salir.
#  * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
#  * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
#  *   (Y no lo duplicarás)
#  * - Si seleccionas mostrar los participantes, se listarán todos.
#  * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
#  *   (Avisando de si lo has eliminado o el nombre no existe)
#  * - Si seleccionas realizar el sorteo, elegirás una persona al azar
#  *   y se eliminará del listado.
#  * - Si seleccionas salir, el programa finalizará.
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2345%20-%20EL%20CALENDARIO%20DE%20ADEVIENTO%202023%20%5BF%C3%A1cil%5D/ejercicio.md

import random

lista_participantes = []

def mostrar_menu():
    print("\nElige una opción:")
    print("1. Añadir participante")
    print("2. Eliminar participante")
    print("3. Mostrar participantes")
    print("4. Realizar sorteo")
    print("5. Salir")
    
def anhadir_participante():
    print("Añadir participante")
    nombre=input("Introduce el nombre del participante: ").strip().lower()
    if nombre not in lista_participantes:
        lista_participantes.append(nombre)
        print(f"El participante {nombre} fue añadido.")
    else:
        print(f"El participante {nombre} ya está en la lista")
        

    
def mostrar_participantes():
    if len(lista_participantes) == 0:
        print("no hay ningun participante en la lista")
    else:
        print("Participantes")
        for p in lista_participantes:
            print(f"- {p}")
            
def borrar_participante():

    participante= input("introduce el nombre del participante a borrar.").strip().lower()
    
    if participante not in lista_participantes:
        print(f"el participante {participante} no existe en la lista")
    else:
        print("Borrar participante")
        lista_participantes.remove(participante)
        print(f"el participante {participante} has sido eliminado correctamente.")
        
        
def realizar_sorteo():
    
    if lista_participantes:
        ganador = random.choice(lista_participantes)
        print(f"el ganador es {ganador}. FELICIDADES!!!")
        lista_participantes.remove(ganador)
    
    else:
        print("No se puede realizar el sorteo porque no hay participantes en la lista.")


def main():
    
    while True:
        mostrar_menu()
        
        opcion = input("selecciona una opcion (del 1 al 5): ").strip()
        
        if opcion == "1":
            anhadir_participante()
        elif opcion =="2":
            borrar_participante()
        elif opcion =="3":
            mostrar_participantes()
        elif opcion =="4":
            realizar_sorteo()
        elif opcion =="5":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor selecciona una opción correcta.")


main()