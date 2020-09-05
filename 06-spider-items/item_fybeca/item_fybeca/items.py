# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst


def transformar_url_imagen(texto):
    url_fybeca = 'https://www.fybeca.com'
    cadena_text = '../..'
    return texto.replace(cadena_text,url_fybeca)


class ProductoFybeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field(
        input_processor = MapCompose( # lista de funciones
            transformar_url_imagen
        ),
        output_processor = TakeFirst()  # Obtiene una lista y con el takefirst solo se toma el primero
    )


    