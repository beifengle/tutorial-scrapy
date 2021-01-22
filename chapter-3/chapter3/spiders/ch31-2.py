import scrapy
from chapter3.items import Chapter3Item

class Ch31Spider(scrapy.Spider):
    name = 'ch31-2'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://toscrape.com/']

    def __init__(self, name=None,*args, **kwargs):
        super(Ch31Spider, self).__init__(*args, **kwargs)
        self.name = name

    def parse(self, response):
        title = response.xpath('//title/text()').extract_first("")
        print("解析提取到title:",title)
        print("name:",self.name)
        hello_item = Chapter3Item()
        hello_item['title'] = title
        yield hello_item


    def closed(self, reason):
        print('===爬虫关闭原因===:', reason)