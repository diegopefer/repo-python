#  * Reto #12
#  * ELIMINANDO CARACTERES
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
#  * - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
#  * - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.


def eliminar_caracteres(cadena1, cadena2):
    cadena1_plana,cadena2_plana = cadena1.lower(), cadena2.lower()
    
    out1,out2 ="",""
    
    for char in cadena1_plana:
        if char not in cadena2_plana:
            out1 += char
    
    for char in cadena2_plana:
        if char not in cadena1_plana:
            out2+= char
    print(f"out1: {out1}")
    print(f"out2: {out2}")

eliminar_caracteres("hola que tal Lucas,todo correcto?","eres un loco Luis, no te aguanto")
