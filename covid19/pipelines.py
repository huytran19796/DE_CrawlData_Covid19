# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class Covid19Pipeline:
    def __init__(self):
        self.connection = pymongo.MongoClient("mongodb://localhost:27017/")
        database = self.connection['covid_data']
        self.collection = database['raw_data']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
