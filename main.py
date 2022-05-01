import subprocess


def invoke_spider(spider_name, **kwargs):
    full_command = f'scrapy crawl {spider_name} '
    for key, value in kwargs.items():
        full_command = full_command + f'-{key} {value} '
    
    print(full_command)
    subprocess.run(full_command, shell=True)


if __name__ == '__main__':
    parameters = {
        'o': 'data/property-sales-data.jl'
    }
    spider_name = 'property_spider'
    invoke_spider(spider_name, **parameters)
