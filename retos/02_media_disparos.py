"""
MEDIA
Calcula la media de un
listado de números de disparos.
"""

kim_yeji = [9.8, 10.4, 10.5, 9.3, 9.7, 10.7, 10.4, 9.9, 10.4, 10.4, 10.0, 10.3, 9.9, 10.2, 9.8, 10.1, 10.2, 9.7, 10.2, 10.0, 9.4, 10.5, 9.7, 9.8]
yusuf_dikec = [9.0, 10.3, 10.2, 10.6, 10.1, 10.6, 9.9, 10.5, 9.2, 9.5, 10.8, 10.7, 10.4, 10.6, 9.1]

def media(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

print(f"Media kim_yeji: {media(kim_yeji):.1f}")
print(f"Media yusuf_dikec: {media(yusuf_dikec):.1f}")