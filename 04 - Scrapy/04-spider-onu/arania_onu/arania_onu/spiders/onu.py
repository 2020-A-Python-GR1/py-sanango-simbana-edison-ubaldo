import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'crawl_onu' # heredado

    allowed_domains = [ # heredado
        'un.org'
    ]

    start_urls = [
        'https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html'
    ]

    regla_uno = (
        Rule(
            LinkExtractor(),
            callback= 'parse_page' # nombre de la funcion que se ejecuta para parsear
        ),
        # segundo parametro vacio
    )

    #rules = regla_uno

    segmentos_url_permitidos = ( # con esto se controla que la info solo sea la que se quiere y no se expanda por otros lados
        'funds-programmes-specialized-agencies-and-others'
    )


    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains= allowed_domains,
                allow= segmentos_url_permitidos
            ),
            callback= 'parse_page'
        ),
        # parametro vacio
    )

    #rules = regla_dos


    segmentos_url_restringidos = (
        'ar/sections',
        'zh/sections',
        'ru/sections'
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
        lista_programas = response.css(
            'div.content > div.field.field-name-body.field-type-text-with-summary.field-label-hidden > div.field-items > div.field-item > h4::text'
        ).extract()

        for agencia in lista_programas:
            with open('onu_agencias1.txt','a+',encoding='utf-8') as archivo:
                archivo.write(agencia + '\n')


