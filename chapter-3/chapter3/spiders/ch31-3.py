# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from chapter3.items import Chapter313Item


class Ch31Spider(CrawlSpider):
	name = 'ch31-3'
	start_urls = [
		'http://quotes.toscrape.com/',
	]
	rules = (
		Rule(link_extractor=LinkExtractor(allow=('quotes.toscrape.com/page/')), callback='parse_page', follow=True),
	)

	def parse_page(self, response):
		print("url_page:", response.url)
		for quote in response.css('.quote'):
			content = quote.css('.text::text').extract_first() #格言内容
			author = quote.css('.author::text').extract_first() #格言作者
			tags = quote.css('.tag::text').extract_first() #格言标签
			item = Chapter313Item(content=content, author=author,tags=tags)
			author_url = response.urljoin(quote.css('span a::attr(href)').extract_first())#作者主页
			print("author_url",author_url)
			#返回作者主页Request，抓取作者生日

			request = scrapy.Request(url=author_url, callback=self.parse_author)
			request.meta['info'] = item #把这里提到的三个字段数据带到下个页面
			yield request


	def parse_author(self,response):
		item = response.meta['info']
		born = response.css('.author-born-date::text').extract_first() #出生年月
		item['born'] = born
		yield item

	def parse_start_url(self, response):
		print('parse_start_url:', response.url)
