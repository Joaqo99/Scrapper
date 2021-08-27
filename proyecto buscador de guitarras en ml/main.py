from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#etapa de selección y filtrado de guitarras
marca = "jackson"
modelo = "kelly"


driver.get("https://instrumentos.mercadolibre.com.ar/instrumentos-cuerdas-guitarras-electricas/usado/" + marca + "/" + modelo) 


#scroll hasta el fondo
pagina = driver.find_element_by_tag_name("html")
pagina.send_keys(Keys.END)


#búsqueda de artículos
guitarras = pagina.find_element_by_class_name("ui-search-layout__item")

#acá entra en acción bs4



