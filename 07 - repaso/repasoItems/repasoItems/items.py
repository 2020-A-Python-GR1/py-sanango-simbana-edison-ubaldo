# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

## AQUÍ PUEDO DEFINIR FUNCIONES QUE ME AYUDEN A LIMPIAR DATOS pero no hace el filtrado eso haec PIPELINES


def transformar_titulo(titulo):
    return titulo.lower()

def transformar_precio(precio):
    return float(precio.replace("€\xa0","").replace(",","."))


def transformar_talla(talla):
    talla = talla.replace("\n","").replace(" ","").replace("\t","")
    tallas = talla.split(",")
    return tallas
 

class RepasoitemsItem(scrapy.Item):
    producto = scrapy.Field(
        input_processor = MapCompose(
            transformar_titulo,
        ),
        output_processor = TakeFirst()
    )

    precio = scrapy.Field(
        input_processor = MapCompose(
            transformar_precio,
        ),
        output_processor = TakeFirst()
    )
    
    talla = scrapy.Field(
        input_processor = MapCompose(
            transformar_talla,
        ),
        #output_processor = TakeFirst()
    )


