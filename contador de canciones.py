from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://music.apple.com/library/songs")

time.sleep(75)

pagina = driver.find_element_by_tag_name("html")
pagina.send_keys(Keys.END)
contenedor = driver.find_element_by_class_name("dt-virtual-scrolling-songs-list-container")
canciones = contenedor.find_elements_by_tag_name("div")


nombres = canciones.find_element_by_class_name("library-track-name__text")
for nombre in nombres:
    print(nombre)

nroCanciones = 0

for cancion in canciones:
    nroCanciones += 1
print("hay " + str(nroCanciones) + " canciones")

