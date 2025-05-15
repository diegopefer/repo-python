# RETO 14
#  * ¿ES UN NÚMERO DE ARMSTRONG?
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
# #  * Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
# Un número es de Armstrong si:
    # Tomas cada uno de sus dígitos,
    # Elevas cada dígito a la cantidad de dígitos que tiene el número,
    # Sumas todos esos valores,
    # Y el resultado es igual al número original.
    # ej: 153
    #     * tiene 3 cifras-> elevamos cada digito al cubo
    #     * como 153 = 153 -> esa numero de amstrong
    

def numero_amstrong(numero):

    suma_digitos = 0
    num_digitos = len(str(numero))
    for num_indi in str(numero):
        suma_digitos += int(num_indi)**num_digitos # Elevar cada dígito a la cantidad de dígitos
        
    
    if suma_digitos == numero:
        print(f"el numero {numero} es un numero amstrong")
    else:
        print(f"el numero {numero} NO es un numero amstrong")
numero_amstrong(23)