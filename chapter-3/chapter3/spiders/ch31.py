import scrapy
import time
from chapter3.items import Chapter3Item
from scrapy.exceptions import CloseSpider

class Ch31Spider(scrapy.Spider):
    name = 'ch31'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://toscrape.com/']

    def parse(self, response):
        title = response.xpath('//title/text()').extract_first("")
        print("解析提取到title:",title)
        hello_item = Chapter3Item()
        hello_item['title'] = title
        time.sleep(5) #方便测试Ctrl-C时reason信息
        # raise CloseSpider(reason="大哥，我不想爬取了。")
        yield hello_item


    def closed(self, reason):
        print('===爬虫关闭原因===:', reason)