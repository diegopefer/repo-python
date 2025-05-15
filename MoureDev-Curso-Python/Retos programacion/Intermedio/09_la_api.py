# reto 09
# Nivel: Medio
# Reto: LA API (APPLICATION PROGRAMMING INTERFACE)
# Enunciado: /*
#  * Llamar a una API es una de las tareas más comunes en programación.
#  *
#  * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#  * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
#  *
#  * Aquí tienes un listado de posibles APIs:
#  * https://github.com/public-apis/public-apis
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2310%20-%20LA%20API%20%5BMedia%5D/ejercicio.md


# --------------------------------------------------

import requests

url = "https://pokeapi.co/api/v2/pokemon/ditto"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data["abilities"])
    
    for ability in data["abilities"]:
        print(ability['ability']['name'])
    
else:
    print("Error en la solicitud:", response.status_code)