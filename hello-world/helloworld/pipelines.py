# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HelloworldPipeline:
    def process_item(self, item, spider):
        print("保存到数据库DB：",item) #假设这里是实现数据存储到数据库
        return item