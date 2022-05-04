import subprocess


def invoke_spider(spider_name, **kwargs):
    full_command = f'scrapy crawl {spider_name} '
    for key, value in kwargs.items():
        full_command = full_command + f'-{key} {value} '
    
    print(full_command)
    subprocess.run(full_command, shell=True)


if __name__ == '__main__':
    spider_parameters = {
        'property_spider': {
            'output': {'O': 'data/property-sales-data.jl'},
            'crawl': False,
        },
        'automobile_spider': {
            'output': {'O': 'data/automobile-repair-dealer-data.jl'},
            'crawl': False,
        }
    }
    for spider, parameters in spider_parameters.items():
        if parameters['crawl']:
            invoke_spider(spider, **parameters['output'])
