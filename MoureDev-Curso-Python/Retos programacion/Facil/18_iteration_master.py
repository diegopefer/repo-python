#  * Reto #18
#  * ITERATION MASTER
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno). ¿De cuántas maneras eres capaz de hacerlo? Crea el código para cada una de ellas.

def iteration_master_for():
    for i in range(1,101,1):
        print(i)
        

def iteration_master_while():
    numero = 1
    while numero <=100:
        print(numero)
        numero+=1
        
def iteration_master_recursivo(numero=1):

    
    if numero <=100:
        print(numero)
        iteration_master_recursivo(numero + 1)


def iteration_master_join():
    
    print( "\n".join(str(i) for i in range(1,101)))
    
def iteration_master_map():
    return list(map(lambda x:x ,range(1,101,1)))

# iteration_master_for()
# iteration_master_while()
# iteration_master_recursivo()
# iteration_master_join()
#print(iteration_master_map())

