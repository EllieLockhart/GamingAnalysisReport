#import scraping libraries
import scrapy

class GamingSpider(scrapy.Spider):
    name = "article"
    start_urls = 'https://www.polygon.com/gaming'

def parse(self, response):
        content = response.xpath(".//div[@class='entry-content']/descendant::text()").extract()
        yield {'article': ''.join(content)}
