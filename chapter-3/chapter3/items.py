# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Chapter3Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()

class Chapter313Item(scrapy.Item):
    # define the fields for your item here like:
    content = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    born = scrapy.Field()
