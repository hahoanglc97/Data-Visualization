import scrapy


class ShopeeCrawlSpider(scrapy.Spider):
    name = 'shopee_crawl'
    allowed_domains = ['shopee.vn']
    start_urls = ['http://shopee.vn/']

    def parse(self, response):
        pass
