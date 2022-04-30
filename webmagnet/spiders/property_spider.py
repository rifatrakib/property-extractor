import scrapy


class PropertySpiderSpider(scrapy.Spider):
    name = 'property_spider'
    allowed_domains = ['data.ct.gov']
    start_urls = ['http://data.ct.gov/']
    
    def parse(self, response):
        pass
