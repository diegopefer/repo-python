#  * Reto #08
#  * AÑOS BISIESTOS
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
#  * - Utiliza el menor número de líneas para resolver el ejercicio.



def anos_bisiestos(ano):
    contador_bisiestos = 0
    while contador_bisiestos < 30:
        ano_bisiesto = (ano % 4 == 0 and  ano%100!=0) or (ano % 4 == 0 and ano%100 ==0 and ano%400==0) 
        if ano_bisiesto:
            contador_bisiestos+=1
            print(f"{ano} -> bisiesto")
        
        ano+=1
        
anos_bisiestos(2025)