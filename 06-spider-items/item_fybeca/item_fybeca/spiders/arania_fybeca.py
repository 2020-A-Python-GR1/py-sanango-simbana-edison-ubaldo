import scrapy
from item_fybeca.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class AraniaFybeca(scrapy.Spider):
    name = 'fybeca'
    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=150Ypp=25'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url = url)


    def parse(self, response):
        productos = response.css('div.product-tile-inner')
        for producto in productos:
            detalles = producto.css('div.detail')
            tiene_detalles = len(detalles) > 0
            if(tiene_detalles): # valida si existe el detalle del producto
                producto_loder = ItemLoader( # instancia que carga propiedades del item 
                    item=ProductoFybeca(), # clase item
                    selector=producto # selector por defecto
                )

                producto_loder.default_output_processor = TakeFirst() # no guarda como arreglo    

                producto_loder.add_css(
                    'titulo',   # nombre de la propiedad del item
                    'a.name::text' # css que contiene el dato que se le quiere dar al nombre de la propiedad del item
                )
                producto_loder.add_xpath(
                    'imagen',
                    'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src' # xpath que contiene el dato
                )

                yield producto_loder.load_item()
