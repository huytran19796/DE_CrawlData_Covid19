import scrapy
import utility
import items

# The spider to crawl data from static home page of the website
class CovidhomeSpider(scrapy.Spider):
    name = "covidhome"
    allowed_domains = ["ncov.moh.gov.vn"]
    start_urls = ["https://ncov.moh.gov.vn/vi/web/guest/dong-thoi-gian"]

    def parse(self, response):
        result = items.Covid19_Infor()
        for data in response.xpath("//li[@class='kbwscwl clearfix cc timeline-item']"):
            result['date'],  result['month'], result['year'] = utility.get_date(data.xpath(".//@data-date").get())
            result['sum'] = utility.get_newCase(data.xpath(".//p[1]/text()").get())
            result['detail'] = utility.get_detail_newCase(data.xpath(".//p[2]/text()").get())
            yield result