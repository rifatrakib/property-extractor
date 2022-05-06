from scrapy.exporters import CsvItemExporter
from itemadapter import ItemAdapter
from scrapy import signals
import json


class JSONLinesPipeline:
    def process_item(self, item, spider):
        formatted_spider_name = spider.name.replace('_', '-')
        data = json.dumps(dict(item)) + '\n'
        with open(f'data/jsonline/{formatted_spider_name}-data.jl', 'a') as data_file:
            data_file.write(data)


class CSVPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline
    
    def spider_opened(self, spider):
        formatted_spider_name = spider.name.replace('_', '-')
        self.file = open(f'data/csv/{formatted_spider_name}-data.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()
    
    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
    
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
