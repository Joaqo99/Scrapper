from bs4 import BeautifulSoup
import requests
#import csv

marca = "jackson"
modelo = "kelly"

source = requests.get("https://instrumentos.mercadolibre.com.ar/instrumentos-cuerdas-guitarras-electricas/usado/" + marca + "/" + modelo).text

soup = BeautifulSoup(source, "lxml")

#csv_file = open("cms_scrape.csv", "w")
#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(["Imagen", "Articulo", "Precio", "Link"])

for articulo in soup.find_all(class_="ui-search-layout__item"):
    titulo = articulo.h2.text
    imagen = articulo.img
    precio = articulo.find(class_="price-tag").text
    link = articulo.find("a")["href"]

    print(titulo)
    print(imagen)
    print(precio)
    print(link)

    #csv_writer.writerow([imagen, titulo, precio, link])

#csv_file.close()
