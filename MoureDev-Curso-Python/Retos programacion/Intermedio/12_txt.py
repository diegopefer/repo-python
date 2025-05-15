# reto 12
# Nivel: Medio
# Reto: TXT
# Enunciado: /*
#  * Crea un programa capaz de interactuar con un fichero TXT.
#  * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección.
#  * Únicamente el código.
#  *
#  * - Si no existe, debe crear un fichero llamado "text.txt".
#  * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
#  *   en una nueva línea cada vez que se pulse el botón "Enter".
#  * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
#  *   a continuación o borrar su contenido y comenzar desde el principio.
#  * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
#  *   el texto que ya posee el fichero. 
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2334%20-%20EL%20TXT%20%5BMedia%5D/ejercicio.md
# --------------------------------------------------

import os

if os.path.exists("dromedariense.txt"):
    opcion = input("Quieres borrar contenido (B) o continuar escribiendo (E)? Escribe la opción que deseas.").strip()
    
    if opcion in ['B','E']:
        if opcion == "B":
            print("Has elegido: [BORRAR]")
            
            with open("dromedariense.txt", "w", encoding="UTF-8") as file:
                print("Introduce el texto linea a linea. Escribe 'salir' al terminar")
                
                while True:
                    linea = input(">")
                    if linea.lower() == "salir":
                        break
                    
                    file.write(linea+ "\n")
        else:
            print("Has elegido: [ESCRIBIR]")
            
            with open("dromedariense.txt", "r", encoding="UTF-8") as file:
                contenido = file.read()
                print(contenido)
            
            quiero_escribir = input ("¿Quieres escribir? (s/n)")
            
            if quiero_escribir == "s":
                with open("dromedariense.txt" , "a") as file:
                    print("Introduce el texto linea a linea. Escribe 'salir' al terminar")
                    
                    while True:
                        linea = input(">")
                        if linea.lower() == 'salir':
                            break
                        file.write(linea+"\n")
            else:
                print("finalizamos las operaciones")
            
    else:
        print("La opción seleccionada no existe!")
        
else:
    filename = input("introduce el nombre del archivo que deseas crear: ").strip()
    
    with open(filename,"w") as file:
        print("Introduce el texto linea a linea. Escribe 'salir' al terminar")
                
        while True:
            linea = input(">")
            if linea.lower() == 'salir':
                break
            file.write(linea+"\n")