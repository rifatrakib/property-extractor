import scrapy


class PropertySpider(scrapy.Spider):
    name = 'property_spider'
    allowed_domains = ['data.ct.gov']
    api_route = 'https://data.ct.gov/api/id/5mzw-sjtu.json'
    query_template = {
        'select': '*, :id',
        'order by': '`listyear` desc, `daterecorded` asc',
        'offset': 0,
        'limit': 100,
    }
    number_of_documents = 0
    start_urls = ['https://data.ct.gov/api/id/5mzw-sjtu.json?$query=select%20*,%20:id%20order%20by%20%60listyear%60%20desc,%20%60daterecorded%60%20asc%20%20|%3E%20select%20count(*)%20as%20__count_alias__&$$read_from_nbe=true&$$version=2.1']
    second_url = api_route + '?$query='
    for key, value in query_template.items():
        second_url = second_url + f'{key} {value} '
    
    def parse(self, response):
        print('--> I am here', response.request.url)
        if response.request.url == self.start_urls[0]:
            print('--> The first url')
            self.number_of_documents = int(response.json()[0]['__count_alias__'])
            print(self.number_of_documents)
            next_url = self.second_url
            yield response.follow(next_url, callback=self.parse)
        else:
            scraped_data = response.json()
            if scraped_data:
                for item in scraped_data:
                    yield item
            
            self.query_template['offset'] += 100
            if self.query_template['offset'] < self.number_of_documents:
                query = '?$query='
                for key, value in self.query_template.items():
                    query = query + f'{key} {value} '
                next_url = self.api_route + query
                print('--> next url', next_url)
                yield response.follow(next_url, callback=self.parse)
            else:
                print('Scraping finished')
