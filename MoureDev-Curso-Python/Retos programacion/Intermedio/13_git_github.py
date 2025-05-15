# reto 13
# Nivel: Difícil
# Reto: GIT Y GITHUB
# Enunciado: /*
#  * ¡Estoy de celebración! He publicado mi primer libro:
#  * "Git y GitHub desde cero"
#  * - Papel: mouredev.com/libro-git
#  * - eBook: mouredev.com/ebook-git
#  *
#  * ¿Sabías que puedes leer información de Git y GitHub desde la gran
#  * mayoría de lenguajes de programación?
#  *
#  * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
#  * - Hash
#  * - Autor
#  * - Mensaje
#  * - Fecha y hora
#  *
#  * Ejemplo de salida:
#  * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
#  *
#  * Se permite utilizar librerías que nos faciliten esta tarea.
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2317%20-%20GIT%20Y%20GITHUB%20%5BDif%C3%ADcil%5D/ejercicio.md
# --------------------------------------------------

import requests
import json
from datetime import datetime

url= "https://api.github.com/repos/mouredev/retos-programacion-2023/commits"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    print("Impresion de los últimos 10 commits del repositorio 'retos programacion 2023 Mouredev' \n")
    for e in data[:10]:
        print(f" {e['sha']} | {e['commit']['author']['name']} | {e['commit']['message']} | {datetime.strptime(e['commit']['committer']['date'],"%Y-%m-%dT%H:%M:%SZ")}")

        
        
else:
    print("error al obtener los datos")
    

