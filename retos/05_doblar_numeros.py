"""
RETO 05

Dobla cada valor de una lista de numeros en una sola linea de código
"""

lista = [1,2,3,4]

print([i*2 for i in lista])

lista_doble = list(map(lambda x : x* 2,lista))
print(lista_doble)
