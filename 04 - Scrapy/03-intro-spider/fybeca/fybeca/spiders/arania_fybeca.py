import scrapy 
import pandas as pd


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

        # nombres productos
        productos = list(etiqueta_contenedora.css(
            "a.name::text"
        ).extract())

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
        #resultado = resultado.sort_values(by='Diferencia precios',ascending=False)
        print(resultado)


        # RESPUESTAS
        
        # cual es el item con mayor y menor precio -- por precio normales
        mayor_precio = resultado.iloc[resultado['Precio normal'].idxmax()]
        print("ITEM CON MAYOR PRECIO NORMAL:")
        print(mayor_precio)

        menor_precio = resultado.iloc[resultado['Precio normal'].idxmin()]
        print("ITEM CON MENOR PRECIO NORMAL:")
        print(menor_precio)

        # cuanto ahorramos si compramos todo como afiliado
        ahorrado = resultado.sum()
        print("AL COMPRAR COMO AFILIADO SE AHORRA:{}".format(ahorrado['Diferencia precios']))

