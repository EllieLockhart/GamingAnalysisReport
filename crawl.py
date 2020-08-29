import scrapy


class CrawlSpider(scrapy.Spider):
    name = 'crawl'
    allowed_domains = ['https://www.polygon.com']
    start_urls = ['https://www.polygon.com']

    def parse(self, response):
        pass
