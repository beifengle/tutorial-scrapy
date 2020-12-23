# -*- coding: utf-8 -*-
from scrapy import cmdline

'''
@Author: lu
@Time: 2020/12/17 17:02
@Desc: 
同一个进程下单线程，按代码添加的爬虫顺序地执行
'''


cmdline.execute("scrapy crawl hello".split())
# cmdline.execute("scrapy crawl hello2".split())#如果有多个爬虫，在这添加
# cmdline.execute("scrapy crawl hello3".split())#如果有多个爬虫，在这添加