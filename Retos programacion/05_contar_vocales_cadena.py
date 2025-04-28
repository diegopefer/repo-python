# Reto 05 (no está en la url del reto)
# Contar vocales en una cadena

# Dada una cadena de texto, deberás contar cuántas vocales (a, e, i, o, u) aparecen en ella. Debes hacerlo de manera que puedas manejar tanto mayúsculas como minúsculas, es decir, que "a" y "A" se consideren iguales.

# Ejemplo práctico:
# Entrada: # "Hola Mundo"
# Salida esperada: 4 (Contando: o, o, u, o)

def contar_vocales(cadena):
    if len(cadena)>0:
        contador = 0
        lista = []
        for char in cadena:
            vocal = char.lower() in "aeiou"
            if vocal:
                contador+=1
                lista.append(char)
        
        return contador,lista

contador_vocales, lista_vocales = contar_vocales("HoLA mUndOo")

print(f"numero de vocales: {contador_vocales}: {lista_vocales}")
                