from bs4 import BeautifulSoup
import requests
import escritor_de_excel

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

#wb = load_workbook('guitarras.xlsx')
#ws = wb.active

tabla_de_guitarras = escritor_de_excel.obtenerLista('guitarras.xlsx')
#print(tabla_de_guitarras)
lista1 = []
lista2 = []
for ii in tabla_de_guitarras:
    marca = ii[0]
    for aaa in ii:
        if aaa == ii[0]:
            pass
        else:
            lista2 = [ii[0], aaa]
            lista1.append(lista2)

print(lista1)
for guitarra in lista1:
    buscarArticulos(guitarra[0], guitarra[1])

#buscarArticulos(marca, modelo)

