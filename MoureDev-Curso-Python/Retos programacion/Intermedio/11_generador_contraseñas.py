# reto 11
# --------------------------------------------------
# Nivel: Medio
# Reto: EL GENERADOR DE CONTRASEÑAS
# Enunciado: /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%233%20-%20EL%20GENERADOR%20DE%20CONTRASE%C3%91AS%20%5BMedia%5D/ejercicio.md


import string
import random

def generador_contraseñas(longitud,usar_mayusculas,usar_numeros,usar_simbolos):
    
    if not (8 <= longitud <= 16):
     raise ValueError ("La longitud debe estar entre 8 y 16")
 
    else:
        constructor_contraseña = list(string.ascii_lowercase)
        
        if usar_mayusculas:
            constructor_contraseña += list(string.ascii_uppercase)
        if usar_numeros:
            constructor_contraseña += list(string.digits)
        if usar_simbolos:
            constructor_contraseña += list(string.punctuation)
            
        
        # generacion contraseña
        
        password = [random.choice(constructor_contraseña) for _ in range(longitud)]
        random.shuffle(password)
        
        return "".join(password)
    
    
    
print(f"Contraseña 1: {generador_contraseñas(12,True,True,True)}")
print(f"Contraseña 2: {generador_contraseñas(9,True,True,True)}")
print(f"Contraseña 3: {generador_contraseñas(10,True,False,False)}")
print(f"Contraseña 4: {generador_contraseñas(8,False,True,True)}")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    