from itemadapter import ItemAdapter
import json


class JSONLinesPipeline:
    def process_item(self, item, spider):
        formatted_spider_name = spider.name.replace('_', '-')
        data = json.dumps(dict(item)) + '\n'
        with open(f'data/{formatted_spider_name}-data.jl', 'a') as data_file:
            data_file.write(data)
