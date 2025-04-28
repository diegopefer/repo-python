# RETOS PROGRAMACIÓN

"""
#1 EL FAMOSO "FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
    - Múltiplos de 3 por la palabra "fizz".
    - Múltiplos de 5 por la palabra "buzz".
    - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} -> fizzbuzz")
        elif i % 3 == 0:
            print(f"{i} -> fizz")
        elif i % 5 == 0:
            print(f"{i} -> buzz")
        else:
            print(i)

# fizzbuzz()


"""
#2 ¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""



def es_anagrama(palabra1,palabra2):
    
    return sorted(palabra1.lower()) == sorted(palabra2.lower())
    
    
    
print(f"¿Es anagrama? {es_anagrama("monja","jamon")}")



#3 LA SUCESIÓN DE FIBONACCI
"""
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci():
    lista_fibonacci = [0,1]
    previo = 1
    anterior_previo = 0
    
    for i in range(1,49):
        suma_fibonacci = anterior_previo + previo
        anterior_previo = previo
        previo = suma_fibonacci
        lista_fibonacci.append(suma_fibonacci)
        
        
        
    print(lista_fibonacci)
        

fibonacci()



#4 ¿ES UN NÚMERO PRIMO?
# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.

def es_primo():
    
    for num in range (1,101):
        if num >= 2:
            is_divisible = False
            
            for i in range(2,num):
                if num % i == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(num)


    
# es_primo()


#7 INVIERTIENDO CADENAS
# Crea un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"



def invertir_cadena(texto):
    aux= ""
    for i in range(len(texto)-1,-1,-1):
        aux += texto[i]
    
    return aux
    
    
print(invertir_cadena("Hola mundo"))