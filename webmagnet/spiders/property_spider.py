import scrapy
from scrapy.loader import ItemLoader
from webmagnet.items import PropertyItem


class PropertySpider(scrapy.Spider):
    name = 'property_spider'
    allowed_domains = ['data.ct.gov']
    api_route = 'https://data.ct.gov/api/id/5mzw-sjtu.json'
    start_urls = ['https://data.ct.gov/api/id/5mzw-sjtu.json?$query=select%20*,%20:id%20order%20by%20%60listyear%60%20desc,%20%60daterecorded%60%20asc%20%20|%3E%20select%20count(*)%20as%20__count_alias__&$$read_from_nbe=true&$$version=2.1']
    
    def property_itemloader(self, data):
        item_data = ItemLoader(item=PropertyItem(), selector=data)
        
        item_data.add_value('id', data[':id'])
        item_data.add_value('serial_number', data.get('serialnumber', None))
        item_data.add_value('list_year', data.get('listyear', None))
        item_data.add_value('date_recorded', data.get('daterecorded', None))
        item_data.add_value('town', data.get('town', None))
        item_data.add_value('address', data.get('address', None))
        item_data.add_value('assessed_value', data.get('assessedvalue', None))
        item_data.add_value('sales_amount', data.get('saleamount', None))
        item_data.add_value('sales_ratio', data.get('salesratio', None))
        item_data.add_value('property_type', data.get('propertytype', None))
        item_data.add_value('residential_type', data.get('residentialtype', None))
        item_data.add_value('non_use_code', data.get('nonusecode', None))
        item_data.add_value('remarks', data.get('remarks', None))
        item_data.add_value('opm_remarks', data.get('opm_remarks', None))
        item_data.add_value('geo_coordinates', data.get('geo_coordinates', None))
        
        return item_data
    
    def parse(self, response):
        number_of_documents = int(response.json()[0]['__count_alias__'])
        for offset in range(0, number_of_documents, 100):
            query = f'select *, :id order by `listyear` desc, `daterecorded` asc offset {offset} limit 100'
            next_url = f'{self.api_route}?$query={query}'
            yield response.follow(next_url, callback=self.property_parser)
    
    def property_parser(self, response):
        scraped_data = response.json()
        for item in scraped_data:
            item_data = self.property_itemloader(item)
            yield item_data.load_item()
