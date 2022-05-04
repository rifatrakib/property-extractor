import scrapy
from scrapy.loader import ItemLoader
from webmagnet.items import AutomobileItem


class AutomobileSpider(scrapy.Spider):
    name = 'automobile_spider'
    allowed_domains = ['data.ct.gov']
    api_route = 'https://data.ct.gov/api/id/apne-w8c6.json'
    start_urls = ['https://data.ct.gov/api/id/apne-w8c6.json?$query=select *, :id  |> select count(*) as __count_alias__&$$read_from_nbe=true&$$version=2.1']
    
    def automobile_itemloader(self, data):
        item_data = ItemLoader(item=AutomobileItem(), selector=data)
        
        item_data.add_value('id', data[':id'])
        item_data.add_value('business_name', data.get('business_name', None))
        item_data.add_value('business_address', data.get('business_address', None))
        item_data.add_value('city', data.get('city', None))
        item_data.add_value('state', data.get('state', None))
        item_data.add_value('zip_code', data.get('zip_code', None))
        item_data.add_value('license_num', data.get('license_num', None))
        item_data.add_value('license_type', data.get('license_type', None))
        item_data.add_value('license_expiration', data.get('license_expiration', None))
        item_data.add_value('geo_coordinates', data.get('geocoded_column', None))
        
        return item_data
    
    def parse(self, response):
        number_of_documents = int(response.json()[0]['__count_alias__'])
        for offset in range(0, number_of_documents, 100):
            query = f'select *, :id order by `city` asc offset {offset} limit 100'
            next_url = f'{self.api_route}?$query={query}'
            yield response.follow(next_url, callback=self.automobile_parser)
    
    def automobile_parser(self, response):
        scraped_data = response.json()
        for item in scraped_data:
            item_data = self.automobile_itemloader(item)
            yield item_data.load_item()
