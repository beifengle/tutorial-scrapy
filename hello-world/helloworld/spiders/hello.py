import scrapy
from helloworld.items import HelloworldItem
from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser

class HelloSpider(scrapy.Spider):
    name = 'hello'  #指定此爬虫spider在项目中的唯一名称
    allowed_domains = ['toscrape.com'] #爬取范围
    start_urls = ['http://toscrape.com/'] #抓取起始地址

    def parse(self, response):
        ''' Contracts合约规则
            @url http://toscrape.com/
            @returns items 1 5
            @returns requests 0 1
            @scrapes title
        '''
        # inspect_response(response, self)  #2.8章节 scrapy shell测试用例代码，打断点调试，并进入shell模式
        # open_in_browser(response)##2.8章节 调用浏览器打开下载得到的响应体
        title = response.xpath('//title/text()').extract_first("")
        print("解析提取到title:",title)
        hello_item = HelloworldItem()
        hello_item['title'] = title
        import time
        time.sleep(5)
        # from scrapy.exceptions import CloseSpider
        # raise CloseSpider(reason="大哥，我不想爬取了。")
        yield hello_item
        # yield scrapy.Request(url="http://books.toscrape.com/",  #2.8章节 scrapy parse测试用例代码
        #                       dont_filter=True,
        #                       callback=self.parse_2)

    def parse_2(self, response):
        ''' Contracts合约规则
                    @url http://books.toscrape.com/
                    @returns items 1 5
                    @scrapes title
                '''
        title = response.xpath('//title/text()').extract_first("").strip()
        print("解析提取到title2:", title)
        hello_item = HelloworldItem()
        hello_item['title'] = title
        yield hello_item

    def closed(self, reason):
        print('===爬虫关闭原因===:', reason)
