# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.exceptions import DropItem

#### DESDE AQUI SE PUEDE GUARDAR A UNA BASE
 

class TransformarTituloAMinusculas(object):
    def process_item(self,item,spider):
        titulo = item['titulo']
        item['titulo'] = titulo.lower()
        return item


class SoloCapsulasPipeline(object):
    def process_item(self,item,spider):
        titulo = item['titulo'] # aqui igual puede ir la imagen
        if('capsula' not in titulo): # solo se queda si es que el titulo tiene la palabra 'capsula'.
            raise DropItem('No tiene capsula')
        else:
            return item 



class ItemFybecaPipeline:
    def process_item(self, item, spider):
        return item
