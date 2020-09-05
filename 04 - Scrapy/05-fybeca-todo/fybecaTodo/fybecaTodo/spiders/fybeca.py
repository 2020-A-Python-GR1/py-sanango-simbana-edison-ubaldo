import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import pandas as pd

class FybecaCrawl(CrawlSpider):
    name = 'crawl_fybeca' # heredado

    allowed_domains = [ # heredado
        'fybeca.com'
    ]

    cantidad = '5000'
    
    start_urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=446&pp={}&s=-1'.format(cantidad),
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=537&pp={}&s=-1'.format(cantidad),
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=627&pp={}&s=-1'.format(cantidad),
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=558&pp={}&s=-1'.format(cantidad),
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=489&pp={}&s=-1'.format(cantidad),
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=562&pp={}&s=-1'.format(cantidad),
    ]

    segmentos_url_permitidos = ( # con esto se controla que la info solo sea la que se quiere y no se expanda por otros lado
        'cat=446&pp={}&s=-1'.format(cantidad),
        'cat=537&pp={}&s=-1'.format(cantidad),
        'cat=627&pp={}&s=-1'.format(cantidad),
        'cat=558&pp={}&s=-1'.format(cantidad),
        'cat=489&pp={}&s=-1'.format(cantidad),
        'cat=562&pp={}&s=-1'.format(cantidad),
    )

    segmentos_url_restringidos = (
        'pages/detail.jsf'
    )

    regla = (
        Rule(
            LinkExtractor(
                allow_domains= allowed_domains,
                allow= segmentos_url_permitidos, #,deny=segmentos_url_restringidos
                deny=segmentos_url_restringidos,
            ),
            callback= 'parse_page'
        ),
        # parametro vacio
    )

    rules = regla


    def parse_page(self,response):

        etiqueta_contenedora = response.css(
            'div.product-tile-inner'
        )

        # nombres productos
        productos = list(etiqueta_contenedora.css(
            "a.name::text"
        ).extract())

        print("TAMAÑO DE PRODUCTOS:{}".format(len(productos)))
        # imagen
        url = list(etiqueta_contenedora.css(
            "div.detail > a.image > img#gImg.productImage::attr(src)"
        ).extract())

        # precio original 
        precio_original = etiqueta_contenedora.css(
            "div.detail > div.side > div.price::attr(data-bind)"
        ).extract()  

        # precio miembro
        precio_miembro = list(etiqueta_contenedora.css(
            "div.detail > div.side > div.price-member > div::attr(data-bind)"
        ).extract())
    
        # limpieza de datos

        precio_miembro_final = list()
        for i in precio_miembro:
            precio = float(i.replace("text:'$' + (","").replace(").formatMoney(2, '.', ',')",""))
            precio_miembro_final.append(precio)


        precio_original_final = list()
        for i in precio_original:
            precio = float(i.replace("text:'$' + (","").replace(").formatMoney(2, '.', ',')",""))
            precio_original_final.append(precio)      


        resultado = pd.DataFrame(zip(productos,
                                    url,
                                    precio_original_final, 
                                    precio_miembro_final), columns=['Productos','Imagen','Precio normal', 'Precio miembro'])

        
        resultado['Diferencia precios'] = resultado['Precio normal'] - resultado['Precio miembro']

        resultado.to_csv(path_or_buf='./data.csv',header=False,index=True,mode='a')