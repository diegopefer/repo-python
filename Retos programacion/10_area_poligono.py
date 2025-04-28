#  * Reto 10
#  * ÁREA DE UN POLÍGONO
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.

def area_poligono(poligono,lado1,lado2):
    
    if poligono == "triangulo":
        print("triangulo")
        area = (lado1*lado2)/2 
    
    elif poligono == "cuadrado":
        print("cuadrado")
        area = (lado1*lado2)
        
    elif poligono == "rectangulo":
        print("rectangulo")
        area = (lado1*lado2)
        
    else:
        print("el poligono proporcionado no es soportado")
        return None
    
    return area

print(int(area_poligono("triangulo", 3, 4)))     # 6
print(int(area_poligono("cuadrado", 5, 5)))      # 25
print(int(area_poligono("rectangulo", 4, 6)))    # 24