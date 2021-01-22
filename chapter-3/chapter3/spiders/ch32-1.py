import scrapy
import time
from chapter3.items import Chapter3Item
from scrapy.exceptions import CloseSpider


class Ch32Spider(scrapy.Spider):
    name = 'ch32'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://toscrape.com/']

    def parse(self, response):
        title = response.css('title')
        print("解析提取到title1:", title)
        # print(dir(response.css('title::text')))
        title = response.xpath('//title')
        print("解析提取到title2:", title)
        title = response.xpath('//title/text()').extract()
        print("解析提取到title3:",title)
        title = response.xpath('//title/text()').extract_first()
        print("解析提取到title4:",title)
        title = response.xpath('//title/text()').re('(Scraping.*?Sandbox)')
        print("解析提取到title5:",title)
        hello_item = Chapter3Item()
        hello_item['title'] = title
        yield hello_item


    def closed(self, reason):
        print('===爬虫关闭原因===:', reason)