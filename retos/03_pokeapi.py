"""
LISTA POKÉMON
Lista los 151 primeros Pokémon
utilizando la PokéAPI.
"""

import requests


def listar_pokemons(url):
    response = requests.get(url)
    
    if response.status_code ==200:
        pokemons = response.json()["results"]
        
        print(f"Número total de pokemons: {len(pokemons)}\n")
        for i, pokemon in enumerate(pokemons):
            print(f"[{i+1}] {pokemon['name']}")
            
        
    else:
        print("Operación no válida")
        
url="https://pokeapi.co/api/v2/pokemon?limit=151"

listar_pokemons(url)