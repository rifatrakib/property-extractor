import subprocess
import pandas as pd


def invoke_spider(spider_name):
    full_command = f'scrapy crawl {spider_name} '
    print(full_command)
    subprocess.run(full_command, shell=True)


def file_segmentation(spider):
    identifier = spider.replace('spider', '').replace('_', '')
    df = pd.read_csv(f'data/csv/{identifier}-data.csv', dtype='object')
    row_count = df.shape[0]
    for cut_off in range(0, row_count, 10000):
        segment = df.iloc[cut_off:cut_off+10000, :]
        segment.to_csv(f'segmented-data/csv/{identifier}/{identifier}-data-{cut_off}-{cut_off+10000}.csv', sep='|')
        segment.to_json(f'segmented-data/json/{identifier}/{identifier}-data-{cut_off}-{cut_off+10000}.json', orient='records')
        segment.to_json(f'segmented-data/jsonline/{identifier}/{identifier}-data-{cut_off}-{cut_off+10000}.jl', orient='records', lines=True)


if __name__ == '__main__':
    spider_parameters = {
        'property_spider': False,
        'automobile_spider': False,
        'business_spider': False,
    }
    for spider, crawl in spider_parameters.items():
        if crawl:
            invoke_spider(spider)
        file_segmentation(spider)
