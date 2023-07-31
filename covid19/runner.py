import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.covidhome import CovidhomeSpider
from spiders.covidapi import CovidapiSpider

settings = get_project_settings()
process = CrawlerProcess(settings)
process.crawl(CovidhomeSpider)
process.crawl(CovidapiSpider)
process.start()  # the script will block here until all crawling jobs are finished