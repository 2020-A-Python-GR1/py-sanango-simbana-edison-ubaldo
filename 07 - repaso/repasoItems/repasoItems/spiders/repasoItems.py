import scrapy 
from repasoItems.items import RepasoitemsItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AsRomaItems(CrawlSpider):
    name = 'asromaitems'

    urls = [
        'https://www.asromastore.com/it/allenamento.html'
    ]


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

        items = response.xpath(
            '/html/body/div[3]/div[2]/div[8]/div/div/div/div/div/div[3]/div/div[1]/div[2]/ul/li'
        )

        for item in items:

            objeto = item.xpath('div/div[2]')   #item.xpath('div/div[2]/h3/a/text()')
            #precioaa = item.xpath('div/div[2]/div[2]/span/span/text()')
            if(objeto):
                print("************************************")
                print(objeto)
                producto_loder = ItemLoader(
                    item= RepasoitemsItem(),
                    selector=item
                )

                #producto_loder.default_output_processor = TakeFirst()

                producto_loder.add_xpath(
                    'producto',
                    'div/div[2]/h3/a/text()'
                )

                producto_loder.add_xpath(
                    'precio',
                    'div/div[2]/div[2]/span/span/text()'
                )

                producto_loder.add_xpath(
                    'talla',
                    'div/div[2]/div[3]/div/div[2]/text()'
                )

                yield producto_loder.load_item()



                                                  # /html/body/div[3]/div[2]/div[8]/div/div/div/div/div/div[3]/div/div[1]/div[2]/ul/li[5]/div/div[2]/div[3]/div/div[2]

        #nuevos_productos_precio = response.xpath("/html/body/div[3]/div[2]/div[8]/div/div/div/div/div/div[3]/div/div[1]/div[2]/ul/li/div/div[2]/div[2]/span/span/text()").extract()
