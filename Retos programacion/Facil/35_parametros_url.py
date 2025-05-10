# RETO 35
# Nivel: Fácil
# Reto: PARÁMETROS URL
# Enunciado: /*
#  * Dada una URL con parámetros, crea una función que obtenga sus valores.
#  * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
#  *
#  * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
#  * los parámetros serían ["2023", "0"]
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2311%20-%20URL%20PARAMS%20%5BF%C3%A1cil%5D/ejercicio.md
# --------------------------------------------------

import re

def parametros_url(url):
    
    parametros_match = re.findall(r'=(.*?)(&|$)',url)
    
    lista_parametros = [p[0] for p in parametros_match]
    
    return lista_parametros
    
    
    

url = "https://retosdeprogramacion.com?year=2023&challenge=0"
print(parametros_url(url))