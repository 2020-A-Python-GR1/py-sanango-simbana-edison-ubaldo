import scrapy 

class IntroSpider(scrapy.Spider):
    name = 'fybeca_spider'

    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=639&s=0&pp=25'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)


    def parse(self, response):
        etiqueta_contenedora = response.css(
            'div.product-tile-inner'
        )

 
        
        
        
        
        
        # para ejecutar se hace lo siguiente: 
            # scrapy crawl name  // en este caso name es introduccion_spider


    