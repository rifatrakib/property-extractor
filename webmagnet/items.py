import scrapy
from datetime import datetime
from nltk.tokenize import word_tokenize
from itemloaders.processors import TakeFirst, MapCompose

replace_map = {
    'RT': 'Route',
}


def replace_underscores(item):
    return item.replace('_', '-').strip()


def format_as_money(item):
    number = float(item)
    return round(number, 2)


def format_as_ratio(item):
    number = float(item)
    return round(number, 6)


def format_titlecase_string(item):
    return item.strip().title()


def format_capitalized_string(item):
    return item.strip().capitalize()


def format_timestamp(item):
    timestamp = item.strip()
    return datetime.fromisoformat(timestamp).isoformat()


def replace_shorthands(item):
    processed_item = []
    for word in word_tokenize(item):
        if word in replace_map:
            processed_item.append(replace_map[word])
        else:
            processed_item.append(word)
    
    return ' '.join(processed_item)


class PropertyItem(scrapy.Item):
    id = scrapy.Field(
        input_processor=MapCompose(replace_underscores),
        output_processor=TakeFirst()
    )
    serial_number = scrapy.Field(
        input_processor=MapCompose(str.strip, int),
        output_processor=TakeFirst()
    )
    list_year = scrapy.Field(
        input_processor=MapCompose(str.strip, int),
        output_processor=TakeFirst()
    )
    date_recorded = scrapy.Field(
        input_processor=MapCompose(format_timestamp),
        output_processor=TakeFirst()
    )
    town = scrapy.Field(
        input_processor=MapCompose(format_titlecase_string),
        output_processor=TakeFirst()
    )
    address = scrapy.Field(
        input_processor=MapCompose(format_titlecase_string),
        output_processor=TakeFirst()
    )
    assessed_value = scrapy.Field(
        input_processor=MapCompose(str.strip, format_as_money),
        output_processor=TakeFirst()
    )
    sales_amount = scrapy.Field(
        input_processor=MapCompose(str.strip, format_as_money),
        output_processor=TakeFirst()
    )
    sales_ratio = scrapy.Field(
        input_processor=MapCompose(str.strip, format_as_ratio),
        output_processor=TakeFirst()
    )
    property_type = scrapy.Field(
        input_processor=MapCompose(format_titlecase_string),
        output_processor=TakeFirst()
    )
    residential_type = scrapy.Field(
        input_processor=MapCompose(format_titlecase_string),
        output_processor=TakeFirst()
    )
    non_use_code = scrapy.Field(
        input_processor=MapCompose(format_titlecase_string),
        output_processor=TakeFirst()
    )
    remarks = scrapy.Field(
        input_processor=MapCompose(format_capitalized_string),
        output_processor=TakeFirst()
    )
    opm_remarks = scrapy.Field(
        input_processor=MapCompose(format_capitalized_string),
        output_processor=TakeFirst()
    )
    geo_coordinates = scrapy.Field()


class AutomobileItem(scrapy.Item):
    id = scrapy.Field(
        input_processor=MapCompose(replace_underscores),
        output_processor=TakeFirst()
    )
    business_name = scrapy.Field(
        input_processor=MapCompose(format_titlecase_string),
        output_processor=TakeFirst()
    )
    business_address = scrapy.Field(
        input_processor=MapCompose(replace_shorthands, format_titlecase_string),
        output_processor=TakeFirst()
    )
    city = scrapy.Field(
        input_processor=MapCompose(format_titlecase_string),
        output_processor=TakeFirst()
    )
    state = scrapy.Field(
        input_processor=MapCompose(format_titlecase_string),
        output_processor=TakeFirst()
    )
    zip_code = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    license_num = scrapy.Field(output_processor=TakeFirst())
    license_type = scrapy.Field(
        input_processor=MapCompose(format_titlecase_string),
        output_processor=TakeFirst()
    )
    license_expiration = scrapy.Field(
        input_processor=MapCompose(format_timestamp),
        output_processor=TakeFirst()
    )
    geo_coordinates = scrapy.Field()


class BusinessItem(scrapy.Item):
    id = scrapy.Field() # :id (str)
    name = scrapy.Field() # name (str)
    business_type = scrapy.Field() # business_type (str)
    status = scrapy.Field() # status (str)
    sub_status = scrapy.Field() # sub_status (str)
    account_number = scrapy.Field() # accountnumber (str)
    annual_report_due_date = scrapy.Field() # annual_report_due_date (datetime)
    began_transacting_in_ct = scrapy.Field() # began_transacting_in_ct (datetime)
    business_street = scrapy.Field() # billingstreet (str)
    business_unit = scrapy.Field() # billing_unit (int)
    business_city = scrapy.Field() # billingcity (str)
    business_country = scrapy.Field() # billingcountry (str)
    business_zip_code = scrapy.Field() # billingpostalcode (str)
    business_state = scrapy.Field() # billingstate (str)
    business_email_address = scrapy.Field() # business_email_address (str)
    business_name_in_state_country = scrapy.Field() # business_name_in_state_country (str)
    citizenship = scrapy.Field() # citizenship (str)
    country_formation = scrapy.Field() # country_formation (str)
    registration_date = scrapy.Field() # date_registration (str)
    formation_place = scrapy.Field() # formation_place (str)
    state_or_territory_formation = scrapy.Field() # state_or_territory_formation (str)
    date_of_organization_meeting = scrapy.Field() # date_of_organization_meeting (datetime)
    dissolution_date = scrapy.Field() # dissolution_date (datetime)
    mail_jurisdiction = scrapy.Field() # mail_jurisdiction (str)
    mailing_address = scrapy.Field() # mailing_address (str)
    mailing_international_address = scrapy.Field() # mailing_international_address (str)
    mailing_jurisdiction_address = scrapy.Field() # mailing_jurisdiction_address (str)
    mailing_jurisdiction_business_street = scrapy.Field() # mailing_jurisdiction_2 (str)
    mailing_jurisdiction_business_unit = scrapy.Field() # mailing_jurisdiction_3 (str)
    mailing_jurisdiction_business_city = scrapy.Field() # mailing_jurisdiction (str)
    mailing_jurisdiction_business_state = scrapy.Field() # mailing_jurisdiction_1 (str)
    mailing_jurisdiction_business_zip_code = scrapy.Field() # mailing_jurisdiction_4 (str)
    mailing_jurisdiction_business_country = scrapy.Field() # mailing_jurisdiction_country (str)
    woman_owned_organization = scrapy.Field() # woman_owned_organization (bool)
    veteran_owned_organization = scrapy.Field() # veteran_owned_organization (bool)
    minority_owned_organization = scrapy.Field() # minority_owned_organization (bool)
    disable_person_owned_organization = scrapy.Field() # org_owned_by_person_s_with (bool)
    category_survey_email_address = scrapy.Field() # category_survey_email_address (str)
    naics_code = scrapy.Field() # naics_code (str)
    naics_sub_code = scrapy.Field() # naics_sub_code (str)
    office_jurisdiction_address = scrapy.Field() # office_jurisdiction_address (str)
    office_jurisdiction_business_street = scrapy.Field() # office_jurisdiction_2 (str)
    office_jurisdiction_business_unit = scrapy.Field() # office_jurisdiction_3 (str)
    office_jurisdiction_business_city = scrapy.Field() # office_jurisdiction (str)
    office_jurisdiction_business_state = scrapy.Field() # office_jurisdiction_1 (str)
    office_jurisdiction_business_zip_code = scrapy.Field() # office_jurisdiction_4 (str)
    office_jurisdiction_country = scrapy.Field() # office_in_jurisdiction_country (str)
    reason_for_administrative_dissolution = scrapy.Field() # reason_for_administrative (str)
    record_address = scrapy.Field() # record_address (str)
    records_address_street = scrapy.Field() # records_address_street (str)
    records_address_unit = scrapy.Field() # records_address_unit (str)
    records_address_city = scrapy.Field() # records_address_city (str)
    records_address_state = scrapy.Field() # records_address_state (str)
    records_address_zip_code = scrapy.Field() # records_address_zip_code (str)
    records_address_country = scrapy.Field() # records_address_country (str)
    created_on = scrapy.Field() # create_dt (datetime)
    total_authorized_shares = scrapy.Field() # total_authorized_shares (int)
