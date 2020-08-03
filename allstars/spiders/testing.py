import scrapy


class TestingSpider(scrapy.Spider):
    name = 'testing'
    allowed_domains = ['pickstar.com.au/our-stars']
    start_urls = ['http://pickstar.com.au/our-stars/']

    def parse(self, response):
        pass
