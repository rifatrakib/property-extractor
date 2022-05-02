import scrapy
from datetime import datetime
from itemloaders.processors import TakeFirst, MapCompose



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


class PropertyItem(scrapy.Item):
    id = scrapy.Field(input_processor=MapCompose(replace_underscores), output_processor=TakeFirst())
    serial_number = scrapy.Field(input_processor=MapCompose(str.strip, int), output_processor=TakeFirst())
    list_year = scrapy.Field(input_processor=MapCompose(str.strip, int), output_processor=TakeFirst())
    date_recorded = scrapy.Field(input_processor=MapCompose(format_timestamp), output_processor=TakeFirst())
    town = scrapy.Field(input_processor=MapCompose(format_titlecase_string), output_processor=TakeFirst())
    address = scrapy.Field(input_processor=MapCompose(format_titlecase_string), output_processor=TakeFirst())
    assessed_value = scrapy.Field(input_processor=MapCompose(str.strip, format_as_money), output_processor=TakeFirst())
    sales_amount = scrapy.Field(input_processor=MapCompose(str.strip, format_as_money), output_processor=TakeFirst())
    sales_ratio = scrapy.Field(input_processor=MapCompose(str.strip, format_as_ratio), output_processor=TakeFirst())
    property_type = scrapy.Field(input_processor=MapCompose(format_titlecase_string), output_processor=TakeFirst())
    residential_type = scrapy.Field(input_processor=MapCompose(format_titlecase_string), output_processor=TakeFirst())
    non_use_code = scrapy.Field(input_processor=MapCompose(format_titlecase_string), output_processor=TakeFirst())
    remarks = scrapy.Field(input_processor=MapCompose(format_capitalized_string), output_processor=TakeFirst())
    opm_remarks = scrapy.Field(input_processor=MapCompose(format_capitalized_string), output_processor=TakeFirst())
    geo_coordinates = scrapy.Field()
