#  * Reto #19
#  * CUADRADO Y TRIÁNGULO 2D
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
#  * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
#  * - EXTRA: ¿Eres capaz de dibujar más figuras?


def cuadrado_trinagulo_2d(tamanho, figura):
    
    if figura.lower() == "cuadrado":
        for _ in range(tamanho):
            print("* " * tamanho)
            
    elif figura.lower() == "triangulo":
        for i in range(1,tamanho +1 ):
            print("* " * i)
    
    elif figura.lower() == "trapecio":
        for i in range(tamanho):
            print("* " * (i + tamanho))
    elif figura.lower() == "rombo":
        # parte superior
        for i in range(tamanho):
            espacios = " " * (tamanho - i - 1) 
            asteriscos = "*" * (2 * i + 1)  
            print(  espacios + asteriscos)
        #parte inferior
        for i in range(tamanho -2 , -1,-1):
            espacios = " " * (tamanho -i -1)
            asteriscos = "*" * (2 * i + 1)
            print(espacios+asteriscos)
            
    elif figura.lower() == "flecha":
        # parte superior
        for i in range(tamanho):
            espacios = " " * (tamanho - i - 1) 
            asteriscos = "*" * (2 * i + 1)  
            print(  espacios + asteriscos)
        #parte inferior
        for _ in range(tamanho):
            espacios = " " * (tamanho -1)
            print(espacios+ "*")

    else:
        print("no es una figura aceptada")
        
        
cuadrado_trinagulo_2d(5,"ROMBO")