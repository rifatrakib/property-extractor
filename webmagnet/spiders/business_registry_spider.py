import scrapy
from scrapy.loader import ItemLoader
from webmagnet.items import BusinessItem


class BusinessSpider(scrapy.Spider):
    name = 'business_spider'
    allowed_domains = ['data.ct.gov']
    api_route = 'https://data.ct.gov/api/id/n7gp-d28j.json'
    start_urls = ['https://data.ct.gov/api/id/n7gp-d28j.json?$query=select%20*,%20:id%20%20|%3E%20select%20count(*)%20as%20__count_alias__&$$read_from_nbe=true&$$version=2.1']
    
    def business_itemloader(self, data):
        item_data = ItemLoader(item=BusinessItem(), selector=data)
        
        item_data.add_value('id', data[':id'])
        item_data.add_value('name', data.get('name', None))
        item_data.add_value('business_type', data.get('business_type', None))
        item_data.add_value('status', data.get('status', None))
        item_data.add_value('sub_status', data.get('sub_status', None))
        item_data.add_value('account_number', data.get('accountnumber', None))
        item_data.add_value('annual_report_due_date', data.get('annual_report_due_date', None))
        item_data.add_value('began_transacting_in_ct', data.get('began_transacting_in_ct', None))
        item_data.add_value('business_street', data.get('billingstreet', None))
        item_data.add_value('business_unit', data.get('billing_unit', None))
        item_data.add_value('business_city', data.get('billingcity', None))
        item_data.add_value('business_country', data.get('billingcountry', None))
        item_data.add_value('business_zip_code', data.get('billingpostalcode', None))
        item_data.add_value('business_state', data.get('billingstate', None))
        item_data.add_value('business_email_address', data.get('business_email_address', None))
        item_data.add_value('business_name_in_state_country', data.get('business_name_in_state_country', None))
        item_data.add_value('citizenship', data.get('citizenship', None))
        item_data.add_value('country_formation', data.get('country_formation', None))
        item_data.add_value('registration_date', data.get('date_registration', None))
        item_data.add_value('formation_place', data.get('formation_place', None))
        item_data.add_value('state_or_territory_formation', data.get('state_or_territory_formation', None))
        item_data.add_value('date_of_organization_meeting', data.get('date_of_organization_meeting', None))
        item_data.add_value('dissolution_date', data.get('dissolution_date', None))
        item_data.add_value('mail_jurisdiction', data.get('mail_jurisdiction', None))
        item_data.add_value('mailing_address', data.get('mailing_address', None))
        item_data.add_value('mailing_international_address', data.get('mailing_international_address', None))
        item_data.add_value('mailing_jurisdiction_address', data.get('mailing_jurisdiction_address', None))
        item_data.add_value('mailing_jurisdiction_business_street', data.get('mailing_jurisdiction_2', None))
        item_data.add_value('mailing_jurisdiction_business_unit', data.get('mailing_jurisdiction_3', None))
        item_data.add_value('mailing_jurisdiction_business_city', data.get('mailing_jurisdiction', None))
        item_data.add_value('mailing_jurisdiction_business_state', data.get('mailing_jurisdiction_1', None))
        item_data.add_value('mailing_jurisdiction_business_zip_code', data.get('mailing_jurisdiction_4', None))
        item_data.add_value('mailing_jurisdiction_business_country', data.get('mailing_jurisdiction_country', None))
        item_data.add_value('woman_owned_organization', data.get('woman_owned_organization', None))
        item_data.add_value('veteran_owned_organization', data.get('veteran_owned_organization', None))
        item_data.add_value('minority_owned_organization', data.get('minority_owned_organization', None))
        item_data.add_value('disable_person_owned_organization', data.get('org_owned_by_person_s_with', None))
        item_data.add_value('category_survey_email_address', data.get('category_survey_email_address', None))
        item_data.add_value('naics_code', data.get('naics_code', None))
        item_data.add_value('naics_sub_code', data.get('naics_sub_code', None))
        item_data.add_value('office_jurisdiction_address', data.get('office_jurisdiction_address', None))
        item_data.add_value('office_jurisdiction_business_street', data.get('office_jurisdiction_2', None))
        item_data.add_value('office_jurisdiction_business_unit', data.get('office_jurisdiction_3', None))
        item_data.add_value('office_jurisdiction_business_city', data.get('office_jurisdiction', None))
        item_data.add_value('office_jurisdiction_business_state', data.get('office_jurisdiction_1', None))
        item_data.add_value('office_jurisdiction_business_zip_code', data.get('office_jurisdiction_4', None))
        item_data.add_value('office_jurisdiction_country', data.get('office_in_jurisdiction_country', None))
        item_data.add_value('reason_for_administrative_dissolution', data.get('reason_for_administrative', None))
        item_data.add_value('record_address', data.get('record_address', None))
        item_data.add_value('records_address_street', data.get('records_address_street', None))
        item_data.add_value('records_address_unit', data.get('records_address_unit', None))
        item_data.add_value('records_address_city', data.get('records_address_city', None))
        item_data.add_value('records_address_state', data.get('records_address_state', None))
        item_data.add_value('records_address_zip_code', data.get('records_address_zip_code', None))
        item_data.add_value('records_address_country', data.get('records_address_country', None))
        item_data.add_value('created_on', data.get('create_dt', None))
        item_data.add_value('total_authorized_shares', data.get('total_authorized_shares', None))
        
        return item_data
    
    def parse(self, response):
        number_of_documents = int(response.json()[0]['__count_alias__'])
        for offset in range(0, 1000, 100):
            query = f'select *, :id order by `id` asc offset {offset} limit 100'
            next_url = f'{self.api_route}?$query={query}'
            yield response.follow(next_url, callback=self.business_parser)
    
    def business_parser(self, response):
        scraped_data = response.json()
        for item in scraped_data:
            item_data = self.business_itemloader(item)
            yield item_data.load_item()
