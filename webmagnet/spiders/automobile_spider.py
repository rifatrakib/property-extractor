import scrapy


class AutomobileSpider(scrapy.Spider):
    name = 'automobile_spider'
    allowed_domains = ['data.ct.gov']
    api_route = 'https://data.ct.gov/api/id/apne-w8c6.json'
    start_urls = ['https://data.ct.gov/api/id/apne-w8c6.json?$query=select *, :id  |> select count(*) as __count_alias__&$$read_from_nbe=true&$$version=2.1']
    
    def parse(self, response):
        number_of_documents = int(response.json()[0]['__count_alias__'])
        for offset in range(0, number_of_documents, 100):
            query = f'select *, :id order by `city` asc offset {offset} limit 100'
            next_url = f'{self.api_route}?$query={query}'
            yield response.follow(next_url, callback=self.automobile_parser)
    
    def automobile_parser(self, response):
        scraped_data = response.json()
        for item in scraped_data:
            yield {
                'id': item.get(':id', None),
                'business_address': item.get('business_address', None),
                'business_name': item.get('business_name', None),
                'city': item.get('city', None),
                'geo_location': item.get('geocoded_column', None),
                'license_expiration': item.get('license_expiration', None),
                'license_num': item.get('license_num', None),
                'license_type': item.get('license_type', None),
                'state': item.get('state', None),
                'zip_code': item.get('zip_code', None),
            }
