import scrapy


class FromrequestSpider(scrapy.Spider):
    name = 'fromrequest'
    allowed_domains = ['x']
    start_urls = ['http://x/']

    def parse(self, response):
        pass
