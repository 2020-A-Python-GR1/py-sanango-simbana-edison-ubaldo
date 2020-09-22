import scrapy
import pandas as pd 


class Repaso(scrapy.Spider):
    name = 'repaso'

    urls = [
        'https://es.wikipedia.org/wiki/Tour_de_Francia'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)


    def parse(self, response):
        
        a = """ # año 
        anio = response.xpath(
            '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr/td[1]/a/text()'
        ).extract()

        print("***********************************")
        print(anio)


        # ganador 
        ganador = response.xpath(
            '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr/td[2]/a/text()'
        ).extract()

        print("***********************************")
        print(ganador)


        # segundo 
        segundo = response.xpath(
            '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr/td[3]/a/text()'
        ).extract()

        print("***********************************")
        print(segundo)


        # tercero
        tercero = response.xpath(
            '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr/td[4]/a/text()'
        ).extract()

        print("***********************************")
        print(tercero) """

        # pais
        paises = response.xpath(
            '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr/td[1]/a/text()'
        ).extract()
        print("***********************************")
        print(paises)

        # victorias
        victorias = response.xpath(
            '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr/td[2]/text()'
        ).extract()

        victoria_lista = list()
        for victoria in victorias:
            victoria = victoria.replace("\n","")
            victoria_lista.append(victoria.split(" ")[0])
        print("***********************************")
        print(victoria_lista)

        # segundo
        segundos = response.xpath(
            '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr/td[3]/text()'
        ).extract()
        segundos_lista = list()
        for segundo in segundos:
            segundo = segundo.replace("\n","")
            segundos_lista.append(segundo)
        print("***********************************")
        print(segundos_lista)


        # terceros
        terceros = response.xpath(
            '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr/td[4]/text()'
        ).extract()
        terceros_lista = list()
        for tercer in terceros:
            tercer = tercer.replace("\n","")
            terceros_lista.append(tercer)        
        print("***********************************")
        print(terceros_lista)


        # totales
        totales = response.xpath(
            '//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr/td[5]/text()'
        ).extract()
        totales_lista = list()
        for total in totales:
            total = total.replace("\n","")
            totales_lista.append(total)    
        print("***********************************")
        print(totales_lista)



        final = pd.DataFrame(zip(paises, 
                                victoria_lista, 
                                segundos_lista, 
                                terceros_lista, 
                                totales_lista), columns=['pais','victorias','segundos','terceros','total'])

        print("*********************************************")
        print(final)

