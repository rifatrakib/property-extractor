import subprocess


def invoke_spider(spider_name):
    full_command = f'scrapy crawl {spider_name} '
    print(full_command)
    subprocess.run(full_command, shell=True)


if __name__ == '__main__':
    spider_parameters = {
        'property_spider': True,
        'automobile_spider': True,
        'business_spider': True,
    }
    for spider, crawl in spider_parameters.items():
        if crawl:
            invoke_spider(spider)
