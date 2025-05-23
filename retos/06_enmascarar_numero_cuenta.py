# Enmascara los numeros de cuenta bancarios menos los 4 ultimos digitos





def enmascarar_numeros_cuenta(cuentas):
    lista_enmascarada = []
    
    for cuenta in cuentas:
        cuenta_enmascarada = cuenta[:2]+((len(cuenta)-4)* "*")+ cuenta[-4:]
        lista_enmascarada.append(cuenta_enmascarada)
    
    return lista_enmascarada

cuentas = ["ES91 2100 1234 5678 9012 3456",
           "ES47 0049 1500 1234 5678 9012",
           "ES62 2100 0418 4502 0005 1332"]

print(enmascarar_numeros_cuenta(cuentas))


