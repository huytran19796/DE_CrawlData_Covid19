import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from covid19.spiders.covidhome import CovidhomeSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(CovidhomeSpider)
process.start()