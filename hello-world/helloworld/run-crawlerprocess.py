# -*- coding: utf-8 -*-
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from helloworld.spiders import hello
'''
@Author: lu
@Time: 2020/12/17 14:09
@Desc: 
'''
process = CrawlerProcess(settings=get_project_settings()) #如果不传入settings，会默认使用默认配置settings
process.crawl(hello.HelloSpider)
#process.crawl(hello.HelloSpider2)#如果还有其它要启动的爬虫，在这里添加一行代码
#process.crawl(hello.HelloSpide3)#如果还有其它要启动的爬虫，在这里添加一行代码
process.start() # the script will block here until all crawling jobs are finished