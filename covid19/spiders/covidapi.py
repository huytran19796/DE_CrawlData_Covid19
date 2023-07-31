import scrapy
import utility
import items

# The spider to crawl data from API of the website
class CovidapiSpider(scrapy.Spider):
    name = "covidapi"
    allowed_domains = ["covid19.gov.vn"]
    current_page = 2
    start_urls = [f"https://covid19.gov.vn/timelinebigstory/1d44b380-0adb-11ec-bf1c-e9c9e7c491f4/{current_page}.htm"]

    def parse(self, response):
        result = items.Covid19_Infor()
        for data in response.xpath("//li[@class='kbwscwl clearfix cc timeline-item']"):
            date, month, year = utility.get_date(data.xpath(".//@data-date").get())
            p = data.xpath(".//p[1]/text()").get()
            if p: 
                sum = utility.get_newCase(data.xpath(".//p[1]/text()").get())
                detail = utility.get_detail_newCase(data.xpath(".//p[2]/text()").get())
            else:
                sum = utility.get_newCase(data.xpath(".//div[1]/span/text()").get())
                detail = utility.get_detail_newCase(data.xpath(".//div[2]/text()").get())

            result['date'] = date
            result['month'] = month
            result['year'] = year
            result['sum'] = sum
            result['detail'] = detail
            yield result
        if self.current_page < 15:
            self.current_page += 1
            yield scrapy.Request(url=f"https://covid19.gov.vn/timelinebigstory/1d44b380-0adb-11ec-bf1c-e9c9e7c491f4/{self.current_page}.htm")
