from bs4 import BeautifulSoup
import requests

class Guitarra:
    def __init__(self, titulo, imagen, precio, link):
        self.titulo = titulo
        self.imagen = imagen
        self.precio = precio
        self.link = link

    def mostrarCaract(self):
        print("Titulo: " + self.titulo + "\nPrecio: " + self.precio + "\nLink: " + self.link + "\n\n")

def buscarArticulos(marca, modelo):
    source = requests.get("https://instrumentos.mercadolibre.com.ar/instrumentos-cuerdas-guitarras-electricas/" + marca + "/usado/" + modelo).text

    soup = BeautifulSoup(source, "lxml")
    count = 0
    
    for articulo in soup.find_all(class_="ui-search-layout__item"):
        #disponible = True
        titulo = articulo.h2.text
        imagen = articulo.img
        precio = articulo.find(class_="price-tag").text
        link = articulo.find("a")["href"]
        count += 1
        nomObj = "guitarra" + str(count)
        nomObj = Guitarra(titulo, imagen, precio, link)

        nomObj.mostrarCaract()

    print(len(soup.find_all(class_="ui-search-layout__item")))

buscarArticulos("jackson", "kelly")
