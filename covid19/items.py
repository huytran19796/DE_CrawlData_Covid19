# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Covid19Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Covid19_Infor(scrapy.Item):
    date = scrapy.Field()
    month = scrapy.Field()
    year = scrapy.Field()
    sum = scrapy.Field()
    detail = scrapy.Field()