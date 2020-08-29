import scrapy 

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)


    def parse(self, response):
        etiqueta_contenedora = response.css(
            'article.product_pod'
        )

        # titulos
        titulos = etiqueta_contenedora.css(
            'h3 > a::text'
        ).extract()
        print("**************TITULOS******************* {}".format(titulos))

        # url
        url = etiqueta_contenedora.css(
            "div.image_container > a > img.thumbnail::attr(src)"
        ).extract()
        print("**************URL********** {}".format(url))


        # stock
        stock = etiqueta_contenedora.css(
            "div.product_price  > p.instock.availability::text"
        ).extract()
        stock_lista = list()
        for i in stock:
            aux = i.split('\n')
            if len(aux) > 2:
                stock_lista.append(aux[2])<class 'float'>
        print("**********STOCK************* {}".format(stock_lista))


        # dinero
        dinero = etiqueta_contenedora.css(
            "div.product_price  > p.price_color::text"
        ).extract()
        dinero_lista = list()
        for i in dinero:
            dinero_lista.append(float(i.split('£')[1]))

        print("*******DINERO*********** {}".format(dinero_lista))
        print(type(dinero_lista[0]))


        # stars
        estrellas = etiqueta_contenedora.css(
            "article.product_pod > p::attr(class)"
        ).extract()
        estrellas_lista = list()
        for i in estrellas:
            estrellas_lista.append(i.split('star-rating ')[1])
        print("**************ESTRELLAS*********** {}".format(estrellas_lista))

        # para ejecutar se hace lo siguiente: 
            # scrapy crawl name  // en este caso name es introduccion_spider


    