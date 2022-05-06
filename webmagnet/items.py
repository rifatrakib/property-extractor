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
