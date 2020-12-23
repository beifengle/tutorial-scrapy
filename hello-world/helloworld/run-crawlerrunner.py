# -*- coding: utf-8 -*-

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from helloworld.spiders import hello
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

'''
@Author: lu
@Time: 2020/12/17 16:46
@Desc: 
'''

configure_logging()#如果不添加，刚scrapy不会有日志输出
runner = CrawlerRunner(settings=get_project_settings())
runner.crawl(hello.HelloSpider)
# runner.crawl(hello.HelloSpider2)#如果有多个爬虫，在这添加
# runner.crawl(hello.HelloSpider3)#如果有多个爬虫，在这添加
d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run() # the script will block here until all crawling jobs are finished