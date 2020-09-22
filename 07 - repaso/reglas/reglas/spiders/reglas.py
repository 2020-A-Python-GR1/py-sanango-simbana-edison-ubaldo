import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ReglasExtractor(CrawlSpider):
    
    name = 'reglas'


    allowed_domains = [ # heredado
        'asromastore.com',
    ]

    start_urls = [
        'https://www.asromastore.com/it/allenamento.html',
    ]

    segmentos_url_permitidos = ( # con esto se controla que la info solo sea la que se quiere y no se expanda por otros lados
        'allenamento.html',
    )

    segmentos_url_restringidos = (
        'en/',
    )

    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains= allowed_domains,
                allow= segmentos_url_permitidos,
                deny=segmentos_url_restringidos
            ),
            callback= 'parse_page'
        ),
        # parametro vacio
    )

    rules = regla_tres

    def parse_page(self,response):
        nuevos_productos_nombre = response.xpath(
            "/html/body/div[3]/div[2]/div[8]/div/div/div/div/div/div[3]/div/div[1]/div[2]/ul/li/div/div[2]/h3/a/text()"
        ).extract()
        #print("*******************************")
        #print(nuevos_productos_nombre)   

        nuevos_productos_precio = response.xpath(
            "/html/body/div[3]/div[2]/div[8]/div/div/div/div/div/div[3]/div/div[1]/div[2]/ul/li/div/div[2]/div[2]/span/span/text()"
        ).extract()
        nuevos_productos_precios_lista = list()
        for precio in nuevos_productos_precio:
            nuevos_productos_precios_lista.append(float(precio.replace("€\xa0","").replace(",",".")))
        #print("*******************************")
        #print(nuevos_productos_precios_lista)   

        resultado = list(zip(nuevos_productos_nombre, nuevos_productos_precios_lista))
        print("*******************************")
        print(resultado)


        for producto in resultado:
            with open('store_nuevos_productos.txt','a+',encoding='utf-8') as archivo:
                archivo.write(producto[0] + ' | ' + str(producto[1]) + '\n')


