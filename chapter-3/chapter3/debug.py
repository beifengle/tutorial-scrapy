from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

crawler = CrawlerProcess(settings)
crawler.crawl('ch3.18-email')  # 爬虫名
crawler.start()




