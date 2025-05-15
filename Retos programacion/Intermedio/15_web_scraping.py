# RETO 15
# Nivel: Difícil
# Reto: WEB SCRAPING
# Enunciado: /*
#  * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
#  * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
#  *
#  * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
#  * del día 8. Mostrando hora e información de cada uno.
#  * Ejemplo: "16:00 | Bienvenida"
#  *
#  * Se permite utilizar librerías que nos faciliten esta tarea.
#  */
# Enlace: https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2318%20-%20WEB%20SCRAPING%20%5BDif%C3%ADcil%5D/ejercicio.md
# --------------------------------------------------


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# iniciar navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless') #ejercicio sin ventana navegador
driver = webdriver.Chrome(options=options)

# apertura de la web
driver.get(" https://holamundo.day")
time.sleep(5)


# buscar elementos de la agenda(contiene hora como actividad)
agenda_items = driver.find_elements(By.CSS_SELECTOR, 'span.rt-Text')

agenda = []

for item in agenda_items:
        if item.text.strip():
            
            texto = item.text.strip()
        #separar hora y actividad
        if texto[:5].count(':') == 1:
            hora = texto[:5]
            actividad = texto[6:].strip()
            agenda.append((hora,actividad))

for i, (hora,actividad) in enumerate(agenda,start=1):
    print(f"[{i}] hora: {hora}: {actividad}")
    

driver.quit()