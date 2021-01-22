import scrapy


class Email1Spider(scrapy.Spider):
    name = 'email-1'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://toscrape.com/']

    def parse(self, response):
        pass
