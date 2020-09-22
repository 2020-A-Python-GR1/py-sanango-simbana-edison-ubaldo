from scrapy.spiders import CSVFeedSpider


class Fifa19(CSVFeedSpider):


    name = 'tech'

    start_urls = [
        'https://people.sc.fsu.edu/~jburkardt/data/csv/trees.csv'
    ]

    #delimiter = ',' # Heredado
    #quotechar = '"' # Heredado
    


    headers = [
        'Index',
        'Girth (in)',
        'Height (ft)',
        'Volume(ft^3)',
    ]


    def parse_row(self, response, row): # Heredado
        #print(type(row))
        with open('tech.txt','a+',encoding='utf-8') as archivo:
            archivo.write(row['Girth (in)'] + ' | ' + row['Height (ft)']  + '\n')


            