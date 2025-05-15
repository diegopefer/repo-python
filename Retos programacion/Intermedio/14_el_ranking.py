# reto 14
# Nivel: Difícil
# Reto: EL RANKING
# Enunciado: /*
#  * Todo llega a su fin... Este es el último reto de programación
#  * semanal de 2023.
#  *
#  * Crea un programa que muestre un listado calculado en tiempo real
#  * con todos los usuarios que han resuelto algún reto de programación
#  * de este año.
#  * - El listado debe estar ordenado por el número de ejercicios resueltos
#  *   por cada usuario (y mostrar ese contador al lado de su nombre).
#  * - También se debe de mostrar el número de usuarios que han participado
#  *   y el número de correcciones enviadas.
#  *
#  * Muchísimas gracias por ayudar a crear este gran recurso
#  * para la comunidad... ¡Prepárate para 2024!
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2348%20-%20EL%20RANKING%20%5BDif%C3%ADcil%5D/ejercicio.md
# --------------------------------------------------

import requests

url = "https://api.github.com/repos/mouredev/retos-programacion-2023/commits"

response = requests.get(url)

usuarios = {}

if response.status_code == 200:
    commits = response.json()
    
    for commit in commits:
        autor = commit['commit']['author']['name']
        if autor in usuarios:
            usuarios[autor] += 1
        else:
            usuarios[autor] = 1
            
    usuarios_ordenados = sorted(usuarios.items(), key = lambda x : x[1],reverse=True)
    total_retos = sum(usuarios.values())
        
    for i , (usuario, retos_resueltos) in enumerate(usuarios_ordenados,start = 1):
      
        print(f"[{i}] {usuario} -> {retos_resueltos} retos resueltos")
        
    
    print(f"\n> numero total de participantes: {len(usuarios_ordenados)}")
    print(f"> numero total de retos resueltos: {total_retos}")

else:
    print("error al obtener datos de la API")